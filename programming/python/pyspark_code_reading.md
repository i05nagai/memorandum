## pyspark code reading

## sql


SparkContext

* [spark/context.py at master · apache/spark](https://github.com/apache/spark/blob/master/python/pyspark/context.py)
* `_jvm`
    * py4jの`gateway.jvm`が入る
    * [spark/java_gateway.py at master · apache/spark](https://github.com/apache/spark/blob/master/python/pyspark/java_gateway.py)
* `_jsc`
    * `_jvm.JavaSparkContext(jconf)`の戻り値が入るので、JavaSparkContextが入っている
    * [spark/context.py at master · apache/spark](https://github.com/apache/spark/blob/master/python/pyspark/context.py#L270)
    * [spark/JavaSparkContext.scala at ba78514da7bf2132873270b8bf39b50e54f4b094 · apache/spark](https://github.com/apache/spark/blob/ba78514da7bf2132873270b8bf39b50e54f4b094/core/src/main/scala/org/apache/spark/api/java/JavaSparkContext.scala)
    * `_jsc.sc()`
        * `JavaSparkContext`はpropertyとしてSparkContextを`sc`にもっているので、`JavaSparkContext`が持っている`SparkContext`を返しているだけ


SparkSession classについて。

* [spark/SparkSession.scala at 40c7add3a4c811202d1fa2be9606aca08df81266 · apache/spark](https://github.com/apache/spark/blob/40c7add3a4c811202d1fa2be9606aca08df81266/sql/core/src/main/scala/org/apache/spark/sql/SparkSession.scala)


* `_sc`
    * 引数のsparkContext
* `_jsc`
    * `_sc._jsc`なので、`JavaSparkContext`
* `_jsparkSession`
    * 引数で明示的に`jsparkSession`が渡されていればそれが使われる
    * 渡されていなければ、`_jvm.SparkSession(self._jsc.sc())`
* `_jvm`
    * 引数のsparkContextの`_sc._jvm`なので、py4jの`gateway.jvm`
* `_jwrapped`
    * `_jsparkSession.sqlContext()`
* `_wrapped`
    * `SQLContext(self._sc, self, self._jwrapped)`
* `createDataFrame` method
    * [spark/session.py at ebc24a9b7fde273ee4912f9bc1c5059703f7b31e · apache/spark](https://github.com/apache/spark/blob/ebc24a9b7fde273ee4912f9bc1c5059703f7b31e/python/pyspark/sql/session.py#L419)
    * DataFrameの作成
    色々呼び出し元はあるが、最終的にはここにたどり着いているように見える。
    * `jrdd = self._jvm.SerDeUtil.toJavaArray(rdd._to_java_object_rdd())`
    * `jdf = _jsparkSession.applySchemaToPythonRDD(jrdd.rdd(), schema.json())`
        * [spark/SparkSession.scala at 40c7add3a4c811202d1fa2be9606aca08df81266 · apache/spark](https://github.com/apache/spark/blob/40c7add3a4c811202d1fa2be9606aca08df81266/sql/core/src/main/scala/org/apache/spark/sql/SparkSession.scala#L728)


DataSet

* ofRows
    * [spark/Dataset.scala at f44ead89f48f040b7eb9dfc88df0ec995b47bfe9 · apache/spark](https://github.com/apache/spark/blob/f44ead89f48f040b7eb9dfc88df0ec995b47bfe9/sql/core/src/main/scala/org/apache/spark/sql/Dataset.scala#L67)

DataFrameの作成。
DataFrameの作成は、`SparkSession.createDataFrame`で行われている。



DataFrame class

* `sql_ctx`
    * 引数のsql_ctx
    * createDataFrameから呼ばれる場合は、SparkSessionの`_wrapped`
* `_sc`
    * 
* `_jdf`
    * 引数のjdf
    * createDataFrameから呼ばれる場合は、javaの`DataFrame`class


DataFrameWriter

* `_df`
    * 引数の`df`
* `_spark`
    * `df.sql_ctx`
* `_jwrite`
    * `_df._jdf.write()`


SQLContext

* 

## gateway


```python
from py4j.java_gateway import java_import
jvm = sc._jvm
java_import(jvm, "org.apache.spark.SparkConf")
```

```python
from py4j.java_gateway import java_import
java_import(sc._jvm, "java.net.URI")
url = sc._jvm.java.net.URI('s3://retty-dwh/')
java_import(sc._jvm, "org.apache.hadoop.fs.FileSystem")
```

## Java
DataFrameはDataSet[Row]と等価

* [spark/Dataset.scala at ee1304199bcd9c1d5fc94f5b06fdd5f6fe7336a1 · apache/spark](https://github.com/apache/spark/blob/ee1304199bcd9c1d5fc94f5b06fdd5f6fe7336a1/sql/core/src/main/scala/org/apache/spark/sql/Dataset.scala)

* [spark/CacheManager.scala at c05baabf10dd4c808929b4ae7a6d118aba6dd665 · apache/spark](https://github.com/apache/spark/blob/c05baabf10dd4c808929b4ae7a6d118aba6dd665/sql/core/src/main/scala/org/apache/spark/sql/execution/CacheManager.scala)
    * cacheQuery
* [spark/InMemoryRelation.scala at 5ad1796b9fd6bce31bbc1cdc2f607115d2dd0e7d · apache/spark](https://github.com/apache/spark/blob/5ad1796b9fd6bce31bbc1cdc2f607115d2dd0e7d/sql/core/src/main/scala/org/apache/spark/sql/execution/columnar/InMemoryRelation.scala)
    * InMemoryRelation

