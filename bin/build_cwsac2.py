#!/usr/bin/env python3
""" Convert cwsac.json to csv files """
import json
import csv
import sys
import shutil
from os import path

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

battle_fields = (#'belligerents',
     'battle',
     'battle_name',
     'state',
     # 'locations',
     'campaign',
     'url',
     'forces_text',
     'strength',
     'results_text',
     'result',
     #'dates',
     'study_area',
     'core_area',
     'potnr_boundary'
)

def battle_csv(data, filename):
    # keys = set()
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, battle_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            # for k in battle_data:
            #     keys.add(k)
            row = dict_subset(battle_data, battle_fields)
            writer.writerow(row)

forces_fields = ('battle',
 'belligerent',
 'description',
 #'commanders',
 'strength',
 'regiments',
 'companies',
 'brigades',
 'divisions',
 'corps',
 'armies',
 'cavalry_regiments',
 'cavalry_brigades',
 'cavalry_divisions',
 'cavalry_corps',
 'cavalry_companies',
 'artillery_batteries',
 'artillery_companies',
 'artillery_regiments',
 'artillery_sections',
 'infantry_regiments',
 'strength_other',
 'ships',
 'guns',
)

def forces_csv(data, filename):
    # fields = set()
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, forces_fields)
        writer.writeheader()
        for battle, battle_data in data.items():
            for belligerent, x in battle_data['forces'].items():
                # for k in x:
                #     fields.add(k)
                row = dict_subset(battle_data, forces_fields)
        for battle, battle_data in sorted(data.items()):
            for belligerent, force_data in sorted(battle_data['forces'].items()):
                row = dict_subset(force_data, forces_fields)
                row['battle'] = battle
                row['belligerent'] = belligerent
                writer.writerow(row)
    # print(fields)

commanders_fields = ('battle', 'belligerent', 'fullname', 'rank',
                     'last_name', 'first_name', 'middle_name', 'suffix')

def commanders_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, commanders_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            for belligerent, x in sorted(battle_data['forces'].items()):
                for commander in x['commanders']:
                    row = commander.copy()
                    row['battle'] = battle
                    row['belligerent'] = belligerent
                    writer.writerow(row)

def dates_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, ('battle', 'spell', 'start_date', 'end_date'))
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            for spell in battle_data['dates']:
                row = spell.copy()
                row['battle'] = battle
                writer.writerow(row)

def locations_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, ('battle', 'state', 'location'))
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            for spell in battle_data['locations']:
                row = spell.copy()
                row['battle'] = battle
                writer.writerow(row)

def copy_json(src, dst):
    shutil.copy(path.join(src, 'cwsac2.json'), dst)
    
def build(src, dst):
    with open(path.join(src, "cwsac2.json"), 'r') as f:
        data = json.load(f)
    
    battle_csv(data, path.join(dst, 'cwsac2_battles.csv'))
    forces_csv(data, path.join(dst, 'cwsac2_forces.csv'))
    commanders_csv(data, path.join(dst, 'cwsac2_commanders.csv'))
    dates_csv(data, path.join(dst, 'cwsac2_dates.csv'))
    locations_csv(data, path.join(dst, 'cwsac2_locations.csv'))
    copy_json(src, dst)
    
                
def main():
    SRC = sys.argv[1]
    DST = sys.argv[2]
    build(SRC, DST)

if __name__ == "__main__":
    main()
    
