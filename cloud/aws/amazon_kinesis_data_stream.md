---
title: Amazon Kinesis Data Stream
---

## Amazon Kinesis Data Stream
You can use Amazon Kinesis Data Streams to collect and process large streams of data records in real time. 
Amazon KDS is a part of Kinesis platform;

* Kinesis Data Firehose
* Kinesis Video Streams

## Concepts
* [Kinesis Data Streams Key Concepts \- Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)

* Data Producer
* Data comsumer
* Data stream
* Shard
* Amazon Kinesis Agent
    * Amazon Kinesis Agent is a pre-built Java application that offers an easy way to collect and send data to your Amazon Kinesis stream.
* Amazon Lambda
* Amazon Kinesis Client Library (KCL)
* Amazon Kinesis Connector Library
* Amazon Kinesis Storm Spout
* Data record
* Retention period
    * the retention period is the length of time that data records are accessible after they added to the stream

* Destination
    * S3
    * Redshift
    * ES
    * Splunk

## IAM
[Step 2: Create an IAM Policy and User \- Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/learning-kinesis-module-one-iam.html)

* Producer
    * DescribeStream
        * Kinesis data stream
    * PutRecord, PutRecords
        * Kinesis data stream
* Consumer
    * DescribeStream
    * GetRecords, GetShardIterator
    * CreateTable, DescribeTable, GetItem, PutItem, Scan, UpdateItem
    * DeleteItem
    * utMetricData

## Shards

* The default shard limit is 500 shards
* capacity per shards
    * write
        * 1MB/sec
        * 1000 records/sec
    * read
        * 2MB/sec

* Record size
    * x KB
    * betwen 1KB and 1024KB
* Max records written
    * y per second
    * (Number of records per second) x (Number of producers)
* Number of consumer applications
    * z


Record size is an integer between 1 and 1024

## Reference
* [Data Lakes and Analytics \| AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/)
* [Amazon Kinesis Data Streams getting started](https://aws.amazon.com/kinesis/data-streams/getting-started/)
