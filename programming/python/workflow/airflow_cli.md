---
title: Airflow CLI
---

## Airflow CLI


## Commands/CLI
実行日`execution_date`でdagのtaskを実行

```
airflow run <dag_id> <task_id> <execution_date>
```

DAGの一覧を表示

```
airflow list_dags
```

`<dag>`のtaskの一覧を表示

* `--tree`
    * taskの一覧をtree形式で表示

```
airflow list_tasks <dag> [--tree]
```

実行日`execution_date`でtaskをtest実行する。

```
airflow test <dag_id> <task_id> <execution_date>
```

`start_date`から`end_date`の期間だとして、`dag_id`のdagをスケジュール実行する。
下記の設定では、dagを2回実行する。

* dag
    * start_date: 2016/1/1
    * end_date: 2016/1/2
    * schedule_interval: @daily
* backfill
    * `airflow backfill dag -s 2016/1/1 2016/1/3`
    * start_date: 2016/1/1
    * end_date: 2016/1/3

```
# airflow backfill dag -s 2016/1/1 2016/1/2
airflow backfill <dag_id> -s start_date -e end_date
```

## Reference
