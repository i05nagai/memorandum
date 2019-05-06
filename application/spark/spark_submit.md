---
title: sprak-submit
---

## sprak-submit


## CLI
```
spark-submit [options] <app jar | python file> [app arguments]
spark-submit --kill [submission ID] --master [spark://...]
spark-submit --status [submission ID] --master [spark://...]
spark-submit run-example [options] example-class [example args]
```

* `--master MASTER_URL`
    * `spark://host:port`
    * `mesos://host:port`
    * `yarn`
    * `local`
* `--deploy-mode DEPLOY_MODE`
    * Whether to launch the driver program locally ("client") or on one of the worker machines inside the cluster ("cluster") (Default: client).
    * `client`
        * driver is local, worker is remote
    * `cluster`
        * driver and worker is remote
* `--class CLASS_NAME`
    * Your application's main class (for Java / Scala apps).
    * Java or Scalaのmain class
* `--name NAME`
    * A name of your application.
    * spark's web UIのapplication name
* `--jars JAR`S
    * Comma-separated list of local jars to include on the driver and executor classpaths.
    * lists of JAR files placed under classpath
    * Specify if you use third party JAR files
* `--packages`
    * Comma-separated list of maven coordinates of jars to include on the driver and executor classpaths.
    * Will search the local maven repo, then maven central and any additional remote repositories given by --repositories.
    * The format for the coordinates should be groupId:artifactId:version.
* `--exclude-packages`
    * Comma-separated list of groupId:artifactId, to exclude while resolving the dependencies provided in --packages to avoid dependency conflicts.
* `--repositories` 
    * Comma-separated list of additional remote repositories to search for the maven coordinates given with --packages.
* `--py-files PY_FILES`
    * Comma-separated list of .zip, .egg, or .py files to place on the PYTHONPATH for Python apps.
    * files are placed in a directory registed to `PYTHONPATH`
    * available format: zip, py
    * comma separated lists
        * `/path/to/file1,/path/to/file2`
    * 実行するpythonファイルの中でimportしたいものがあるときは、こちらでファイルを渡す
* `--files FILES`
    * Comma-separated list of files to be placed in the working directory of each executor.
    * the files are placed in working directory
    * data/configuration files used in worker nodes
    * e.g. `/path/to/file1,/path/to/file2`
* `--conf PROP=VALUE`
    * Arbitrary Spark configuration property.
* --properties-file FILE
    * Path to a file from which to load extra properties.
    * If not specified, this will look for conf/spark-defaults.conf.
    * SparkConfにで指定する設定を記載したファイル
* `--driver-memory MEM`
    * Memory for driver (e.g. 1000M, 2G) (Default: 1024M).
    * driverの使用するメモリ
    * `512m`, `15g`と指定する 
* `--driver-java-options`
    * Extra Java options to pass to the driver.
* `--driver-library-path`
    * Extra library path entries to pass to the driver.
* --driver-class-path
    * Extra class path entries to pass to the driver. Note that jars added with --jars are automatically included in the classpath.
* `--executor-memory MEM`
    * Memory per executor (e.g. 1000M, 2G) (Default: 1G).
    * the size of memory executor uses
    * e.g. `512m`, `15g`
* --proxy-user NAME
    * User to impersonate when submitting the application.  This argument does not work with --principal / --keytab.
* `--verbose, -v`
    * Print additional debug output.

Spark standalone with cluster deploy mode only:

* --driver-cores NUM
    * Cores for driver (Default: 1).

Spark standalone or Mesos with cluster deploy mode only:

* --supervise
    * If given, restarts the driver on failure.
* --kill SUBMISSION_ID
    * If given, kills the driver specified.
* --status SUBMISSION_ID
    * If given, requests the status of the driver specified.

Spark standalone and Mesos only:

* --total-executor-cores NUM
    * Total cores for all executors.

Spark standalone and YARN only:

* --executor-cores NUM
    * Number of cores per executor.
    * (Default: 1 in YARN mode, or all available cores on the worker in standalone mode)
    * 各executorの使うcpu core

YARN-only:

* --driver-cores NUM
    * Number of cores used by the driver, only in cluster mode (Default: 1).
* --queue QUEUE_NAME
    * The YARN queue to submit to (Default: "default").
* --num-executors NUM
    * Number of executors to launch (Default: 2).
    * If dynamic allocation is enabled, the initial number of executors will be at least NUM.
    * `spark.executor.instances`
    * executorの総数
* --archives ARCHIVES
    * Comma separated list of archives to be extracted into the working directory of each executor.
* --principal PRINCIPAL
    * Principal to be used to login to KDC, while running on secure HDFS.
* --keytab KEYTAB
    * The full path to the file that contains the keytab for the principal specified above.
    * This keytab will be copied to the node running the Application Master via the Secure Distributed Cache, for renewing the login tickets and the delegation tokens periodically.

## Usage

```
${SPARK_HOME}/bin/spark-submit \
  --master <master-url> \
  --class <main-class>
  --name <name>
  ... # other options
  <application-jar> \
  [application-arguments]
```

Run PySpark script

```
${SPARK_HOME}/bin/spark-submit \
  --master spark://192.168.10.1:7077 \
  --files /host/data/data.csv \
  --files /host/data/data.json \
  /path/to/pyspark_script.py \
  <arg1>
```

## Tips

### python code arguments
* [Can I add arguments to python code when I submit spark job? - Stack Overflow](https://stackoverflow.com/questions/32217160/can-i-add-arguments-to-python-code-when-i-submit-spark-job)

Pass arguments to python files

```
spark-submit args.py arg1 arg2
# ['/spark/args.py', 'arg1', 'arg2']
```

### Precedence of configuration
設定の優先順位は以下の順序

1. SparkConf
2. `spark-submit`のオプション

## Reference
