# American Civil War Battle Data

## Download

Download the latest version from [figshare](https://figshare.com/articles/acw_battle_data/1515995). 

Please cite if you use this data.

## Install/Build

A current(ish) version of the data is available [here](http://acw-battle-data.readthedocs.io/en/latest/).

However, you may want to build the data from source. But realistically, I am writing this for future me.

Clone the repository to your machine,
```console
$ git clone  https://github.com/jrnold/acw_battle_data.git
```
[Invoke](http://www.pyinvoke.org/) is used for the workflow management.
The most common tasks is to build the data:
```console
invoke build
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
