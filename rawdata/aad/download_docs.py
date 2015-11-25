# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 06:13:35 2014

Download the field descriptions for each field of the  Records About Civil War Battle Sites, created 1990 - 1993, documenting the period 4/12/1861 - 5/13/1865. - Record Group 220

@author: jrnold
"""

import os
import os.path
import re

import requests

from bs4 import BeautifulSoup

DST_DIR = 'docs/field_info'
# arbitrary, just needed on
URL = "http://aad.archives.gov/aad/record-detail.jsp?dt=295&mtch=385&cat=WR25&tf=F&sc=16478,16486,16479,16480,16488&bc=,sl,fd&txt_16479=01%2F01%2F1861&op_16479=6&nfo_16479=D,8,1861&txt_16480=12%2F31%2F1865&op_16480=4&nfo_16480=D,8,1861&sort=16478%20desc&rpp=10&pg=1&rid=320&rlst=320,314,323,3,2,1,321,9,6,10"
BASE_URL = "http://aad.archives.gov/aad"
DST_JSON = 'events.json'

if not os.path.exists(DST_DIR):
    os.makedirs(DST_DIR)
    
def get_field_info(row):
    cols = row.find_all('td')
    href = re.search(r"javascript:popup\('(.*?)',", cols[0].a['href']).group(1)
    url = '%s/%s' % (BASE_URL, href)
    print (url)
    r = requests.get(url)
    field = cols[0].a.contents[0].strip()
    return (field, r.text)

soup = BeautifulSoup(requests.get(URL).text, 'html5lib')
table = soup.find('div', id='content').table
for row in table.find_all('tr')[1:]:
    field, info = get_field_info(row)
    print(field)
    with open(os.path.join(DST_DIR, '%s.html' % field), 'w') as f:
        f.write(info)
        print("writing to %s.html" % field)
       
 
            
    
  
    
