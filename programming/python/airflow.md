---
title: airflow
---

## airflow

* downstream/upstream
    * taskがA, Bで、AのあとにBが実行されるとき
    * Aがupstream
    * Bがdownstream
* task
    * operatorがinstance化されるとtaskと呼ばれる
* task instance
    * 実行中のtask
    * running, failed, skipped, up for retryなどの状態を持つ
* Queue
    * taskをqueueして、実行するにはexecutorをCeleryExecutorに変更する必要がある
    * CeleryExecutorを使うには、airflow用のdbをMySQLなどに変更する必要がある
        * defaultはsqlite
    * Queueに入ったtaskはworkerが引き受ける
    * queueは名前をつける
    * QueueはBaseOperatorの引数として、指定できる
    * queueは複数つけることができる
    * default(未指定)のqueueは`airflow.cfg`で指定されている
* Worker
    * taskをqueueに登録して、queue内のtaskを引き受けるのがworker
    * 例えば、sparkで実行するtaskをspark用のqueueにいれて、spark用のworkerのみがそのtaskを引き受けるということもできる
* Service Level Agreement
    * taskが正常終了するまでの期限を記載できる
    * 期限までに終了しなければ、missed SLAとして記録される
    * 期限はtimedeltaで指定
* Trigger rules
    * すべてのoperatorで指定できる
    * 親のoperatorの終了状態をtriggerに、実行制御ができる
* zombie & undead
* policy
    * taskに対して、policyを設定できる
    * 特定の条件を満たすtask (operator)に対する設定を記述できる
    * 例えば、特定のoperatorはあるqueueにいれるなど
* XComs
    * cross communication
    * task間でのmessageや状態のやり取りができる
    * taskは`xcom_push()`
* Pools
    * 並列実行するtaskをpoolすることができる
    * 各poolは、taskを並列に実行するworkerの数を割り当てることができる
    * WebUIからも設定可能
    * operatorのpool引数で、



## Install

```
pip install airflow
```

2系でしか動かないっぽい。
以下のコマンドで、初期化とサーバの立ち上げができる。

```
airflow initdb
airflow webserver -p 8080
```

## Usage

Defaultだと~/airflowに作業用のディレクトリが作られる。

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

### Pool
* poolはWeb UIから作成できる。
* `Admin->Pool`から新しくpoolを作る。
* pool名とslot数を決める。
    * pool名はid
    * slot数はpool内のtaskの同時実行数
* poolを作成すると、airflowのpython script内でoperatorを作る際にpool名を指定できる


## Commands

```
airflow run <dag_id> <task_id> <execution_date>
```


```
airflow list_dags
```

* DAGの一覧を表示

```
airflow list_tasks <dag> [--tree]
```

* DAGのtaskの一覧を表示
* `--tree`
    * taskの一覧をtree形式で表示

```
airflow test <dag_id> <task_id> <execution_date>
```

* execution_dateとして、taskを実行する

```
airflow backfill <dag_id> -s start_date -e end_date
```

* dag_idを実際に実行する


## Scheduling
DAGにScheduleを設定できる。
scheduleを設定しない場合は、手動実行。
scheduleは`airflow.DAG`クラスを作成時に`schedule_intaval`引数に指定する。
3通りの指定が可能

1. cron形式の指定も可能。
    * presetと同じ表現力
2. presetも利用可能
    * `None`
    * `@once`
    * `@hourly`
    * `@daily`
    * `@weekly`
    * `@monthly`
    * `@yearly`
3. datetime.timedelta
    * 一番柔軟に指定できる

```python
airflow.DAG(schedule_interval="0 * * * *")
airflow.DAG(schedule_interval=@hourly)
```

* [Scheduling & Triggers — Airflow Documentation](https://airflow.incubator.apache.org/scheduler.html)


## Tips

よくある落とし穴。
見ておいた方が良い。

* [Common Pitfalls - Airflow - Apache Software Foundation](https://cwiki.apache.org/confluence/display/AIRFLOW/Common+Pitfalls)

### TemplateNotFound Error
TemplateNotFoundというエラーがでる場合、bashcommandの引数の最後にスペースがあるか確認する。
Bash scriptを直接呼ぶ場合は、最後にスペースが必要。
そうでない場合は、引数はJinja templateとして扱われるので、templateの引数が空でも必要。

* [python - TemplateNotFound error when running simple Airflow BashOperator - Stack Overflow](https://stackoverflow.com/questions/42147514/templatenotfound-error-when-running-simple-airflow-bashoperator)


### Webserver
Gunicornはport 80での起動は推奨されていない。
airflowのwebserverも80での起動はできない場合があるっぽい。
1024より上にするのが良いっぽい。

* [python - Can't run gunicorn on port 80 while deploying django app on AWS EC2 - Stack Overflow](https://stackoverflow.com/questions/32298481/cant-run-gunicorn-on-port-80-while-deploying-django-app-on-aws-ec2)


### Error with --debug
* [AIRFLOW-1165 airflow webservice crashes on ubuntu16 - python3 - ASF JIRA](https://issues.apache.org/jira/browse/AIRFLOW-1165)


```
airflow webserver --debug
```

とすると、エラーがでる。
2017/5/2にmasterで修正済みらしい。

### Delete Default DAG
* [Airflow: how to delete a DAG? - Stack Overflow](https://stackoverflow.com/questions/40651783/airflow-how-to-delete-a-dag)

`airflow initdb`するとdbにexampleのDAGが登録される。
exampleのDAGが不要な場合は、`airflow.cfg`で`load_examples = False`を指定する。

もしくはDAGを削除するには以下のテーブルからレコードを削除する必要があるので、defaultのDAGのdag_idを登録する必要がある。

```sql
DELETE FROM xcom WHERE dag_id=''
DELETE FROM task_instance WHERE dag_id=''
DELETE FROM sla_miss WHERE dag_id=''
DELETE FROM log WHERE dag_id=''
DELETE FROM job WHERE dag_id=''
DELETE FROM dag_run WHERE dag_id=''
DELETE FROM dag WHERE dag_id=''
```

### ExtDeprecatonWarning

```
/home/makoto-nagai/.pyenv/versions/airflow_check/local/lib64/python2.7/site-packages/flask/exthook.py:71: ExtDeprecationWarning: Importing flask.ext.cache is deprecated, use flask_cache instead.
  .format(x=modname), ExtDeprecationWarning
```

### log
log rotate機能は現在ないっぽい。



## Configs
`airflow.cfg`の設定ファイルについて。

* parallelism
    * task instanceの最大同時実行数
* dag_concurrency
    * schedulerが並列に実行するtask instanceの数
* worker
    * web serverを実行するworkerの数?

## Reference
* [Apache Airflow (incubating) Documentation — Airflow Documentation](https://airflow.incubator.apache.org/)
* [Airflowによるデータパイプラインのスケジュールとモニタリング - Speee DEVELOPER BLOG](http://tech.speee.jp/entry/2016/07/07/050000)


