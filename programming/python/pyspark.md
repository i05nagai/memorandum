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
以下が基本となる。

```python
import pyspark
conf = pyspark.SparkConf().setMaster("local").setAppName("Example")
sc = pyspark.SparkContext(conf=conf)
```

### SparkContext
* `sc.parallelize([])`
    * listをRDDとしてよみこむ
* `sc.textFile("/path/to/textfile")`
    * textfileをRDDとしてよみこむ

### Hive
```
import pyspark.sql as sql
hive_context = pyspark.sql.HiveContext(sc)
rows = hive_context.sql("SELECT * from users")
```

* `hive_context.jsonFile("path/to/json")`
    * jsonファイルをテーブルとして読み込む

### SharedVariable
通常それぞれの nodeでプログラム中の変数は独立している。
`accumulator`と`broadcast`変数は、例外的にnode間での変数を共有している。
以下でflatMapの結果を収集できる。

```python
file = sc.textFile("path/to/inputfile")
# initnialize to 0
blankLines = sc.accumulator(0)

def extractCallSigns(line):
    global blankLines
    if line == "":
        blankLines += 1
    return line.split(" ")

callSigns = file.flatMap(extractCallSigns)
print("Blank lines: {0}".format(blankLines.value))
```

### Load data
Local pathからの読み込みは全てのノードから同じpathで見ることができる必要がある。 
`parallelize`でworkerに送ることはできるので、遅い。
一般に、HDFS, NFS, S3などに置くことが推奨される。

* `sc.textFile("path/to/file")`
* `sc.sequenceFile(file, "org.apache.hadoop.io.Text", "org.apache.hadoop.io.IntWritable")`
    * hadoop sequence file

### Save data
* `rdd.saveAsTextFile(path/to/outputFile)`
* `rdd.saveAsSequenceFile(outputFile)`

### functions
* `lag`
    * parititionしたものの一つ前の行の値と置き換える
    * [pyspark.sql module — PySpark 2.1.0 documentation](http://spark.apache.org/docs/2.1.0/api/python/pyspark.sql.html#pyspark.sql.functions.lag)
    * Window関数

### RDD
以下はtransform

* `map`
* `flatMap`
* `filter(lambda x: "" in x)`
    * RDDをfilterする
* `distinct()`
* `intersection(rdd2)`
* `union(rdd2)`
* `subtract(rdd2)`
* `cartesian(rdd2)`
    * tupleの集合を作る
* `glom`
    * RDDのpartitionの内容を配列にしたRDDを生成する

以下はaction
* `reduce(lambda x, y: x + y)`
* `fold(zero, func)`
    * 最初の呼び出しで、zeroとして定義した値を渡せる
    * 文字列を連結して返す時、0として空文字列を渡すなど
* `aggregate(zeroValue, seqOp, combOp)`
    * reduce, foldは同じ型を返すが、aggregateは別の型を返すことができる
    * `seqOp = lambda acc, val: `
    * `seqOp = lambda acc, acc2: `
* `collect()`
    * listを返す
* `take(n)`
    * n個とってlistを返す
* `takeOrdered(num, ordering)`
* `takeSample(withReplacement, num, [seed])`
    * `withReplacement`がTrueだと
* `top(n)`
* `count()`
* `countByValue()`
    * 要素の出現回数を数える
    * (要素, 回数)のtupleの集合が変える
* `foreach(func)`
    * 各要素に対して処理をする

次はpariRDDに対するTransformation

* `reduceByKey(func)`
    * keyごとにreduceする
* `groupByKey()`
    * keyごとにvaluesをlistにする
* `combineByKey(createCombiner, mergeValue, mergeCombiners, partitioner)`
* `mapValues(func)`
* `flatMpaValues(func)`
    * 
* `keys()`
    * keyの一覧
* `values()`
    * 値のlist
* `sortByKeys()`
    * keyでsort
* `subtractByKey(other)`
* `join(other)`
* `rightOuterJoin(other)`
    * keyが同じものを、(key, (elem1, elem2))で右外結合
* `leftOuterJoin(other)`
    * keyが同じものを、(key, (elem1, elem2))で左外結合
* `cogroup(other)`
    * keyが同じものを、(key (list1, list2))でまとめる
    * list2はotherの中でkeyのvalue


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

* persist()
    * actionを何度も実行するときに利用する
    * DISK_ONLY
        * ディスクのみに格納
        * シリアライズあり
    * MEMORY_ONLY
        * メモリのみに格納
        * シリアライズなし
    * MEMORY_ONLY_SER
        * メモリのみに格納
        * シリアライズあり
    * MEMORY_AND_DISK
        * メモリからあふれた分はディスクに格納
        * シリアライズなし
    * MEMORY_AND_DISK_SER
        * メモリからあふれた分はディスクに格納
        * シリアライズあり
    * OFF_HEAP
        * Tachyonに格納
    * [SparkのRDDについて - TASK NOTES](http://www.task-notes.com/entry/20160112/1452525344)
    * [spark/dataframe.py at a848d552ef6b5d0d3bb3b2da903478437a8b10aa · apache/spark](https://github.com/apache/spark/blob/a848d552ef6b5d0d3bb3b2da903478437a8b10aa/python/pyspark/sql/dataframe.py#L522)

## Data Sources
* [Spark SQL and DataFrames - Spark 2.2.0 Documentation](https://spark.apache.org/docs/latest/sql-programming-guide.html)

DataFrameから直接保存やloadができる。

ファイルに直接SQLを実行できる。

```scala
val sqlDF = spark.sql("SELECT * FROM parquet.`examples/src/main/resources/users.parquet`")
```

### Save Modes

* error
* append
* overwrite
    * data sourceに保存するときに、上書きで保存
* ignore

## Tips

### function passing to pyspark
pysparkのAPIに関数を渡すとき、objectのメンバ関数を渡すと、オブジェクト全体をworkerに送る。
オブジェクトが大きい場合は、これがbottleneckになる。
また、オブジェクトがpickleできないときは、エラーとなる。
関数のメンバ変数を使いたい場合は、以下のようにする。


```python
class WordFunctions(object):
    def getMatchesNoreference(self, rdd):
        query = self.query
        return rdd.filter(lambda x: query in x)
```


## Docker
* [CoorpAcademy/docker-pyspark: Docker image of Apache Spark with its Python interface, pyspark.](https://github.com/CoorpAcademy/docker-pyspark)

```
export PYTHONPATH=/usr/bin/python3:$SPARK_HOME/python:$(ls -a ${SPARK_HOME}/python/lib/py4j-*-src.zip)
```


## Reference
* [Welcome to Spark Python API Docs! — PySpark 2.1.0 documentation](http://spark.apache.org/docs/2.1.0/api/python/index.html)
* [EMR上でPython3系でpysparkする - Qiita](http://qiita.com/uryyyyyyy/items/672a4058aba754b389d1)
* [EMRのpysparkでPython３系を使う - Qiita](http://qiita.com/azaazato/items/ae5c90c3df1616284fd0)
* [Databricks Spark Knowledge Base · GitBook](https://www.gitbook.com/book/databricks/databricks-spark-knowledge-base/details)
