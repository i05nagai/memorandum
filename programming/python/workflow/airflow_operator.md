---
title: Airflow Operator
---

## Airflow Operator
Tips for operators.


## API
BaseOperatorで定義されている共通の引数

* start_date
    * 最初のexecution_dateになる
    * dailyのtaskの開始は`00:00:00`
    * houlyのtaskの開始は`00:00`
    * 開始をずらしたい場合は、TimeDeltaSensor, TimeSensor
* depends_on_past
    * trueにすると、上流のtaskのsucceedをまつ
* wait_for_downstream
* pool
    * 使用するpool名を記載
    * Noneの場合は、defaultのpoolに入る
* sla
    * taskの期待する実行時間をtimedeltaで指定
    * 1時間で終わってほしいときは、1hourで指定
    * 実行時間の上限、これを超えるとSLA missというlogが出力
* trigger_rule
    * 依存しているtaskのstateに応じて実行を制御する
    * ` all_success | all_failed | all_done | one_success | one_failed | dummy`
    * defaultはall_success
    * all_sccess: 依存しているtaskが全てsuccess
    * all_faild: 依存しているtaskが全てfailed
    * one_success: 依存しているtaskが全1つでも成功
    * one_failed: 依存しているtaskが全1つでもfailed

## Macros
bashOperatorのcommandの中で`{{ ds }}` とした場合は、`{{ somechar }}`で囲まれた中身が評価された結果で実行される。
Macroとして利用できるものとして以下がある。
基本的にはoperatorは、execution dateを受け取ってその日付に対する処理をするようにした方が良い。
failした場合の再実行の際には、日付を気にする必要がなくなる。

* `{{ ds }}`
    * `YYYY-MM-DD`形式のexecution date
* `{{ ds_nodash }}`
* `{{ yesterday_ds }}`
    * `YYYY-MM-DD`形式のexecution date - 1
* `{{ tomorrow_ds }}`
    * `YYYY-MM-DD`形式のexecution date + 1

任意形式の日付が欲しい場合は `macros.ds_format`を使う。

* `yesterday = '{{ macros.ds_format(yesterday_ds, "%Y-%m-%d", "%Y/%m/%d") }}'`
* `today = '{{ macros.ds_format(ds, "%Y-%m-%d", "%Y/%m/%d") }}'`

## Scheduling operators
以下はcodeに基づく仕様ではなく、経験に基づく挙動の原則。
Airflowのscheudulerの挙動は仕様としてはまとめられていないので、細かい挙動はsource codeを読む必要がある。

* queueにあるtask instanceはworkerによって順次実行される
* schedulerはtask instanceのstateが以外で、task instanceのexecution dateが1 schedule interval前であれば、task instanceをqueueにつむ


## SubDag operator
* `dag1`
    * `sub_dag1` (dag11)
    * `sub_dag2` (dag12)
* `dag11`
    * `operator111`
* `dag12`
    * `operator121`

2018/2/02 00:00:00+00:00

* `dag1` DagRun
    * `sub_dag1`
        * dagid=`dag1`, taskid=`sub_dag1` task instance (execution date: 2018/02/01 00:00:00+00:00)
        * dagid=`dag1.sub_dag1` DagRun (execution date: 2018/02/01 00:00:00+00:00)
    * `sub_dag2`
        * taskid=`sub_dag2` task instance (execution date: 2018/02/01 00:00:00+00:00)
        * dagid=`dag1.sub_dag2` DagRun (execution date: 2018/02/01 00:00:00+00:00)
* `sub_dag1`
    * dagid=`dag1.sub_dag1`, taskid=`operator111`
* `sub_dag2`
    * dagid=`dag2.sub_dag1`, taskid=`operator121`


## Docker operator
commandに複数の引数を渡す場合は`'["bash", "echo", "{{ ds }}"]'`で文字列で渡せばtemplateを展開する。

### macros in Docker operator
* `command` argumentのみでmacrosが使える

```python
t2 = DockerOperator(task_id='docker_2', dag=dag, image='docker_2', command='{{ ds }}')
```

### Docker operator with xcom pull and xcom push
* [Programming soup: Airflow Docker with Xcom push and pull](http://szborows.blogspot.jp/2017/12/airflow-docker-with-xcom-push-and-pull.html)
    * `xcom_push=True`stdoutの結果をxcomにpushするo
    * `xcom_all=True`で全てのstdoutの結果をpush, `False`でlast lineのみ

```python
dag = DAG('docker', default_args=default_args, schedule_interval=timedelta(1))
t1 = DockerOperator(task_id='docker_1', dag=dag, image='docker_1', xcom_push=True)
t2 = DockerOperator(task_id='docker_2', dag=dag, image='docker_2', command='{{ ti.xcom_pull(task_ids="docker_1") }}')
t2.set_upstream(t1)
```

## Pass value to another task with xcom
python operatorでpython operatorの結果を他のtaskに渡す。

```python
def operator1(dag):
    def operator1_func(**kwargs):
        import subprocess
        import json
        today = kwargs['templates_dict']['today']
        path = '/path/to/script1.sh'
        # shell script return json strings
        result = subprocess.check_output([ "bash", path, today, ])
        result = json.loads(result)
        value = result['key']
        # set key values
        kwargs['ti'].xcom_push(key='key', value=value)

    # macros
    templates_dict = {
        'today': '{{ ds }}',
    }
    operator = python_operator.PythonOperator(
        task_id='task1',
        python_callable=operator1_func,
        priority_weight=5,
        templates_dict=templates_dict,
        provide_context=True,
        dag=dag)
    return operator


def operator2(dag):
    def operator2_func(**kwargs):
        import subprocess
        # get value from task1
        value = kwargs['ti'].xcom_pull(task_ids='task1', key='key')
        path = '/path/to/script2.sh'
        print(value)
        # execute another shell script
        subprocess.check_output([ "bash", path, value])

    operator = python_operator.PythonOperator(
        task_id='task2',
        python_callable=operator2_func,
        provide_context=True,
        dag=dag)
    return operator
```

## Reference
