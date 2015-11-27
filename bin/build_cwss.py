""" Convert Civil War Soldiers and Sailors XML file to csv tables """
from lxml import etree as ET
import re
import csv
from datetime import datetime as dt
from datetime import date
import calendar
import sys
from os import path

import pyparsing as pp

namespaces = {
'd' : "http://schemas.microsoft.com/ado/2007/08/dataservices",
'm' :"http://schemas.microsoft.com/ado/2007/08/dataservices/metadata",
'': "http://www.w3.org/2005/Atom"
}

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
    'SummarySource',
    # 'TheaterName',
    )
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
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
            writer.writerow(battle)
            
def theaters_csv(root, dst):
    theaters = {}
    with open(dst, 'w') as f:
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
    with open(dst, 'w') as f:
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
    with open(dst, 'w') as f:
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
                    if re.search("\\S", properties.find(xmlns("d:%sEnemyCommander" % ordinal)).text) and battlecode not in ("VA068", "VA095"):
                        writer.writerow({'BattlefieldCode' : battlecode.upper(),
                                         'belligerent' : enemy,
                                         'commander_number' : i + 1,
                                         'commander' : guid_clean(properties.find(xmlns("d:%sEnemyCommander" % ordinal)).text)
                                         })
                if properties.find(xmlns("d:%sUSCommander" % ordinal)).text is not None:
                    if (battlecode == "MO026" and ordinal == "Second"):
                        # Fix Alfred Pleasonton for MO026
                        writer.writerow({'BattlefieldCode': "MO026",
                                         "belligerent": "US",
                                         "commander_number": 2,
                                         "commander": "90849b39-6f3a-4d88-af29-ddded5d1733a"})
                    else:
                        if re.search("\\S", properties.find(xmlns("d:%sUSCommander" % ordinal)).text) and battlecode not in ("VA068", "VA095", "SC009"):
                            writer.writerow({'BattlefieldCode' : battlecode.upper(),
                                             'belligerent' : "US",
                                             'commander_number' : i + 1,  
                                             'commander' : guid_clean(properties.find(xmlns("d:%sUSCommander" % ordinal)).text)
                            })
        # Fix commanders for VA068
        writer.writerow({"BattlefieldCode": "VA068",
                         "belligerent": "Confederate",
                         "commander_number": 1,
                         "commander": "9e1353da-e14e-4a33-9169-19b95b173cd1"})
        writer.writerow({"BattlefieldCode": "VA068",
                         "belligerent": "Confederate",
                         "commander_number": 2,
                         "commander": "67a922f1-6dc9-4ba8-89aa-e33f842197e2"})
        # James Wilson
        writer.writerow({"BattlefieldCode": "VA068",
                         "belligerent": "US",
                         "commander_number": 1,
                         "commander": "460c9e8f-625e-490f-8eda-7385907b8d3f"})
        # August Kautz
        writer.writerow({"BattlefieldCode": "VA068",
                         "belligerent": "US",
                         "commander_number": 2,
                         "commander": "cb8dc6d1-211d-4278-875a-5f479f65d85b"})
        # Add Mahone for VA072
        writer.writerow({"BattlefieldCode": "VA072",
                         "belligerent": "Confederate",
                         "commander_number": 4,
                         "commander": "9e1353da-e14e-4a33-9169-19b95b173cd1"})
        # Add Fitzhugh Lee for VA086
        writer.writerow({"BattlefieldCode": "VA086",
                         "belligerent": "Confederate",
                         "commander_number": 2,
                        "commander": "67a922f1-6dc9-4ba8-89aa-e33f842197e2"})
        # Add Renshaw for TX003
        writer.writerow({"BattlefieldCode": "TX003",
                         "belligerent": "US",
                         "commander_number": 2,
                         "commander": "65815655-0c83-4511-9e7b-2ce4d0ca632c"})
        # Fix commanders for VA095
        # US: A. A. Humphreys
        writer.writerow({"BattlefieldCode": "VA095",
                         "belligerent": "US",
                         "commander_number": 1,
                         "commander": "0739970d-f176-49aa-958c-f26397e326bb"})
        # CS: Thomas Rosser
        writer.writerow({"BattlefieldCode": "VA095",
                         "belligerent": "Confederate",
                         "commander_number": 1,
                         "commander": "0dca3f2d-e93f-4908-bda9-bb23f411857b"})
        # CS: William Mahone
        writer.writerow({"BattlefieldCode": "VA095",
                         "belligerent": "Confederate",
                         "commander_number": 2,
                         "commander": "9e1353da-e14e-4a33-9169-19b95b173cd1"})
        # Change US SC009 commander to Quincy Gilmore
        writer.writerow({"BattlefieldCode": "SC009",
                         "belligerent": "US",
                         "commander_number": 1,
                         "commander": "0da38dda-60e3-47f7-a3fa-4f8c10e1900d"})
                        
                                        
def forces_csv(root, dst):
    fields = ('BattlefieldCode', 'belligerent', 'TroopsEngaged', "Casualties")
    with open(dst, 'w') as f:
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
    fields = ("PersonID", "ID", "LastName", "Suffix", "FirstName", "MiddleName", "MiddleInitial", "Keywords", "Rank", "Bio", "BioSource", "NarrativeLink1", "NarrativeLink2")
    with open(dst, 'w') as f:
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
            
def battleunitslink_csv(root, dst):
    fields = (
    'BattlefieldCode',
    'Comment',
    'Source',
    'UnitCode'
    )
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):            
            row = {}
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            for fld in fields:
                row[fld] = properties.find(xmlns('d:%s' % fld)).text
            row['BattlefieldCode'] = row['BattlefieldCode'].upper()
            writer.writerow(row)
            
def units_csv(root, dst):
    fields = (
    'ID',
    'UnitCode',
    'UnitName',
    )
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for i, entry in enumerate(root.findall('.//%s' % xmlns('entry'))):           
            row = {}
            properties = entry.find('./%s/%s' % (xmlns('content'), xmlns('m:properties'))) 
            for fld in fields:
                row[fld] = properties.find(xmlns('d:%s' % fld)).text
            writer.writerow(row) 

def build(src, dst):
    
    parser = ET.XMLParser(encoding = 'cp1252')

    with open(path.join(src, 'battle.xml'), 'rb') as f:
        battles = ET.fromstring(f.read(), parser)    
    commander_csv(battles, path.join(dst, "cwss_commanders.csv"))
    battle_csv(battles, path.join(dst, 'cwss_battles.csv'))
    forces_csv(battles, path.join(dst, 'cwss_forces.csv'))
    theaters_csv(battles, path.join(dst, 'cwss_theaters.csv'))
    campaigns_csv(battles, path.join(dst, 'cwss_campaigns.csv'))

    with open(path.join(src, 'persons.xml'), 'rb') as f:
            persons = ET.fromstring(f.read(), parser)  
    people_csv(persons, path.join(dst, 'cwss_persons.csv'))

    with open(path.join(src, 'battleunitlink.xml'), 'rb') as f:
            battleunitlinks = ET.fromstring(f.read(), parser)  
    battleunitslink_csv(battleunitlinks, path.join(dst, 'cwss_battleunitlinks.csv'))

    with open(path.join(src, 'units.xml'), 'rb') as f:
            battleunitlinks = ET.fromstring(f.read(), parser)  
    units_csv(battleunitlinks, path.join(dst, 'cwss_units.csv'))

def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)

if __name__ == "__main__":
    main()
