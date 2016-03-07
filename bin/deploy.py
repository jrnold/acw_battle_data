#!/usr/bin/env python
import json
import subprocess as sp
import os.path as path
import zipfile
import tarfile
import os
import sys

def get_version(filename):
    with open(filename, 'r') as f:
        version = json.load(f)['version']
    return version

def zipdir(src, filename, rootdir = None):
    zip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(src):
        for file in files:
            zip.write(path.join(root, file),
            arcname = file if not rootdir else path.join(rootdir, file))
    zip.close()

def tardir(src, filename, rootdir = None):
    tarf = tarfile.open(filename, 'w:gz')
    for root, dirs, files in os.walk(src):
        for file in files:
            tarf.add(path.join(root, file),
            arcname = file if not rootdir
            else path.join(rootdir, file))
    tarf.close()

def deploy(data_dir, bucket, region):
    version = get_version(path.join(data_dir, "datapackage.json"))
    tardir(data_dir, 'acw_battle_data-%s.tar.gz' % version, "acw_battle_data")
    zipdir(data_dir, 'acw_battle_data-%s.zip' % version, "acw_battle_data")
    sp.check_call(['aws', 's3', 'sync', '--delete', '--region', region,
              data_dir, 's3://%s/v%s/' % (bucket, version)])
    sp.check_call(['aws', 's3', 'sync',
                 '--exclude', '*',
                 '--include', 'acw_battle_data*.tar.gz',
                 '--include', 'acw_battle_data*.zip',
                 '--region', region,
                  ".", 's3://%s/' % bucket])

def main():
    data_dir, bucket, region = sys.argv[1:4]
    deploy(data_dir, bucket, region)

if __name__ == "__main__":
    main()
