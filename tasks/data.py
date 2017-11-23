#!/usr/bin/env python3
"""Command line tasks to build and deploy the ACW Battle Data."""
import os
import shutil
from os import path
import logging

from invoke import task


LOGGER = logging.getLogger(__name__)


@task
def setup(ctx):
    """Setup directory structure."""
    os.makedirs(ctx.dst, exist_ok=True)


@task(setup)
def unit_sizes(ctx):
    """Build unit size data."""
    shutil.copy(path.join(ctx.src, 'rawdata', 'unit_sizes', 'unit_sizes.csv'),
                ctx.dst)
    shutil.copy(
        path.join(ctx.src, 'rawdata', 'unit_sizes', 'eicher_units_table.csv'),
        ctx.dst)


@task(setup)
def aad(ctx):
    """Build the AAD CWSAC initial data."""
    ctx.run(f"{ctx.python} -m acwbattledata.aad {ctx.src} {ctx.dst}")


@task(setup)
def cwsac(ctx):
    """Build the CWSAC Report I data."""
    ctx.run(f"{ctx.python} -m acwbattledata.cwsac {ctx.src} {ctx.dst}")


@task(setup)
def cws2(ctx):
    """Build the CWSAC Report II data."""
    ctx.run(f"{ctx.python} -m acwbattledata.cws2 {ctx.src} {ctx.dst}")


@task
def download_cwss(ctx):
    """Download CWSS data."""
    files = ('old/battle.xml',
             'old/persons.xml',
             'old/battleunitlink.xml',
             'new/tsv/Regiments_Unitz.tsv',
             'new/tsv/State_Name.tsv',
             'new/tsv/Unititle.tsv',
             'new/tsv/Contitle.tsv',
             'new/tsv/Category.tsv')
    for file_ in files:
        basefilename = path.basename(file_)
        dstfile = path.join(ctx.cwss.data_dir, basefilename)
        if not os.path.exists(dstfile):
            ctx.run(f"aws s3 cp --region {ctx.cwss.s3.region} "
                    f" s3://{ctx.cwss.s3.bucket}/{file_} "
                    f" {dstfile} ")
        else:
            print(f"{dstfile} exists")


@task(pre=[setup, download_cwss])
def cwss(ctx):
    """Build the CWSS data."""
    ctx.run(f"{ctx.python} -m acwbattledata.cwss "
            f" {ctx.src} {ctx.cwss.data_dir} {ctx.dst}")


@task(pre=[setup, aad, cwsac, cws2, cwss, unit_sizes])
def nps(ctx):
    """Build the NPS Combined Data."""
    ctx.run(f"{ctx.Rscript} bin/build_nps_combined.R {ctx.src} {ctx.dst}")


@task(setup)
def bodart(ctx):
    """Build data from Bodart."""
    ctx.run(f"{ctx.python} -m acwbattledata.bodart {ctx.src} {ctx.dst}")


@task(setup)
def dyer(ctx):
    """Build data from Dyer (1908)."""
    ctx.run(f"{ctx.python} -m acwbattledata.dyer {ctx.src} {ctx.dst}")


@task(setup)
def fox(ctx):
    """Build data from Fox."""
    ctx.run(f"{ctx.python} -m acwbattledata.fox {ctx.src} {ctx.dst}")


@task(setup)
def greer(ctx):
    """Build weekly casualty data from Greer."""
    ctx.run(f"{ctx.python} -m acwbattledata.greer {ctx.src} {ctx.dst}")


@task(setup)
def kennedy(ctx):
    """Build casualty data from Kennedy."""
    ctx.run(f"{ctx.python} -m acwbattledata.kennedy {ctx.src} {ctx.dst}")


@task(setup)
def livermore(ctx):
    """Build casualty data from Kennedy."""
    ctx.run(f"{ctx.Rscript} bin/build_livermore.R "
            f"{ctx.src} {ctx.dst}")
    ctx.run(f"{ctx.python} -m acwbattledata.livermore_to_cwsac "
            f"{ctx.src} {ctx.dst}")


@task(setup)
def thorpe(ctx):
    """Build Thorpe data."""
    ctx.run(f"{ctx.python} -m acwbattledata.thorpe {ctx.src} {ctx.dst}")


@task(setup)
def nyt(ctx):
    """Build New York Times chronology data."""
    shutil.copy(
        path.join(ctx.src, "rawdata", "nytimes_civil_war_chronology",
                  "nytimes_civil_war_chronology.json"), ctx.dst)


@task(setup)
def phisterer(ctx):
    """Build phisterer data."""
    ctx.run(f"{ctx.python} -m acwbattledata.phisterer {ctx.src} {ctx.dst}")


@task(setup)
def shenandoah(ctx):
    """Build the NPS Shenandoah Report Data."""
    ctx.run(f"{ctx.python} -m acwbattledata.shenandoah {ctx.src} {ctx.dst}")


@task(pre=[setup, unit_sizes])
def clodfelter(ctx):
    """Build the Clodfelter data."""
    ctx.run(f"{ctx.python} -m acwbattledata.clodfelter {ctx.src} {ctx.dst}")
    ctx.run(f"{ctx.Rscript} bin/update_clodfelter_forces.R "
            f"{ctx.src} {ctx.dst}")


@task(setup)
def cdb90(ctx):
    """Build the CDB90 data."""
    ctx.run(f"{ctx.python} -m acwbattledata.cdb90 {ctx.src} {ctx.dst}")


@task(setup)
def civilwarorg(ctx):
    """Build the civilwar.org data."""
    ctx.run(f"{ctx.python} -m acwbattledata.civilwarorg {ctx.src} {ctx.dst}")


@task(setup)
def misc(ctx):
    """Build some miscellaneous datasets."""
    ctx.run(f"{ctx.python} -m acwbattledata.misc {ctx.src} {ctx.dst}")


@task(setup)
def battlemisc(ctx):
    """Build miscellaneous battle data."""
    ctx.run(f"{ctx.python} -m acwbattledata.battlemisc {ctx.src} {ctx.dst}")


@task(setup)
def ships(ctx):
    """Build the dataset on ships."""
    ctx.run(f"{ctx.python} -m acwbattledata.ships {ctx.src} {ctx.dst}")


@task(setup)
def wikipedia(ctx):
    """Build wikipedia data."""
    ctx.run(f"{ctx.python} -m acwbattledata.wikipedia {ctx.src} {ctx.dst}")


@task(setup)
def eicher(ctx):
    """Build Eicher datasets."""
    ctx.run(f"{ctx.python} -m acwbattledata.eicher {ctx.src} {ctx.dst}")


@task(setup)
def download_wikipedia(ctx):
    """Download wikipedia data."""
    outdir = path.join(ctx.src, 'wikipedia')
    ctx.run(f"{ctx.python} bin/download_wikipedia.py {ctx.src} {outdir}")


DATA_TASKS = [
    unit_sizes, aad, shenandoah, cwsac, cws2, cwss, nps, bodart, dyer, fox,
    greer, kennedy, livermore, thorpe, nyt, phisterer, clodfelter, cdb90,
    ships, civilwarorg, wikipedia, eicher, misc, battlemisc]
"""Tasks to run before build."""


@task(setup)
def datapackage(ctx):
    """Build datapackage.json"""
    ctx.run(f"{ctx.python} -m acwbattledata.datapackage {ctx.src} {ctx.dst}")


@task(pre=[*DATA_TASKS, datapackage])
def build(ctx):
    """Build all datasets."""
    pass
