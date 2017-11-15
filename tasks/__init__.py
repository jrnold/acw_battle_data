#!/usr/bin/env python3
"""Command line tasks to build and deploy the ACW Battle Data."""
from invoke import Collection

from . import data, misc

ns = Collection(misc.clean, misc.doc, misc.deploy)
ns.add_task(data.build, name='build', default=True)
ns.add_collection(Collection.from_module(data))
