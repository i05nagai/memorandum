## Apach Spark

## spark standalone mode
* [Spark Standalone Mode - Spark 2.2.0 Documentation](https://spark.apache.org/docs/latest/spark-standalone.html)

```
./sbin/start-master.sh
```

```
http://localhost:8080
```

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
    * コンマ区切りで渡す
    * `/path/to/file1,/path/to/file2`
* --py-files
    * PYTHONPATHに記載された場所に追加されるファイル
    * zipやpyなど
    * コンマ区切りで渡す
    * `/path/to/file1,/path/to/file2`
    * 実行するpythonファイルの中でimportしたいものがあるときは、こちらでファイルを渡す
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

pythonに引数を渡す方法。

* [Can I add arguments to python code when I submit spark job? - Stack Overflow](https://stackoverflow.com/questions/32217160/can-i-add-arguments-to-python-code-when-i-submit-spark-job)

以下の方法で渡ことができる。

```
spark-submit args.py a b c d e 
# ['/spark/args.py', 'a', 'b', 'c', 'd', 'e']
```

```
Usage: spark-submit [options] <app jar | python file> [app arguments]
Usage: spark-submit --kill [submission ID] --master [spark://...]
Usage: spark-submit --status [submission ID] --master [spark://...]
Usage: spark-submit run-example [options] example-class [example args]

Options:
  --master MASTER_URL         spark://host:port, mesos://host:port, yarn, or local.
  --deploy-mode DEPLOY_MODE   Whether to launch the driver program locally ("client") or
                              on one of the worker machines inside the cluster ("cluster")
                              (Default: client).
  --class CLASS_NAME          Your application's main class (for Java / Scala apps).
  --name NAME                 A name of your application.
  --jars JARS                 Comma-separated list of local jars to include on the driver
                              and executor classpaths.
  --packages                  Comma-separated list of maven coordinates of jars to include
                              on the driver and executor classpaths. Will search the local
                              maven repo, then maven central and any additional remote
                              repositories given by --repositories. The format for the
                              coordinates should be groupId:artifactId:version.
  --exclude-packages          Comma-separated list of groupId:artifactId, to exclude while
                              resolving the dependencies provided in --packages to avoid
                              dependency conflicts.
  --repositories              Comma-separated list of additional remote repositories to
                              search for the maven coordinates given with --packages.
  --py-files PY_FILES         Comma-separated list of .zip, .egg, or .py files to place
                              on the PYTHONPATH for Python apps.
  --files FILES               Comma-separated list of files to be placed in the working
                              directory of each executor.

  --conf PROP=VALUE           Arbitrary Spark configuration property.
  --properties-file FILE      Path to a file from which to load extra properties. If not
                              specified, this will look for conf/spark-defaults.conf.

  --driver-memory MEM         Memory for driver (e.g. 1000M, 2G) (Default: 1024M).
  --driver-java-options       Extra Java options to pass to the driver.
  --driver-library-path       Extra library path entries to pass to the driver.
  --driver-class-path         Extra class path entries to pass to the driver. Note that
                              jars added with --jars are automatically included in the
                              classpath.

  --executor-memory MEM       Memory per executor (e.g. 1000M, 2G) (Default: 1G).

  --proxy-user NAME           User to impersonate when submitting the application.
                              This argument does not work with --principal / --keytab.

  --help, -h                  Show this help message and exit.
  --verbose, -v               Print additional debug output.
  --version,                  Print the version of current Spark.

 Spark standalone with cluster deploy mode only:
  --driver-cores NUM          Cores for driver (Default: 1).

 Spark standalone or Mesos with cluster deploy mode only:
  --supervise                 If given, restarts the driver on failure.
  --kill SUBMISSION_ID        If given, kills the driver specified.
  --status SUBMISSION_ID      If given, requests the status of the driver specified.

 Spark standalone and Mesos only:
  --total-executor-cores NUM  Total cores for all executors.

 Spark standalone and YARN only:
  --executor-cores NUM        Number of cores per executor. (Default: 1 in YARN mode,
                              or all available cores on the worker in standalone mode)

 YARN-only:
  --driver-cores NUM          Number of cores used by the driver, only in cluster mode
                              (Default: 1).
  --queue QUEUE_NAME          The YARN queue to submit to (Default: "default").
  --num-executors NUM         Number of executors to launch (Default: 2).
                              If dynamic allocation is enabled, the initial number of
                              executors will be at least NUM.
  --archives ARCHIVES         Comma separated list of archives to be extracted into the
                              working directory of each executor.
  --principal PRINCIPAL       Principal to be used to login to KDC, while running on
                              secure HDFS.
  --keytab KEYTAB             The full path to the file that contains the keytab for the
                              principal specified above. This keytab will be copied to
                              the node running the Application Master via the Secure
                              Distributed Cache, for renewing the login tickets and the
                              delegation tokens periodically.

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

## Tips

### Spark History Server
* [Monitoring and Instrumentation - Spark 2.2.0 Documentation](https://spark.apache.org/docs/latest/monitoring.html)

hisotry serverの設定は以下の環境変数で変更可能。

```
export SPARK_HISTORY_OPTS="$SPARK_HISTORY_OPTS -Dspark.history.ui.port=900
```

### nohup can't execute '--': No such file or directory
alpine linuxで以下のようなerrorがでる。

```
nohup: can't execute '--': No such file or directory
```

* [docker - CrashLoopBackOff in spark cluster in kubernetes: nohup: can't execute '--': No such file or directory - Stack Overflow](https://stackoverflow.com/questions/44661274/crashloopbackoff-in-spark-cluster-in-kubernetes-nohup-cant-execute-no-s)

この場合は

```
apk --update add coreutils
```

か、起動用のscriptを以下のように書き換える。

```
/usr/spark/bin/spark-submit --class org.apache.spark.deploy.master.Master $SPARK_MASTER_INSTANCE --port $SPARK_MASTER_PORT --webui-port $SPARK_WEBUI_PORT
```

## Configs
* Node = Worker
    * nodeは複数のexecutorをもつ
* Executor
    * executorは複数のtaskをもつ
* task
* driver
* cluster manager

* --num-executors
    * `spark.executor.instances`
    * executorの総数
* --executor-cores
    * 各executorの使うcpu core
* --executor-memory
    * 各executorの使うmemory
* --driver-memory
* spark.executor.cores
    * 各executorの利用するcpu core
* spark.executor.memory
    * 各executorの利用するmemory

## Tuning
* [How-to: Tune Your Apache Spark Jobs (Part 2) – Cloudera Engineering Blog](https://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/)
* [Spark num-executors setting - Hortonworks](https://community.hortonworks.com/questions/56240/spark-num-executors-setting.html)


* 6 node
* 各nodeに16 cores, 64GB memory
* `yarn.nodemanager.resource.memory-mb`は64 * 1024 = 64512 MB
* `yarn.nodemanager.resource.cpu-vcores`は15

この状況でmemoryとCPUの割り振りを考えるが、Hadoop DaemonとOS用のResourceは残す必用がある。

案として`--num-executors 6 --executor-cores 15 --executor-memory 63G`は良くない。

* 各executorが1つのnodeにいる
* 各executorが15のcpu coreとmemory 63GBを使う

`--num-executors 17 --executor-cores 5 --executor-memory 19G`の方が良い。

* 3 executorがAMを除く(AMは2 executors)全てのnodeに割り振られる
* memoryは63 / 3 = 21から21 * 0.93でだいたい19
    * 0.93はOSとかHadoop Daemonを考慮しての掛け目

### Reason: Container killed by YARN for exceeding memory limits.


### Skipped Stage
* [What does "Stage Skipped" mean in Apache Spark web UI? - Stack Overflow](https://stackoverflow.com/questions/34580662/what-does-stage-skipped-mean-in-apache-spark-web-ui)

Cacheのdataを利用可能で、stageを実行する必要がない場合にskipされる。
また、shufflingは多くのfileを生成するがこれらは、RDDが不要になるまで削除されるずに残る。
これらのfileが利用可能な場合もまた、stageがskipされる要因になる。

## Reference
* [Submitting Applications - Spark 1.6.0 Documentation](https://spark.apache.org/docs/1.6.0/submitting-applications.html)
* [Sparkアプリケーションの実行方法（spark-submit） - TASK NOTES](http://www.task-notes.com/entry/20160103/1451810637)
* [Deep Dive into Spark SQL's Catalyst Optimizer - The Databricks Blog](https://databricks.com/blog/2015/04/13/deep-dive-into-spark-sqls-catalyst-optimizer.html)
* [How-to: Tune Your Apache Spark Jobs (Part 2) – Cloudera Engineering Blog](https://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/)* 
