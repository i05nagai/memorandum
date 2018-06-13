---
title: pyenv
---

## pyenv
pythonの仮想環境作成する。
`python`コマンドのversionは変わらない。
`python`コマンドのversionを変更する場合は、`pyenv-virtualenv`をいれる。

```
brew install pyenv
```

`bash_profile`などに以下を追加する。

```
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
export PYENV_ROOT=/usr/local/var/pyenv
```

### for Linux
Linuxの場合は、

```
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
```

### pyenvに特定のversionのpythonをInstall

以下のコマンドでインストール可能なpythonのversionが表示される。

```
pyenv install -l
```

例えば、2.7.9のpythonをインストールしたければ以下のようにかく。

```
pyenv install 2.7.9
```

### 全体で利用するバージョンの設定
`3.5.2`は、installされているpythonを指定する。
pyenvのpythonのversionが設定される。

```
pyenv global 3.5.2
```

### 特定のディレクトリ以下のversionの指定

`3.5.2`は、installされているpythonを指定する。
カレントディレクト以下で利用するpyenvのpythonのversionが設定される。

```
pyenv local 3.5.2
pyenv version
# 3.5.2
cd ..
pyenv version
# other version
```

## Reference
