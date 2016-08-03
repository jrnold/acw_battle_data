# American Civil War Battle Data

This project contains various data on the American Civil War.
See the documentation at https://readthedocs.org/projects/acw-battle-data

## Install/Build

A current(ish) version of the data is available [here](http://acw-battle-data.readthedocs.io/en/latest/).

However, you may want to build the data from source. But realistically, I am writing this for future me.

Clone the repository to your machine,
```console
$ git clone --recursive https://github.com/jrnold/acw_battle_data.git
```
The `--recursive` argument is needed because this repository depends on several [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
If you did not originally clone the repository with this argument, you can initialize
the submodules with
```console
$ git submodule --init
```
The submodules are initialized if the sub-directories of `dependencies` (e.g. `dependencies/cwss`) are not empty.

Before starting, a copy of the [Civil War Soldiers and Sailors Database](https://www.nps.gov/civilwar/soldiers-and-sailors-database.htm) needs to be installed. This is not included in the repository directly since it is several gigs.
```console
$ cd dependencies/cwss
$ python download.py
```
See the instructions in `dependencies/cwss/README.md` for more detailed instructions;
this step requires installing the [AWS command line interface](https://aws.amazon.com/cli/).

To build the data, run the following from the main directory
```shell
$ source activate acw_battle_data
$ make build
```

To build the [Sphinx documentation](http://www.sphinx-doc.org/en/stable/contents.html) for the project run
```
$ make docs
```

## Prerequisites

For python dependencies create and activate a [conda](http://conda.pydata.org/docs/using/envs.html#create-a-separate-environment) environment.

```shell
conda env create -f environment.yml
```

## Licenses

- Documentation and other text: [CC-BY](http://creativecommons.org/licenses/by/4.0/).
- Code: [BSD 3-Clause License](http://opensource.org/licenses/BSD-3-Clause).
