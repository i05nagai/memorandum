---
title: EMR
---

## EMR
Elastic Map Reduce

* Hadoop
* Spark

## custom jar file
EMRでdefaultで提供されいてるjarファイルがある。

* script-runner.jar
    * cluster内でscriptを実行する
    * `s3://region.elasticmapreduce/libs/script-runner/script-runner.jar`
        * reagionはEMRのregion


```sh
aws emr add-steps \
    --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://region.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://mybucket/script-path/my_script.sh","--option","args"]
```


* command-runner.jar
    * [Command Runner - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ReleaseGuide/emr-commandrunner.html)
    * 以下のcommandを実行する場合はこちらを使う
        * spark-submit
        * s3-dist-cp



## Steps
Clusterでの処理は、stepという形で追加する。
Cluster modeでは、S3に作業用のファイルなどをおく必要がある。
Client modeでは、ローカルのファイルを利用できる。
クラスタ作成時に、stepを指定おく方法と、作成後に`aws emr add-steps`などでstepを追加する方法がある。

* Type
    * typeごとに実行されるコマンドが決まっている
    * Spark, Hive, etc
* Name
    * stepの名前
* ActionOnFailure
    * failしたときにどうするか
    * CONTINUE
        * failしたときにINSTANCEを終了しない
    * TERMINATE_CLUSTER
        * テップが失敗した場合、クラスターを停止します。クラスターの停止保護が有効で、自動終了が無効な場合は、クラスターは停止されません。
    * CANCEL_AND_WAIT
        * ステップが失敗した場合、残りのステップをキャンセルします。
        * `--no-auto-terminate`がある場合は、全てのstepが終了しても終了しない
* Args
    * 必要な引数
    * 配列として渡す

Spark programm


```sh
aws emr add-steps \
    --cluster-id j-2AXXXXXXGAPLF \
    --steps Type=CUSTOM_JAR,Name="Spark Program",Jar="command-runner.jar",ActionOnFailure=CONTINUE,Args=[spark-example,SparkPi,10]
```


```sh
aws emr add-steps \
    --cluster-id j-2AXXXXXXGAPLF \
    --steps Name="Command Runner",Jar="command-runner.jar",Args=["spark-submit","Args..."]
```


### Spark
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
````

stepの情報を取得

```
aws emr describe-step
    --cluster-id <value>
    --step-id <value>
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

## Billing

* nomarlized instance hours
    * [AWS | Amazon EMR | FAQs](https://aws.amazon.com/emr/faqs/)
    * instance sizeごとに倍率をかけて利用時間をだしたもの
    * smallが1で大きくなるごとに倍率が増えて、最大で64
    * m1.smallを1時間使って1 hourになる


## Web UI
* [Amazon EMR クラスターでホストされているウェブサイトの表示 - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ManagementGuide/emr-web-interfaces.html)

Security上の理由で、これらはmaster node上のlocalhost上でのみ閲覧可能。
外部から見るためには、sshのport forwardingが必要。


| インターフェイスの名前 | URI                                    |
|------------------------|----------------------------------------|
| YARN ResourceManager   | http://master-public-dns-name:8088/    |
| YARN NodeManager       | http://slave-public-dns-name:8042/     |
| Hadoop HDFS NameNode   | http://master-public-dns-name:50070/   |
| Hadoop HDFS DataNode   | http://slave-public-dns-name:50075/    |
| Spark HistoryServer    | http://master-public-dns-name:18080/   |
| Zeppelin               | http://master-public-dns-name:8890/    |
| Hue                    | http://master-public-dns-name:8888/    |
| Ganglia                | http://master-public-dns-name/ganglia/ |
| HBase UI               | http://master-public-dns-name:16010/   |

* [オプション 1: ローカルポートフォワーディングを使用してマスターノードへの SSH トンネルをセットアップする - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ManagementGuide/emr-ssh-tunnel-local.html)
* [Option 2, Part 2: Configure Proxy Settings to View Websites Hosted on the Master Node - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html)

SSHのport forwardingで直接見れない場合もSSHで接続可能であれば閲覧可能。

1. Open a terminal window. On Mac OS X, choose `Applications > Utilities > Terminal`. On other Linux distributions, terminal is typically found at `Applications > Accessories > Terminal`.
2. To establish an SSH tunnel with the master node using dynamic port forwarding, type the following command. Replace ~/dpi_rsa.pem with the location and filename of the private key file (.pem) used to launch the cluster.
    * Note: Port `port_num` used in the command is a randomly selected, unused local port.

```
ssh -i ~/key -ND port_num hadoop@hostname
```

4. Type yes to dismiss the security warning.


### Option1. local port forwarding
`YARN ResourceManager`にaccessしたい場合

```
ssh -i ~/mykeypair.pem -N -L 8157:ec2-###-##-##-###.compute-1.amazonaws.com:8088 hadoop@ec2-###-##-##-###.compute-1.amazonaws.com
```

* `mykeypari.pem`
    * masterに設定されているkeypair
* `8157`
    * local側のport
* `ec2-###-##-##-###.compute-1.amazonaws.com`
    * 接続先からアクセスするhost
