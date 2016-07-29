# American Civil War Battle Data

This project contains various data on the American Civil War.
See the documentation at https://readthedocs.org/projects/acw-battle-data

## Build

```shell
$ source activate acw_battle_data
$ make build
$ make docs
```

## Prerequisites

For python dependencies create and activate a [conda](http://conda.pydata.org/docs/using/envs.html#create-a-separate-environment) environment.

```shell
conda env create -f environment.yml
```

If you are using Windows, then run the following command instead.

```shell
conda env create -f environment_win64.yml
```

R package dependencies are managed using packrat

Additional dependencies

- pdflatex (for building a pdf of the manual)
- bash
- [jq](https://stedolan.github.io/jq/)

## Licenses

- Documentation and other text: [CC-BY](http://creativecommons.org/licenses/by/4.0/).
- Code: [BSD 3-Clause License](http://opensource.org/licenses/BSD-3-Clause).
