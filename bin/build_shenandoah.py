#!/usr/bin/env python3
import sys
import os
import fnmatch
from os import path
import csv
import datetime
import json

import yaml


def load_data(src):
    data = []
    for filename in os.listdir(path.join(src, "yaml")):
        if fnmatch.fnmatch(filename, "*.yaml"):
            fn = path.join(src, "yaml", filename)
            with open(fn, 'r') as f:
                data.append(yaml.load(f))
    return data
    
def clean_battle(battle):
    row = {}
    if 'Number' not in battle:
        print(battle['Battle'])
    row['battle_number'] = battle['Number']
    row['battle_name'] = battle['Battle']
    row['cwsac_id'] = battle['CWSAC']
    row['start_date'] = datetime.datetime.strptime(battle['Start Date'], "%d %B %Y").\
        strftime("%Y-%m-%d")
    try:
        row['end_date'] = datetime.datetime.strptime(battle['End Date'], "%d %B %Y").\
            strftime("%Y-%m-%d")
    except KeyError:
        row['end_date'] = row['start_date']
    row['campaign'] = battle['Campaign']
    return row
    
def build_battles(data, dst):
    battles = [clean_battle(x) for x in data]
    fieldnames = ('battle_number',
                  'battle_name',
                  'cwsac_id',
                  'start_date',
                  'end_date',
                  'campaign')
    with open(path.join(dst, 'shenandoah_battles.csv'), 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(battles)
        
def clean_forces(battle):
    forces = []
    for i in ("U", "C"):
        x = {}
        x["battle_number"] = battle["Number"]
        x["cwsac_id"] = battle["CWSAC"]
        if i == "U":
            x["belligerent"] = "US"
        else:
            x["belligerent"] = "Confederate"
        x['description'] = battle["Forces Engaged"][i]["text"]
        try:
            x['strength_min'] = battle["Forces Engaged"][i]["strength_min"]
            x['strength_max'] = battle["Forces Engaged"][i]["strength_max"]
        except KeyError:
            x['strength_min'] = battle["Forces Engaged"][i]["strength"]
            x['strength_max'] = battle["Forces Engaged"][i]["strength"]
        x['casualties_text'] = battle["Casualties"][i]["text"]
        for j in ("casualties", "killed", "wounded", "missing_captured"):
            x[j] = battle["Casualties"][i][j]
        forces.append(x)
    return forces
        
def build_forces(data, dst):
    fieldnames = ('battle_number',
                  'cwsac_id',
                  'belligerent',
                  'description',
                  'strength_min',
                  'strength_max',
                  'casualties_text',
                  'casualties',
                  'killed',
                  'wounded',
                  'missing_captured')
    with open(path.join(dst, 'shenandoah_forces.csv'), 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in data:
            writer.writerows(clean_forces(battle))
            
def clean_commanders(battle):
    ret = []
    for i in ("U", "C"):
        x = {}
        x["battle_number"] = battle["Number"]
        x["cwsac_id"] = battle["CWSAC"]
        if i == "U":
            x["belligerent"] = "US"
        else:
            x["belligerent"] = "Confederate"
        commanders = battle["Principal Commanders"][i]
        for cmdr in commanders:
            for j in ("last_name", "first_name", "middle_name", "rank"):
                try:
                    x[j] = cmdr[j]
                except KeyError:
                    x[j] = None
        ret.append(x)
    return ret
    
def build_commanders(data, dst):
    fieldnames = ('battle_number',
                  'cwsac_id',
                  'belligerent',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'rank')
    with open(path.join(dst, 'shenandoah_commanders.csv'), 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle in data:
            writer.writerows(clean_commanders(battle))
            
def build_json(data, dst):
    with open(path.join(dst, 'shenandoah.json'), 'w') as f:
        json.dump(data, f)
    
def build(src, dst):
    data = load_data(src)
    build_battles(data, dst)
    build_forces(data, dst)
    build_commanders(data, dst)
    build_json(data, dst)
 
def main():
    src, dst = sys.argv[1:3]
    #src = "../rawdata/shenandoah"
    #dst = "../data"
    build(src, dst)

if __name__ == "__main__":
    main()
