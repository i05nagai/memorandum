## EMR
Elastic Map Reduce

* Hadoop
* Spark

両方使えるらしい。

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

作成済みのクラスタにstepを追加

```sh
aws emr add-steps
    --cluster-id j-2AXXXXXXGAPLF
    --steps Type=Spark,Name="Spark Program",ActionOnFailure=CONTINUE,Args=[--class,org.apache.spark.examples.SparkPi,/usr/lib/spark/lib/spark-examples.jar,10]
```

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

SSHのport forwardingで直接見れない場合もSSHで接続可能であれば閲覧可能。

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


## Reference
* [AWS EMRを動かしてみよう。 - Qiita](http://qiita.com/uzresk/items/76ba0c9700e1d78fe5e3) 
* [（オプション）追加のソフトウェアをインストールするためのブートストラップアクションの作成 - Amazon EMR](http://docs.aws.amazon.com/ja_jp/emr/latest/DeveloperGuide/emr-plan-bootstrap.html)
* * [Configuring Applications - Amazon EMR](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html)

