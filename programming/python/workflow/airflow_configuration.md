---
title: Airlfow Configuration
---

## Airlfow Configuration
description for `airflow.cfg`
`$AIRFLOW_HOME`に、`airflow.cfg`が作られ、 defaultだと`~/airflow`が`$AIRFLOW_HOME`になっている。
設定ファイルは以下のような`ini`形式になっている。

```ini
[core]
sql_alchemy_conn = my_conn_string
```

環境変数で上書き可能で、formatは`$AIRFLOW__{SECTION}__{KEY}`の形式である。
上の例の場合は`$AIRFLOW__CORE__SQL_ALCHEMY_CONN`に値を設定すれば良い。
`SECTION`と`KEY`の間は`_`が2つであることに注意する。

* [An Effective Airflow Setup](http://the-efficient-programmer.com/programming/an-effective-airflow-setup.html)

設定を変更しそうな項目は、以下。

```bash
# ${AIRFLOW_HOME}は適当なpathが定義されているとする
export AIRFLOW__CORE__AIRFLOW_HOME="${AIRFLOW_HOME}"
export AIRFLOW__CORE__DAGS_FOLDER="${AIRFLOW_HOME}/dags"
export AIRFLOW__CORE__BASE_LOG_FOLDER="${AIRFLOW_HOME}/logs"
# Executer
export AIRFLOW__CORE__EXECUTOR="CeleryExecutor"
# defaultのexampleをいれるか
export AIRFLOW__CORE__LOAD_EXAMPLES="False"
# Airflowで使うDB
export AIRFLOW__CORE__SQL_ALCHEMY_CONN="mysql://user_name:password@db_host:db_port/db_name"
export AIRFLOW__CORE__SQL_ALCHEMY_POOL_SIZE=5
# 並列性の設定
export AIRFLOW__CORE__PARALLELISM=2
export AIRFLOW__CORE__DAG_CONCURRENCY=3
export AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG=1
# ?
export AIRFLOW__CORE__FERNET_KEY="cryptography_not_found_storing_passwords_in_plain_text"
# webserverのBASEのURL
export AIRFLOW__WEBSERVER__BASE_URL="https://0.0.0.0:8080"
# webserverのHostとport
export AIRFLOW__WEBSERVER__WEB_SERVER_HOST="0.0.0.0"
export AIRFLOW__WEBSERVER__WEB_SERVER_PORT=8080
# serverのworker
export AIRFLOW__WEBSERVER__WORKERS=1
# logの場所
export AIRFLOW__WEBSERVER__ACCESS_LOGFILE="/path/to/access_log.log"
export AIRFLOW__WEBSERVER__ERROR_LOGFILE="/path/to/error_log.log"
# webserverにユーザ認証機能をつける場合はTrue, Backendも以下に変更が必用。
export AIRFLOW__WEBSERVER__AUTHENTICATE="True"
export AIRFLOW__WEBSERVER__AUTH_BACKEND="airflow.contrib.auth.backends.password_auth"
# workerの並列性
export AIRFLOW__CELERY__CELERYD_CONCURRENCY=3
# worker用のDB
export AIRFLOW__CELERY__BROKER_URL="sqla+mysql://db_user_name:password@db_host:db_port/db_name"
export AIRFLOW__CELERY__CELERY_RESULT_BACKEND="db+mysql://db_user_name:password@db_host:db_port/db_name"
# celeryのflowerの設定
export AIRFLOW__CELERY__FLOWER_HOST="0.0.0.0"
export AIRFLOW__CELERY__FLOWER_PORT=5555
# schedulerのlogの場所
export AIRFLOW__SCHEDULER__CHILD_PROCESS_LOG_DIRECTORY="${AIRFLOW_HOME}/logs/scheduler"
# schedulerの並列性
export AIRFLOW__SCHEDULER__MAX_THREADS=1
```

## airflow.cfg

```cfg
task_log_reader = file.task
```

* `task_log_reader`
    * [15.9. logging.handlers — Logging handlers — Python 2.7.14 documentation](https://docs.python.org/2/library/logging.handlers.html)
    * [Integration — Airflow Documentation](http://airflow.incubator.apache.org/integration.html?highlight=bigquery)

### Web Authentification
password 認証をつける方法。
password subpackageをインストールする。

```
pip install airflow[password]
```

`airlfow.cfg`に以下を設定する。

```ini
[webserver]
authenticate = True
auth_backend = airflow.contrib.auth.backends.password_auth
```

defaultでuserは作られていないので、userを以下で追加する。

```python
$ cd ~/airflow
$ python
Python 2.7.9 (default, Feb 10 2015, 03:28:08)
Type "help", "copyright", "credits" or "license" for more information.
>>> import airflow
>>> from airflow import models, settings
>>> from airflow.contrib.auth.backends.password_auth import PasswordUser
>>> user = PasswordUser(models.User())
>>> user.username = 'new_user_name'
>>> user.email = 'new_user_email@example.com'
>>> user.password = 'set_the_password'
>>> session = settings.Session()
>>> session.add(user)
>>> session.commit()
>>> session.close()
>>> exit()
```

### SSL
SSLを設定する場合は、証明書と公開鍵の場所を`airflow.cfg`に記載する。
設定した場合は、URLは`https://`でアクセスする。

```ini
[webserver]
web_server_ssl_cert = <path to cert>
web_server_ssl_key = <path to key>
```

defaultでは、portは変わらないので、SSLのportを変更したい場合は、`airflow.cfg`に以下を変更する。

```ini
[webserver]
web_server_port = 443
base_url = http://<hostname or IP>:443
```

なぜかdaemon化するときは、certfileが必要(1.8.0)。

### Concurrency/Parallesm
`airflow.cfg`の設定ファイルについてで、以下は並列にかかわるパラメータ。
airflowの挙動に慣れるまでは、すべて`1`に変更しておいた方が良い。

* parallelism
    * schedulerが並列に実行するpython instanceの数
    * taskの並列実行数
* dag_concurrency
    * dagごとのtask instandeの並列実行数
    * workerが空いていても、この同時実行数を超えない
* max_active_runs_per_dag
    * dagごとのrunsのtaskの最大数
* worker
    * web serverを実行するworkerの数
    * web serverのmulti processの数

celeryを使う場合は

* celeryd_concurrency
    * celeryのworkerの数
    * workerがtaskを実行するので、taskの最大同時実行数

`celeryd_concurrency >= dag_concurrency >= max_active_runs_per_dag`の関係っぽい

max_active_runs_per_dag
<img src="./image/airflow_03_max_active_runs_per_dag.png"/>

parallelism
<img src="./image/airflow_04_parallelism.png"/>


### Logging to GCS
* [Integration — Airflow Documentation](http://airflow.incubator.apache.org/integration.html?highlight=bigquery#gcp-google-cloud-platform)

### Connection to GCP
* [Apache Airflow: How to add a connection to Google Cloud with CLI](https://medium.com/google-cloud/apache-airflow-how-to-add-a-connection-to-google-cloud-with-cli-af2cc8df138d)
* [google cloud storage - Airflow Remote logging not working - Stack Overflow](https://stackoverflow.com/questions/46293020/airflow-remote-logging-not-working)
    * `googleapis.com/auth/devstorage.full_control `
    * `airflow[gcp_api]`のinstallが必要
        * ` gcloud SDK`が必要
* [How to aggregate data for BigQuery using Apache Airflow | Google Cloud Big Data and Machine Learning Blog  |  Google Cloud Platform](https://cloud.google.com/blog/big-data/2017/07/how-to-aggregate-data-for-bigquery-using-apache-airflow)

## Tips

### integration with upstart
* [Configuration — Airflow Documentation](https://airflow.incubator.apache.org/configuration.html#integration-with-upstart)
* [incubator-airflow/scripts/upstart at master · apache/incubator-airflow](https://github.com/apache/incubator-airflow/tree/master/scripts/upstart)


## Reference
