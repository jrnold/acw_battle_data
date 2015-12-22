# American Civil War Battle Data

This project contains various data on the American Civil War.
See the documentation at https://readthedocs.org/projects/acw-battle-data

## Build

This uses conda for Python de

```shell
$ python build.py
```
This will build the data in the directory, ``data``.

To build html documenation
```shell
$ cd docs/ && make html
```
and pdf documentation
```shell
$ cd docs/ && make html
```

## Prerequesites

For python dependencies create and activate a [conda](http://conda.pydata.org/docs/using/envs.html#create-a-separate-environment) environment.

```shell
conda env create -f environment.yml
```

R package dependencies are managed using packrat

Additional dependencies

- pdflatex (for building a pdf of the manual)
- bash
- [jq](https://stedolan.github.io/jq/)


## Licenses

- Documentation and other text: [CC-BY](http://creativecommons.org/licenses/by/4.0/).
- Code: [BSD 3-Clause License](http://opensource.org/licenses/BSD-3-Clause).
