## python/pyspark

## Install
* [spark 2.0系Tips #1 Jupyterでpyspark - Qiita](http://qiita.com/takaomag/items/bff9a7df24c4fbab2785)

For OSX

* [MacBook に spark を入れるには、brew install apache-spark 一発でできちゃった件 - Qiita](http://qiita.com/HirofumiYashima/items/e6d2a40abc71110a7b72)

```
brew install apache-spark
```

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

## API

### functions
* `lag`
    * parititionしたものの一つ前の行の値と置き換える
    * [pyspark.sql module — PySpark 2.1.0 documentation](http://spark.apache.org/docs/2.1.0/api/python/pyspark.sql.html#pyspark.sql.functions.lag)
    * Window関数

### RDD
* `repartitionAndSortWithinPartitions`
    * 戻り値はrdd
    * [pyspark.RDD.repartitionAndSortWithinPartitions](http://takwatanabe.me/pyspark/generated/generated/pyspark.RDD.repartitionAndSortWithinPartitions.html)
* `toDF`
    * DataFrameのtoDFとはまた異なる
    * `schema`と`sampleRation`からDataFrameを作る
    * [spark/session.py at d935e0a9d9bb3d3c74e9529e161648caa50696b7 · apache/spark](https://github.com/apache/spark/blob/d935e0a9d9bb3d3c74e9529e161648caa50696b7/python/pyspark/sql/session.py#L43)
    * [pyspark.sql module — PySpark 1.6.2 documentation](https://spark.apache.org/docs/1.6.2/api/python/pyspark.sql.html#pyspark.sql.DataFrame.toDF)


### DataFrame
* [Spark DataframeのSample Code集 - Qiita](http://qiita.com/taka4sato/items/4ab2cf9e941599f1c0ca)

## Reference
* [Welcome to Spark Python API Docs! — PySpark 2.1.0 documentation](http://spark.apache.org/docs/2.1.0/api/python/index.html)
* [EMR上でPython3系でpysparkする - Qiita](http://qiita.com/uryyyyyyy/items/672a4058aba754b389d1)
* [EMRのpysparkでPython３系を使う - Qiita](http://qiita.com/azaazato/items/ae5c90c3df1616284fd0)

