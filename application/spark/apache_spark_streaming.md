---
title: Apache Spark Streaming
---

## Apache Spark Streaming


## Foreach
- https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#output-sinks

You can use either class or function.

```python
def process_row(row):
    # Write row to storage
    pass

query = streamingDF.writeStream.foreach(process_row).start()
```

```python
class ForeachWriter:
    def open(self, partition_id, epoch_id):
        # Open connection. This method is optional in Python.
        pass

    def process(self, row):
        # Write row to connection. This method is NOT optional in Python.
        pass

    def close(self, error):
        # Close the connection. This method in optional in Python.
        pass

query = streamingDF.writeStream.foreach(ForeachWriter()).start()
```


#### Watermarking
[Structured Streaming Programming Guide \- Spark 2\.4\.0 Documentation](http://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#window-operations-on-event-time)

* You can define the watermark of a query by specifying the event time column and the threshold on how late the data is expected to be in terms of event time
* For a specific window starting at time T, the engine will maintain state and allow late data to update the state until (max event time seen by the engine - late threshold > T)

```scala
import spark.implicits._

val words = ... // streaming DataFrame of schema { timestamp: Timestamp, word: String }

// Group the data by window and word and compute the count of each group
val windowedCounts = words
    .withWatermark("timestamp", "10 minutes")
    .groupBy(
        window($"timestamp", "10 minutes", "5 minutes"),
        $"word")
    .count()
```

## Tips
- [Long\-running Spark Streaming Jobs on YARN Cluster \- Passionate Developer](http://mkuthan.github.io/blog/2016/09/30/spark-streaming-on-yarn/)
- [24/7 Spark Streaming on YARN in Production \- inovex\-Blog](https://www.inovex.de/blog/247-spark-streaming-on-yarn-in-production/)
- [How\-to: Tune Your Apache Spark Jobs \(Part 2\) \- Cloudera Engineering Blog](https://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-2/)
- [Resolve the Error "Container killed by YARN for exceeding memory limits" in Spark on Amazon EMR](https://aws.amazon.com/premiumsupport/knowledge-center/emr-spark-yarn-memory-limit/)
- [Chapter 4\. Log Aggregation for Long\-running Applications \- Hortonworks Data Platform](https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.5.0/bk_yarn-resource-management/content/ch_log_aggregation.html)

#### Loggign level

```
log4j.logger.org.apache.spark.sql.execution.streaming.StreamExecution=DEBUG
```

#### Checkpointing
- [Improving Spark Streaming Checkpointing Performance With AWS EFS \- Yuval Itzchakov’s Blog](https://blog.yuvalitzchakov.com/improving-spark-streaming-checkpoint-performance-with-aws-efs/)

#### Consuming a Kafka topic but zero events receive
- [Re: kafka structured streaming source refuses to read](http://mail-archives.apache.org/mod_mbox/spark-user/201701.mbox/%3cCAAswR-7JG3Bo8JMJgXu8Fg9NuKZun_z6LgJsptccgL_uvXbQgQ@mail.gmail.com%3e)


## Reference
* [Structured Streaming Programming Guide \- Spark 2\.4\.0 Documentation](http://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
