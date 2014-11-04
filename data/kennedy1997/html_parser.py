from os import path
import json
import pyparsing as pp
import re

from lxml import html

def org_table_row(x):
    return '| %s |' % ' | '.join(x)

def parse_casualties(x):
    comma = pp.Literal(",").suppress()
    prefix = pp.Regex("(Estimated )?Casualties:").suppress()
    number = pp.Regex("[0-9]{1,3}(,[0-9]{3})*")("casualty")
    number.setParseAction(lambda s,l,t: [int(t[0].replace(",", ""))])
    country = pp.oneOf(("US", "CS"))("country")
    stat = pp.Group(number + country)
    phrase = prefix + stat + comma + stat
    try:
        data = {}
        toks = phrase.parseString(x)
        for tok in toks:
            country = tok.asDict()
            data[country['country']] = country['casualty']
    except pp.ParseException:
        data = None
    return (re.sub("(Estimated )?Casualties: *", "", x), data)

def parse_battle(cwsacref, page):
    with open(page, 'r') as f:
        foo = html.parse(page).getroot()
    keyword = foo.find_class('keyword')
    us_casualties = ' '
    cs_casualties = ' '
    i_casualties = ' '
    if len(keyword) == 1:
        casualties, data = parse_casualties(keyword[0].text)
        if data:
            us_casualties = str(data["US"])
            cs_casualties = str(data["CS"])
    else:
        casualties = ' '.join([x.text for x in keyword])
    return (cwsacref, casualties, us_casualties, cs_casualties)

def main():
    htmldir = './html'
    metadatafn = path.join(htmldir, 'METADATA.json')
    with open(metadatafn, 'r') as f:
        metadata = json.load(f)
    battlelist  = dict((k, path.join(htmldir, path.basename(v))) 
                       for k, v in metadata['battles'].iteritems())
    for k, v in battlelist.iteritems():
        try:
            row = parse_battle(k, v)
            print org_table_row(row)
        except IOError:
            pass

if __name__ == '__main__':
    main()
