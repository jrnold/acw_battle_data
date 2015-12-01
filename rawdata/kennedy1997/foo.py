import csv
import yaml
import json
import os
from os import path

STATES = {'North Dakota' : 'ND',
 'Colorado' : 'CO',
 'South Carolina' : 'SC',
 'Indiana' : 'IN',
 'West Virginia' : 'WV',
 'Oklahoma' : 'OK',
 'Kentucky' : 'KY',
 'Idaho' : 'ID',
 'North Carolina' : 'NC',
 'Ohio' : 'OH',
 'Arkansas' : 'AR',
 'Alabama' : 'AL',
 'District of Columbia' : 'DC',
 'Louisiana' : 'LA',
 'Florida' : 'FL',
 'Tennessee' : 'TN',
 'Georgia' : 'GA',
 'Missouri' : 'MO',
 'Mississippi' : 'MS',
 'Maryland' : 'MD',
 'Pennsylvania' : 'PA',
 'Texas' : 'TX',
 'Virginia' : '',
 'Minnesota' : 'MN',
 'New Mexico' : 'NM',
 'Kansas': 'KS'}

with open('kennedy1997.yaml', 'r') as f:
    data = yaml.load(f)

for battle in data:
    data[battle]['state'] = STATES[data[battle]['state'].strip()]

with open('kennedy1997.yaml', 'w') as f:
    data = yaml.dump(data, f, default_flow_style = False)
