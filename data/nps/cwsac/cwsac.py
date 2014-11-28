#!/usr/bin/env python3
"""
Parse the html pages of CWSAC and save as a more formatted JSON.
""" 
from os import path
import glob
import re
import sys
import calendar
from datetime import date
import json

import nameparser
from lxml import html
from lxml import etree
import pyparsing as pp
import yaml

URL_BASE = 'http://www.nps.gov/hps/abpp/battles'
EXCLUDE = ['bystate.html']

def _month_number(x):
    """Return the month number for the fullname of a month"""
    return list(calendar.month_name).index(x)

def subset(d, keys):
    return dict([(k, v) for k, v in d.items() if k in keys])

RANKS = {'Lieutenant': ["Lt."],
         'First Lieutenant': ['1st Lt.'],
         'Captain': ['Capt.'],
         'Captain (Naval)': ['Capt. (Naval)'],
         'Major': ['Maj.'],
         'Lieutenant Colonel': ['Lt. Col.'],
         'Brevet Colonel': ['BCol.'],
         'Colonel': ['Col.'],
         'Brigadier General': ['Brig. Gen.'],
         'Lieutenant General': ['Lt. Gen.'],
         'Major General': ['Maj. Gen.', 'Major Gen.'],
         'General': ['Gen.'],
         # Naval
         'Lieutenant (Naval)': ["Lt. (Naval)"],
         'Flag Officer': ["Flag-Officer"],
         'Acting Master': ["Acting Master"],
         'Commander': ["Cdr."],
         'Lieutenant Commander': ["Lt. Cdr.", 'Lt. Comdr.'],         
         'Acting Rear Admiral': ["Acting Rear Adm."],
         'Rear Admiral': ["Rear Adm."],
         'Admiral': ["Adm."],         
         # Indian
         'Chief': ['Chief']}

RANKS_LOOKUP = {}
for k, v in RANKS.items():
    for x in v:
        RANKS_LOOKUP[x] = k

def parse_commanders(x):
    # Grammar
    LBRAK, RBRAK, COMMA = (pp.Literal(x).suppress() for x in "[],")
    AND = pp.Literal("and").suppress()
    and_ = pp.Optional(COMMA) + AND
    NAME = pp.Word(pp.srange("[A-Z]"), pp.alphas + pp.alphas8bit, min=2)
    RANK = pp.Or(pp.Literal(rnk) for rnk in RANKS_LOOKUP.keys())("rank")
                        # ('Lt. Gen.', 'Brig. Gen.', 'Maj. Gen.', 'Lt. Col.',
                        #  'Lt. Cdr.',  'Lt. Comdr.', '1st Lt.', 'Rear Adm.', 'Bvt. Col.', 'BCol.',
                        #  'Gen.', 'Maj.',  'Col.', 'Capt.', 'Cdr.', 'Lt.', 'Adm.', 
                        #  'Chief', 'Flag-Officer', 'Acting Master'))("rank")
    ABBR = pp.Regex(r"([A-Z]\.)+")
    SUFFIX = pp.Literal("Jr.")
    NOCMDR = pp.Literal("No Union commander")("none")
    USN = pp.Literal("U.S.N.")("usn")
    BELLIGERENT = pp.oneOf(' '.join(('US', 'CS', 'I')))("belligerent")
    
    nametoken = ABBR | pp.quotedString | NAME
    name = (pp.OneOrMore(nametoken) + pp.Optional(COMMA + SUFFIX))("fullname")
    name.addParseAction(lambda s,l,t: ' '.join(t))
    
    cmdrname = (RANK + name + pp.Optional(COMMA + USN))
    commander = pp.Group(cmdrname | NOCMDR)
    commander_list = pp.Group(pp.delimitedList(commander, ",") +
                              pp.Optional(and_ + commander))("commanders")
    milforce = pp.Group(commander_list + LBRAK + BELLIGERENT + RBRAK)
    grammar = pp.delimitedList(milforce, ";")
    toks = grammar.parseString(x)

    # A smarter grammar could probably have avoided this
    res = {}
    for _force in toks:
        k = _force['belligerent']
        res[k] = [x.asDict() for x in _force['commanders']
                  if "none" not in x.asDict()]
    return res

def parse_preservation_priority(x):
    """Parse preservation_priority

    Parse cwsac:preservation_priority into cwsac:military_importance and
    cwsac:preservation_class.
    """
    MISSING = pp.Literal("N/D") | pp.Literal("N/A")
    MISSING.addParseAction(lambda s,l,t: [None])
    PRIORITY = pp.Word(pp.alphas) + "." + pp.Word(pp.nums)
    PRIORITY.addParseAction(lambda s,l,t: [''.join(t)])
    CLASS = pp.Literal("Class").suppress()
    OP = pp.Literal("(").suppress()
    CP = pp.Literal("(").suppress()
    priority =  (PRIORITY | MISSING)
    milimport = pp.Word(pp.srange("[A-D]"))
    grammar = priority + OP + CLASS + milimport + pp.Optional(CP)
    toks =  grammar.parseString(x).asList()
    return toks

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

