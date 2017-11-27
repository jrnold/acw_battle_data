"""Build ship level data."""
import shutil
import sys
from os import path

FILES = ('ships.csv', )

def copyfiles(src, dst):
    for fn in FILES:
        srcfile = path.join(src, "rawdata", "ships", fn)
        dstfile = path.join(dst, fn)
        print("Writing: %s" % dstfile)
        shutil.copy(srcfile, dstfile)


def main():
    src = sys.argv[1]
    dst = sys.argv[2]
    print("Building ships data")
    copyfiles(src, dst)


if __name__ == '__main__':
    main()
