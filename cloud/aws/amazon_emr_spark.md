---
title: Amazon EMR Spark
---

## Amazon EMR Spark
* [Spark ステップの追加 - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ReleaseGuide/emr-spark-submit-step.html)
* [Submitting Applications - Spark 2.1.1 Documentation](https://spark.apache.org/docs/latest/submitting-applications.html)

sparkの場合は、`spark-submit`コマンドが実行されるので、引数`Args`には、`spark-submit`に渡すものをわたす。


クラスタ作成時にstepを指定

```sh
aws emr create-cluster \
--name "Add Spark Step Cluster" \
--release-label emr-5.4.0 \
--applications Name=Spark \
--ec2-attributes KeyName=myKey\
--instance-type m3.xlarge
--instance-count 3 \
--steps Type=Spark,Name="Spark Program",ActionOnFailure=CONTINUE,Args=[--class,org.apache.spark.examples.SparkPi,/usr/lib/spark/lib/spark-examples.jar,10]
--use-default-roles
```

クラスタ作成時にstepを指定 with `command-runner.jar`

```sh
aws emr create-cluster \
--name "Add Spark Step Cluster" \
--release-label emr-5.4.0 \
--applications Name=Spark
--ec2-attributes KeyName=myKey
--instance-type m3.xlarge
--instance-count 3 \
--steps Type=CUSTOM_JAR,Name="Spark Program",Jar="command-runner.jar",ActionOnFailure=CONTINUE,Args=[spark-example,SparkPi,10]
--use-default-roles
```

作成済みのクラスタにstepを追加(shorthand)

```sh
aws emr add-steps
    --cluster-id j-2AXXXXXXGAPLF
    --steps Type=Spark,Name="Spark Program",ActionOnFailure=CONTINUE,Args=[--class,org.apache.spark.examples.SparkPi,/usr/lib/spark/lib/spark-examples.jar,10]
```

作成済みのクラスタにstepを追加(json file)

```sh
aws emr add-steps
    --cluster-id j-2AXXXXXXGAPLF
    --steps path_to_json
```

```json
[
  {
    "Name": "string",
    "Args": ["string", ...],
    "Jar": "string",
    "ActionOnFailure": "TERMINATE_CLUSTER"|"CANCEL_AND_WAIT"|"CONTINUE",
    "MainClass": "string",
    "Type": "CUSTOM_JAR"|"STREAMING"|"HIVE"|"PIG"|"IMPALA",
    "Properties": "string"
  }
]
```

Get step information

```
aws emr describe-step
    --cluster-id <value>
    --step-id <value>
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

## Spark History Server
EMRのspark history serverは以下の形式で実行されている。

```
/usr/lib/jvm/java-openjdk/bin/java \
    -cp /usr/lib/spark/conf/:/usr/lib/spark/jars/*:/etc/hadoop/conf/ \
    -XX:OnOutOfMemoryError=kill -9 %p -Xmx1g org.apache.spark.deploy.history.HistoryServer
```

`/usr/lib/spark/conf/spark-defaults.sh`の中で、history logの場所が`hdfs:///var/log/spark/apps`として保存されている。


## Logging
* [View Log Files - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-view-web-log-files.html)
* [View Log Files - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-view-web-log-files.html#emr-manage-view-web-log-files-debug)
* [View Application History - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-cluster-application-history.html)
    * `EMR 5.8`からWeb UIでSpark Applicationのjobのlogがみれる

EMRのmaster nodeでspark-submitすると結果が以下のようにでる。
`tracking URL`に実行Logが記録される。
stdoutなども記録されている。
sparkのlog dirは`/usr/lib/spark/conf/`の中で`/var/log/spark`として指定されている。


log4jのloggingは、`containers/<container-id>`に出力される。

## Configuration
* spark.history.fs.logDirectory
    * `hdfs:///var/log/spark/apps`
* spark.eventLog.dir
    * `hdfs:///var/log/spark/apps`

`/usr/lib/spark` is SPARK_HOME.

```
yarn logs -applicationId <application-id> -containerId <container-id>
```


## Tips

### spark-submit fields
spark submitの引数にS3のfileを指定できる。
EMRの場合はS3に必要なscriptなどをuploadして、利用することになる。

```
spark-submit \
        --deploy-mode cluster \
        --executor-cores 2 \
        --executor-memory 4G \
        --num-executors 12 \
        --py-files s3://path/to/python_lib.py,s3://path/to/settings.py \
        s3://path/to/script.py <arg1> <arg2>
```

#### Add steps
EMRを起動する時に、`command-runner.jar`に`spark-submit`を指定できるが、`spark-submit`を直接実行するのではなくて、`s3://`にuploadしたshell scriptを実行するようにした方が良い。
開発のdebugの際などに、EMRのstepから実行commandをcopyする必要がでてくる。

```json
  {
    "Args": [
      "spark-submit",
      "--deploy-mode",
      "cluster",
      "--executor-cores",
      "4",
      "--executor-memory",
      "8G",
      "--num-executors",
      "4",
      "--files",
      "${path_to_s3_spark}/file.txt",
      "${path_to_s3_spark}/file.py"
    ],
    "Type": "CUSTOM_JAR",
    "ActionOnFailure": "CANCEL_AND_WAIT",
    "Jar": "command-runner.jar",
    "Properties": "=",
    "Name": "Step1"
  },
```

以下のような形にする。

```json
  {
    "Args": [
      "${path_to_s3_spark}/run_step1.sh"
    ],
    "Type": "CUSTOM_JAR",
    "ActionOnFailure": "CANCEL_AND_WAIT",
    "Jar": "script-runner.jar",
    "Properties": "=",
    "Name": "Step1"
  },
```

#### Add environment variables to spark/pyspark
* [Configuring Applications - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html)

configurationに以下を設定する。

```json
{
  "Classification": "spark-defaults",
  "Properties": {
    "spark.yarn.appMasterEnv.ENVIRONMENT_NAME": "${ENVIRONMENT_NAME}",
    "spark.yarn.executorEnv.ENVIRONMENT_NAME": "${ENVIRONMENT_NAME}"
  }
}
```

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

## Error

#### Error
* [amazon web services - Cannot create temp dir with proper permission: /mnt1/s3 - Stack Overflow](https://stackoverflow.com/questions/41221821/cannot-create-temp-dir-with-proper-permission-mnt1-s3)

* 以下のerror
    * S3上のfile作成でerror
    * この場合はfolder名と同じfileを作成しているとerrorになった

```
17/08/29 07:15:46 INFO GPLNativeCodeLoader: Loaded native gpl library
17/08/29 07:15:46 INFO LzoCodec: Successfully loaded & initialized native-lzo library 
17/08/29 07:15:46 INFO deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
17/08/29 07:15:46 INFO deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
17/08/29 07:15:46 INFO deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
17/08/29 07:15:46 INFO deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
17/08/29 07:15:46 INFO deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
17/08/29 07:15:47 WARN ConfigurationUtils: Cannot create temp dir with proper permission: /mnt1/s3
java.nio.file.AccessDeniedException: /mnt1
	at sun.nio.fs.UnixException.translateToIOException(UnixException.java:84)
	at sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:102)
	at sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:107)
	at sun.nio.fs.UnixFileSystemProvider.createDirectory(UnixFileSystemProvider.java:384)
	at java.nio.file.Files.createDirectory(Files.java:674)
	at java.nio.file.Files.createAndCheckIsDirectory(Files.java:781)
	at java.nio.file.Files.createDirectories(Files.java:767)
	at com.amazon.ws.emr.hadoop.fs.util.ConfigurationUtils.getTestedTempPaths(ConfigurationUtils.java:244)
	at com.amazon.ws.emr.hadoop.fs.s3n.S3NativeFileSystem.initialize(S3NativeFileSystem.java:440)
	at com.amazon.ws.emr.hadoop.fs.EmrFileSystem.initialize(EmrFileSystem.java:109)
	at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:2717)
	at org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:93)
	at org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:2751)
	at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:2733)
	at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:377)
	at org.apache.hadoop.fs.Path.getFileSystem(Path.java:295)
	at org.apache.hadoop.mapred.LineRecordReader.<init>(LineRecordReader.java:108)
	at org.apache.hadoop.mapred.TextInputFormat.getRecordReader(TextInputFormat.java:67)
	at org.apache.spark.rdd.HadoopRDD$$anon$1.liftedTree1$1(HadoopRDD.scala:252)
	at org.apache.spark.rdd.HadoopRDD$$anon$1.<init>(HadoopRDD.scala:251)
	at org.apache.spark.rdd.HadoopRDD.compute(HadoopRDD.scala:211)
	at org.apache.spark.rdd.HadoopRDD.compute(HadoopRDD.scala:102)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:323)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:287)
	at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:323)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:287)
	at org.apache.spark.rdd.MapPartitionsRDD.compute(MapPartitionsRDD.scala:38)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:323)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:287)
	at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:87)
	at org.apache.spark.scheduler.Task.run(Task.scala:99)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:322)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
	at java.lang.Thread.run(Thread.java:748)
```

## Reference
