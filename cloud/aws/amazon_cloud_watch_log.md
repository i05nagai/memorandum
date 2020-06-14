---
title: Amazon CloudWatch Log
---

## Amazon CloudWatch Log


## SubscriptionFilter
- [Using CloudWatch Logs Subscription Filters \- Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html)

CloudWatch Log can send the log to some destinations including Kinesis data firehose.


Sample event

- owner
    - The AWS Account ID of the originating log data.
- logGroup
    - The log group name of the originating log data.
- logStream
    - The log stream name of the originating log data.
- subscriptionFilters
    - The list of subscription filter names that matched with the originating log data.
- mMesageType
    - CONTROL_MESSAGE
        - are sent by CWL to check if the subscription is reachable. They do not contain actual data.
    - DATA_MESSAGE
- logEvents
    - The actual log data, represented as an array of log event records. The "id" property is a unique identifier for every log event.

```
{
    "owner": "111111111111",
    "logGroup": "CloudTrail",
    "logStream": "111111111111_CloudTrail_us-east-1",
    "subscriptionFilters": [
        "Destination"
    ],
    "messageType": "DATA_MESSAGE",
    "logEvents": [
        {
            "id": "31953106606966983378809025079804211143289615424298221568",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        },
        {
            "id": "31953106606966983378809025079804211143289615424298221569",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        },
        {
            "id": "31953106606966983378809025079804211143289615424298221570",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        }
    ]
}
```

## Reference
