import re
import csv

EXAMPLES = (
"NEW YORK--15th Cavalry. Union loss, 1 killed, 1 wounded. Total, 2.",
"NEW YORK--5th Cavalry. PENNSYLVANIA--18th Cavalry. Union loss, 40 killed and wounded.",
"INDIANA--3d Cavalry. MAINE--16th Infantry. MASSACHUSETTS--12th, 13th and 39th Infantry. NEW HAMPSHIRE--1st Cavalry. NEW JERSEY--3d Cavalry. NEW YORK--8th and 22d Cavalry; 94th, 97th and 104th Infantry. PENNSYLVANIA--11th, 88th, 90th, 107th, 190th and 191st Infantry. VERMONT--1st Cavalry. UNITED STATES--Battery \"C & E\" 4th Arty. Union loss (including Riddell's Shop), 50 killed, 250 wounded. Total, 300.",
"WEST VIRGINIA--6th Cavalry. Union loss, 2 wounded.",
"MARYLAND--1st P. H. B. Cavalry; Battery \"B\" Light Arty. NEW YORK--1st Lincoln, 1st Veteran, 15th and 21st Cavalry; 20th Indpt. Battery Light Arty. OHIO--8th Cavalry; 34th Mounted Infantry. PENNSYLVANIA--14th, 20th and 22d Cavalry. WEST VIRGINIA--1st, 2d, 5th and 7th Cavalry; Batteries \"B\" and \"D,\" Light Arty.; 11th and 15th Infantry. UNITED STATES--Battery \"B,\" 5th Arty. Union loss, 15 killed and missing.",
"NEW YORK--19th Cavalry. PENNSYLVANIA--6th Cavalry. Union loss, 4 killed, 20 wounded. Total, 24.",
"MASSACHUSETTS--2d Cavalry. MICHIGAN--1st, 5th, 6th and 7th Cavalry. NEW YORK--4th, 6th, 9th and 19th Cavalry. PENNSYLVANIA--6th and 17th Cavalry. UNITED STATES--1st and 2d Cavalry; Batteries \"B & L,\" and \"D,\" 2d Arty. Union loss, 30 killed, 70 wounded, 200 captured and missing. Total, 300.",
"INDIANA--20th Infantry. UNITED STATES--2d Sharpshooters. Union loss, 8 killed, 14 wounded, 59 missing. Total, 81.",
"INDIANA--1st Cavalry (Detachment); 43d Infantry. IOWA--36th Infantry. KANSAS--5th Cavalry > > (Detachment). MISSOURI--7th Cavalry (Detachment); Battery \"E,\" 2d Light Arty. OHIO--77th Infantry. Union loss, 100 killed, 250 wounded, 1100 captured and missing. Total, 1450."
)

# with open('engagements.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     data = [row for row in reader]

# makes it easier to pick out the pattern, especially numbers
def remove_punct(x):
    return re.sub(r'[^0-9A-Za-z\s]', '', x)

def spaces(x):
    return re.sub(r'\s+', ' ', x)

RE_KWM = re.compile(r"(\d+) killed wounded and missing", re.I)
RE_KW = re.compile(r"(\d+) killed and wounded(?! (and|wounded|missing|captured))", re.I)
RE_K = re.compile(r"(\d+) killed(?! (and|wounded|missing|captured))", re.I)
RE_W = re.compile(r"(\d+) wounded", re.I)
RE_M = re.compile(r"(\d+) missing", re.I)
RE_CM = re.compile(r"(\d+) captured and missing", re.I)
RE_TOTAL = re.compile(r"total (\d+)", re.I)

def regroup(regex, x):
    m = regex.search(x)
    if m:
        return m.group(1)

def parse_losses(x):
    x = spaces(remove_punct(x))
    d = {}
    d['kwm'] = regroup(RE_KWM, x)
    d['kw'] = regroup(RE_KW, x)
    d['k'] = regroup(RE_K, x)
    d['w'] = regroup(RE_W, x)
    d['m'] = regroup(RE_M, x)
    d['mp'] = regroup(RE_CM, x)
    d['total'] = regroup(RE_TOTAL, x)
    return d

if __name__ == "__main__":
    for row in EXAMPLES:
        text = spaces(remove_punct(row))
        print(text)
        print(parse(text))


    
    
