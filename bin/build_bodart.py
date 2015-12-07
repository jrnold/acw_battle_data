""" Create csv files from bodart1908/battles.py """
import csv
import os.path
import sys
import shutil

import nameparser
import yaml

RANKS = {"Gen.-Lt." : "Lt. Gen", # "General-Leutnant",
         "Gen." : "Gen.", # "General",
         "GM." : "Maj. Gen.", # "General-Major",
         "Adm." : "Adm.", # "Admiral",
         "GL." : "Lt. Gen.", # "General-Leutnant",
         "BM." : "Brig. Gen.", # "Brigade-General",
         "Brig.-Gen." : "Brig. Gen.", # "Brigade-General",
         "Oberst" : "Col.", # "Oberst",
         "B.-G." : "Brig. Gen.", # "Brigade-General",
         "Brig. Gen." : "Brig. Gen.", # "Brigade-General",
         "komm. Gen." : "Gen.", # "General",
         "Brig-Gen." : "Brig. Gen.", # Brigade-General",
         "G.-L." : "Lt. Gen.", # "General-Leutnant",
         "Brigadier Obst." : "Col.", # Brigadier Oberst" 
}

CATEGORIES = ("Schlacht",
              "Treffen",
              "Kapitulation",
              "Einnahme",
              "Belagerung",
              )


def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

fields_forces = (
    "battle_id",
    "belligerent",
    "victor",
    "strength",
    "strength_engaged",
    "infantry",
    "cavalry",
    "artillery",
    "guns",
    "killed",
    "killed_percent",    
    "killed_generals",
    "killed_officers",
    "killed_wounded",
    "killed_wounded_percent",
    "killed_wounded_generals",
    "killed_wounded_officers",
    "wounded",
    "wounded_percent",
    "wounded_generals",
    "wounded_officers",
    "captured",
    "captured_generals",
    "captured_officers",
    "missing",
    "missing_percent",
    "missing_generals",
    "missing_officers",
    "casualties",
    "casualties_percent",
    "casualties_officers",
    "casualties_generals",
    "losses_guns",
    "losses_caissons",
    "losses_cannon",
    "losses_canons",
    "losses_flags",
    "losses_munition_wagons",
    "losses_wagons",
    "note"
)

def forces_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = fields_forces
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle_id, v in enumerate(data):
                for side in ('victor', 'loser'):
                    row = dict_subset(v[side], fieldnames)
                    row['victor'] = (side == 'victor')
                    row['battle_id'] = battle_id
                    writer.writerow(row)

def commanders_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle_id',
                  'belligerent',
                  'name',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'suffix',
                  'rank',
                  'dbpedia')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle_id, v in enumerate(data):
                for side in ('victor', 'loser'):
                    if 'commanders' in v[side]:
                      cmdrs = v[side]['commanders']
                      for cmdr in cmdrs:
                          row = cmdr.copy()
                          row['battle_id'] = battle_id
                          row['belligerent'] = v[side]['belligerent']
                          row['rank'] = RANKS[row['rank']]
                          if 'dbpedia' not in row:
                              row['dbpedia'] = None
                          else:
                              row['dbpedia'] = "https://dbpedia.org/resource/%s" % row['dbpedia']
                          writer.writerow(row)

def generals_killed_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle_id',
                  'belligerent',
                  'name',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'suffix',
                  'rank', 
                  'date',
                  'dbpedia')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle_id, v in enumerate(data):
                for side in ('victor', 'loser'):
                    if 'generals_killed' in v[side]:
                        for x in v[side]['generals_killed']:
                            row = x.copy()
                            row['battle_id'] = battle_id
                            row['belligerent'] = v[side]['belligerent']
                            row['rank'] = RANKS[row['rank']]
                            if 'dbpedia' not in row:
                                row['dbpedia'] = None
                            else:
                                row['dbpedia'] = "https://dbpedia.org/resource/%s" % row['dbpedia']
                            writer.writerow(row)
                    
def battle_csv(src, dst):
    fields = [
        'battle_id',
        'name',
        'other_names', 
        'start_date',
        'end_date',
        'location',
        'category_schlacht',
        'category_treffen',
        'category_belagerung',
        'category_kapitulation',
        'category_einnahme',
        'category_size',
        'page'
    ]
    with open(src, 'r') as f:
        data = yaml.load(f)
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fields, extrasaction = 'ignore')
        writer.writeheader()
        for battle_id, row in enumerate(data):
            row['other_names'] = ';'.join(row['other_names'])
            row['battle_id'] = battle_id
            for category in CATEGORIES:
                row['category_' + category.lower()] = int(category in row['category'])
            writer.writerow(row)

def bodart_to_cwsac(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('from', 'to', 'relation')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle_id, v in enumerate(data):
            if 'cwsac' in v:
                for link in v['cwsac']:
                    row = {'from': battle_id,
                           'to': link['uri'],
                           'relation': link['relation']}
                    writer.writerow(row)
                

def bodart_to_dbpedia(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('from', 'to', 'relation')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for battle, v in enumerate(data):
            if 'dbpedia' in v:
                for link in v['dbpedia']:
                    row = {'from': battle,
                           'to': link['uri'],
                           'relation': link['relation']}
                    writer.writerow(row)

def build(src, dst):
    filename = os.path.join(src, "bodart.yaml")
    battle_csv(filename, os.path.join(dst, "bodart1908_battles.csv"))
    forces_csv(filename, os.path.join(dst, "bodart1908_forces.csv"))
    commanders_csv(filename, os.path.join(dst, "bodart1908_commanders.csv"))
    generals_killed_csv(filename, os.path.join(dst, "bodart1908_generals_killed.csv"))
    bodart_to_cwsac(filename, os.path.join(dst, "bodart1908_to_dbpedia.csv"))
    bodart_to_dbpedia(filename, os.path.join(dst, "bodart1908_to_cwsac.csv"))

    
def main():
    src, dst = sys.argv[1:3]
    build(src, dst)
    
if __name__ == "__main__":
    main()
