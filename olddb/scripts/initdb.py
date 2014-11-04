""" Clean and create the database """
import sys

import sqlalchemy as sa

from acwbdb import model

def main():
    engine = sys.argv[1]
    model.Base.metadata.bind = sa.create_engine(engine)
    model.Base.metadata.drop_all()
    model.Base.metadata.create_all()
    print("Initialized database %s" % engine)

if __name__ == '__main__':
    main()