def ldom(y, m):
    """ Last day of the month"""
    return date(y, m, calendar.monthrange(y, m)[1])

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
    end_date = ldom(toks['end']['year'], toks['end']['m'])
    if 'start' in toks:
        m = toks['start']['m']
        if 'year' in toks['start']:
            y = toks['start']['year']
        else:
            y = toks['end']['year']
        start_date = date(y, m, 1)
    else:
        start_date = date(end_date.year, end_date.month, 1)
    return (start_date, end_date)

def find_result(tree):
    # The pages use the color the battle to indicate the result
    if len(tree.xpath('//font[@color="#1C7807"]')):
        result = "Inconclusive"
    elif len(tree.xpath('//font[@color="#003364"]')):
        result = "Union"
    elif len(tree.xpath('//font[@color="#A6660F"]')):
        result = "Confederate"
    else:
        print("Could not find result")
        result = None
    return result

def parse_html(src):
    """Find all p elements in the battle summary td element

    Usually the paragraph looks like <b>Property name:</b> stuff.
    However, I found some malformed HTML on some pages. It seemed
    easier to convert the paragraph to plain text and split it on the
    colon.
    """
    def _get_battle_data_td(doc):
        """Get html element with battle summary from webpage

        Returns the td element containing the battle summary
        """
        return doc.xpath("/html/body/table/tr[2]/td[2]")[0]

    def _get_battle_title(el):
        """Get battle title in the battle summary td element"""
        return el.find("b/font/font/font").text.strip()

    fields = {'other_names' : 'Other Names:',
              'location' : 'Location:',
              '_campaign':  'Campaign:',
              'dates' : r'Dates?\(s\):', 
              'principal_commanders' : 'Principal Commanders:',
              'forces_text' : 'Forces Engaged:',
              'casualties_text' : 'Estimated Casualties:', 
              'description' : 'Description:', 
              'results_text' : r'Results?\(s\):', 
              'cwsac_reference' : r'CWSAC Reference #:', 
              '_preservation' : 'Preservation Priority:',
              '_national_park_unit' : 'National Park Unit:',
              'assoc_battles':
              'Battles Associated with the Operations:'}

    battle = path.splitext(path.basename(src))[0].upper()
    if battle == 'AR010A':
        battle = 'AR010'
    data = {'battle': battle}
    tree = html.parse(src)
    td = _get_battle_data_td(tree)
    data['battle_name'] = _get_battle_title(td).replace('\u0092', "'")
    data['url'] = '%s/%s' % (URL_BASE, path.basename(src))
    data['result'] = find_result(tree)

    last_field = None
    for x in td.findall(".//p"):
        has_field = False
        text = x.text_content().strip()
        # Text cleaning
        # replace non-breaking spaces
        text = text.replace('\xa0', ' ')
        # double quotes
        text = text.replace('\x93', '"')
        text = text.replace('\x94', '"')
        # apostraphes
        text = text.replace('\u0092', "'")
        # hyphen
        text = text.replace('\x96', "-")
        # replace internal returns and carriage returns
        text = re.sub(r'(\r|\n)', ' ', text)
        text = re.sub(r' +', ' ', text)
        # make it all unicode
        for k, v in fields.items():
            if re.match(v, text, re.I):
                data[k] = text.split(':', 1)[1].strip()
                has_field = True
                last_field = k
                break
        # some descriptions have multiple paragraphs
        # I need to append them to the previous paragraph
        if not has_field:
            if last_field == 'description':
                data[last_field] += '\n\n%s' % text
            else:
                print(text)
    return data

def parse_estimated_casualties(x):
    # easier to remove ',' than handle comma formatted numbers
    x = re.sub(",", "", x)
    # Missing values
    NA = pp.CaselessLiteral("unknown")
    NA.addParseAction(lambda s,l,t: [None])
    # No casualties
    NONE = pp.Regex("(none( known)?|few)", re.I)
    NONE.addParseAction(lambda s,l,t: [0])
    # Numeric casualties
    NUM = pp.Word(pp.nums)
    NUM.addParseAction(lambda s,l,t: [int(t[0])])
    TOTAL = pp.CaselessLiteral("total").suppress()
    APPROX = pp.Literal("approx.").suppress()
    OP = pp.Literal("(").suppress()
    CP = pp.Literal(")").suppress()
    CS = pp.Literal("CS").suppress()
    US = pp.Literal("US").suppress()
    IND = pp.Literal("I").suppress()
    casualties = (NA | pp.Optional(APPROX) +  NUM | NONE)
    total_cas = (casualties + TOTAL) | (TOTAL + casualties) | casualties
    total_cas = total_cas.setResultsName('total')
    us_cas = (US + casualties | casualties + US).setResultsName('US')
    cs_cas = (CS + casualties | casualties + CS).setResultsName('CS')
    ind_cas = (IND + casualties | casualties + IND).setResultsName('I')
    combat_cas = us_cas | cs_cas | ind_cas
    casualty_list = OP + pp.delimitedList(combat_cas, delim=';') + CP
    grammar = pp.StringStart() + pp.Optional(total_cas) + pp.Optional(casualty_list) + pp.StringEnd()
    toks = grammar.parseString(x).asDict()
    return toks

