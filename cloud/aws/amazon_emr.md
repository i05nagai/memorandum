---
title: Amazon EMR
---

## Amazon EMR
Elastic Map Reduce.
EMR supports many cluster software including:

* Hadoop
* Spark
* ganglia

## custom jar file
EMRでdefaultで提供されいてるjarファイルがある。
stepで処理を実行する際に利用する。

`script-runner.jar`

* cluster内でscriptを実行する
* S3にuploadしているshell scriptなどを実行できる
* `s3://region.elasticmapreduce/libs/script-runner/script-runner.jar`
    * reagionはEMRのregion


```sh
aws emr add-steps \
    --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://region.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://mybucket/script-path/my_script.sh","--option","args"]
```

`command-runner.jar`

* [Command Runner - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-commandrunner.html)
* 以下のcommandを実行する場合はこちらを使う
    * spark-submit
    * s3-dist-cp

## Steps
* [hadoop - How to execute a shell script on all nodes of an EMR cluster? - Stack Overflow](https://stackoverflow.com/questions/36102316/how-to-execute-a-shell-script-on-all-nodes-of-an-emr-cluster)
    * stepはmaster nodeのみで実行される

Clusterでの処理は、stepという形で追加する。
Cluster modeでは、S3に作業用のファイルなどをおく必要がある。
Client modeでは、localのfileを利用できる。
cluster作成時に、stepを指定おく方法と、作成後に`aws emr add-steps`などでstepを追加する方法がある。

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
        * stepが失敗した場合、クラスターを停止します。クラスターの停止保護が有効で、自動終了が無効な場合は、クラスターは停止されません。
    * CANCEL_AND_WAIT
        * stepが失敗した場合、残りのステップをキャンセルします。
        * `--no-auto-terminate`がある場合は、全てのstepが終了しても終了しない
* Args
    * 必要な引数
    * 配列として渡す
* Jar
    * 実行jar

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

## Pricing
* [料金 - Amazon EMR | AWS](https://aws.amazon.com/jp/emr/pricing/)

EC2のinstanceを借りるより安い。
1時間単位で課金されるので、一旦起動したら一時間使った方が良い。
起動した時点で課金が開始される。

* nomarlized instance hours
    * [AWS | Amazon EMR | FAQs](https://aws.amazon.com/emr/faqs/)
    * instance sizeごとに倍率をかけて利用時間をだしたもの
    * smallが1で大きくなるごとに倍率が増えて、最大で64
    * m1.smallを1時間使って1 hourになる

## SSH
To Master Node

アカウント名は、haddoopで、keyはcluster作成時に指定したkey pairである。

```
ssh hadoop@ec2-###-##-##-###.compute-1.amazonaws.com -i ~/mykeypair.pem
```

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

1. Open a terminal window. On Mac OS X, choose `Applications > Utilities > Terminal`.
On other Linux distributions, terminal is typically found at `Applications > Accessories > Terminal`.
2. To establish an SSH tunnel with the master node using dynamic port forwarding, type the following command.
Replace ~/key.pem with the location and filename of the private key file (.pem) used to launch the cluster.
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
* shutdown-actionsのlogは、`node`の以下の対応するnodeのstdoutに出力される。


## Environment variables
* [amazon web services - How to set a custom environment variable in EMR to be available for a spark Application - Stack Overflow](https://stackoverflow.com/questions/42395020/how-to-set-a-custom-environment-variable-in-emr-to-be-available-for-a-spark-appl)



## Logging
* [Configure Cluster Logging and Debugging - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-debugging.html)

default logfiles

* by default, each cluster write log files in `/mnt/var/log/ ` on the master node
* step logs
    * generated by the Amazon EMR service
    * `/mnt/var/log/hadoop/steps/` on the master node
    * `/mnt/var/log/hadoop/steps/s-stepId1/` for the first step
* Hadoop and YARN component logs
    * stored in separate folders in`/mnt/var/log`
    * directories for Hadoop component
        * `hadoop-hdfs/`
        * `hadoop-mapreduce/`
        * `hadoop-httpfs/`
        * `hadoop-yarn/`
        * `hadoop-state-pusher/`
            * is for the output of the Hadoop state pusher process.
* Bootstrap action logs
    * stored in `/mnt/var/log/bootstrap-actions/` on the master node
    * `/mnt/var/log/bootstrap-actions/1/ ` for first bootstrap action
* Instance state logs
    * sotred in `/mnt/var/log/instance-state/` on the master node
    * information about CPU, memory state, garbage collector threads of the node

Archive Log Files to Amazon S3

* you need to enable this feature
* from CLI, you need to specify `--log-uri`
* you can use `lifecycle` settings in `S3` to automatically delete archived logs


```
aws emr create-cluster \
    --name "Test cluster" \
    --release-label emr-4.0.0 \
    --log-uri s3://mybucket/logs/ \
    --applications Name=Hadoop Name=Hive Name=Pig \
    --use-default-roles \
    --ec2-attributes KeyName=myKey \
    --instance-type m4.large \
    --instance-count 3
```

## View log files
* [View Log Files - Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-view-web-log-files.html#emr-manage-view-web-log-files-debug)

View Log Files on the Master Node

* `/mnt/var/log/application`
    * log specific to application such as `Spark`, Hadoop, Hive
* `/mnt/var/log/hadoop/steps/N`
    * `N` is step id.
    * `controller`
        * Information about the processing of the step.
        * If your step fails while loading, you can find the stack trace in this log.
    * `syslog`
        * Describes the execution of Hadoop jobs in the step.
    * `stderr`
        * The standard error channel of Hadoop while it processes the step.
    * `stdout`
        * The standard output channel of Hadoop while it processes the step.

View Log Files Archived to Amazon S3


* `/JobFlowId/node/`
    * bootstrap action
    * instance state
    * application logs for the node
    * The logs for each node are stored in a folder labeled with the identifier of the EC2 instance of that node.
* `/JobFlowId/node/instanceId/application`
    * log specific to application such as `Spark`, Hadoop, Hive
    * e.g. `JobFlowId/node/instanceId/hive/hive-server.log`
* `/JobFlowId/steps/N/`
    * `/mnt/var/log/hadoop/steps/N`
* `/JobFlowId/containers`
    * The logs for each YARN application are stored in these locations.


## Tips

### Add tags to EC2 instance
EC2 instanceにtagをつけたい場合は、add-tagsを使う
cluster内の全てのinstanceにtagを付与できる。

```
aws emr add-tags --resource-id j-xxxxxxx --tags name="John Doe"
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

Stepで追加する場合は、以下のstepを追加する。

```sh
aws emr add-steps
    --cluster-id j-2AXXXXXXGAPLF
    --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://region.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh","--toree","--ds-packages","--python-packages","'ggplot nilearn'","--ml-packages","--cached-install","--notebook-dir","s3://path/to/jupyter-notebook/","--port","8080","--jupyterhub","--jupyterhub-port","8001","--copy-samples"]
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
