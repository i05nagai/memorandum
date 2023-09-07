---
title: airflow
---

## airflow
Always write a function in dag file which returns the DAG instance.
Then call the function in main clause in dag file.

* You can unit-test the tasks by testing Dag instances to check whether the instance has expected values or data
* subdag operators can be easy to access other dag instances

## Install

```
pip install airflow
```

以下のコマンドで、初期化とサーバの立ち上げができる。

```
airflow initdb
airflow webserver -p 8080
```

airflowコマンドを一度でも実行すると、defaultだと`~/airflow`に作業用のディレクトリが作られる。

```sh
# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
export AIRFLOW_HOME=~/airflow
# initialize the database
airflow initdb
# start the web server, default port is 8080
airflow webserver -p 8080
```

DAGを追加するときは、`$AIRFLOW_HOME/dags/`以下にdagsを定義したpythonファイルを配置する。
defuaultで幾つかexampleのdagが追加されているので、動作確認が可能。

defaultのDBはsqliteになっているが、slqiteはtaskのworkerとweb serverからの同時アクセスができずに、動作が不安定になるっぽいので、すぐにMySQLなどに変更した方が良い。
また、MySQLなどに変更すれば、CeleryExecutorを入れてtaskの並列実行と手動実行ができるようになる。
celeryを使う場合は、 手動実行にもschedulerが必要になっているので、schedulerは起動させる。
workerは起動しないと、taskが処理されないので、起動する。

```
airflow worker
airflow scheduler
airflow webserver -p 8080
```

### Scaling out with Celery
taskの並列処理にはceleryが必要。
Web UIからTaskの手動実行する場合もCeleryが必要。

