# -*- coding: utf-8 -*-
import re
import sys
import calendar
import csv

re_newentry = re.compile("([0-9][,.]?[0-9]{3}|[0-9]{1,3})[. ]*(.*?)[—-](.*)")
with open(sys.argv[1], 'r') as f:
    text = f.read()

para = re.split('\n\n+', text, flags=(re.M))

def date_parser(x, year):
    MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December')
    MONTHDICT = dict((x, i + 1) for i, x in enumerate(MONTHS))
    months = '|'.join(MONTHS)
    days = '[0-9]{1,2}'
    #m = re.match(r'(?P<month1>%s)
    m = re.match(r'(?P<month1>%s)(?:\s+(?P<day1>%s)(?:d|th))?(?:\s+(?:and|to))?(?:\s+(?P<month2>%s))?(?:\s+(?P<day2>%s)(?:d|th))?' % (months, days, months, days), x)
    if not m:
        print(x)
    else:
        date = m.groupdict()
        date['month1'] = MONTHDICT[date['month1']]
        if not date['day1']:
            date['day1'] = 1
            date['day2'] = calendar.monthrange(year, date['month1'])[1]
            date['monthonly'] = True
        else:
            date['monthonly'] = False
        if not date['month2']:
            date['month2'] = date['month1']
        else:
            date['month2'] = MONTHDICT[date['month2']]
        if not date['day2']:
            date['day2'] = date['day1']
        return ('%s-%s-%s' % (year, date['month1'], date['day1']),
                '%s-%s-%s' % (year, date['month1'], date['day2']),
                date['monthonly'])

data = []
for p in para:
    lines = p.split('\n')
    if lines[0] == '':
        continue
    if lines[0][0] == "#":
        year = int(lines[0][2:])
        continue
    if len(lines) != 2:
        print("Error too many lines: %s" % lines)
        break
    m = re_newentry.match(lines[1])
    if not m:
        print("Error non match: %s" % lines[1])
        break
    id = int(re.sub('[.,]', '', m.group(1)))
    if id == 1666:
        continue
    start_date, end_date, monthonly  = date_parser(m.group(2), year)
    location = re.sub("\(.*?\)\.?", "", lines[0]).strip()
    location = re.sub("[.,]$", "", location).strip()
    state = ''
    if re.search(r'\bWest Va\.?$', location):
        state = "WV"
    elif re.search(r'\bVa[,.]?$', location):
        state = "VA"
    elif re.search(r'\bTenn\.?$', location):
        state = "TN"
    elif re.search(r'\bN\.? *C\.?$', location):
        state = "NC"
    elif re.search(r'\bS\.? *C\.?$', location):
        state = "SC"
    elif re.search(r'\bAla\.?$', location):
        state = "AL"
    elif re.search(r'\bTex(as)?$', location):
        state = "TX"
    elif re.search(r'\bNeb$', location):
        state = "NB"
    elif re.search(r'\bFla\.?$', location):
        state = "FL"
    elif re.search(r'\bGa\.?$', location):
        state = "GA"
    elif re.search(r'\bLa\.?$', location):
        state = "LA"
    elif re.search(r'\bArk\.?$', location):
        state = "AR"
    elif re.search(r'\bInd(ian)?\.? Terr?(itory)?\.?$', location):
        state = "OK"
    elif re.search(r'\bInd\.?$', location):
        state = "IN"
    elif re.search(r'\bUtah Terr?(itory)?\.?$', location):
        state = "UT"
    elif re.search(r'\bKy\.?$', location):
        state = "KY"
    elif re.search(r'\bMiss\.?$', location):
        state = "MS"
    elif re.search(r'\bCol\.?( Terr?)\.?$', location):
        state = "CO"
    elif re.search(r'\bCal$', location):
        state = "CA"
    elif re.search(r'\b(?:Missouri|Mo)\.?$', location):
        state = "MO"
    elif re.search(r'\b(Kansas|Kan|Ks)\.?$', location):
        state = "KS"
    elif re.search(r'\b(Oregon|Or)$', location):
        state = "OR"
    elif re.search(r'\b(Arizona Terr?\.?|A\. T\.?)$', location):
        state = "AZ"
    elif re.search(r'\bD\. *C\.?$', location):
        state = "DC"
    elif re.search(r'\bNev\.? Terr?$', location):
        state = "NV"
    elif re.search(r'\b(Dak(ota)?\.? Terr?|D\. T\.?)$', location):
        state = "ND"
    elif re.search(r'\b(Pa|Penn)\.?$', location):
        state = "PA"
    elif re.search(r'\bMd?$', location):
        state = "MD"
    elif re.search(r'\b(?:N\.? *M|New Mexico)\.?$', location):
        state = "NM"
    elif re.search(r'\bMinn\.?$', location):
        state = "MN"
    elif re.search(r'\bWashington Ter$', location):
        state = "WA"
    elif re.search(r'\bI\. T\.?$', location):
        state = "OK"
    elif re.search(r'\bInd. Terr?\.?$', location):
        state = "OK"
    elif re.search(r'\bOh\.?$', location):
        state = "OH"
    elif re.search(r'\bIll\.?$', location):
        state = "IL"
    else:
        print(location)
    data.append({'location': lines[0],
                 'state': state,
                 'start_date': start_date,
                 'end_date': end_date,
                 'monthonly': monthonly,
                 'id': int(re.sub('[.,]', '', m.group(1))),
                 'description': m.group(3)})

with open('engagements.csv', 'w') as f:
    writer = csv.DictWriter(f, ('id', 'start_date', 'end_date', 'monthonly', 'location', 'state', 'description'))
    writer.writeheader()
    writer.writerows(data)

