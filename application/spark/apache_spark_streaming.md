---
title: Apache Spark Streaming
---

## Apache Spark Streaming


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

## Reference
* [Structured Streaming Programming Guide \- Spark 2\.4\.0 Documentation](http://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
