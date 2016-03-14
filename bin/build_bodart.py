""" Create csv files from bodart1908/battles.py """
import csv
import os.path
import sys
import shutil

import yaml
import json

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

def battle_csv(src, dst):
    fields = [
        'battle_id',
        'battle_name',
        'other_names',
        'start_date',
        'end_date',
        'location',
        'state',
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
        for row in data:
            row['other_names'] = ';'.join(row['other_names'])
            for category in CATEGORIES:
                row['category_' + category.lower()] = int(category in row['category'])
            writer.writerow(row)
    print("Writing: %s" % dst)

fields_forces = (
    "battle_id",
    "belligerent",
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
        writer = csv.DictWriter(f, fieldnames, extrasaction = 'ignore')
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle in data:
                for side in battle['forces']:
                    row = battle['forces'][side]
                    row['battle_id'] = battle['battle_id']
                    row['belligerent'] = side
                    writer.writerow(row)
    print("Writing: %s" % dst)

def commanders_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle_id',
                  'belligerent',
                  'full_name',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'suffix',
                  'rank',
                  'dbpedia')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames, extrasaction = 'ignore')
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle in data:
                for side in battle['forces']:
                    for i, row in enumerate(battle['forces'][side]['commanders']):
                          row['battle_id'] = battle['battle_id']
                          row['belligerent'] = side
                          row['rank'] = RANKS[row['rank']]
                          if 'dbpedia' not in row:
                              row['dbpedia'] = None
                          else:
                              row['dbpedia'] = "https://dbpedia.org/resource/%s" % row['dbpedia']
                          writer.writerow(row)
    print("Writing: %s" % dst)

def generals_killed_csv(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    fieldnames = ('battle_id',
                  'belligerent',
                  'full_name',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'suffix',
                  'rank',
                  'date',
                  'dbpedia')
    with open(dst, 'w') as f:
        writer = csv.DictWriter(f, fieldnames, extrasaction = 'ignore')
        writer.writeheader()
        with open(dst, 'w') as f:
            for battle in data:
                for side in battle['forces']:
                    if 'generals_killed' in battle['forces'][side]:
                        for i, row in enumerate(battle['forces'][side]['generals_killed']):
                            row['battle_id'] = battle['battle_id']
                            row['belligerent'] = side
                            row['rank'] = RANKS[row['rank']]
                            if 'dbpedia' not in row:
                                row['dbpedia'] = None
                            else:
                                row['dbpedia'] = "https://dbpedia.org/resource/%s" % row['dbpedia']
                            writer.writerow(row)
    print("Writing: %s" % dst)

def bodart_to_cwsac(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    ret = []
    for battle in data:
        if 'cwsac' in battle:
            ret.append({'battles_from': [battle['battle_id']],
                        'battles_to': battle['cwsac']['ids'],
                        'relation': battle['cwsac']['relation']})
    with open(dst, 'w') as f:
        json.dump(ret, f)
    print("Writing: %s" % dst)

def bodart_to_dbpedia(src, dst):
    with open(src, 'r') as f:
        data = yaml.load(f)
    ret = []
    for battle in data:
        if 'cwsac' in battle:
            ret.append({'battles_from': [battle['battle_id']],
                        'battles_to': battle['dbpedia']['ids'],
                        'relation': battle['dbpedia']['relation']})
    with open(dst, 'w') as f:
        json.dump(ret, f)
    print("Writing: %s" % dst)

def build(src, dst):
    srcdir = os.path.join(src, "rawdata", "bodart1908")
    filename = os.path.join(srcdir, "bodart.yaml")
    battle_csv(filename, os.path.join(dst, "bodart1908_battles.csv"))
    forces_csv(filename, os.path.join(dst, "bodart1908_forces.csv"))
    commanders_csv(filename, os.path.join(dst, "bodart1908_commanders.csv"))
    generals_killed_csv(filename, os.path.join(dst, "bodart1908_generals_killed.csv"))
    bodart_to_cwsac(filename, os.path.join(dst, "bodart1908_to_cwsac.json"))
    bodart_to_dbpedia(filename, os.path.join(dst, "bodart1908_to_dbpedia.json"))


def main():
    print("Building Bodart data")
    src, dst = sys.argv[1:3]
    build(src, dst)

if __name__ == "__main__":
    main()
