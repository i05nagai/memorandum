## python/pyspark

## Configuration

```json
[
    {
        "Classification": "spark-env",
        "Properties": {},
        "Configurations": [
            {
                "Classification": "export",
                "Properties": {
                    "PYSPARK_PYTHON": "python34"
                },
                "Configurations": []
            }
        ]
    }
]
```

## Pricing
* [料金 - Amazon EMR | AWS](https://aws.amazon.com/jp/emr/pricing/)

EC2のinstanceを借りるより安い。
1時間単位で課金されるので、一旦起動したら一時間使った方が良い。
起動した時点で課金が開始される。

## SSH
To Master Node

アカウント名は、haddoopで、keyはcluster作成時に指定したkey pairである。

```
ssh hadoop@ec2-###-##-##-###.compute-1.amazonaws.com -i ~/mykeypair.pem
```

## Commands
Cluster IDを以下でえる。 

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
* [Welcome to Spark Python API Docs! — PySpark 2.1.0 documentation](http://spark.apache.org/docs/2.1.0/api/python/index.html)
* [EMR上でPython3系でpysparkする - Qiita](http://qiita.com/uryyyyyyy/items/672a4058aba754b389d1)
* [EMRのpysparkでPython３系を使う - Qiita](http://qiita.com/azaazato/items/ae5c90c3df1616284fd0)
