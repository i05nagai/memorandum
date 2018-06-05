---
title: Anaconda
---

## Anaconda
* condaはpackage manager
* anacondaはplatform

仮想環境構築

```
conda create -n py2 python=2.7 numpy scipy pandas jupyter
#anacondaとしてまとめて入れることも可能。
conda create -n anaconda2 python=2.7 anaconda
```

仮想環境確認

```
conda env list
# こちらでも出る。
conda info -e
```

仮想環境の出入り

```
# 仮想環境に入る
source activate py2
# windowsではactivate py2
# 仮想環境から抜ける
source deactivate
# windowsではdeactivate
```

仮想環境の削除

```
conda remove -n py2 --all
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

## Reference
* [What is Anaconda? | Anaconda](https://www.anaconda.com/what-is-anaconda/)
* [Anaconda: Documentation |](https://docs.anaconda.com/)
