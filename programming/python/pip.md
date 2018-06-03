---
title: pip
---

## pip

## Install
* [install - pip error while installing Python: "Ignoring ensurepip failure: pip 8.1.1 requires SSL/TLS" - Stack Overflow](https://stackoverflow.com/questions/37723236/pip-error-while-installing-python-ignoring-ensurepip-failure-pip-8-1-1-requir/37723517)

Ubuntu

```
apt-get install libssl-dev
# or
apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libsqlite3-dev
```

CetOS

```
yum install openssl-devel
# or
yum install zlib-devel bzip2-devel sqlite sqlite-devel openssl-devel
```

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

## Tips


## Reference
