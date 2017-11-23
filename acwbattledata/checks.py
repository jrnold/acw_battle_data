"""Check datapackage.json and output."""
import json
import logging
import sys

LOGGER = logging.getLogger(name=__name__)


def primary_key_exists(data):
    """Check primary keys in a schema.

    - if a csv file, does it specify a primary key
    - if a primary key is specified, check that it refers to a valid field.
    """
    for resource in data['resources']:
        try:
            schema = resource['schema']
        except KeyError:
            continue
        try:
            primary_key = schema['primaryKey']
        except:
            LOGGER.error(f"{resource['name']} does not have a primary key.")
            continue
        fields = set(x['name'] for x in schema['fields'])
        for pk in primary_key:
            if pk not in fields:
                LOGGER.error(f"{resource['name']}: {pk} is not a valid field.")


def run(infile):
    with open(infile, 'r') as fp:
        datapkg = json.load(fp)
    primary_key_exists(datapkg)


def main():
    logging.basicConfig()
    run(sys.argv[1])

if __name__ == '__main__':
    main()
