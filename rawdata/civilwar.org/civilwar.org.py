# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import json

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://www.civilwar.org/battlefields/"

def get_campaign_small(soup):
    try:
        x = soup.find('h3', class_ = 'alt', text = 'Campaign').\
            find_next_sibling('ul').li.get_text().strip()
    except AttributeError:
        x = None
    return x
        
def get_location_small(soup):
    return soup.find('h3', class_ = 'alt', text = 'Location').\
        find_next_sibling('ul').li.get_text().strip()
        
def get_dates_small(soup):
    return soup.find('h3', class_ = 'alt', text = 'Dates').\
        find_next_sibling('ul').find('li', class_ = 'last').text.strip()
    
def get_result_small(soup):
    return soup.find('h3', class_ = 'alt', text = 'Result').\
        find_next_sibling('ul').find('li').get_text().strip()
        
def get_forces_small(soup):
    try:
        forces = soup.find('h3', class_ = 'alt', text = 'Forces Engaged').\
            find_next_sibling('ul').find_all('li')
        return (forces[0].get_text().strip(), forces[1].get_text().strip())
    except AttributeError:
        return (None, None)
        
def get_casualties_small(soup):
    try:
        forces = soup.find('h3', class_ = 'alt',
                           text = 'Estimated Casualties').\
            find_next_sibling('ul').find_all('li')
        return (forces[0].get_text().strip(), forces[1].get_text().strip())
    except AttributeError:
        return (None, None)    
    
def get_description_small(soup):
    return soup.find('div', id = 'battlefielddesc').get_text().strip()
    
def get_union_commander_small(soup):
    data = []
    try:
        commanders = soup.find('h3', class_ = 'alt',
                                    text = 'Union Commander').\
            find_next_sibling('ul').li.find_all('a')
    
        for cmdr in commanders:
            data.append({'union_commander_name': cmdr.text.strip(),
                         'union_commander_url': cmdr['href']})
    except AttributeError:
        pass
    return data


def get_confederate_commander_small(soup):
    data = []
    try:
        commanders = soup.find('h3', class_ = 'alt',
                                          text = 'Confederate Commander').\
            find_next_sibling('ul').li.find_all('a')
        for cmdr in commanders:
            data.append({'confederate_commander_name': cmdr.text.strip(),
                         'confederate_commander_url': cmdr['href']})
    except AttributeError:
        pass
    return data


def parse_battle_small(soup):
    data = {}
    data['campaign'] = get_campaign_small(soup)
    data['location'] = get_location_small(soup)       
    data['dates'] = get_dates_small(soup)
    data['union_commanders'] = get_union_commander_small(soup)
    data['confederate_commanders'] = get_confederate_commander_small(soup) 
    data['union_forces'], data['confederate_forces'] = get_forces_small(soup)  
    data['result'] = get_result_small(soup)
    data['description'] = get_description_small(soup)
    return data
    
    
def get_description(soup):
    return soup.find('div', class_ = 'battlefield_sub_intro').get_text().strip()
    
def get_alternate_names(soup):
    return soup.find('p', class_ = 'battle-alternate').get_text().strip()
    
def get_location(soup):
    return soup.find('p', class_ = 'battle-location').get_text().strip()
    
def get_campaign(soup):
    try:
        x = soup.find('div', class_ = 'bfs-campaign').p.get_text().strip()
    except AttributeError:
        x = None
    return x
    
def get_battle_dates(soup):
    return soup.find('div', class_ = 'battle-dates').get_text().strip()
    
def get_total_engaged(soup):
    return soup.find('div', class_ = 'bfs-engaged').\
        find('p', text = re.compile('Total:')).get_text().\
        split(':')[1].strip()
        
def get_union_forces(soup):
    return soup.find('div', class_ = 'bfs-engaged').\
        find('div', class_ = 'forces').\
        find('div', class_ = 'union').get_text()
        
def get_confederate_forces(soup):
    return soup.find('div', class_ = 'bfs-engaged').\
        find('div', class_ = 'forces').\
        find('div', class_ = 'confederate').get_text()
        
def get_union_commander(soup):
    commanders = soup.find('div', class_ = 'bfs-commanders').\
        find('div', class_ = 'union').\
        find_all('a')
    data = []
    for cmdr in commanders:
        data.append({'union_commander_name': cmdr.text,
                     'union_commander_url': cmdr['href']})
    return data
        
def get_confederate_commander(soup):
    commanders = soup.find('div', class_ = 'bfs-commanders').\
        find('div', class_ = 'confederate').\
        find_all('a')
    data = []
    for cmdr in commanders:
        data.append({'confederate_commander_name': cmdr.text,
                     'confederate_commander_url': cmdr['href']})
    return data
            
def get_total_casualties(soup):
    return soup.find('div', class_ = 'bfs-casualties').\
        find('p').get_text()
        
def get_union_casualties(soup):
    return soup.find('div', class_ = 'bfs-forces').\
        find('h3', text = 'Union').\
        find_next_sibling('p').get_text()
    
def get_confederate_casualties(soup):    
    return soup.find('div', class_ = 'bfs-forces').\
        find('h3', text = 'Confederate').\
        find_next_sibling('p').get_text()
        
def get_result(soup):
    return soup.find('div', class_ = 'bfs-result').\
        find('p').get_text()
            
def parse_battle_large(soup):
    data = {}
    data['description'] = get_description(soup)  
    data['alternate_names'] = get_alternate_names(soup)
    data['battle_dates'] = get_battle_dates(soup) 
    data['location'] = get_location(soup)
    data['campaign'] = get_campaign(soup)
    data['total_forces'] = get_total_engaged(soup)
    data['union_forces'] = get_union_forces(soup)
    data['confederate_forces'] = get_confederate_forces(soup)
    data['total_casualties'] = get_total_casualties(soup)
    data['union_casualties'] = get_union_casualties(soup)
    data['confederate_casualties'] = get_confederate_casualties(soup)
    data['confederate_commanders'] = get_confederate_commander(soup)
    data['union_commanders'] = get_confederate_commander(soup)
    data['result'] = get_result(soup)
    return data
    
def get_battle_page(href):
    soup = BeautifulSoup(requests.get(href).text, 'lxml')
    if soup.find('li', class_ = 'nav-facts'):
        print('FACTS')
        href += '?tab=facts'
        pg = parse_battle_large(BeautifulSoup(requests.get(href).text, 'lxml'))
        pg['url'] = href
    else:
        pg = parse_battle_small(soup)
        pg['url'] = href
    return pg
    
    
def get_battle_links():
    dst = 'civilwar.org.json'
    html = requests.get(BASE_URL).text
    soup = BeautifulSoup(html, "lxml")
    options = soup.find('select', id = 'myselectbox').find_all('option')[1:]
    battles = dict((x['value'], x.text) for x in options)
    data = []
    for link, name in battles.items():
        print(link)
        btl = get_battle_page(link)
        btl['name'] = name
        data.append(btl)
    with open(dst, 'w') as f:
        json.dump(data, f)

def main():
    pass

if __name__ == "__main__":
    main()