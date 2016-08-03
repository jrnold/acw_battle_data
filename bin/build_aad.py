#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import csv
import sys
import datetime
import shutil
import re
from os import path
import urllib.parse

def yn(x):
    return 1 if x.lower() == "y" else 0

def rm_na(x):
    return x if x in "N/A" else None

def tf(x):
    return 1 if x.lower() == "true" else 0

def clean_sig(x):
    x = x.strip()
    if len(x) > 1:
        x = x[0]
    return x

fields = (
    "reference_number",
    "event",
    "type",
    "start_date",
    "end_date",
    "theater",
    "campaign",
    "threats",
    "ownership_federal",
    "ownership_local",
    "ownership_private",
    "ownership_state",
    "ownership_unknown",
    "park",
    "integrity",
    "military",
    "interpretive_political",
    "interpretive_commander_loss",
    "interpretive_casualties",
    "interpretive_tactics_strategy",
    "interpretive_public_mind",
    "interpretive_combat_arm",
    "interpretive_military_firsts",
    "interpretive_minority_troops",
    "interpretive_economic",
    "interpretive_archaelolgical",
    "interpretive_logistics",
    "interpretive_individual_bravery",
    "interpretive_group_behavior",
    "interpretive_joint_ops",
    "interpretive_coop_armies",
    "interpretive_naval",
    # "comments",
    # "dispute",
    "military_jim",
    "military_ed",
    "military_bill",
    "protected_acres",
    "protected_percent",
    "county",
    # "acreage",
    # "unprotect",
    "land_value",
    "priority1",
    "url"
)

def build(src, dst):
    with open(path.join(src, "rawdata", "aad", "events.json"), 'r', encoding="utf8") as f:
        data = json.load(f)

    rows = []
    for k, v in sorted(data.items(), key = lambda x: x[1]["Reference Number"]["value"]):
        row = {}
        row["url"] = k
        row["reference_number"] = v["Reference Number"]["value"].upper()
        row["event"] = v["Event"]["meaning"]
        row["type"] = v["Type"]["meaning"]
        row["start_date"] = datetime.datetime.strptime(v["Date1"]["meaning"], "%m/%d/%Y").\
            strftime("%Y-%m-%d")
        row["end_date"] = datetime.datetime.strptime(v["Date2"]["meaning"], "%m/%d/%Y").\
            strftime("%Y-%m-%d")
        row["theater"] = v["Theater Code"]["meaning"]
        row["campaign"] = v["Campaign Code"]["meaning"]
        row["threats"] = rm_na(v["Threats"]["value"])
        row["ownership_federal"] =  yn(v["Ownership: Federal Government"]["value"])
        row["ownership_local"] =  yn(v["Ownership: Local Government"]["value"])
        row["ownership_private"] =  yn(v["Ownership: Private"]["value"])
        row["ownership_state"] =  yn(v["Ownership: State Government"]["value"])
        row["ownership_unknown"] =  yn(v["Ownership: Unknown"]["value"] )
        row["park"] =  tf(v["Park"]["value"])
        row["integrity"] =  v["Integrity"]["value"]
        row["military"] =  v["Military"]["value"]
        row["interpretive_political"] = yn(v["Interpretive Potential: Effect Upon Regional or State Political Situation"]["value"])
        row["interpretive_commander_loss"] = yn(v["Interpretive Potential: Loss of Significant Commander (Wounding, Death, Relieved of Command)"]["value"])
        row["interpretive_casualties"] = yn(v["Interpretive Potential: Unusually High Casualties"]["value"])
        row["interpretive_tactics_strategy"] = yn(v["Interpretive Potential: Illustrates Important Lessons in Military Tactics and Strategy"]["value"])
        row["interpretive_public_mind"] = yn(v["Interpretive Potential: Unusual Importance in the Public Mind and Imagination"]["value"])
        row["interpretive_combat_arm"] = yn(v["Interpretive Potential: Significant Participation of Cavalry, Artillery, or Other Single Combat Arm"]["value"])
        row["interpretive_military_firsts"] = yn(v["Interpretive Potential: Military Firsts"]["value"])
        row["interpretive_minority_troops"] = yn(v["Interpretive Potential: Participation of Significant Numbers of Minority Troops"]["value"])
        row["interpretive_economic"] = yn(v["Interpretive Potential: Significant Economic Consequences"]["value"])
        row["interpretive_archaelolgical"] = yn(v["Interpretive Potential: High Archaeological Potential"]["value"])
        row["interpretive_logistics"] = yn(v["Interpretive Potential: Unusually Significant Logistics or Supply Feat"]["value"])
        row["interpretive_individual_bravery"] = yn(v["Interpretive Potential: Exceptional Individual Initiative in Bravery or Command"]["value"])
        row["interpretive_group_behavior"] = yn(v["Interpretive Potential: Exceptional Group Behavior"]["value"])
        row["interpretive_joint_ops"] = yn(v["Interpretive Potential: Illustrates Joint Operations (Army_Navy)"]["value"])
        row["interpretive_coop_armies"] = yn(v["Interpretive Potential: Illustrates Cooperation of Separate Military Departments or Armies"]["value"])
        row["interpretive_naval"] = yn(v["Interpretive Potential: Naval Operations"]["value"])
    #    row["comments"] =  v["Comments"]["meaning"]
    #    row["dispute"] =  v["Dispute"]["meaning"]
        row["military_jim"] =  clean_sig(v["Jim"]["value"])
        row["military_ed"] =  clean_sig(v["Ed"]["value"])
        row["military_bill"] =  clean_sig(v["Bill"]["value"])
        row["protected_acres"] =  v["Protected"]["value"]
        row["protected_percent"] =  v["Percent"]["value"]
        row["county"] =  v["County"]["value"]
        #row["acreage"] =  v["Acreage"]["value"]
        #row["unprotect"] =  v["Unprotect"]["value"]
        row["land_value"] =  v["Value"]["value"]
        row["priority1"] =  tf(v["Priority1"]["value"])
        rows += [row]

    dst_file = path.join(dst, "aad_battles.csv")
    with open(dst_file, 'w', encoding="utf8") as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        writer.writerows(rows)
    print("Writing: %s" % dst_file)

def copy_files(src, dst):
    src_file = path.join(src, "rawdata", "aad", "events.json")
    dst_file = path.join(dst, 'aad_events.json')
    shutil.copy(src_file, dst_file)
    print("Writing: %s" % dst_file)

def main():
    print("Building AAD data")
    src = sys.argv[1]
    dst = sys.argv[2]
    build(src, dst)
    copy_files(src, dst)

if __name__ == "__main__":
    main()
