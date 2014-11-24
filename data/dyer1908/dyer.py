""" Data from Dyer's Compendium """
from os import path
from xml.etree.cElementTree import iterparse, tostring
from datetime import datetime as datetime_
from datetime import date as date_
from datetime import timedelta
import re
import csv
import os.path

import requests

from loss_parser import *

_months = dict(zip(["Jan", "Feb", "March", "April", "May", "June",
                   "July", "Aug", "Sept", "Oct", "Nov", "Dec"],
                  range(1, 13)))

with open('engagement_types.csv', 'r') as f:
    reader = csv.DictReader(f)
    ENGAGEMENT_TYPES = dict((x['from'], x['to']) for x in reader)
    
STATES = {
    'Minnesota': 'MN',
    'California': 'CA',
    'Missouri': 'MO',
    'Alabama': 'AL',
    'Mississippi': 'MI',
    'Pennsylvania': 'PA',
    'Arkansas': 'AR',
    'West Virginia': 'WV',
    'North Carolina': 'NC',
    'South Carolina': 'SC',
    'Florida': 'FL',
    'Kansas': 'KS',
    'Georgia': 'GA',
    'Virginia': 'VA',
    'Louisiana': 'LA',
    'Maryland': 'MD',
    'Texas': 'TX',
    'Tennessee': 'TN',
    'Kentucky': 'KY'
    }


def xml_to_csv(source, writer):
    context = iterparse(source, events=("start", "end", "start-ns"))
    state = None
    nevent = 1
    for event, elem in context:
        if event == "start":
            if elem.tag == "div1" and elem.get('type') == "state":
                state = elem.get("n")
            elif elem.tag == "div2" and elem.get('type') == "year":
                year = elem.get("n")
        elif event == "end":
            ## Process a div3
            if elem.tag == "div3" and elem.get('ana') == "interp-event":
                head = elem.find("head")
                ## Parse Date
                startDate = None
                endDate = None
                date = head.find("date")
                if date is not None:
                    date_value = date.get("value")
                    if re.match("186[1-5]-00", date_value) is not None:
                        yyyy = int(date_value[:4])
                        if date.text == "Jan. to April":
                            startDate = date_(yyyy, 1, 1)
                            endDate = date_(yyyy, 4, 30)
                        else:
                            for k, v in _months.items():
                                if date.text.startswith(k):
                                    startDate = date_(yyyy, v, 1)
                                    if v is not 12:
                                        endDate = date_(yyyy, v + 1, 1) - timedelta(1)
                                    else:
                                        endDate = date_(yyyy, 12, 31)
                                    break
                    else:
                        startDate = datetime_.strptime(date_value,
                                                       "%Y-%m-%d").date()
                        endDate = startDate
                elif head.find("dateRange") is not None:
                    date_range = head.find("dateRange")
                    if date_range.text == "Feb. 14-29":
                        startDate = date_(1863, 2, 14)
                        endDate = date_(1863, 2, 28)
                    elif date_range.text == "Feb 6-8":
                        startDate = date_(1864, 2, 6)
                        endDate = date_(1864, 2, 8)
                    else:
                        startDate = datetime_.strptime(date_range.get("from"),
                                                   "%Y-%m-%d").date()
                        endDate = datetime_.strptime(date_range.get("to"),
                                                 "%Y-%m-%d").date()
                # Event type
                event_type_tmp = head.findtext("rs")
                if event_type_tmp in ENGAGEMENT_TYPES:
                    event_type = ENGAGEMENT_TYPES[event_type_tmp]
                else:
                    if nevent == 4319:
                        event_type = "Reoccupation" # Re-occupation of New Madrid
                    elif nevent == 6348:
                        event_type = "Reopening" # Oct. 26-29: Re-opening, Tennessee River
                    else:
                        event_type = ""
                ## head_text
                event = tostring(head, method = "text", encoding = 'utf-8').decode('utf-8')
                # Text
                text = elem.findtext("p").strip()
                ## Casualties
                losses = parse_losses(text)
                
                #print nevent, state, year, startDate, endDate, event_type
                data = {'battle' : nevent,
                        'event_type' : event_type,
                        'state' :STATES[state],
                        'year' : year,
                        'battle_name' : event,
                        'start_date' : startDate,
                        'end_date' : endDate,
                        'text' : text.strip(),
                        'cas_k' : losses['k'],
                        'cas_w' : losses['w'],
                        'cas_m' : losses['m'],
                        'cas_kw' : losses['kw'],
                        'cas_mp' : losses['mp'],
                        'cas_kwm' : losses['kwm'],
                        'cas_total' : losses['total'],
                        'text': text,
                        }
                writer.writerow(data)
                nevent += 1

                         
def main():
    header = ['battle',
              'event_type',
              'state',
              'year',
              'battle_name',
              'start_date',
              'end_date',
              'text',
              'cas_k',
              'cas_w',
              'cas_m',
              'cas_kw',
              'cas_mp',
              'cas_kwm',
              'cas_total'
         ]
    FILE = "Perseus_text_2001.05.0140.xml"
    URL = "http://www.perseus.tufts.edu/hopper/dltext?doc=Perseus%3Atext%3A2001.05.0140"
    DST = "engagements.csv"

    if not os.path.exists(FILE):
        r = requests.get(URL)
        print(r)
        with open(FILE, 'w') as f:
            f.write(r.text)

    with open(FILE, 'r') as src:
        with open(DST, "w") as dst:
            writer = csv.DictWriter(dst, header)
            writer.writeheader()
            xml_to_csv(src, writer)

if __name__ == "__main__":
    main()                     
    


