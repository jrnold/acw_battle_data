#!/usr/bin/env python3
"""Command line tasks to build and deploy the ACW Battle Data."""
import re
import os
import shutil
from os import path
import logging
import sys

from invoke import task


LOGGER = logging.getLogger(__name__)


@task
def clean(ctx):
    """Clean project by deleting created data."""
    LOGGER.info(f"Deleting output directory {ctx.dst}")
    shutil.rmtree(ctx.dst)
    for fname in os.listdir(ctx.src):
        filename = path.join(ctx.src, fname)
        if re.match('^.*(\.tar\.gz|\.zip)$', fname):
            LOGGER.info(f"Deleting {filename}")
            os.remove(filename)


@task()
def deploy(ctx, force=False):
    """Upload data to to AW3 S3."""
    if not path.exists(ctx.dst):
        LOGGER.error(f"{ctx.dst} does not exist")
    if not len(os.listdir(ctx.dst)):
        LOGGER.error(f"{ctx.dst} is empty")
        if not force:
            sys.exit(1)
    if not path.exists(path.join(ctx.dst, "datapackage.json")):
        LOGGER.error(f"{ctx.dst} does not exist")
        if not force:
            sys.exit(1)
    ctx.run(f"{ctx.python} -m acwbattledata.deploy "
            f"{ctx.dst} {ctx.S3.bucket}/{ctx.S3.prefix} {ctx.S3.region}")


@task()
def doc(ctx, target='html'):
    """Build project documentation.

    Parameters
    ----------
    target: str
        The target in the Sphinx ``Makefile`` to run.

    """
    ctx.run(f"make -C {ctx.doc} {target}")


@task()
def check_tables(ctx, outfile="table_checks.log"):
    """Check table schema."""
    with open(outfile, 'w') as fp:
        ctx.run(f"goodtables --table-limit 100 --table-limit 10000 "
                f"{ctx.dst}/datapackage.json", out_stream=fp)
        ctx.run(f"{ctx.python} "
                f"-m acwbattledata.checks {ctx.dst}/datapackage.json",
                out_stream=fp)
