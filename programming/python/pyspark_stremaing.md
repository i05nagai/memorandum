---
title: pyspark streaming
---

## pyspark streaming

## API
- [pyspark\.sql\.streaming — PySpark 2\.4\.0 documentation](http://spark.apache.org/docs/2.4.0/api/python/_modules/pyspark/sql/streaming.html)

- `DataStreamWriter`

- `DataStreamWriter.outputMode`
    - `append`
        - Only the new rows in the streaming DataFrame/Dataset will be written to the sink
    * `append`
        * Only the new rows in the streaming DataFrame/Dataset will be written to the sink
    * `complete`
        * All the rows in the streaming DataFrame/Dataset will be written to the sink every time these is some updates
    * `update`
        * only the rows that were updated in the streaming DataFrame/Dataset will be written to the sink every time there are some updates. If the query doesn't contain aggregations, it will be equivalent to `append` mode.
- `trigger`
    - `processingTime`
        - a processing time interval as a string, e.g. '5 seconds', '1 minute'.  Set a trigger that runs a query periodically based on the processing time. Only one trigger can be set.
        - by default `processingTime='0 seconds'`
        - e.g. `2 seconds`, `1 minute`
    - `once`
        - if set to True, set a trigger that processes only one batch of data in a streaming query then terminates the query. Only one trigger can be set.


- explode
    - [pyspark\.sql module — PySpark master documentation](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=explode)


## Reference
- [Spark streaming with PySpark reading socket – Nitin Gupta – Medium](https://medium.com/@nitingupta.bciit/spark-streaming-with-pyspark-reading-socket-c7a9e317585d)
- [Spark Streaming \- Reading data from TCP Socket](https://sparkbyexamples.com/spark-streaming-from-tcp-socket/)