* [Configuration — Airflow Documentation](https://pythonhosted.org/airflow/configuration.html)

Installは、

```
pip install apache-airflow[mysql]
pip install apache-airflow[celery]
```

でOK。
使用するDBの設定は`airlfow.cfg`の以下を変更する。
password`;`は含まない方が良い。
Celeryのworkerなどでエラーが出る場合もある。

```ini
sql_alchemy_conn = mysql://[user_name]:[password]@[host]:[port]/[db_name]
broker_url = sqla+mysql://[user_name]:[password]@[host]:[port]/[db_name]
celery_result_backend = db+mysql://[user_name]:[password]@[host]:[port]/[db_name]
```

`pip install airflow[mysql]`で`mysql_config`がない系のエラーがでる場合は、

* mysql-devel
* mysql-community-devel

をいれると解決する場合がある。
また、MySQLは5.6.4以降にする必要がある。
Celeryの依存ライブラリである、kombuはGitHubの最新版をbuildしてinstallする必要がある。
なのでpipでCeleryをいれる場合は、kombuは削除して、入れ直す。

### Pool
* poolはWeb UIから作成できる。
* `Admin->Pool`から新しくpoolを作る。
* pool名とslot数を決める。
    * pool名はpoolのidになる
    * slot数はpool内のtaskの同時実行数
* poolを作成すると、airflowのpython script内でoperatorを作る際にpool名を指定できる

## Security
* [Security — Airflow Documentation](https://airflow.incubator.apache.org/security.html)

## Scheduling
* [Scheduling & Triggers — Airflow Documentation](https://airflow.incubator.apache.org/scheduler.html)

DAGごとにcronのようなscheduleを設定できる。
scheduleを設定しない場合は、手動実行のみ可能。
scheduleは`airflow.DAG`クラスを作成時に`schedule_interval`引数で指定する。
3通りの指定が可能

1. cron形式の指定も可能。
    * presetと同じ表現力
2. presetと呼ばれる以下の表現可能
    * `None`
    * `@once`
    * `@hourly`
    * `@daily`
    * `@weekly`
    * `@monthly`
    * `@yearly`
3. datetime.timedelta
    * 一番柔軟に指定できる

例えば1時間ごとに実行の場合は以下のように指定する。

```python
airflow.DAG(schedule_interval="0 * * * *")
airflow.DAG(schedule_interval=@hourly)
```

### Term/Conecepts
用語と概念

* downstream/upstream
    * taskのA, Bがあった場合、AのあとにBが実行されるとき
    * Aがupstream
    * Bがdownstream
* opertor
    * 個々のtaskはscriptの中では`Operator` instanceとして作成する
* sensor
    * Sensors are a special type of Operator that are designed to do exactly one thing - wait for something to occur.
* task
    * operatorがinstance化されるとtaskと呼ばれる
* task instance
    * 実行中のtask
    * `running`, `failed`, `skipped`, `up for retry`などの状態を持つ
* DAG
    * task(or operator or task instance)の集まりに実行順序関係をつけたもの
* plugin
    * https://github.com/airflow-plugins/
* Queue
    * taskをqueueして、実行するにはexecutorをCeleryExecutorに変更する必要がある
    * CeleryExecutorを使うには、airflow用のdbをMySQLなどに変更する必要がある
        * defaultはsqlite
    * queueに入ったtaskは、taskのworkerが引き受ける
    * queueは名前(id)をつける
    * queueはBaseOperatorの引数として、指定できる
    * queueは複数つけることができる
    * default(未指定)のqueueは`airflow.cfg`で指定されている
* Worker
    * taskをqueueに登録して、queue内のtaskを引き受けるのがworker
    * 例えば、sparkで実行するtaskをspark用のqueueにいれて、spark用のworkerのみがそのtaskを引き受けるということもできる
    * web serverのworkerとtaskのworkerそれぞれ存在する
* Service Level Agreement
    * taskが正常終了するまでの期限を記載できる
    * 期限までに終了しなければ、missed SLAとしてlogが記録される
    * 期限はtimedeltaで指定
* Trigger rules
    * すべてのoperatorで指定できる
    * 親のoperatorの終了状態(success, failedなど)をtriggerに、実行制御ができる
* zombie & undead
* policy
    * taskに対して、policyを設定できる
    * 特定の条件を満たすtask (operator)に対する設定を記述できる
    * 例えば、特定のoperatorはあるqueueにいれるなど
* XComs
    * cross communication
    * task間でのやり取りをするための、key, value store
    * `python operator`内で、実行結果などを保存でき、他の`python operator`から取り出すことができる。
* hooks
    * https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/connections.html
    * A Hook is a high-level interface to an external platform that lets you quickly and easily talk to them without having to write low-level code that hits their API or uses special libraries
    * Hook to S3
* Pools
    * 並列実行するtaskをpoolすることができる
    * poolにつまれたtaskを、何個のworkerが処理するかを指定できる
    * Web UIからも設定可能
    * operatorのpool引数で、operatorの所属するpoolを指定する
        * 何も指定しない場合はdefault poolに入る
* schedule_interval
    * 実行間隔
* execution_date
    * taskがschedulingされている日で実行された日とは異なる
    * base_dateが`2017-07-01`でschedule_intervalが`1 day`の場合で、scheduleをONにしたのが`2017-07-05`の場合は、DAGは5回実行される。このときのexecution_dateは
        * `2017-07-01`
        * `2017-07-02`
        * `2017-07-03`
        * `2017-07-04`
        * `2017-07-05`
    * schedule_intervalが`1 day`でJSTの場合、`2017-07-05 09:00:00+9:00`=`2017-07-05 00:00:00+0:00`にexecution date`2017-07-04 00:00:00`のDagRunが実行される
        * schedule_interval分前のexecution_dateになる
* running date
    * taskが実行された日
    * 上記の例ではrunning dateは全てのtaskで同じ
* dagのstart_dateとend_date
    * 有効期間と考えて良い
    * この期間
* Dag Runs
    * 指定したexecution dateでdagを実行する
    * start_dateを指定できるが

DAG Runsで実験

* 条件
    * execution_date
        * 2017-07-02
    * start_date
        * 2017-07-02
    * end_date
        * 2017-07-04
* result
    * 2017-07-02がexecution date
    * 1回実行される
* 条件
    * execution_date
        * blank
    * start_date
        * 2017-07-02
    * end_date
        * 2017-07-04
* result
    * createした日時がexecution dateになる
    * start_date, ednd_dateの間であれば1回実行される

## Scheduling spark jobs
* [Scheduling Spark jobs with Airflow – Insight Data](https://blog.insightdatascience.com/scheduling-spark-jobs-with-airflow-4c66f3144660)
* [Automated Model Building with EMR, Spark, and Airflow - Agari](https://www.agari.com/automated-model-building-emr-spark-airflow/)

BashOperatorで`spark-submit`をする

## Tips
よくある落とし穴。
見ておいた方が良い。

* [Common Pitfalls - Airflow - Apache Software Foundation](https://cwiki.apache.org/confluence/display/AIRFLOW/Common+Pitfalls)

### worker and Scheduler need to access dag folder
schedulerとworkerからdagsのfolderは見えている必要がある。
webserverも見えている必要がある。

workerやschedulerをremoteやdockerで扱う場合は注意が必要。

### Ignore dag file
DAG folderに`.airflowignore`fileをおくと、fileに記載されているfileは無視される。

### With postgres
postgresを使う場合は`psycopg2`と合わせて使うことが推奨されている。

```cfg
[core]
sql_alchemy_conn = "postgresql+psycopg2://scott:tiger@localhost/mydatabase"
```

### With redis broker

```
broker_url = redis://:password@hostname:port/db_number
```

### Timezone
Pitfallsにも記載してあるが、UTC前提で開発されている部分があるらしいので、Airflowのarchitecture全体でUTCにしておいた方が、良いらしい。

### Webserver
* [python - Can't run gunicorn on port 80 while deploying django app on AWS EC2 - Stack Overflow](https://stackoverflow.com/questions/32298481/cant-run-gunicorn-on-port-80-while-deploying-django-app-on-aws-ec2)

Gunicornはport 80での起動は推奨されていない。
airflowのwebserverも80での起動はできない場合があるっぽい。
1024より上にするのが良い。

### Delete DAG
DAGを削除するには以下のテーブルからレコードを削除する必要がある。

```sql
DELETE FROM xcom WHERE dag_id='';
DELETE FROM task_instance WHERE dag_id='';
DELETE FROM sla_miss WHERE dag_id='';
DELETE FROM log WHERE dag_id='';
DELETE FROM job WHERE dag_id='';
DELETE FROM dag_run WHERE dag_id='';
DELETE FROM dag WHERE dag_id='';
```

もしくは、`$AIRFLOW_HOME/dags`から該当のscriptを削除して、`airflow resetdb`でDBをresetする。


### Warning: ExtDeprecatonWarning
Warningがでる。
対処は調べてない。

```
..flask/exthook.py:71: ExtDeprecationWarning: Importing flask.ext.cache is deprecated, use flask_cache instead.
  .format(x=modname), ExtDeprecationWarning
```

### Restart scheduler/worker/webserver
prcessをkillして再起動する。

```
cat $AIRFLOW_HOME/airflow-webserver.pid | xargs kill -9 && rm $AIRFLOW_HOME/airflow-webserver.pid
cat $AIRFLOW_HOME/airflow-scheduler.pid | xargs kill -9 && rm $AIRFLOW_HOME/airflow-scheduler.pid
cat $AIRFLOW_HOME/airflow-worker.pid | xargs kill -9 && rm $AIRFLOW_HOME/airflow-worker.pid
```

再起動は起動時と同じコマンドを使う必要がある。

### log rotation
log rotate機能はない。
jobのlogは日付ごとに出力されるので、logrotateされているといえる。
webserver, worker, schedulerのprocessのlog, stdout, stderrはlogrotateされない。

### DAGの追加
* 要確認
    * DAGを追加する場合は、`airflow resetdb`した方が良いが、DBが初期化される
    * dag pathにDAG用のpython fileをおいた時点で、schedular以外では使えるようになる。
    * schedularに載せるためには、`airflow upgradedb`が必要。

### Executors
* [API Reference — Airflow Documentation](https://airflow.incubator.apache.org/code.html?highlight=localexecutor#executors)

* SequentialExecutor
    * sqlite可能
    * 1つのtaskのみが動く
    * debug用
* LocalExecutor
    * localでmulti taskが動く
    * sqlite不可
    * subprocessで動く
* CeleryExecutor
* MesosExecutor

### DAG scriptの更新
dagを定義したスクリプトの変更は、web serverやDBの更新なしで反映される。

### Delay a start time of task
dailyのscheduleは基本的に、各日付の`00:00:00`に開始される。
開始時刻をずらしたい場合は、最も上流のtaskとして`TimeSensor`か`TimeDeltaSensor`をいれる。
`TimeSensor`は、指定した時間になるまで待つ、`TimeDeltaSensor`は指定時間待つだけのoperatorである。
UCTでやっている場合に、日本時間AM00:00まで待つには、`TimeSensor`は15時まで、`TimeDeltaSensor`は15時間待てば良い。
ただ、15時間待っている間、DAGはRunning状態であるから、 実際にtaskが開始された時刻を通知すると便利である。
その場合は通知用の関数`notify_to_start_dag`を作成して、operatorの`on_success_callable`に渡す。

```python
import airflow.operators.sensors as sensors
sensors.TimeSensor(
    task_id="time_sensor"
    target_time=datetime.time(hour=0, minute=0, second=0)
    dag=dag,
    on_success_callback=notify_to_start_dag)
sensors.TimeDeltaSensor(
    task_id="time_delta_sensor"
    delta=datetime.timedelta(hours=0, minutes=0, seconds=0),
    dag=dag,
    on_success_callback=notify_to_start_dag)
```

`TimeSensor`の15時というのは、taskが始まってから最初に訪れるUTC時間の15時までという意味になる。
つまり、taskの開始時に15時を過ぎていたら、次の日の15時まで待つ。
また、TimeSensorやTimeDeltaSensorで待っている間は、workerが消費され続ける。

* [airflow.operators.sensors — Airflow Documentation](https://airflow.incubator.apache.org/_modules/airflow/operators/sensors.html)

### re run failed dags
* [python - How to restart a failed task on Airflow - Stack Overflow](https://stackoverflow.com/questions/43270820/how-to-restart-a-failed-task-on-airflow)

taskがfailした場合は、failしたtaskをWebUIでClearすれば、failしたtaskから再実行される。
failしたtaskに依存しているdownstream taskの状態(upstream  failed)も合わせてclearされる。

### Ad hoc query
Web UIでAdhoc queryをAirflowのserverに対して実行できる。
接続の設定が必要。
`Admin->Connections`から`mysql_default`をEditで接続に必要な情報を入力する。

* Host
* Login
    * login user
* Password
* port
* Schema
    * DB name

`mysql default`でなくても新しく作成しても良い。
passwordなどはdefaultでは、plain textでDBに保存されるので、必要であれば、pythonの`cryptography`をinstallしておく。

* [FAQ — Airflow Documentation](https://airflow.incubator.apache.org/faq.html#why-are-connection-passwords-still-not-encrypted-in-the-metadata-db-after-i-installed-airflow-crypto)

```
pip install apache-airflow[crypto]
```

でできる。

## Web UI

<img src="./image/airflow_05_dags.png" width="50%">

<img src="./image/airflow_02_tree_view.png" width="50%">

## docker
* [puckel/docker-airflow: Docker Apache Airflow](https://github.com/puckel/docker-airflow)

officialではないが、docker imageが提供されている。

```
docker pull puckel/docker-airflow
```

`CeleryExecutor`で実行したい場合は、以下を実行する。

```
docker-compose -f docker-compose-CeleryExecutor.yml up -d
```

自分のdagを登録したい場合は、docker-compose fileを編集する。
また、defaultのexampleが不要の場合は、yaml内のwebserverのevironemtにある`LOAD_EX=n`とする。

```yaml
- volume:
  - /path/to/local/dags:/usr/local/airflow/airflow/dags
```

必要なpython packageがある場合は、`requirements.txt`に必要なpackageを記載して、docker内の`/requirements.txt`にmountすれば良い。
docker-composeの`volumes`ではなぜかファイルがディレクトリとしてマウントされてしまう場合がある。
その場合は、`Dockerfile`を直接編集して、`COPY requirements.txt /requirements.txt`をつけてbuildする。

## Multinode
* http://site.clairvoyantsoft.com/setting-apache-airflow-cluster/

## Connection
* [pre-configured airflow "Connections" · Issue #75 · puckel/docker-airflow](https://github.com/puckel/docker-airflow/issues/75)
    * CLIからのconnectionの追加
* [Apache Airflow: How to add a connection to Google Cloud with CLI](https://medium.com/google-cloud/apache-airflow-how-to-add-a-connection-to-google-cloud-with-cli-af2cc8df138d)
    * dagでのconnectionの追加

```
airflow connections --add --conn_id=gcp --conn_type=google_cloud_platform --conn_extra='{ "extra__google_cloud_platform__key_path":"/usr/local/airflow/secrets/gcp_key.json", "extra__google_cloud_platform__project": "gcp-project", "extra__google_cloud_platform__scope": "https://www.googleapis.com/auth/cloud-platform"}'
```

## Airflow with supervisord
* [Re: airflow supervisord scripts do not work](http://mail-archives.apache.org/mod_mbox/airflow-dev/201608.mbox/%3CCAK+2U_2BqDEfyvf2xa=RaGuDA6Fusmqx+HyyHX0DxE9ti=K5Xw@mail.gmail.com%3E)
* [Supervisordの練習(Airflow)](https://blog.masu-mi.me/post/2017/04/12/start_supervisord/)

### Health check
`/health` がhealthcheck用のWeb UI URL

### Notification
DAGの開始時に通知をしたい

Operatorの一番最初に`slack_operator`をいれる。
`TimeSensor`にしておけば、時間をずらしたい時にそのまま利用できるので、`TimeSensor`で良い。

DAGの開始時に通知をしたい

一番最後に実行されるoperatorにのsuccessをつける


各operatorの開始時に通知をしたい

?

各operatorのsuccess/fail/retry時に通知

DAGの`default_args`に`callback_on_success`の設定をする。


* `context`
    * dict
    * 'next_execution_date'
        * datetime.datetime(2018, 5, 23, 0, 0)
    * 'dag_run'
        * <DagRun dag_id @ 2018-05-22 00:00:00: scheduled__2018-05-22T00:00:00, externally triggered: False>
    * 'tomorrow_ds_nodash'
        * str
        * '20180523'
    * 'run_id', 'scheduled__2018-05-22T00:00:00'
    * 'test_mode'
        * False
    * 'prev_execution_date'
        * datetime.datetime(2018, 5, 21, 0, 0)
    * 'conf'
        * <module 'airflow.configuration' from '/usr/local/lib/python2.7/dist-packages/airflow/configuration.pyc'>
    * 'tables'
        * None
    * 'task_instance_key_str'
        * str
        * 'etl__start_dag__20180522'
    * 'END_DATE'
        * str
        * '2018-05-22'
    * 'execution_date'
        * datetime.datetime(2018, 5, 22, 0, 0)
    * 'ts'
        * str
        * '2018-05-22T00:00:00'
    * 'macros'
        * <module 'airflow.macros' from '/usr/local/lib/python2.7/dist-packages/airflow/macros/__init__.pyc'>
    * 'params'
        * dict
        * {}
    * 'ti'
        * <TaskInstance: dag_id.task_id 2018-05-22 00:00:00 [success]>
    * 'var'
        * {u'json': None, u'value': None}
    * 'ds_nodash'
        * u'20180522'
    * 'dag'
        * <DAG: etl>
    * 'end_date'
        * '2018-05-22'
    * 'latest_date'
        * '2018-05-22'
    * 'ds'
        * '2018-05-22'
    * 'task_instance'
        * <TaskInstance: dag_id.task_id 2018-05-22 00:00:00 [success]>
    * 'yesterday_ds_nodash'
        * u'20180521'
    * 'task'
        * <Task(DummyOperator): start_dag>
    * 'yesterday_ds'
        * '2018-05-21'
    * 'ts_nodash'
        * u'20180522T000000'
    * 'tomorrow_ds'
        * '2018-05-23'

## Reference
* [Apache Airflow (incubating) Documentation — Airflow Documentation](https://airflow.incubator.apache.org/)
* [Airflowによるデータパイプラインのスケジュールとモニタリング - Speee DEVELOPER BLOG](http://tech.speee.jp/entry/2016/07/07/050000)
* [Airflow: a workflow management platform – Airbnb Engineering & Data Science – Medium](https://medium.com/airbnb-engineering/airflow-a-workflow-management-platform-46318b977fd8)
* [Airflow - データパイプラインのスケジュールと監視をプログラムしてみた - Qiita](http://qiita.com/haminiku/items/b431e9cd1cf4e300f8f0)
* [Airflow: When Your DAG is Far Behind The Schedule](http://hafizbadrie.com/airflow/2016/12/12/airflow-when-your-dag-is-far-behind-the-schedule.html)
* [ETL example — ETL Best Practices with Airflow v1.8](https://gtoonstra.github.io/etl-with-airflow/etlexample.html)
* [Advanced Airflow (Lesson 1) : TriggerDagRunOperator | Sid Anand | Pulse | LinkedIn](https://www.linkedin.com/pulse/airflow-lesson-1-triggerdagrunoperator-siddharth-anand)
* [Bytepawn – Luigi vs Airflow vs Pinball](http://bytepawn.com/luigi-airflow-pinball.html)
