# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 06:13:35 2014

Get all records from the NARA Access to Archival Databases (AAD) series:
Records About Civil War Battle Sites, created 1990 - 1993, documenting the period 4/12/1861 - 5/13/1865 - Record Group 220

- html pages with the search results were downloaded manually on Nov 18, 2014
- this follows each link in those pages, and for each link
   - downloads and saves the page
   - parses the html and extracts the data from the table
- the data for all events is written to a json file

@author: jrnold
"""

import os
import os.path
import re
import json
import urllib.parse

import requests

from bs4 import BeautifulSoup

FILENAME = "indices/NARA - AAD - Display Partial Records - Events File, 4 12 1861 - 5 13 1865 page %d.html"
MAX_PAGE = 8
DST_DIR = 'records'
BASE_URL = 'http://aad.archives.gov/aad'
DST_JSON = 'events.json'

if not os.path.exists(DST_DIR):
    os.makedirs(DST_DIR)
    
def get_battle(x):
    return soup2.find('div', id='content').table.find_all('tr')[1].\
        find_all('td')[1].contents[0].strip()

def parser(x):
    data = {}
    table = x.find('div', id = 'content').table
    for row in table.find_all('tr')[1:]:  
        cols = row.find_all('td')
        field = cols[0].a.contents[0].strip()
        value = cols[1].contents[0].strip()
        meaning = cols[2].contents[0].strip()
        data[field] = {'value': value, 'meaning': meaning}
    return data

nrecords = 0
events = {}   
for i in range(1, MAX_PAGE + 1):
    with open(FILENAME % i, 'r') as f:
        soup = BeautifulSoup(f, 'html5lib')
        table = soup.find('table', id = 'queryResults').tbody
        for row in table.find_all('tr'):
            href = re.sub('\n', '', row.find_all('td')[0].a['href'])
            r = requests.get('%s/%s' % (BASE_URL, href))
            text = r.text
            soup2 = BeautifulSoup(text, 'html5lib')
            battle = get_battle(soup2)
            with open(os.path.join(DST_DIR, '%s.html' % battle), 'w') as f2:
                f2.write(text)
                print("writing to %s/%s.html" % (DST_DIR, battle))

            parsed_url = urllib.parse.urlparse(href)
            params1 = urllib.parse.parse_qs(parsed_url.query)
            params2 = {'dt': params1['dt'][0],
                       'rid': params1['rid'][0]}
            url = urllib.parse.urlunparse(('http:', 
                                           'aad.archives.gov',
                                           'aad' + '/' + parsed_url.path,
                                           '',
                                           urllib.parse.urlencode(params2),
                                           ''))
            events[url] = parser(soup2)
            nrecords += 1

with open(DST_JSON, 'w') as f:
    json.dump(events, f, indent=1)
    print("writing to %s" % DST_JSON)
            
 
            
    
  
    
