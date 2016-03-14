import csv
import json
import sys
import os.path as path

def build(src, dst):
    with open(src, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    ret = []
    for row in data:
        ret.append({
            'battles_from': [row['isqno']],
            'battles_cwsac': [row['cwsac_id']],
            'relation': 'eq'
        })
    with open(dst, 'w') as f:
        json.dump(dst, f)

def main():
    print("Building CDB90 data")
    src, dst = sys.argv[1:3]
    build(path.join(src, 'rawdata', 'cdb90', 'cdb90_to_cwsac.csv'),
          path.join(dst, 'cdb90_to_cwsac.json'))

if __name__ == "__main__":
    main()
