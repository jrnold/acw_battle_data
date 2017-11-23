import datetime
import re
import os
from ruamel.yaml import YAML
yaml = YAML(typ='safe')
yaml.default_flow_style = False
yaml.representer.ignore_aliases = lambda x: True


def iter_files():
    outdir = 'engagements'
    for filename in os.listdir(outdir):
        fn = os.path.join(outdir, filename)
        state, ext = os.path.splitext(fn)
        state = state.split("/")[1]
        if ext == '.yml':
            with open(fn, 'r') as fp:
                data = yaml.load(fp)
            yield (state, data


from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF, UnorderedGroup, OrderedChoice, Sequence
from arpeggio import RegExMatch as _
from arpeggio import ParserPython

def ordinal():
    return _('\d+(st|nd|rd|th)')

def punct():
    return _("[.,;:]")

def integer():
    return _("\d+")

def list_sep():
    return [(",", "and"), ",", "and"]

def quoted(x):
    return ('"', x, '"')

def parens(x):
    return ("(", x, ")")


NAVY_ORG = ["UNITED STATES NAVY", ]

SHIP_NAMES = [
    "Conestoga",
    "Lexington",
    "Tyler",
    "Brooklyn",
    "Octorora",
    "Hartford",
    "Ossippee",
    "Itasca",
    "Oneida",
    "Galena",
    "Metacomet",
    "Richmond",
    "Port Royal",
    "Lackawanna",
    "Seminole",
    "Monongahela",
    "Tecumseh"
]

def ship():
    return quoted(SHIP_NAMES)

def ship_list():
    """Lists of Ships

    - U. S. Gunboats "Conestoga", "Lexington" and "Tyler".

    """
    return ship(), ZeroOrMore(Optional(list_sep), ship())

def navy_units():
    return NAVY_ORG, _('-+'), ship_list()


ARMY_ORG = [
  ("ALABAMA", Optional(("and", "TENNESSEE"))),
 'ARKANSAS',
 'CALIFORNIA',
 'COLORADO',
 'CONNECTICUT',
 'DAKOTA',
 'DELAWARE',
 'DISTRICT OF COLUMBIA',
 'FLORIDA',
 'IDAHO TERRITORY',
 'ILLINOIS',
 ("INDIANA", Optional("LEGION")),
 'IOWA',
 'KANSAS',
 'KENTUCKY',
 'LOUISIANA',
 'MAINE',
 'MARYLAND',
 'MASSACHUSETTS',
 'MICHIGAN',
 'MINNESOTA',
 ('MISSISSIPPI', Optional(("MARINE", "BRIGADE"))),
 'MISSOURI',
 'NEBRASKA',
 'NEVADA',
 'NEW HAMPSHIRE',
 'NEW JERSEY',
 'NEW MEXICO',
 'NEW YORK',
 'NORTH CAROLINA',
 'OHIO',
 'OREGON',
 'PENNSYLVANIA',
 'RHODE ISLAND',
 'SOUTH CAROLINA',
 'TENNESSEE',
 'TEXAS',
 ('UNITED', 'STATES', Optional([("COLORED", "TROOPS")])),
 'VERMONT',
 'VIRGINIA',
 'WASHINGTON',
 'WEST VIRGINIA',
 'WISCONSIN']

def army_org():
    return ARMY_ORG

NAMED_UNITS = [
    "Landgraeber's Battery F, 2nd Light Artillery",
    "Landgraeber's Battery Flying Artillery",
    "Landgraeber's Battery Flying Artillery ("F" 2nd Artillery)",
    "Cogswell's Independent Battery Light Artillery"
    "Latham's Co. Cavalry",
    "Chicago Board of Trade Battery Light Artillery",
    "Fremont's Hussars",
    "Benton Hussars",
    "Bowen's Battalion Cavalry",
    "Jenks' and Smith's Cavalry Cos.",
    "Phelps' Regt. Infantry",
    "5th Co. Sharpshooters.",
    "Wright's Battalion Cavalry",
    "Jenks' and Smith's Cavalry Cos.",
]

def named_unit():
    return sorted(NAMED_UNITS, key=lambda x: -len(x))

def army_unit_name():
    """Single unit name

    - 1st Cavalry (Detachment)
    - 5th Cavalry
    - Battery "B", 1st Light Artillery

    """
    return [named_unit,
            ordinal_unit_list,
            artillery_battery
           ]


def army_units():
    """Lists of Units.

    - KENTUCKY--5th Cavalry
    - PENNSYLVANIA--7th Cavalry (Detachment); 78th and 79th Infantry

    """
    return ARMY_ORG, _('-+'), (OneOrMore(army_unit_name, Optional(punct)))


def units():
    return [navy_units(), army_units()]

def unit_list():
    return ZeroOrMore(units(), Optional(punct()))


def one_battery():
    return "Battery", quoted_letter

def multiple_batteries():
    return "Batteries", OneOrMore(Optional(list_sep), quoted_letter)

def artillery_battery():
    """Artillery Batteries.

    - "Battery \"B\", 1st Light Artillery (Section)"

    """
    return (Optional("Independent"),
            [one_battery, multiple_batteries],
            Optional(punct),
            Optional(ordinal),
            Optional("Independent"),
            Optional(["Light", "Heavy"]), "Artillery",
            Optional([section, detachments])
           )

ex = "Battery \"B\", 1st Light Artillery"
print(ParserPython(artillery).parse(ex))
ex = "Battery \"B\", 1st Light Artillery (Section)"
print(ParserPython(artillery).parse(ex))