* `hadoop@ec2-###-##-##-###.compute-1.amazonaws.com`
    * 接続先のuser`haddop`
    * 接続先`ec2-###-##-##-###.compute-1.amazonaws.com`
* `8088`
    * 接続先からアクセスするport番号

以上の設定で、`http://localhost:8157`にアクセスすると`http://ec2-###-##-##-###.compute-1.amazonaws.com`にアクセスできる。
接続先のportごとにlocalのportが必要。


### Option2. dynamic port forwarding
aws-cliでもできる。

```
ssh -i ~/mykeypair.pem -N -D 8157 hadoop@ec2-###-##-##-###.compute-1.amazonaws.com
```

* `mykeypari.pem`
    * masterに設定されているkeypair
* `8157`
    * local側のport
* `hadoop@ec2-###-##-##-###.compute-1.amazonaws.com`
    * 接続先のuser`haddop`
    * 接続先`ec2-###-##-##-###.compute-1.amazonaws.com`

以上の接続をした後に、browserのsocksの設定をする。

* [オプション 2、パート 2: マスターノードでホストされるウェブサイトを表示するようにプロキシを設定する - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html)

For Chrome

* [Chrome Web Store - foxy proxy](https://chrome.google.com/webstore/search/foxy%20proxy)
    * Foxy Proxy Standardをinstallする
* 以下のxmlを`foxyproxy-settings.xml`という名前で保存
* Chrome ExtensionのFoxyProxyのoptionから`Import/Export`を選ぶ
* importで`foxyproxy-settings.xml`を指定する。


```xml
<?xml version="1.0" encoding="UTF-8"?>
<foxyproxy>
   <proxies>
      <proxy name="emr-socks-proxy" id="2322596116" notes="" fromSubscription="false" enabled="true" mode="manual" selectedTabIndex="2" lastresort="false" animatedIcons="true" includeInCycle="true" color="#0055E5" proxyDNS="true" noInternalIPs="false" autoconfMode="pac" clearCacheBeforeUse="false" disableCache="false" clearCookiesBeforeUse="false" rejectCookies="false">
         <matches>
            <match enabled="true" name="*ec2*.amazonaws.com*" pattern="*ec2*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            <match enabled="true" name="*ec2*.compute*" pattern="*ec2*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            <match enabled="true" name="10.*" pattern="http://10.*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            <match enabled="true" name="*10*.amazonaws.com*" pattern="*10*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
            <match enabled="true" name="*10*.compute*" pattern="*10*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" /> 
            <match enabled="true" name="*.compute.internal*" pattern="*.compute.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false"/>
            <match enabled="true" name="*.ec2.internal* " pattern="*.ec2.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false"/>	  
       </matches>
         <manualconf host="localhost" port="8157" socksversion="5" isSocks="true" username="" password="" domain="" />
      </proxy>
   </proxies>
</foxyproxy>
```

FoxyProxyのproxyの設定をUse `emr-socks-proxy` をONにする。
ブラウザで`http://ec2-###-##-##-###.compute-1.amazonaws.com/ganlgia`や `http://ec2-###-##-##-###.compute-1.amazonaws.com:8088/`

## Debug
* [クラスタログとデバッグを構成する - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ManagementGuide/emr-plan-debugging.html)

SSHでmaster nodeに接続する。
特に設定しなくともHadoopはデフォルトでmasterにログを残す。
`/mnt/var/log/hadoop/`の下に、stepごと、bootstrapごとにまとまっている。
ただし、clusterがerrorやstepの終了で、terminateになるとLogも消える。

S3にlogを出力する。
S3にlogを出力するように設定しておけば、clusterが終了しても、logがS3に出力され、参照可能になる。
logの出力間隔は5分間隔。
設定するには、cluster作成時にS3のpathを指定しておく必要がある。
CLIの場合は以下のオプションをつける。

```
aws emr create-cluster --log-uri s3://mybucket/logs/
```

```
--enable-debugging
```

## bootstrap action
* [(Optional) Create Bootstrap Actions to Install Additional Software - Amazon EMR](http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-bootstrap.html)

* Hadoop userとして実行できる
* `sudo`で実行できる
* 16個までのbootstrap actionを追加できる

`filename`には、実行ファイルを指定する。

```
aws emr create-cluster --bootstrap-action Path=s3://mybucket/filename",Args=[arg1,arg2]
```

bootstrap actionとして、defaultで提供されているものがいくつかある。
以下は`run-if`で、masterでのみ実行されるようになっている。

```
aws emr create-cluster --bootstrap-action Path=s3://elasticmapreduce/bootstrap-actions/run-if,Args=["instance.isMaster=true","echo running on master node"]
```

jsonの形式の場合は

```json
[
  {
    "Path": "string",
    "Args": ["string", ...],
    "Name": "string"
  },
  {
    "Path": "string",
    "Args": ["string", ...],
    "Name": "string"
  }
  ...
]
```

### Shutdown action
* [(Optional) Create Bootstrap Actions to Install Additional Software - Amazon EMR](http://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-plan-bootstrap.html#bootstrap_Shutown)

* `/mnt/var/lib/instance-controller/public/shutdown-actions/`にclusterの終了時に実行したいscriptsをおく
* cluster終了時に上記foluderのscriptが並列に全て実行される
* scriptsは60sec以内終わる必用がある
* `/mnt/var/lib/instance-controller/public/shutdown-actions/`はdefaultでは作成されないので、自分で作成する必要がある

    


## ganglia
wgetが使える。

以下にgangliaのwebのcodeがある。

```
/usr/share/ganglia
```


```
/var/lib/ganglia
```

にgangliaのrddなどが保存されている。

## logs
EMRのmaster nodeでspark-submitすると結果が以下のようにでる。
`tracking URL`に実行Logが記録される。
stdoutなども記録されている。


* [ログファイルを表示する - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ManagementGuide/emr-manage-view-web-log-files.html)

sparkのlog dirは`/usr/lib/spark/conf/`の中で`/var/log/spark`として指定されている。


## Spark History Server
EMRのspark history serverは以下の形式で実行されている。

```
/usr/lib/jvm/java-openjdk/bin/java -cp /usr/lib/spark/conf/:/usr/lib/spark/jars/*:/etc/hadoop/conf/ -XX:OnOutOfMemoryError=kill -9 %p -Xmx1g org.apache.spark.deploy.history.HistoryServer
```

`/usr/lib/spark/conf/spark-defaults.sh`の中で、history logの場所が`hdfs:///var/log/spark/apps`として保存されている。


## Tips

### Error

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

### Add tags to EC2 instance
EC2 instanceにtagをつけたい場合は、add-tagsを使う
cluster内の全てのinstanceにtagを付与できる。

```
aws emr add-tags --resource-id j-xxxxxxx --tags name="John Doe"
```

### Add environment variables to spark/pyspark
configurationに以下を設定する。


```json
{
  "Classification": "spark-defaults",
  "Properties": {
    "spark.yarn.appMasterEnv.RETTY_DWH_ENVIRONMENT_NAME": "${RETTY_DWH_ENVIRONMENT_NAME}",
    "spark.yarn.executorEnv.RETTY_DWH_ENVIRONMENT_NAME": "${RETTY_DWH_ENVIRONMENT_NAME}"
  }
}
```

## Run jupyter notebook and jupyter hub on Amazon EMR
* [Run Jupyter Notebook and JupyterHub on Amazon EMR | AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/running-jupyter-notebook-and-jupyterhub-on-amazon-emr/)

以下にEMRのsetup用のscriptが追いてある。

```sh
s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh
```

以下のbootstrap commandで起動時にsetup可能。

```sh
aws emr create-cluster \
    --release-label emr-5.8.0 \
  --name 'emr-5.8.0 jupyter/ cli example' \
  --applications Name=Hadoop Name=Hive Name=Spark Name=Pig Name=Tez Name=Ganglia Name=Presto \
  --ec2-attributes KeyName=<your-ec2-key>,InstanceProfile=EMR_EC2_DefaultRole \
  --service-role EMR_DefaultRole \  
  --instance-groups \
    InstanceGroupType=MASTER,InstanceCount=1,InstanceType=c3.4xlarge \
    InstanceGroupType=CORE,InstanceCount=4,InstanceType=c3.4xlarge \
  --region us-east-1 \
  --log-uri s3://<your-s3-bucket>/emr-logs/ \
  --bootstrap-actions \
    Name='Install Jupyter notebook',Path="s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh",Args=[--r,--julia,--toree,--torch,--ruby,--ds-packages,--ml-packages,--python-packages,'ggplot nilearn',--port,8880,--password,jupyter,--jupyterhub,--jupyterhub-port,8001,--cached-install,--notebook-dir,s3://<your-s3-bucket>/notebooks/,--copy-samples]
```

Stepでついっかする場合は、以下のstepを追加する。

```sh
aws emr add-steps
    --cluster-id j-2AXXXXXXGAPLF
    --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://region.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh","--toree","--ds-packages","--python-packages","'ggplot nilearn'","--ml-packages","--cached-install","--notebook-dir","s3://retty-dpi/work_nagai/jupyter_notebook/","--port","8080","--jupyterhub","--jupyterhub-port","8001","--copy-samples"]
```

```json
[
  {
    "Name": "Install jupyter notebook",
    "Args": ["string", ...],
    "Jar": "CUSTOM_JAR",
    "ActionOnFailure": "TERMINATE_CLUSTER"|"CANCEL_AND_WAIT"|"CONTINUE",
    "MainClass": "string",
    "Type": "CUSTOM_JAR"|"STREAMING"|"HIVE"|"PIG"|"IMPALA",
    "Properties": "string"
  }
]
````

* --r
    * Install the IRKernel for R.
* --toree
    * sparkを使う場合は必要
    * Install the Apache Toree kernel that supports Scala, PySpark, SQL, SparkR for Apache Spark.
* --julia
    * Install the IJulia kernel for Julia.
* --torch
    * Install the iTorch kernel for Torch (machine learning and visualization).
* --ruby
    * Install the iRuby kernel for Ruby.
* --ds-packages
    * Install the Python data science-related packages (scikit-learn pandas statsmodels).
* --ml-packages
    * Install the Python machine learning-related packages (theano keras tensorflow).
* --bigdl
    * Install Intel’s BigDL deep learning libraries.
* `--python-packages 'package1,package2'`
    * Install specific Python packages (for example, ggplot and nilearn).
* --port
    * Set the port for Jupyter notebook. The default is 8888.
* --user
    * Set the default user for JupyterHub, default is jupyter
* `--password string`
    * Set the password for the Jupyter notebook.
* --localhost-only
    * Restrict Jupyter to listen on localhost only. The default is to listen on all IP addresses.
* --jupyterhub
    * Install JupyterHub.
* --jupyterhub-port
    * Set the port for JuputerHub. The default is 8000.
* --notebook-dir
    * S3にjupyter notbookを保存できる
    * localも指定可能
    * Specify the notebook folder. This could be a local directory or an S3 bucket.
* --cached-install
    * Use some cached dependency artifacts on S3 to speed up installation.
* --ssl
    * Enable SSL. For production, make sure to use your own certificate and key files.
* --copy-samples
    * Copy sample notebooks to the notebook folder.
* --spark-opts
    * User-supplied Spark options to override the default values.
* --python3
    * Packages and apps installed for Python 3 instead of Python 2.
* --s3fs
    * Use s3fs instead of the default, s3contents for storing notebooks on Amazon S3. This argument can cause slowness if the S3 bucket has lots of files.


default

* paswordなし port `8888`
* JupyterHub
    * port: 8000
## With jupyter
* [spark-emr-jupyter/emr_bootstrap.sh at master · mikestaszel/spark-emr-jupyter](https://github.com/mikestaszel/spark-emr-jupyter/blob/master/emr_bootstrap.sh)
* [ETL Offload with Spark and Amazon EMR - Part 2 - Code development with Notebooks and Docker](https://www.rittmanmead.com/blog/2016/12/etl-offload-with-spark-and-amazon-emr-part-2-code-development-with-notebooks-and-docker/)
* [SilviaTerra/docker-emr-poc](https://github.com/SilviaTerra/docker-emr-poc)
* [AWS EMR+ Jupyter + spark 2.x – Mudit – Medium](https://medium.com/@muppal/aws-emr-jupyter-spark-2-x-7da54dc4bfc8)
* [Jupyter Notebooks with PySpark on AWS EMR | Mike Staszel](http://mikestaszel.com/2017/10/16/jupyter-notebooks-with-pyspark-on-aws-emr/)
* [EMR上でPython3系でpysparkする - Qiita](https://qiita.com/uryyyyyyy/items/672a4058aba754b389d1)


## Reference
* [AWS EMRを動かしてみよう。 - Qiita](http://qiita.com/uzresk/items/76ba0c9700e1d78fe5e3) 
* [（オプション）追加のソフトウェアをインストールするためのブートストラップアクションの作成 - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/DeveloperGuide/emr-plan-bootstrap.html)
* [Configuring Applications - Amazon EMR](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html)