def parse_battle(alldata, src, campaigns, casualties, strengths, results):
    battle = path.splitext(path.basename(src))[0].upper()
    # One manual edit
    if battle == 'AR010A':
        battle = 'AR010'
    data = parse_html(src)
    # preservation
    preservation, significance = parse_preservation_priority(data['_preservation'])
    data['preservation'], data['significance'] = preservation, significance
    if data['significance'] == 'NA':
        data['significance'] = None
    # cols = [c.name for c in model.CwsacBattle.__table__.c]
    # dates
    daterange = parse_dates(data['dates'])
    for x in ('start_date', 'end_date'):
        data[x] = daterange[x].strftime("%Y-%m-%d")
    if data['other_names'] == "None":
        data['other_names'] = None
    # states
    data['state'] = path.basename(src)[:2].upper()
    # uri
    data['url'] = path.join(URL_BASE, path.basename(src))
    # operation
    data['operation'] = 'assoc_battles' in data
    # results
    # data['result'] = results[data['results_text']]
    # Participants
    forces = {}
    if (re.search(r'\[I\]', data['principal_commanders']) is not None):
        forces["I"] =  {'commanders' : []}
    if (re.search(r'\[CS\]', data['principal_commanders'])
        is not None):
        forces["CS"] = {'commanders' : []}        
    if (re.search(r'\[US\]', data['principal_commanders'])
        is not None):
        forces["US"] = {'commanders' : []}        

    ## Campaign
    data['campaign'] = campaigns[battle]
                        
    # Casualties
    ## Manual parses 
    if battle in casualties:
        if 'casualties' in casualties[battle]:
            data['casualties'] = casualties[battle]['casualties']
        if 'forces' in casualties[battle]:
            for belligerent in casualties[battle]['forces']:
                for k, v in casualties[battle]['forces'][belligerent].items():
                    forces[belligerent][k] = casualties[battle]['forces'][belligerent][k]
    else:
        ## 0 casualty battles
        if re.match("None( known)?", data['casualties_text'], re.I):
            for belligerent in forces:
                forces[belligerent]['casualties'] = 0
            data['casualties'] = 0
        else:
            # Auto parsing
            try:
                cas = parse_estimated_casualties(data['casualties_text'])
                if 'total' in cas:
                    data['casualties'] = cas['total']
                for belligerent in ('US', 'CS', 'I'):
                    if belligerent in forces and belligerent in cas:
                        forces[belligerent]['casualties'] = cas[belligerent]
            # Print failed parses
            except pp.ParseException:
                print("%s: %s" % (battle, data['casualties_text']))

    # Forces
    for k, v in strengths[battle].items():
        if k in ('US', 'CS', 'I'):
            for j, x in v.items():
                forces[k][j] = x
        else:
            data[k] = v
            
    # Commanders
    try:
        commanders = parse_commanders(data['principal_commanders'])
        # print(battle)
        # print(commanders)
        for k, v in commanders.items():
            for x in v:
                parsed_name = nameparser.HumanName(x['fullname']).as_dict()
                forces[k]['commanders'].append({'fullname' : x['fullname'],
                                                'first_name': parsed_name['first'],
                                                'last_name': parsed_name['last'],
                                                'middle_name': parsed_name['middle'],
                                                'suffix': parsed_name['suffix'],
                                                'rank' : RANKS_LOOKUP[x['rank']]})
    except pp.ParseException:
        print("%s: %s" % (battle, data['principal_commanders']))
        
    ## Strengths
    data['belligerents'] = forces

    # drop temporary keys
    keytodel = [k for k in data.keys() if k[0] == "_"]
    for k in keytodel:
        del data[k]

    alldata[battle] = data


def parse_battle_summaries(src):
    srcdir = path.join(src, 'html')
    ## Dictionary of campaign battles
    campaigns = yaml.load(open(path.join(src, 'battle_campaigns.yaml'), 'r'))
    casualties = yaml.load(open(path.join(src, 'casualties.yaml'), 'r'))
    strengths = yaml.load(open(path.join(src, 'forces.yaml'), 'r'))
    results = yaml.load(open(path.join(src, "results.yaml"), 'r'))
    files = glob.glob("%s/*.htm" % srcdir)
    battles = {}
    for i, x in enumerate(files):
        #if i > 1: break
        print(x)
        if re.match(r'[a-z]{2}[0-9]{3}[a-z]?\.htm', path.basename(x)):
            parse_battle(battles, x, campaigns, casualties, strengths, results)
    return battles


def load(datadir):
    print("loading cwsac")
    data = parse_battle_summaries(datadir)
    #data['ranks'] = [k for k in RANKS.keys()]
    return data

if __name__ == '__main__':
    datadir = "."
    with open("cwsac.json", "w") as f:
        json.dump(load(datadir), f, indent=2)
