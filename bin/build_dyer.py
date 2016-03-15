""" Data from Dyer's Compendium """
from os import path
from xml.etree.cElementTree import iterparse, tostring
from datetime import datetime as datetime_
from datetime import date as date_
from datetime import timedelta
import re
import csv
import os.path
import sys
import shutil

import requests

_months = dict(zip(["Jan", "Feb", "March", "April", "May", "June",
                   "July", "Aug", "Sept", "Oct", "Nov", "Dec"],
                  range(1, 13)))

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

EXAMPLES = (
"NEW YORK--15th Cavalry. Union loss, 1 killed, 1 wounded. Total, 2.",
"NEW YORK--5th Cavalry. PENNSYLVANIA--18th Cavalry. Union loss, 40 killed and wounded.",
"INDIANA--3d Cavalry. MAINE--16th Infantry. MASSACHUSETTS--12th, 13th and 39th Infantry. NEW HAMPSHIRE--1st Cavalry. NEW JERSEY--3d Cavalry. NEW YORK--8th and 22d Cavalry; 94th, 97th and 104th Infantry. PENNSYLVANIA--11th, 88th, 90th, 107th, 190th and 191st Infantry. VERMONT--1st Cavalry. UNITED STATES--Battery \"C & E\" 4th Arty. Union loss (including Riddell's Shop), 50 killed, 250 wounded. Total, 300.",
"WEST VIRGINIA--6th Cavalry. Union loss, 2 wounded.",
"MARYLAND--1st P. H. B. Cavalry; Battery \"B\" Light Arty. NEW YORK--1st Lincoln, 1st Veteran, 15th and 21st Cavalry; 20th Indpt. Battery Light Arty. OHIO--8th Cavalry; 34th Mounted Infantry. PENNSYLVANIA--14th, 20th and 22d Cavalry. WEST VIRGINIA--1st, 2d, 5th and 7th Cavalry; Batteries \"B\" and \"D,\" Light Arty.; 11th and 15th Infantry. UNITED STATES--Battery \"B,\" 5th Arty. Union loss, 15 killed and missing.",
"NEW YORK--19th Cavalry. PENNSYLVANIA--6th Cavalry. Union loss, 4 killed, 20 wounded. Total, 24.",
"MASSACHUSETTS--2d Cavalry. MICHIGAN--1st, 5th, 6th and 7th Cavalry. NEW YORK--4th, 6th, 9th and 19th Cavalry. PENNSYLVANIA--6th and 17th Cavalry. UNITED STATES--1st and 2d Cavalry; Batteries \"B & L,\" and \"D,\" 2d Arty. Union loss, 30 killed, 70 wounded, 200 captured and missing. Total, 300.",
"INDIANA--20th Infantry. UNITED STATES--2d Sharpshooters. Union loss, 8 killed, 14 wounded, 59 missing. Total, 81.",
"INDIANA--1st Cavalry (Detachment); 43d Infantry. IOWA--36th Infantry. KANSAS--5th Cavalry > > (Detachment). MISSOURI--7th Cavalry (Detachment); Battery \"E,\" 2d Light Arty. OHIO--77th Infantry. Union loss, 100 killed, 250 wounded, 1100 captured and missing. Total, 1450."
)

# with open('engagements.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     data = [row for row in reader]

# makes it easier to pick out the pattern, especially numbers
def remove_punct(x):
    return re.sub(r'[^0-9A-Za-z\s]', '', x)

def spaces(x):
    return re.sub(r'\s+', ' ', x)

RE_KWM = re.compile(r"(\d+) killed wounded and missing", re.I)
RE_KW = re.compile(r"(\d+) killed and wounded(?! (and|wounded|missing|captured))", re.I)
RE_K = re.compile(r"(\d+) killed(?! (and|wounded|missing|captured))", re.I)
RE_W = re.compile(r"(\d+) wounded", re.I)
RE_M = re.compile(r"(\d+) missing", re.I)
RE_CM = re.compile(r"(\d+) captured and missing", re.I)
RE_TOTAL = re.compile(r"total (\d+)", re.I)

def regroup(regex, x):
    m = regex.search(x)
    if m:
        return int(m.group(1))

def parse_losses(x):
    x = spaces(remove_punct(x))
    d = {}
    d['kwm'] = regroup(RE_TOTAL, x) or regroup(RE_KWM, x)
    d['k'] = regroup(RE_K, x)
    d['w'] = regroup(RE_W, x)
    d['kw'] = regroup(RE_KW, x)
    d['m'] = regroup(RE_M, x) or regroup(RE_CM, x)
    if d['kwm']:
        for i in ('k', 'w', 'm', 'kw'):
            d[i] = d[i] or 0
        if not d['k'] and not d['kw'] and not d['w'] and not d['m']:
            d['k'] = d['kw'] = d['w'] = d['m'] = None
    if d['kw'] and not d['k'] and not d['w']:
        d['k'] = None
        d['w'] = None
    elif d['kw'] is not None and d['kw'] == 0:
        if d['k'] or d['w']:
            d['kw'] = d['k'] + d['w']
    return d

def xml_to_csv(source, writer, engagement_types):
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
                if event_type_tmp in engagement_types:
                    event_type = engagement_types[event_type_tmp]
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
                        'casualties' : losses['kwm'],
                        'killed' : losses['k'],
                        'wounded' : losses['w'],
                        'killed_wounded' : losses['kw'],
                        'missing_captured' : losses['m'],
                        'text': text
                        }
                writer.writerow(data)
                nevent += 1



def load_engagement_types(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        data = dict((x['from'], x['to']) for x in reader)
    return data

def build_engagements(src, dst):
    header = ('battle',
              'event_type',
              'state',
              'year',
              'battle_name',
              'start_date',
              'end_date',
              'text',
              'casualties',
              'killed',
              'wounded',
              'killed_wounded',
              'missing_captured'
         )
    xmlfile = os.path.join(src, "Perseus_text_2001.05.0140.xml")
    url = "http://www.perseus.tufts.edu/hopper/dltext?doc=Perseus%3Atext%3A2001.05.0140"
    dstfile = os.path.join(dst, "dyer_engagements.csv")

    engagement_types = load_engagement_types(os.path.join(src, 'engagement_types.csv'))

    with open(xmlfile, 'r') as src:
        with open(dstfile, "w") as dstf:
            writer = csv.DictWriter(dstf, header)
            writer.writeheader()
            xml_to_csv(src, writer, engagement_types)

def build(src, dst):
    dyer_src = os.path.join(src, 'rawdata', 'dyer1908')
    build_engagements(dyer_src, dst)

def main():
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
