""" Convert Civil War Soldiers and Sailors XML file to csv tables """
from lxml import etree as ET
import re
import csv
from datetime import datetime as dt
from datetime import date
import calendar
import sys
from os import path

import pandas
import pyparsing as pp
import yaml

namespaces = {
'd' : "http://schemas.microsoft.com/ado/2007/08/dataservices",
'm' :"http://schemas.microsoft.com/ado/2007/08/dataservices/metadata",
'': "http://www.w3.org/2005/Atom"
}

URL = "http://www.nps.gov/civilwar/search-battles-detail.htm?battleCode=%s"

def _month_number(x):
    """Return the month number for the fullname of a month"""
    return list(calendar.month_name).index(x)

def ldom(y, m):
    """ Last day of the month"""
    return date(y, m, calendar.monthrange(y, m)[1])

def xmlns(x):
    xsplit = x.split(':')
    if len(xsplit) == 1:
        xsplit = ['', xsplit[0]]
    return "{%s}%s" % (namespaces[xsplit[0]], xsplit[1])

def battle_csv(root, dst):
    fields = (
    'BattlefieldCode',
    'BattleName',
    'BattleType',
    'BeginDate',
    'EndDate',
    'State',
    'TheaterCode',
    'CampaignCode',
    'Result',
    'TotalCasualties',
    #'CampaignDates',
    #'CampaignName',
    'Comment',
    'ID',
    'ShortSummary',
    'ShortSummarySource',
    'Summary',
    'SummarySource'
    # 'TheaterName',
    )
    print("Writing: %s" % dst)
    with open(dst, 'w', encoding='utf8') as f:
        writer = csv.DictWriter(f, list(fields) + ['URL'])
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            battle = {}
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            for fld in fields:
                battle[fld] = properties.find(xmlns('d:%s' % fld)).text
                if battle[fld]: 
                    battle[fld] = battle[fld].strip()
            battle['BattlefieldCode'] = battle['BattlefieldCode'].upper()
            if battle['BeginDate']:
                battle['BeginDate'] = dt.strptime(battle['BeginDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
            if battle['EndDate']:
                battle['EndDate'] = dt.strptime(battle['EndDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
            battle['URL'] = URL % battle['BattlefieldCode']
            writer.writerow(battle)
            
def theaters_csv(root, dst):
    theaters = {}
    print("Writing: %s" % dst)    
    with open(dst, 'w', encoding='utf8') as f:
        writer = csv.DictWriter(f, ('TheaterCode', 'TheaterName'))
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            theater_code = properties.find(xmlns('d:TheaterCode')).text
            theater_name = properties.find(xmlns('d:TheaterName')).text
            if theater_code:
                theaters[theater_code] = theater_name
        theaters_rows = [{'TheaterCode': k, 'TheaterName': v} for k, v in sorted(theaters.items())]
        writer.writerows(theaters_rows)

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
        
def campaigns_csv(root, dst):
    campaigns = {}
    print("Writing: %s" % dst)
    with open(dst, 'w', encoding='utf8') as f:
        writer = csv.DictWriter(f, ('CampaignCode', 'CampaignName', 'CampaignDates', 
                                    'CampaignStartDate', 'CampaignEndDate', 'TheaterCode'))
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            campaign_code = properties.find(xmlns('d:CampaignCode')).text
            campaign_name = properties.find(xmlns('d:CampaignName')).text
            campaign_dates = properties.find(xmlns('d:CampaignDates')).text
            if campaign_dates is not None and len(campaign_dates.strip()) > 0:
                start_date, end_date = parse_month_range(campaign_dates)
            else:
                start_date = end_date = None
            theater_code = properties.find(xmlns('d:TheaterCode')).text
            if campaign_code and campaign_code.strip() != '' and campaign_code not in campaigns:
                campaigns[campaign_code] = {'CampaignCode': campaign_code,
                                            'CampaignName': campaign_name,
                                            'CampaignDates': campaign_dates,
                                            'CampaignStartDate': start_date,
                                            'CampaignEndDate': end_date,
                                            'TheaterCode': theater_code}
        for k, v in sorted(campaigns.items()):
            writer.writerow(v) 

def guid_clean(x):
    if x:
        return re.search(r"{(.*)}", x).group(1).lower()
           
def commander_csv(root, dst):
    fields = ('BattlefieldCode', 'belligerent', 'commander_number', 'commander')
    print("Writing: %s" % dst)            
    with open(dst, 'w', encoding='utf8') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for entry in root.findall('.//%s' % xmlns('entry')):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            battlecode = properties.find(xmlns("d:BattlefieldCode")).text.strip().upper()
            enemy = properties.find(xmlns("d:EnemyName")).text
            # NC002 battle code is empty
            if battlecode in ("NC002", "MO026"):
                enemy = "Confederate"
            if battlecode in ("MN002"):
                enemy = "Native American"
            for i, ordinal in enumerate(("First", "Second", "Third")):
                if properties.find(xmlns("d:%sEnemyCommander" % ordinal)).text is not None:
                    if re.search("\\S", properties.find(xmlns("d:%sEnemyCommander" % ordinal)).text):
                        writer.writerow({'BattlefieldCode' : battlecode.upper(),
                                         'belligerent' : enemy,
                                         'commander_number' : i + 1,
                                         'commander' : guid_clean(properties.find(xmlns("d:%sEnemyCommander" % ordinal)).text)
                                         })
                if properties.find(xmlns("d:%sUSCommander" % ordinal)).text is not None:
                    if (battlecode == "MO026" and ordinal == "Second"):
                        # Fix Alfred Pleasonton for MO026
                        # The XML file gives the name rather than the UUID
                        writer.writerow({'BattlefieldCode': "MO026",
                                         "belligerent": "US",
                                         "commander_number": 2,
                                         "commander": "90849b39-6f3a-4d88-af29-ddded5d1733a"})
                    else:
                        if re.search("\\S", properties.find(xmlns("d:%sUSCommander" % ordinal)).text):
                            writer.writerow({'BattlefieldCode' : battlecode.upper(),
                                             'belligerent' : "US",
                                             'commander_number' : i + 1,  
                                             'commander' : guid_clean(properties.find(xmlns("d:%sUSCommander" % ordinal)).text)
                            })
                                        
def forces_csv(root, dst):
    fields = ('BattlefieldCode', 'belligerent', 'TroopsEngaged', "Casualties")
    with open(dst, 'w', encoding='utf8') as f:
        print("Writing: %s" % dst)        
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for entry in root.findall('.//%s' % xmlns('entry')):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            battlecode = properties.find(xmlns("d:BattlefieldCode")).text
            enemy = properties.find(xmlns("d:EnemyName")).text
            # NC002 battle code is empty
            if battlecode in ("NC002", "MO026"):
                enemy = "Confederate"
            if battlecode in ("MN002"):
                enemy = "Native American"
            writer.writerow({'BattlefieldCode' : battlecode.upper(),
                             'belligerent' : enemy,
                             'TroopsEngaged': properties.find(xmlns("d:EnemyTroopsEngaged")).text,
                             'Casualties': properties.find(xmlns("d:EnemyCasualties")).text,
                           })
            writer.writerow({'BattlefieldCode' : battlecode.upper(),
                            'belligerent' : "US",
                             'TroopsEngaged': properties.find(xmlns("d:USTroopsEngaged")).text,
                             'Casualties': properties.find(xmlns("d:USCasualties")).text,
                          })
                          
def people_csv(root, dst):
    fields = ("PersonID", "ID",
              "LastName", "Suffix", "FirstName", "MiddleName", "MiddleInitial",
              "Rank", "Bio", "BioSource", "NarrativeLink1", "NarrativeLink2")
    with open(dst, 'w', encoding='utf8') as f:
        print("Writing: %s" % dst)        
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            row = {}
            for fld in fields:
                if fld == "LastName":
                    last_name = properties.find(xmlns('d:LastName')).text
                    if last_name:
                        last_name = re.split(r",\s+", last_name)
                        if len(last_name) > 1:
                            row["LastName"], row["Suffix"] = last_name
                            if row["Suffix"] == "Jr":
                                row["Suffix"] = "Jr."
                        else:
                            row["LastName"] = last_name[0]
                            row["Suffix"] = ""
                elif fld != "Suffix":
                    row[fld] = properties.find(xmlns('d:%s' % fld)).text
            if row["FirstName"] == "Stand Watie":
                row["FirstName"] = "Stand"
                row["LastName"] = "Watie"
            writer.writerow(row)   

def people_keywords_csv(root, dst):
    fields = ("PersonID", "Keyword")
    with open(dst, 'w', encoding='utf8') as f:
        print("Writing: %s" % dst)      
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties')))
            id = properties.find(xmlns('d:PersonID')).text
            row = {'PersonID': id}
            keywords = properties.find(xmlns('d:Keywords')).text
            if keywords is None:
                continue
            replacements = (
                (';', ','),
                ('""', '"'),       
                ('" "', '", "'),
                (', ,', ', '),
                (" 'CS", ' "CS'),
                ('"Brigadier General,', '"Brigadier General",'),
                ('"Brigadier General,', '"Brigadier General",'),
                ('"European American"Major General"', '"European American", "Major General"'),
                ('European American" Commanders', 'European American", Commanders'),
                ('"KS - Slave State, "John Brown",', '"KS - Slave State", "John Brown",'),
                ('"European American" Minister', '"European American", Minister'),
                ('"European American "Commanders', '"European American", Commanders'),
                ('"Major General, Male', '"Major General", Male'),
                ('"Lieutenant Colonel, Male', '"Lieutenant Colonel", Male'),
                ('"Brigadier General" Male', '"Brigadier General", Male'),
                ('"CS - Commander - VA064,"CS - Commander - VA114"', '"CS - Commander - VA064", "CS - Commander - VA114"'),
                
                )
            for strfrom, strto in replacements:
                keywords = keywords.replace(strfrom, strto)
            if id in ("ecb8a078-2c3c-4056-b2b5-013fe3e91fa3",
                      "f2f4eda1-b51f-4f8e-ad2d-379a1eb685f3",
                      "15a8b826-e060-430a-bb4c-61936b75252e",
                      "22dc9bfe-6bfa-4f8a-a48f-694e947cc8d7",
                      "02b4fa9a-541a-45c7-9097-ab1aee538c6c",
                      "d428cfef-5c7a-4230-b394-b195481d9a9f",
                      "d6d0545e-4764-49d2-bcdd-b97262573342",
                      "d3b0a222-2294-41d9-96b9-bc78996d55ae",
                      "8f232cc9-43e7-4627-ab45-d8fe6873c472",
                      "77a0625d-2996-4af0-b46f-db7388f851d5",
                      "21d06a25-9c4f-4dea-a766-f60d20632999",
                      "84b6d739-3384-4291-86ba-f75ae6637069",
                      "a3f15046-9028-421d-bbe0-fb6c341a991f",
            ):
                # missing final quote
                keywords += '"'
            try:
                # The list of keywords is not really yaml
                # It is quoted and unquoted strings separated by commas
                # But it is consistent with syntax for a yaml list and easier than writing a regex.
                for kw in yaml.load("[" + keywords + "]"):
                    row['Keyword'] = kw
                    writer.writerow(row)
            except TypeError:
                pass
            
def battleunitslink_csv(root, comments, dst):
    fields = (
    'BattlefieldCode',
    'Comment',
    'Source',
    'UnitCode',
    'companies',
    'batteries',
    'detachment',
    'section'
    )
    with open(dst, 'w', encoding='utf8') as f:
        print("Writing: %s" % dst)
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):            
            row = {}
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            for fld in ('BattlefieldCode', 'Comment', 'Source', 'UnitCode'):
                try:
                    row[fld] = properties.find(xmlns('d:%s' % fld)).text.strip()
                except AttributeError:
                    row[fld] = None
            row['BattlefieldCode'] = row['BattlefieldCode'].upper()
            try:
                row.update(comments[(row['BattlefieldCode'], row['UnitCode'])])
            except KeyError:
                pass
            writer.writerow(row)
            
def build_units(src, dst):
    srcfile = path.join(src, 'dependencies', 'cwss',
                        'data', 'new', 'tsv', 'Regiments_Unitz.tsv')
    dstfile = path.join(dst, 'cwss_regiments_units.csv')
    data = pandas.read_csv(srcfile, sep = '\t')
    data.rename(columns = lambda k: k.lower().replace('reg_', ''),
                inplace = True)
    data.rename(columns = {'function': 'func'}, inplace = True)
    data = data.query('~ isdelete')
    # remove some test rows
    data = data[~ data.unit_code.str.match('admin[0-9]', flags = re.IGNORECASE)]
    # clean whitepace
    data.func = data.func.str.strip()
    for i in ('type', 'special', 'ethnic', 'unit_name', 'func'):
        data.replace({i: {'0': ''}}, inplace = True)
    data.replace({'side': {'U': 'US', 'C': 'Confederate'}},
                 inplace = True)
    # Fix bad funcs
    data.loc[data['unit_code'].isin(('CAL0105R', 'CVA0108R0M')), 'func'] = None
    data.duplicate = data.duplicate.fillna(0).astype('int64')
    for x in ('pubdate',
              'updatedate',
              'updateby',
              'comments',
              'updatetype',
              'isdelete',
              'longhistory',
              'history',
              'arm'):
        del data[x]
    print("Writing: %s" % dstfile)
    data.to_csv(dstfile, index = False)

def build_state_names(src, dst):
    srcfile = path.join(src, 'dependencies', 'cwss',
                        'data', 'new', 'tsv', 'State_Name.tsv')
    dstfile = path.join(dst, 'cwss_state_names.csv')
    data = pandas.read_csv(srcfile, sep = '\t')
    data.rename(columns = lambda k: k.lower().replace('state_', ''),
                       inplace = True)
    data = data.query('~ isdelete')        
    for x in ('updateby',
              'updatedate',
              'updatetype',
              'pubdate',              
              'isdelete',
              'comments'):
        del data[x]
    print("Writing: %s" % dstfile)
    data.to_csv(dstfile, index = False)

def build_unit_titles(src, dst):
    src_unititles = path.join(src, 'dependencies', 'cwss',
                          'data', 'new', 'tsv', 'Unititle.tsv')
    src_contitles = path.join(src, 'dependencies', 'cwss',
                          'data', 'new', 'tsv', 'Contitle.tsv')
    dstfile = path.join(dst, 'cwss_unittiles.csv')
    unititles = pandas.read_csv(src_unititles, sep = '\t')
    contitles = pandas.read_csv(src_contitles, sep = '\t')
    newdata = pandas.concat([unititles, contitles])
    newdata.rename(columns = lambda k: k.lower(), inplace = True)
    newdata = newdata.query('~ isdelete')    
    for col in ('updatedate',
                'updateby',
                'updatetype',
                'isdelete',
                'comments',
                'pubdate'):
        del newdata[col]
    newdata.replace({'side': {'C': 'Confederate',
                              'U': 'US'}})
    print("Writing: %s" % dstfile)
    newdata.to_csv(dstfile, index = False)

def build_category(src, dst):
    srcfile = path.join(src, 'dependencies', 'cwss',
                          'data', 'new', 'tsv', 'Category.tsv')
    dstfile = path.join(dst, 'cwss_categories.csv')
    data = pandas.read_csv(srcfile, sep = '\t')
    data.rename(columns = lambda k: k.lower(), inplace = True)
    data['abbr'] = data['abbr'].str.strip()
    data['description'] = data['description'].str.strip()
    data = data.query('~ isdelete & abbr != ["0", "o", "C1", "C2"]')
    for col in ('updatedate',
                'updateby',
                'isdelete',
                'updatetype',
                'comments',
                'pubdate',
                'pk_id'):
        del data[col]
    print("Writing: %s" % dstfile)
    data.to_csv(dstfile, index = False)

def build(src, dst):
    parser = ET.XMLParser(encoding = 'cp1252')
    cwssdir = path.join(src, 'dependencies', 'cwss')
    with open(path.join(cwssdir, 'data', 'old', 'battle.xml'), 'rb') as f:
        battles = ET.fromstring(f.read(), parser)    
    commander_csv(battles, path.join(dst, "cwss_commanders.csv"))
    battle_csv(battles, path.join(dst, 'cwss_battles.csv'))
    forces_csv(battles, path.join(dst, 'cwss_forces.csv'))
    theaters_csv(battles, path.join(dst, 'cwss_theaters.csv'))
    campaigns_csv(battles, path.join(dst, 'cwss_campaigns.csv'))

    with open(path.join(cwssdir, 'data', 'old', 'persons.xml'), 'rb') as f:
            persons = ET.fromstring(f.read(), parser)  
    people_csv(persons, path.join(dst, 'cwss_people.csv'))
    people_keywords_csv(persons, path.join(dst, 'cwss_people_keywords.csv'))    

    # This file includes the "parsed" comments. Number of batteries, companies, detachments, etc. mentioned
    # in the comments about the unit.
    comments = {}
    with open(path.join(src, 'rawdata', 'cwss', 'battle_units.csv'), 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            comments[(row['BattlefieldCode'], row['UnitCode'])] = dict((k, v) for k, v in row.items()
                                                                       if k in ('companies', 'batteries', 'detachment', 'section'))
    with open(path.join(cwssdir, 'data', 'old', 'battleunitlink.xml'), 'rb') as f:
            battleunitlinks = ET.fromstring(f.read(), parser)
    battleunitslink_csv(battleunitlinks, comments, path.join(dst, 'cwss_battle_units.csv'))
    build_unit_titles(src, dst)
    build_state_names(src, dst)
    build_category(src, dst)
    build_units(src, dst)

def main():
    src = str(sys.argv[1])
    dst = str(sys.argv[2])
    build(src, dst)

if __name__ == "__main__":
    main()
