# -*- coding: utf-8 -*-
"""
List of people and links of biographies from civilwar.org
"""
import sys
import os.path
import json

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://www.civilwar.org/education/history/biographies"

def parse_bio_link(el):
    name = el.a.next.replace('»', '').strip()
    url = el.a['href']
    rank = el.a.em.text.strip()
    return {'name': name, 'url': url, 'rank': rank}
    

def parse_bio_list(el):
    data = []
    for li in el.find_all('li'):
        data.append(parse_bio_link(li))
    return data
    
def get_bio_list(soup, id):
    return parse_bio_list(soup.find('div', id = id))

def get_history_biographies():
    html = requests.get(BASE_URL).text
    soup = BeautifulSoup(html, "lxml")
    list_ids = {'Confederate': 'templatelist-140006199',
               'Union': 'templatelist-140006197'}
    return dict((k, get_bio_list(soup, v)) for k,v in list_ids.items()) 

def write_links(dst):
    links = get_history_biographies()
    with open(dst, 'w') as f:
        json.dump(links, f)

def main():
    dst = 'biographies_links.json'
    write_links(dst)

if __name__ == "__main__":
    main()
