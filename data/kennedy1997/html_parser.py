import re
import os
import os.path
import csv
import glob
import calendar
from datetime import date

import pyparsing as pp
from bs4 import BeautifulSoup

months = ('January', 'February', 'March',
          'April', 'May', 'June',
          'July', 'August', 'September',
          'October', 'November', 'December')

regex1 = re.compile(''.join([r'(?P<name>.*)\s*,\s*(?P<state>.*)\s*?\((?P<battle>[A-Z]{2}[0-9]{3}[A-Z]?)\)',
                             r'\s*,?\s*(?P<county>.*)\s*,\s*(?P<date>(?:%s).*)$' % '|'.join(months)]))

def _month_number(x):
    """Return the month number for the fullname of a month"""
    return list(calendar.month_name).index(x)

def parse_dates(x):
    """Parse Date Ranges"""
    comma = pp.Literal(",").suppress()
    hyphen = pp.Literal("-").suppress()
    month = pp.oneOf(list(calendar.month_name)[1:])
    month = month.setResultsName('m')
    month.addParseAction(lambda s,l,t: [_month_number(t[0])])
    day = pp.Word(pp.nums).setResultsName('d')
    day.addParseAction(lambda s,l,t: [int(t[0])])
    year = pp.Word(pp.nums).setResultsName('year')
    year.addParseAction(lambda s,l,t: [int(t[0])])

    one_date = (month + day + comma + year).setResultsName('date')
    start_date = (month + day + pp.Optional(comma + year)).setResultsName('start')
    end_date = (pp.Optional(month) + day + comma + year).setResultsName('end')
    date_range = start_date + hyphen + end_date
    # date_range needs to be first or one_date will pick up
    # start_dates with a year
    grammar =  date_range | one_date
    toks = grammar.parseString(x)
    if 'date' in toks:
        start_date = end_date = date(toks['year'],
                                     toks['m'],
                                     toks['d'])
    else:
        start_d = toks['start']['d']
        start_m = toks['start']['m']
        if 'year' in toks['start']:
            start_y = toks['start']['year']
        else:
            start_y = toks['end']['year']
        start_date = date(start_y, start_m, start_d)
        end_d = toks['end']['d']
        if 'm' in toks['end']:
            end_m = toks['end']['m']
        else:
            end_m = toks['start']['m']
        end_y = toks['end']['year']
        end_date = date(end_y, end_m, end_d)
    return {'start_date' : start_date, 'end_date' : end_date}

def parse_file(filename):
    with open(filename, 'r', encoding = 'cp1252', errors = 'ignore') as f:
        soup = BeautifulSoup(f)
    title = soup.find_all('span', class_='subsectiontitle')[0]
    data = {}
    data['campaign'] = title.a.text
    data['description'] = [x for x in title.strings][2].strip()
    m = regex1.match(data['description'])
    data['filename'] = os.path.basename(filename)
    if m:
        for i in ('name', 'state', 'battle', 'county'):
            data[i] = m.group(i)
        if filename == "html/cw_002802_siegeofyorkt.htm": # somethings fucked with this encoding
            start_date = "1862-04-15"
            end_date = "1862-05-04"
        else:
            parsed =  parse_dates(m.group('date'))
            start_date = parsed['start_date'].strftime('%Y-%m-%d')
            end_date = parsed['end_date'].strftime('%Y-%m-%d')
        data['start_date'] = start_date
        data['end_date'] = end_date
    elif filename == 'html/cw_002813_glendalevirg.htm':
        data['name'] = "Glendale and White Oak Swamp"
        data['state'] = "Virginia"
        data['start_date'] = "1862-06-30"
        data['end_date'] = "1862-06-30"
        data['battle'] = "VA020"
        data['county'] = "Henrico County"
    else:
        print(data['description'])
    return data

def main():
    rows = []
    for filename in glob.glob('html/*.htm'):
        if os.path.basename(filename) != 'cw_000108_app_the384pr.htm':
            rows += [parse_file(filename)]
    with open('kennedy_battles.csv', 'w') as f:
        writer = csv.DictWriter(f, ('filename', 'battle', 'name', 
                                    'state', 'county', 'start_date', 'end_date',
                                    'description', 'campaign'))
        writer.writeheader()
        writer.writerows(rows)
    print("Wrote to %s" % "kennedy_battles.csv")
    # print(parse_dates("April 15, 1862"))
    # print(parse_dates("May 4, 1862"))
    # print(parse_dates("April 15-May 4, 1862"))
    # print(parse_dates("April 15 - May 4, 1862"))

if __name__ == '__main__':
    main()
