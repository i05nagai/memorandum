---
title: Amazon Kinesis Data Firehose
---

## Amazon Kinesis Data Firehose
Amazon Kinesis Data Firehose is a fully managed service for delivering real-time streaming data to destinations such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon Elasticsearch Service (Amazon ES), and Splunk.

* Amazon KDF
    * fully managed service for delivering real-time streaming data
* Amazon KDS
    * not fully managed service for delivering real-time streaming data

* shardによる性能調整が不要
    * 投入データ料におうじた従量課金
* 1秒あたり2500回のPUTが可能、サポート経由で上限緩和が可能


## Conceptso
* record
    * A record can be as large as 1,000 KB.
* buffer size
    * in MB
* buffer interval
    * in second

## Custom prefix for S3 
- [Custom Prefixes for Amazon S3 Objects \- Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html)


- `<evaluated prefix><suffix>`
- suffix: `<delivery stream name>-<delivery stream version>-<year>-<month>-<day>-<hour>-<minute>-<second>-<uuid><file extension>`
    - you cannot change the suffix field


For prefix, you can use the expression `{namespace:value}` in custom prefix.


* timestamp namespace
    * always UTC
    * kinesis uses the approximate arrival timestamp of the oldest record that's contained in the Amazon S3 object being written
    * If you use the timestamp namespace more than once in the same prefix expression, every instance evaluates to the same instant in time.
* firehose namespace



## Firehose/streams
* Kinesis Streams
    * EC2、EMR、Lamnda等、複数のアプリケーションから参照する事が可能です。
    *  ャードの増減により性能調整が可能です。
* kinesis firehose
    * 登録可能なデータの仕様はKinesis Streamsと共通です。
    * 登録されたデータは、S3、Redshiftに自動的にエクスポートされます。
* Kinesis analytics
    * Amazon Kinesisに登録されたストリームデータのタイムウィンドウ処理、直近の一定時間を対象とした集計などがSQLにより可能となります。

## Kinesis firehose with splunk
[Tutorial: Sending VPC Flow Logs to Splunk Using Amazon Kinesis Data Firehose \- Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/vpc-splunk-tutorial.html)

```
AWS service -> cloud watch -> kinesis data firehose + lambda -> splunk instance
```


#### Splunk endpoint
- [Select destination \- Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html#create-destination-splunk)
- [SplunkDestinationConfiguration \- Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/APIReference/API_SplunkDestinationConfiguration.html#Firehose-Type-SplunkDestinationConfiguration-S3BackupMode)
- [Install and configure the Splunk Add\-on for Amazon Kinesis Firehose on a paid Splunk Cloud deployment \- Splunk Documentation](https://docs.splunk.com/Documentation/AddOns/released/Firehose/RequestFirehose)
    - Indexer acknowledgement should be enabled


- CloudWatchLoggingOptions
- HECAcknowledgmentTimeoutInSeconds
- HECEndpoint
- HECEndpointType
- Splunk endpoint type
- Authentication token
- HEC acknowledgement timeout
- Retry duration
- S3 backup mode
    - FailedEventsOnly | AllEvents
    - defaut is `FailedEventsOnly`
- S3Configuration
    - 


## Source

## Desitination
- [Select destination \- Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html#create-destination-s3)


## Price
* 1GB \$0.029 up to 500TB/month
* 1GB \$0.025 up to 1.5PB/month
* 1GB \$0.020 up to 3PB/month
* ask AWS more than 5PB/month


## Processor
- https://stackoverflow.com/questions/60734063/aws-firehose-where-is-the-definition-of-the-event-format-to-process-in-lambda


## Tip

#### Decoding data

```python
import base64
import gzip
import io

gzip_data = base64.b64decode(data)
raw_data = gzip.GzipFile(fileobj=io.BytesIO(gzip_data)).read().decode("utf-8")
```

## Reference
* [What Is Amazon Kinesis Data Firehose? \- Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
* [AWS再入門 Amazon Kinesis編 ｜ Developers.IO](http://dev.classmethod.jp/cloud/aws/cm-advent-calendar-2015-aws-re-entering-kinesis/)
