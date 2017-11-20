import sys
import json
import os.path as path

import yaml


def build(src, dst):
    with open(src, 'r', encoding="utf8") as f:
        data = yaml.load(f)
    newdata = []
    for x in data:
        newx = {
            'battles_from':  [btl['id'] for btl in x['battles_from']],
            'battles_to': [btl['id'] for btl in x['battles_cwsac']],
            'relation': x['relation']
        }
        newdata.append(newx)
    with open(dst, 'w', encoding="utf8") as f:
        json.dump(newdata, f)


def main():
    src, dst = sys.argv[1:3]
    build(path.join(src, 'rawdata', 'livermore1900',
                    'livermore_to_cwsac.yaml'),
          path.join(dst, 'livermore_to_cwsac.json'))


if __name__ == '__main__':
    main()
