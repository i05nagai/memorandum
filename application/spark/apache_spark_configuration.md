---
title: Apache Spark Configuration
---

## Apache Spark Configuration
Spark provides three locations to configure the system:

* Spark properties
    * control most application parameters
    * can be set by using a SparkConf object, or through Java system properties.
* Environment variables
    * can be used to set per-machine settings, such as the IP address, 
    * `conf/spark-env.sh` script on each node.
* Logging
    * can be configured through `log4j.properties`


## Spark Properties
* 3 way to specify
    * `spark-submit` reads configuration from `${SPARK_HOME}/conf/spark-defaults.conf`
        * path to configuration dir are overrided by `SPARK_CONF_DIR`
    * `SparkConf`
    * command line arugments of `spark-submit`
* You can view at `http://<driver>:4040`


Configure from CLI

```
./bin/spark-submit \ 
  --name "My app" \ 
  --master local[4] \  
  --conf spark.eventLog.enabled=false \ 
  --conf "spark.executor.extraJavaOptions=-XX:+PrintGCDetails -XX:+PrintGCTimeStamps" \ 
  --conf spark.hadoop.abc.def=xyz \ 
  myApp.jar
```


### List of Spark Properties
* `spark.logConf`
    * false by default
    * Logs the effective SparkConf as INFO when a SparkContext is started.

Spark UI

`eventLog` is logs for spark history server.

* `spark.eventLog.dir`
    * `file:///tmp/spark-events` by default
    * directory must exist before execution
* `spark.eventLog.compress`
* `spark.eventLog.logBlockUpdates.enabled`
* `spark.eventLog.enabled`
* `spark.eventLog.overwrite`
* `spark.eventLog.buffer.kb`
* `spark.eventLog.enabled`


## Environment variables

## Logging
`log4j` is used.

* `${SPARK_HOME}/conf/log4j.properties` file
    * configure `log4j`a
    * you can copy from `log4j.properties.template`

## Tips

### Master URL
* [Submitting Applications - Spark 2.3.0 Documentation](https://spark.apache.org/docs/latest/submitting-applications.html)


* `local`
    * Run Spark locally with one worker thread
* `local[K]`
    * Run Spark locally with K worker threads
* `local[K,F]`
    * Run Spark locally with K worker threads and F maxFailures
* `local[*]`
    * Run Spark locally with as many worker threads as logical cores on your machine.
* `local[*,F]`
    * Run Spark locally with as many worker threads as logical cores on your machine and F maxFailures.
* `spark://HOST:PORT`
    * Connect to the given Spark standalone cluster master.
    * `7077` by default port



### spark-warehouse
* [hadoop - Why there are many spark-warehouse folders got created? - Stack Overflow](https://stackoverflow.com/questions/45819568/why-there-are-many-spark-warehouse-folders-got-created)

## Reference
* [Configuration - Spark 2.3.0 Documentation](https://spark.apache.org/docs/latest/configuration.html)
