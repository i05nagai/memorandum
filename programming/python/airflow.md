---
title: airflow
---

## airflow

## Install

```
pip install airflow
```

2系でしか動かないっぽい。

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
airflow backfill <dag_id>
```




## Reference
* [Apache Airflow (incubating) Documentation — Airflow Documentation](https://airflow.incubator.apache.org/)
=======
airflow initdb
airflow webserver -p 8080
```


