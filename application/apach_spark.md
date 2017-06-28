## Apach Spark

## Commands

### spark-submit

```
${SPARK_HOME}/bin/spark-submit \
  --master <master-url> \
  --class <main-class>
  --name <name>
  ... # other options
  <application-jar> \
  [application-arguments]
```

* --master
    * 
* --deploy-mode
    * client
        * driverがlocal, workerはremote
    * cluster
        * driverもremote
* --class
    * Java or Scalaのmain class
* --name
    * spark's web UIのapplication name
* --jars
    * classpathに置かれる JAR files
    * third partyのJARに依存する場合は追加する
* --files
    * working directoryにおかれるファイル
    * workerで使うdata fileとか
* --py-files
    * PYTHONPATHに記載された場所に追加されるファイル
    * zipやpyなど
* --executor-memory
    * executorの使用するメモリ
    * `512m`, `15g`と指定する 
* --driver-memory
    * driverの使用するメモリ
    * `512m`, `15g`と指定する 
* --total-executors-core
* --properties-file
    * SparkConfにで指定する設定を記載したファイル

```
spark.master    local[4]
spark.app.name  "My Spark apps"
spark.ui.port   36000
```

設定の優先順位は以下の順序

1. SparkConf
2. `spark-submit`のオプション

## API

### SparkConf
* [SparkContextメモ(Hishidama's Apache Spark SparkContext Memo)](http://www.ne.jp/asahi/hishidama/home/tech/scala/spark/SparkContext.html#h_SparkConf)

キー`spark.master`と値`hoge_master`などで保持されている。
使用できるconfigの一覧は以下。

* [Configuration - Spark 2.1.1 Documentation](https://spark.apache.org/docs/latest/configuration.html#available-properties)

* `spark.debug.maxToStringFields`
    * string型として扱うfieldの最大数
    * string型の出力はoverheadになるので、デフォルトで制限がある

* `spark.sql.shuffle.partitions`
    * データのshufleするときの分割数
    * 代数が少ない時は
    * [Spark SQL Programming Guide - Spark 1.2.0 Documentation](https://spark.apache.org/docs/1.2.0/sql-programming-guide.html)


## Reference
* [Submitting Applications - Spark 1.6.0 Documentation](https://spark.apache.org/docs/1.6.0/submitting-applications.html)
* [Sparkアプリケーションの実行方法（spark-submit） - TASK NOTES](http://www.task-notes.com/entry/20160103/1451810637)

