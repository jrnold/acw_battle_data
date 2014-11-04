import csv
import re
import calendar

import yaml
import pyparsing as pp

def _month_number(x):
    """Return the month number for the fullname of a month"""
    return list(calendar.month_name).index(x)

def parse_month_range(x):
    """Parse Date Ranges"""
    hyphen = pp.Literal("-").suppress()
    month = pp.oneOf(list(calendar.month_name)[1:])
    month = month.setResultsName('m')
    month.addParseAction(lambda s,l,t: [_month_number(t[0])])
    year = pp.Word(pp.nums).setResultsName('year')
    year.addParseAction(lambda s,l,t: [int(t[0])])

    end_month = (month + year).setResultsName('end')
    start_month = (month + pp.Optional(year)).setResultsName('start')
    grammar = pp.Optional(start_month + hyphen) + end_month
    toks = grammar.parseString(x)
    end_year = toks['end']['year']
    end_month = toks['end']['m']
    if 'start' in toks:
        start_month = toks['start']['m']
        if 'year' in toks['start']:
            start_year = toks['start']['year']
        else:
            start_year = toks['end']['year']
    else:
        start_year = end_year
        start_month = end_month
    return (start_year, start_month, end_year, end_month)

def parse_campaigns(src):
    """ Parse campaigns """
    data = yaml.load(open(path.join(src, 'campaigns.yaml'), 'r'))
    return data

with open("campaigns.yaml", "r") as f:
    data = yaml.load(f)
    for x in data:
        campaign = x['campaign']
        months = re.search(r"\[(.*)\]", campaign).group(1)
        x['start_year'], x['start_month'], x['end_year'], x['end_month'] = parse_month_range(months)

with open('campaigns.csv', 'w') as f:
    writer = csv.DictWriter(f, ('campaign', 'theater', 'start_year', 'start_month',
                                'end_year', 'end_month', 'dbpedia'))
    writer.writeheader()
    writer.writerows(data)

