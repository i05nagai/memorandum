---
title: Apache Sparkk Tuning
---

## Apache Sparkk Tuning
* Cluster-wide monitoring tools
    * can provide insight into overall cluster utilization and resource bottlenecks.
    * Ganglia
        * a Ganglia dashboard can quickly reveal whether a particular workload is disk bound, network bound, or CPU bound.
* OS profiling tools
    * can provide fine-grained profiling on individual nodes.
    * dstat
    * iostat
    * iotop
* JVM utilities
    * jstack
        * for providing stack traces,
    * jmap
        * for creating heap-dumps,
    * jstat
        * for reporting time-series statistics 
    * jconsole
        * for visually exploring various JVM properties are useful for those comfortable with JVM internals.

## CPU core/ memory
* [Understanding your Apache Spark Application Through Visualization - The Databricks Blog](https://databricks.com/blog/2015/06/22/understanding-your-spark-application-through-visualization.html)
* [How-to: Tune Your Apache Spark Jobs (Part 2) – Cloudera Engineering Blog](https://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/)
* [Spark num-executors setting - Hortonworks](https://community.hortonworks.com/questions/56240/spark-num-executors-setting.html)

* `--num-executors` or `spark.executor.instances` configuration property
    * control the number of executors requested.
    * you will be able to avoid setting this property by turning on dynamic allocation with the `spark.dynamicAllocation.enabled` property.

* spark.executor.cores
    * 各executorの利用するcpu core
* spark.executor.memory
    * 各executorの利用するmemory

memoryの構成は以下。

* yarn.nodemanager.resource.memory-mb
    * Executor container
        * spark.yarn.executor.memoryOverhead
            * executroが使用するmememoryの超過可能分
            * このoverheadの分はmemoryが利用可能
            * defaultは`max(384, .07 * spark.executor.memory)`
        * spark.executor.memory
            * executorのheap size
            * JVMはこのheap 領域は使わない？
            * spark.shuffle.memoryFraction
                * defaultで0.2
            * spark.storage.memoryFraction

<div style="text-align: center">
<img src="http://blog.cloudera.com/wp-content/uploads/2015/03/spark-tuning2-f1.png">
</div>

* 6 node
* 各nodeに16 cores, 64GB memory
* `yarn.nodemanager.resource.memory-mb`は64 * 1024 = 64512 MB
* `yarn.nodemanager.resource.cpu-vcores`は15

この状況でmemoryとCPUの割り振りを考えるが、Hadoop DaemonとOS用のResourceは残す必用がある。

案として`--num-executors 6 --executor-cores 15 --executor-memory 63G`は良くない。

* 各executorが1つのnodeにいる
* 各executorが15のcpu coreとmemory 63GBを使う

`--num-executors 17 --executor-cores 5 --executor-memory 19G`の方が良い。

* 3 executorがAMを除く(AMは2 executors)全てのnodeに割り振られる
* memoryは63 / 3 = 21から21 * 0.93でだいたい19
    * 0.93はOSとかHadoop Daemonを考慮しての掛け目

## Reference
