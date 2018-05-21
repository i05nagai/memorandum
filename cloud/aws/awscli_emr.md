---
title: awscli emr
---

## awscli emr

## Usage
get list of Cluster ID

```
aws emr list-clusters
```

cluster IDを指定すると、より詳細な情報が得られる。
Public DNS名などもえることができる。

```
aws emr list-instances --cluster-id j-2AL4XXXXXX5T9
```

master nodeにファイルをおく。

* `--key-pair-file`
    * cluster作成時に指定したkey pair
    * aws CLIで設定することもできる
* `--src`
    * 転送するfile path
* `--dest`
    * 転送先のfile path
    * 

```
aws emr put
--cluster-id <value>
--key-pair-file <value>
--src <value>
[--dest <value>]
```

master nodeにファイルからファイルを取得

* `--key-pair-file`
    * cluster作成時に指定したkey pair
    * aws CLIで設定することもできる
* `--src`
    * 取得するmaster nodeのfile path
* `--dest`
    * 取得したファイルをおくfile path

```
aws emr get
--cluster-id <value>
--key-pair-file <value>
--src <value>
[--dest <value>]
```

## Reference
