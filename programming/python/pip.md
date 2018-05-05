---
title: pip
---

## pip

## install
`get-pip.py`はpipと同じversionが使える。

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py pip==9.0.1
```

For Linux,

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user pip==9.0.1
```

## Editable install
* [pip install — pip 9.0.1 documentation](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)

`setup.py`との重複を防ぎつつ、`requirements.txt`を提供したい場合は`requirements.txt`に以下を記載する。

```
-e .
```

`-e`でsetuptoolsのdevelop modeでのinstallを実行するようになる。


## CLI

* `--user`
    * userのHOME directoyrにinstallする

## Reference
