---
title: PySpark
---

## PySpark

## Install
* [spark 2.0系Tips #1 Jupyterでpyspark - Qiita](http://qiita.com/takaomag/items/bff9a7df24c4fbab2785)

For OSX

* [MacBook に spark を入れるには、brew install apache-spark 一発でできちゃった件 - Qiita](http://qiita.com/HirofumiYashima/items/e6d2a40abc71110a7b72)

```
brew install apache-spark
```

## API

### pyspark.sql.SparkSession
In usual, `SparkSession` is denoted by `spark`.

* `spark_session.read.json()`
    * readには、pathかpathのlistが渡せる
    * pathは`*`, `[]`が使える

### pyspark.sql.types

* `IntegerType()`
* `StringType()`

* `StructType`
    * `StructType([StructField('col_name', IntegerType(), True)])`
* `StructField(name, dataType, nullable=True, metadata=None)`
    * [pyspark.sql module — PySpark 2.2.0 documentation](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=structtype#pyspark.sql.types.StructField)

### pyspark.sql.DataFrame
pyspark.sql.DataFrame

* `df.withColumn(colName, col)`
    * [pyspark.sql module — PySpark 2.2.0 documentation](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=withcolumn#pyspark.sql.DataFrame.withColumn)
    * 新しいcolumnを追加する
    * `colName`が名前
    * 戻り値はDataFrame

```python
>>> df.withColumn('age2', df.age + 2).collect()
[Row(age=2, name=u'Alice', age2=4), Row(age=5, name=u'Bob', age2=7)]
```

* `df.colname`
    * [spark/dataframe.py at master · apache/spark](https://github.com/apache/spark/blob/master/python/pyspark/sql/dataframe.py#L1024)
    * `colname`はDataFrameで定義されているcolumnの名前
    * DataFrameは`__getattr__` methodがoverrideされているのでcolnameをinstance変数として扱える
    * 戻り値はColumn型

* `df.explan()`
    * 標準出力にexplainを出力する
    * 内部的には`df._jdf.queryExecution().toString()`を`print`している
    * 標準出力以外に出す場合は`print`の出力先を奪うか、外側で`df._jdf.queryExecution().toString()`を直接呼ぶ
* `df.distinct()`
    * 同じ行を削除
* `df.write.format("com.databricks.spark.csv").save("/data/home.csv")`
    * save as csv


* `Column(jc)`
    * jcはjavaのColumn型？
* `Column.alias()`
    * 戻り値はColumn型
* `Column.cast()`
    * 戻り値はColumn型


* `pyspark.sql.Window`
    * DataFrameのWindowを定義するためのutility

```python
>>> # ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
>>> window = Window.orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
>>> # PARTITION BY country ORDER BY date RANGE BETWEEN 3 PRECEDING AND 3 FOLLOWING
>>> window = Window.orderBy("date").partitionBy("country").rangeBetween(-3, 3)
```


### pyspark.sql.functions
pyspark.sql.functions

* `regexp_extract(str, patttern, idx)`
    * strのcolumnでpatternにmatchするものだけを
    * 戻り値はColumn型
    * str
        * column name
    * pattern
        * javaの正規表現
        * groupを指定
    * idx
        * 正規表現のmatchしたgroupのindex
        * `(\d+)(aaa)`なら`idx=1`で数字、`idx=2`で`aaa`がかえる
* `lag`
    * parititionしたものの一つ前の行の値と置き換える
    * [pyspark.sql module — PySpark 2.1.0 documentation](http://spark.apache.org/docs/2.1.0/api/python/pyspark.sql.html#pyspark.sql.functions.lag)
    * Window関数
* `udf(f=None, returnType=StringType)`
    * methodからsqlのudf functionを生成する
    * [pyspark.sql module — PySpark 2.2.0 documentation](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=structtype#pyspark.sql.functions.udf)
    * udfに渡すfunctionはudfと同じscopeにいないとだめ？


### pyspark.SparkContext
In usual, `SparkContext` is denoted by `sc`.

```python
conf = pyspark.SparkConf(
).setMaster(
    "local"
).setAppName(
    "pytest-pyspark-local-testing"
)
sc = pyspark.SparkContext.getOrCreate(conf=conf)
```

* `sc.parallelize(c, numSlices=None)`
    * [pyspark package — PySpark 2.2.0 documentation](http://spark.apache.org/docs/latest/api/python/pyspark.html?highlight=parallelize#pyspark.SparkContext.parallelize)
    * listをRDDとしてよみこむ
    * pythonのcollectionをnumSlices個のListに分割
    * 順序は適当?
* `sc.textFile("/path/to/textfile")`
    * textfileをRDDとしてよみこむ
    * gzに圧縮されているものも読み込める
    * file globで複数のファイルもまとめて読み込める


```python
>>> rdd = spark_context.parallelize([(0, 5), (3, 8), (2, 6), (0, 8), (3, 8), (1, 3)])
# rdd[0]: (0, 5)
# rdd[1]: (3, 8)
>>> sc.parallelize([0, 2, 3, 4, 6], 5).glom().collect()
[[0], [2], [3], [4], [6]]
>>> sc.parallelize(xrange(0, 6, 2), 5).glom().collect()
[[], [0], [], [2], [4]]
```

jsonの読み込み

```python
rdd = sc.textFile('python/test_support/sql/*.json.gz')
df2 = spark.read.json(rdd)
df2.dtypes
[('age', 'bigint'), ('name', 'string')]
```

## API
以下が基本となる。

```python
import pyspark
conf = pyspark.SparkConf().setMaster("local").setAppName("Example")
sc = pyspark.SparkContext(conf=conf)
```

jsonの読み込み
directoryを読み込む場合は`/path/to/*`とする必要がある。

```python
>>> df1 = spark.read.json('python/test_support/sql/*.json.gz')
>>> df1.dtypes
[('age', 'bigint'), ('name', 'string')]
```

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
* `rdd.partitionBy(numPartitions, partitionFunc=portable_hash)`
* `rdd.mapPartitions(f, preservesPartitioning=False)`
    * 下記の例だと`[1, 2]`が一つのpartition
    * `f(iterator)`
        * fの引数はpartitionのiterator
        * 戻り値はparititionのiteratorである必要がある

```python
# [[1, 2], [3, 4]]
rdd = sc.parallelize([1, 2, 3, 4], 2)
# iterator = [1, 2] or [3, 4]
def f(iterator): yield sum(iterator)
rdd.mapPartitions(f).collect()
# [3, 7]
```

* `rdd.repartitionAndSortWithinPartitions(numPartitions=None, partitionFunc=<function portable_hash at 0x7f51f1ac0668>, ascending=True, keyfunc=<function <lambda> at 0x7f51f1ab3ed8)`
    * 戻り値はrdd
    * [pyspark.RDD.repartitionAndSortWithinPartitions](http://takwatanabe.me/pyspark/generated/generated/pyspark.RDD.repartitionAndSortWithinPartitions.html)
    * documentにあやまりがある
    * [pyspark package — PySpark 2.2.0 documentation](http://spark.apache.org/docs/latest/api/python/pyspark.html?highlight=mappartition#pyspark.RDD.repartitionAndSortWithinPartitions)
    * keyFuncは行をうけとり、sortのkeyを返す関数
    * 下の例ではlambda functionでnumPartitions=2個に分けている
    * 各行は(key, value)である必用がある
        * 下の例では(key=0, value=5)
        * valueが複数ある場合は片方はtuple(0, (5, 0, 5))

```python
rdd = sc.parallelize([(0, 5), (3, 8), (2, 6), (0, 8), (3, 8), (1, 3)])
rdd2 = rdd.repartitionAndSortWithinPartitions(2, lambda x: x % 2, True)
rdd2.glom().collect()
# [[(0, 5), (0, 8), (2, 6)], [(1, 3), (3, 8), (3, 8)]]
rdd = sc.parallelize([(0, 5), (3, 8), (2, 6), (0, 8), (3, 8), (1, 3)])
rdd2 = rdd.repartitionAndSortWithinPartitions(2, lambda x: x % 2, 2)
rdd2.glom().collect()
# [[(0, 5), (0, 8), (2, 6)], [(1, 3), (3, 8), (3, 8)]]
```

* `rdd.toDF`
    * DataFrameのtoDFとはまた異なる
    * `schema`と`sampleRatio`からDataFrameを作る
    * sample rationはDataFrameの型の推定などに利用するsampleの割合を指定する
    * 内部的には、SparkSessionのcreateDataFrameを呼んでいる
    * `createDataFrame`の引数は`samplingRatio`だが、toDFは`sampleRation`
    * `sampleRatio`は[0, 1]で指定
    * [spark/session.py at d492cc5a21cd67b3999b85d97f5c41c3734b1ba3 · apache/spark](https://github.com/apache/spark/blob/d492cc5a21cd67b3999b85d97f5c41c3734b1ba3/python/pyspark/sql/session.py#L43)


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
* df.describe()
    * 戻り値はDataFrame

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

## Docker
* [CoorpAcademy/docker-pyspark: Docker image of Apache Spark with its Python interface, pyspark.](https://github.com/CoorpAcademy/docker-pyspark)

```
export PYTHONPATH=/usr/bin/python3:$SPARK_HOME/python:$(ls -a ${SPARK_HOME}/python/lib/py4j-*-src.zip)
```

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


### Error: No module named ...
* [Running Spark Python Applications](https://www.cloudera.com/documentation/enterprise/5-5-x/topics/spark_python.html)

java/scalaはpackageを1つのjarにまとめることができるので、packageの依存関係の解決は容易。
しかし、pysparkを使う場合はpythonのpackageの問題がある。
`spark-submit`で`--py-files`optionを利用して、依存しているpackageを渡す。
もしくは、program内の`SparkContext`で`addPyFile()`で必要なFileを追加する。

pytestでこのErrorがでる場合は、spark_contextに以下を追加すると良い。

```python
import some_module_to_be_tested

# Here spark_context is fixture of pytest. 
# spark_context is pyspark.SparkContext class
def test_func(spark_context):
    spark_context.addPyFile(some_module_to_be_tested.__file__)
```

## Reference
* [Welcome to Spark Python API Docs! — PySpark 2.1.0 documentation](http://spark.apache.org/docs/2.1.0/api/python/index.html)
* [EMR上でPython3系でpysparkする - Qiita](http://qiita.com/uryyyyyyy/items/672a4058aba754b389d1)
* [EMRのpysparkでPython３系を使う - Qiita](http://qiita.com/azaazato/items/ae5c90c3df1616284fd0)
* [Databricks Spark Knowledge Base · GitBook](https://www.gitbook.com/book/databricks/databricks-spark-knowledge-base/details)
* [msukmanowsky/pyspark-testing: Unit and integration testing with PySpark can be tough to figure out, let's make that easier.](https://github.com/msukmanowsky/pyspark-testing)
