#!/usr/bin/env python
"""Deploy ACW Battle data.

- create .zip and .tar.gz archives
- upload both original files and archives to S3

"""
import json
import subprocess as sp
import os.path as path
import zipfile
import tarfile
import os
import sys


def get_version(filename):
    with open(filename, 'r', encoding="utf8") as f:
        version = json.load(f)['version']
    return version


def zipdir(src, filename, rootdir=None):
    zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(src):
        for file_ in files:
            arcname = file_ if not rootdir else path.join(rootdir, file_)
            zipf.write(path.join(root, file_), arcname=arcname)
    zipf.close()


def tardir(src, filename, rootdir=None):
    tarf = tarfile.open(filename, 'w:gz')
    for root, dirs, files in os.walk(src):
        for file_ in files:
            arcname = file_ if not rootdir else path.join(rootdir, file_)
            tarf.add(path.join(root, file_), arcname=arcname)
    tarf.close()


def deploy(data_dir, s3_bucket, s3_region):
    version = get_version(path.join(data_dir, "datapackage.json"))
    tardir(data_dir, f"acw_battle_data-{version}.tar.gz", "acw_battle_data")
    zipdir(data_dir, f"acw_battle_data-{version}.zip", "acw_battle_data")
    sp.check_call(['aws', 's3', 'sync', '--delete', '--region', s3_region,
                   data_dir, f"s3://{s3_bucket}/v{version}/"])
    sp.check_call(['aws', 's3', 'sync',
                 '--exclude', '*',
                 '--include', 'acw_battle_data*.tar.gz',
                 '--include', 'acw_battle_data*.zip',
                  ".", f"s3://{s3_bucket}/"])


def main():
    data_dir, bucket, region = sys.argv[1:4]
    deploy(data_dir, bucket, region)


if __name__ == "__main__":
    main()
