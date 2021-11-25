---
title: Kinesis Streams
---

## Kinessi Streams
Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service.

* shardで性能を調節する
    * 1 shardあたり、1MB/secのInputと2MB/secのoutput or 1000PUT/sec
    * どちらかを超過する場合はshardを増やす必要がある

## Price
料金のかかる所は以下の3箇所
値段は参考までに、US East Ohio

* dollars per shard per hour1
    * 0.015 USD
* PUT payload unit、1,000,000 unitごと
    * 25KB単位ごとに1Unitとなる
    * 5KBのrecordをPUTする場合は1 unit
    * 45KBのrecordをPUTする場合は2 unit
    * 1MBのrecordをPUTする場合は40 unit
    * 1000000 untiで$0.014
* 拡張データ保持期限 (最大 7 日間)、シャード時間ごと
    * defaultの24時間保存より増やすと料金が増える
    * 1 shardあたり1時間ふやすごとに料金がかかる
    * 1 shardあたり1 hourの増加で$0.020

* 1時間1 shardの利用で

## Lambda

```python
import base64
import decimal
import json
import logging
import os
from aws_kinesis_agg.deaggregator import deaggregate_records

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
table = boto3.resource("dynamodb").Table("table_name")


def handler(event, context) -> None:
    with table.batch_writer(overwrite_by_pkeys=["partition_key", "sort_key"]) as db_writer:
        records = deaggregate_records(event['Records'])
        for record in event["Records"]:
            logger.info(record)
            data = json.loads(base64.b64decode(record["kinesis"]["data"]), parse_float=decimal.Decimal)
            db_writer.put_item(data)
```

## Referece
* [Amazon Kinesis Data Streams \- AWS](https://aws.amazon.com/kinesis/data-streams/)
* [AWS再入門 Amazon Kinesis編 ｜ Developers.IO](http://dev.classmethod.jp/cloud/aws/cm-advent-calendar-2015-aws-re-entering-kinesis/)
