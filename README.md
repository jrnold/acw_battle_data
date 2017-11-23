Bil# American Civil War Battle Data

This project contains various data on the American Civil War.
See the documentation at https://readthedocs.org/projects/acw-battle-data

## Install/Build

A current(ish) version of the data is available [here](http://acw-battle-data.readthedocs.io/en/latest/).

However, you may want to build the data from source. But realistically, I am writing this for future me.

Clone the repository to your machine,
```console
$ git clone  https://github.com/jrnold/acw_battle_data.git
```
[Invoke](http://www.pyinvoke.org/) is used for the workflow management.
The most common tasks are:
```console
# to build the data
invoke build
# to deploy/upload the data to S3
invoke deploy
# clean old data
invoke clean
```

To see the all the available tasks,
```console
invoke --list
```

## Prerequisites

For python dependencies create and activate a [conda](http://conda.pydata.org/docs/using/envs.html#create-a-separate-environment) environment.

```shell
conda env create -f environment.yml
```

## Licenses

- Documentation and other text: [CC-BY](http://creativecommons.org/licenses/by/4.0/).
- Code: [BSD 3-Clause License](http://opensource.org/licenses/BSD-3-Clause).
