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


## IAM, Role, Policy
- [Actions, Resources, and Condition Keys for Amazon Elastic MapReduce \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticmapreduce.html)
- [Actions, Resources, and Condition Keys for AWS Services \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html#actions_table)

* one for the EMR Cluster to use as a service
    * AmazonElasticMapReduceRole
        * for the EMR service
* one to place on your Cluster Instances to interact with AWS from those instances
    * AmazonElasticMapReduceforEC2Role
        * for EC2 profile


#### Service roles
- [Service Role for Amazon EMR \(EMR Role\) \- Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role.html)




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

You can connect to Master node with user name `hadoop` and private key which you specify when you create the cluster

```
ssh hadoop@ec2-###-##-##-###.compute-1.amazonaws.com -i ~/mykeypair.pem
```

## Web UI
* [Amazon EMR クラスターでホストされているウェブサイトの表示 - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/ManagementGuide/emr-web-interfaces.html)

Security上の理由で、これらはmaster node上のlocalhost上でのみ閲覧可能。
外部から見るためには、sshのport forwardingが必要。

| Interface name         | URI                                    |
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
`YARN ResourceManager` にaccessしたい場合

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
特に設定しなくともHadoopはdefaultでmasterにlogを残す。
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
* [aws-samples/emr-bootstrap-actions: This repository hold the Amazon Elastic MapReduce sample bootstrap actions](https://github.com/aws-samples/emr-bootstrap-actions)

* Hadoop userとして実行できる
* `sudo`で実行できる
* 16個までのbootstrap actionを追加できる

`filename`には、実行ファイルを指定する。

```
aws emr create-cluster --bootstrap-action Path=s3://mybucket/filename",Args=[arg1,arg2]
```

bootstrap actionとして、defaultで提供されているものがいくつかある。
以下は`run-if`で、masterでのみ実行されるようになっている。
`run-if`で2つめの引数に`s3://`のpathを指定すれば、s3からdlして実行されるが、`emr`のversionによってはerrorになる。
https://forums.aws.amazon.com/thread.jspa?threadID=222418

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
    "Path":"s3://ap-northeast-1.elasticmapreduce/bootstrap-actions/run-if",
    "Args": [
        "instance.isMaster=true",
        "s3://path/to/file"
    ],
    "Name":"comment"
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
* `/emr/service-nanny `
    * Logs written by the service nanny process.
* `/mnt/var/log/application`
    * Logs specific to an application such as Hadoop, Spark, or Hive.

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


## Cloudwatch
* [Monitor CloudWatch Events \- Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-cloudwatch-events.html)

* Amazon EMR tracks events and keeps information about them for up to seven days

#### Cloudwatch Metrics
[Monitor Metrics with CloudWatch \- Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.html#UsingEMR_ViewingMetrics_MetricsReported)

These metrics can be used for Autocaling.


## Default and Custom EMR
* [Using the Default Amazon Linux AMI for Amazon EMR \- Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-default-ami.html)
* [Using a Custom AMI \- Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami.html)

A custom AMI is useful if you want to do the following

* Encrypt the EBS root device volumes (boot volumes) of EC2 instances in your cluster. For more information
* Pre-install applications and perform other customizations instead of using bootstrap actions. This can improve cluster start time and streamline the startup work flow. For more information and an example, see Creating a Custom Amazon Linux AMI from a Preconfigured Instance.
* Implement more sophisticated cluster and node configurations than bootstrap actions allow.


If you use Amazon linux AMI with creation date of 2018-08-11, the Oozie server fails to starts.
You can get the appropriate AMI ID by the following commands

```
aws ec2 \
    --region us-east-1 \
    describe-images \
        --owner amazon \
        --query 'Images[?Name!=`null`]|[?starts_with(Name, `amzn-ami-hvm-2018.03`) == `true`].[CreationDate,ImageId,Name]' \
        --output text | sort -rk1
```

Restrictions of custom AMI

* Custom AMI 'ami-0132f06b8806d60d2' is not valid: The AMI must have only one EBS volume. AMIs with multiple EBS volumes are not supported.
    * Thus, the default AMI is not used as Custom AMI

## IAM
- [Actions, Resources, and Condition Keys for Amazon Elastic MapReduce \- AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonelasticmapreduce.html#amazonelasticmapreduce-editor)

- Resource Type
    - cluster
- ARN
    - `arn:${Partition}:elasticmapreduce:${Region}:${Account}:cluster/${ClusterId}`
- Condition key
    - `elasticmapreduce:ResourceTag/${TagKey}`
- Resource Type
    - editor
- ARN
    - `arn:${Partition}:elasticmapreduce:${Region}:${Account}:editor/${EditorId}`
- Condition key
    - `elasticmapreduce:ResourceTag/${TagKey}`

#### IAM Role
- [Configure IAM Roles for Amazon EMR Permissions to AWS Services and Resources \- Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles.html)


- EMR Role
- EMR Role for EC2
- Automatic Scaling Role
- The IAM Role for EMR Notebooks
- Service-Linked Role
    - A service-linked role is a unique type of IAM role that is linked directly to Amazon EMR. The service-linked role is predefined by Amazon EMR and includes the permissions that Amazon EMR requires to call Amazon EC2 on your behalf to clean up cluster resources after they are no longer in use

## Tips

#### Add tags to EC2 instance
EC2 instanceにtagをつけたい場合は、add-tagsを使う
cluster内の全てのinstanceにtagを付与できる。

```
aws emr add-tags --resource-id j-xxxxxxx --tags name="John Doe"
```

#### Load data from Dynamo DB
- [Hive Command Examples for Exporting, Importing, and Querying Data in DynamoDB \- Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/EMR_Hive_Commands.html)


```sql
CREATE EXTERNAL TABLE hiveTableName (col1 string, col2 bigint, col3 array<string>)
STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler' 
TBLPROPERTIES (
    "dynamodb.table.name" = "dynamodbtable1",
    "dynamodb.column.mapping" = "col1:name,col2:year,col3:holidays"
);

SET dynamodb.throughput.read.percent=1.0;

INSERT OVERWRITE DIRECTORY 'hdfs:///user/<username>/tablename' SELECT * FROM hiveTableName;
```

#### Run query to the data in Dynamo DB

```sql
CREATE EXTERNAL TABLE hive_purchases(
    customerId bigint,
    total_cost double,
    items_purchased array<String>
)
STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
TBLPROPERTIES (
    "dynamodb.table.name" = "Purchases",
    "dynamodb.column.mapping" = "customerId:CustomerId,total_cost:Cost,items_purchased:Items"
);
SET dynamodb.throughput.read.percent=1.0;

SELECT max(total_cost) from hive_purchases where customerId = 717;
```

#### Yarn zombie process
- [Yarn zombie processes \- Cloudera Community](https://community.cloudera.com/t5/Cloudera-Manager-Installation/Yarn-zombie-processes/td-p/32318)

#### Yarn log aggregation
- [AWS Blog » YARN Log aggregation on EMR Cluster – How to ?](https://aws.mannem.me/?p=1003)

#### Health check of nodes
- [Apache Hadoop 2\.9\.2 – NodeManager](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/NodeManager.html#Health_checker_service)


#### Usercache directory in yarn
- [yarn \+ usercache \+ folder became with huge size \- Hortonworks](https://community.hortonworks.com/questions/201820/yarn-usercache-folder-became-with-huge-size.html)

#### Unbalanced HDFS
- [Why HDFS data Becomes unbalanced](https://docs.hortonworks.com/HDPDocuments/HDP3/HDP-3.1.0/data-storage/content/why_hdfs_data_becomes_unbalanced.html)

#### Safemode exception
- [HDFS goes into read\-only mode and errors out with "Name node is in safe mode"](https://community.pivotal.io/s/article/HDFS-goes-into-readonly-mode-and-errors-out-with-Name-node-is-in-safe-mode)
- [What is Safemode in Hadoop? \- DataFlair](https://data-flair.training/forums/topic/what-is-safemode-in-hadoop/)

#### Disk space for namenodes
- [Troubleshoot Disk Space Issues with EMR Core Nodes](https://aws.amazon.com/premiumsupport/knowledge-center/core-node-emr-cluster-disk-space/)
- [HDFS Metadata Directories Explained](https://hortonworks.com/blog/hdfs-metadata-directories-explained/)
- [Why are the HDFS edit logs retained after a checkpoint operation is complete? \- Hortonworks](https://community.hortonworks.com/questions/16018/why-are-the-hdfs-edit-logs-retained-after-a-checkp.html)
- [A Guide to Checkpointing in Hadoop \- Cloudera Engineering Blog](https://blog.cloudera.com/blog/2014/03/a-guide-to-checkpointing-in-hadoop/)
- [Edit Logs piling up under nn current directory and\.\.\. \- Cloudera Community](https://community.cloudera.com/t5/Storage-Random-Access-HDFS/Edit-Logs-piling-up-under-nn-current-directory-and-using-lot/td-p/26105)
- [Best Practices and Tips for Optimizing AWS EMR](https://cloud.netapp.com/blog/optimizing-aws-emr-best-practices)
- [BigInsights: Hadoop Cleaning up your HDFS Trash \- POWER me up Blog](https://www.ibm.com/developerworks/community/blogs/powermeup/entry/BigInsights_Hadoop_Cleaning_up_you_HDFS_Trash?lang=en)
- [Top 10 NameNode\-related problems \| MapR](https://mapr.com/blog/top-10-namenode-related-problems/)
- [Developer Blog: Don't fill your HDFS disks \(upgrading to CDH 5\.4\.2\)](http://gbif.blogspot.com/2015/05/dont-fill-your-hdfs-disks-upgrading-to.html)
- [HDFS Architecture Guide](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
- [Amazon EMR: five ways to improve the way you use Hadoop](https://cloudacademy.com/blog/amazon-emr-five-ways-to-improve-the-way-you-use-hadoop/)
- [archive\.cloudera\.com/cdh4/cdh/4/hadoop/hadoop\-project\-dist/hadoop\-hdfs/hdfs\-default\.xml](http://archive.cloudera.com/cdh4/cdh/4/hadoop/hadoop-project-dist/hadoop-hdfs/hdfs-default.xml)
- [What is the use of fsimage in hadoop? \| Edureka Community](https://www.edureka.co/community/33860/what-is-the-use-of-fsimage-in-hadoop)
- [Secondary Namenode \- What it really do?](http://blog.madhukaraphatak.com/secondary-namenode---what-it-really-do/)


## Security Groups
* https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-sg-specify.html

* EmrManagedMasterSecurityGroup
* EmrManagedSlaveSecurityGroup
* ServiceAccessSecurityGroup
* AdditionalMasterSecurityGroups
* AdditionalSlaveSecurityGroups

## Reference
* [AWS EMRを動かしてみよう。 - Qiita](http://qiita.com/uzresk/items/76ba0c9700e1d78fe5e3) 
* [Configuring Applications - Amazon EMR](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html)
