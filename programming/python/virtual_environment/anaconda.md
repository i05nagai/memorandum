---
title: Anaconda
---

## Anaconda
* condaはpackage manager
* anacondaはplatform
    * with many packages
* minicondaはplatform
    * without packages

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

## CLI

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

## managing packages
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

check packages

```
# 現在入っているパッケージリスト
conda list

# -nで仮想環境下も選択可能
conda list -n py2

# エクスポートして再利用することも可能だが、
# pipで入れたパッケージはエクスポートできないのでpip freezeで別途出力しておく必要がある。
conda list --export > env.txt
conda create -n py2_copy --file env.txt
```

## CLI
create environment

```
conda create -n env_name packages
```

activate environment

```
souce activate env_name
source deactivate env_name
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

## Tips

### Difference between anaconda and miniconda
* [python \- Anaconda vs miniconda \- Stack Overflow](https://stackoverflow.com/questions/45421163/anaconda-vs-miniconda)

## Reference
* [What is Anaconda? | Anaconda](https://www.anaconda.com/what-is-anaconda/)
* [Anaconda: Documentation |](https://docs.anaconda.com/)
