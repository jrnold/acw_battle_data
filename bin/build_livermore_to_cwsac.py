import sys
import json
import os.path as path

import yaml


def build(src, dst):
    with open(src, 'r', encoding="utf8") as f:
        data = yaml.load(f)
    for x in data:
        x['battles_from'] = [btl['id'] for btl in x['battles_from']]
        x['battles_to'] = [btl['id'] for btl in x['battles_cwsac']]
    with open(dst, 'w', encoding="utf8") as f:
        json.dump(data, f)


def main():
    src, dst = sys.argv[1:3]
    build(path.join(src, 'rawdata', 'livermore1900',
                    'livermore_to_cwsac.yaml'),
          path.join(dst, 'livermore_to_cwsac.json'))


if __name__ == '__main__':
    main()
