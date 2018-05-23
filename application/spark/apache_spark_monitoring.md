---
title: Apache Spark Monitoring
---

## Apache Spark Monitoring
* Cluster-wide monitoring tools
    * can provide insight into overall cluster utilization and resource bottlenecks. For instance, a Ganglia dashboard can quickly reveal whether a particular workload is disk bound, network bound, or CPU bound.
    * Ganglia
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

## Reference
* [Monitoring and Instrumentation - Spark 2.3.0 Documentation](https://spark.apache.org/docs/latest/monitoring.html)
