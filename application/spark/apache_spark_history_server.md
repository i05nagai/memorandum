---
title: Apache Spark History Server
---

## Apache Spark History Server
SparkContextは実行時にWeb UIを起ち上げるが、実行が終了するとWeb UIは見れない。
Web UIで実行logにaccessする場合はhistory serverを使う。

## Start
Start history server.

```
${SPARK_HOME}/sbin/start-history-server.sh
```

You can access `http://<server-url>:18080` by default.

Stop hisotry server

```
${SPARK_HOME}/sbin/start-history-server.sh
```

## Environment variables
hisotry serverの設定は以下の環境変数で変更可能。

* SPARK_DAEMON_MEMORY
* SPARK_DAEMON_JAVA_OPTS
* SPARK_DAEMON_CLASSPATH
* SPARK_PUBLIC_DNS
* SPARK_HISTORY_OPTS
    * `spark.history.*`の設定ができる

```
export SPARK_HISTORY_OPTS="$SPARK_HISTORY_OPTS -Dspark.history.ui.port=9000"
```

## Configurations
* `spark.history.fs.logDirectory`
    * default: `file://tmp/spark-events`
    * log fileNo場所
* `spark.history.ui.port`
    * default: `18080`


## REST API


## Metrics
History serverで見られるlogはMetricsのDropwizard Metricsのlibraryで取得できるもの。
`$SPARK_HOME/conf/metrics.properties.`にconfigurationをおく。
fileの場所は`spark.metrics.conf`で変更できる。

## Reference
* [Monitoring and Instrumentation - Spark 2.3.0 Documentation](https://spark.apache.org/docs/latest/monitoring.html)
