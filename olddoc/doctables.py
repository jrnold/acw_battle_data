import sys
sys.path.append("../python")
import os
from os import path

import acward
import acward.cwsac
import acward.dbpedia
import acward.livermore
import acward.kennedy
import acward.phister
import acward.bodart
import acward.dyer

from acward import doctable

def main():
    """Document table objects in the database"""
    acward.CONFIG.load("../config.yaml")
    TABLES = path.join(acward.CONFIG.paths['doc'], '_tables')
    print TABLES
    meta = acward.Base.metadata
    if not path.exists(TABLES):
        os.makedirs(TABLES)
    else:
        pass
    tablelist = path.join(acward.CONFIG.paths['doc'], 'tablelist.rst')
    f0 = open(tablelist, 'w')
    f0.write("""Tables\n============\n\n""")
    ## Do this so it is traversed alphabetically
    for k in sorted(meta.tables.keys()):
        table = meta.tables[k]
        newfile = path.join(TABLES, table.name + '.rst')
        print("writing to %s" % newfile)
        with open(newfile, 'w') as f:
            f.write(acward.doctable.doctable(table))
        f0.write("\n%s\n%s\n" % (k, '-' * len(k)))
        f0.write('\n.. include:: %s\n' % path.relpath(newfile, path.dirname(tablelist)))
    f0.close()
    
if __name__ == '__main__':
    main()
    
    

