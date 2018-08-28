---
title: conda
---

## conda

## Install
* [Installing on Linux — Conda documentation](https://conda.io/docs/user-guide/install/linux.html#install-linux-silent)

For Linux,

Get shell scripts. [Miniconda — Conda](https://conda.io/miniconda.html)

```
curl -L -O https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh
```

* license agreement
* install location
    * default `~/miniconda2`
* Add install location to PATH

Silent installation

```
bash Miniconda2-latest-Linux-x86_64.sh -b -p $HOME/miniconda2
```

For OSX,

```
cd /tmp
curl -L -O https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
bash Miniconda2-latest-MacOSX-x86_64.sh -b -p $HOME/miniconda2
```

## CLI
```
conda config [-h] [--json] [--debug] [--verbose]
                    [--system | --env | --file FILE]
                    (--show [SHOW [SHOW ...]] | --show-sources | --validate | --describe [DESCRIBE [DESCRIBE ...]] | --write-default | --get [KEY [KEY ...]] | --append KEY VALUE | --prepend KEY VALUE | --set KEY VALUE | --remove KEY VALUE | --remove-key KEY | --stdin)
conda config: error: one of the arguments --show --show-sources --validate --describe --write-default --get --append --prepend/--add --set --remove --remove-key --stdin is required
```

```
conda list
```

## Usage
Create virtual environment 

```
# Create with packages
conda create -n py2 python=2.7 numpy scipy pandas jupyter
# Create with anaconda packages
conda create -n anaconda2 python=2.7 anaconda
# general
conda create -n env_name packages
```

List all virtual environment

```
conda env list
# or
conda info -e
```

Activate virtual environment

```
# Activate
source activate py2
# for windows, 'activate py2'
source activate env_name
source deactivate env_name
```

Deactivate virtual environment

```
source deactivate
# In windows, 'deactivate'
```

Delete virtual enviornment

```
conda remove -n <evn-name> --all
```


install package

```
conda install package
```

```
conda env list
```

Delete environment

```
conda remove -n py2 --all
```

### managing packages
Install and uninstall

```
# pipと同じでスペース区切りで複数OK
conda install numpy scipy
# バージョン指定も可能
conda install numpy=1.10.4
# -nで環境名を指定もできる
conda install -n py2 numpy scipy

conda update numpy # update

# pipも使える。condaにないときはこちらを利用
pip install numpy
# 仮想環境に入れるときは、activateしなければいけない
source activate py2;pip install numpy

# uninstall
conda uninstall -n py2 numpy
```

Create environment from an exported file

```
# You can export packages in conda environment but
# packages installed by pip is need to be exported by `pip freeze`
conda list --export > env.txt
conda create -n py2_copy --file env.txt
```

## Configuration

## Reference
