---
title: Amazon DynamoDB
---

## Amazon DynamoDB

## Core concepts
* Tables
    * A table is a collection of data
    * The primary key for Music consists of two attributes (Artist and SongTitle)
    * Other than the primary key, tables are schemaless
    * When you create a table, in addition to the table name, you must specify the primary key of the table
* Items
    * Each table contains zero or more items
    * In DynamoDB, there is no limit to the number of items you can store in a table.
* Attributes
    * DynamoDB supports nested attributes up to 32 levels deep
* Primary key
    * Partition key
        * A simple primary key, composed of one attribute known as the partition key.
    * partition key and sort keys
        * Referred to as a composite primary key, this type of key is composed of two attributes.
* Secondary index
    * You can create one or more secondary indexes on a table
    * A secondary index lets you query the data in the table using an alternate key, in addition to queries against the primary key.
    * Global secondary index
    * Local secondary index
* High availability and durability
    * All of your data is stored on solid state disks (SSDs) and automatically replicated across multiple Availability Zones in an AWS region

## DataTypes
* scalar types
    * number
    * string
    * binary
    * Boolean
    * null
* document types
    * list
    * map
* set types
    * string set
    * number set
    * binary set

* string
* 

## Query
- [Working with Queries \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html)

- Query results are always sorted by the sort key value. If the data type of the sort key is Number, the results are returned in numeric order; otherwise, the results are returned in order of UTF-8 bytes. By default, the sort order is ascending. To reverse the order, set the ScanIndexForward parameter to false.

## Limits
* [Limits in DynamoDB \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html)

RRU = Read Request unit
WRU = Write Request unit

- provisioned table
    - 1 RCU = 1 strongly consistent read/sec, or 2 eventually consistent reads/sec, for items up to 4 KB in size.
    - 1 WCU = 1 write/sec, for items up to 1 KB in size.
        - for 10 KB data, you need 10 WCU to write data in a sec?
    - per table (depends on region)
        - 40,000 RCU
        - 40,000 WCU
    - per account (depends on region)
        - 80,000 RCU
        - 80,000 WCU
    - Minimum throughput for any table or global secondary index  (depends on region)
        - 1 RCU
        - 1 WCU
    - Increasing RCU/WCU
        - The new settings do not take effect until the UpdateTable operation is complete.
    - Decreasing RCU/WCU
        - The new settings do not take effect until the UpdateTable operation is complete.
- on demand
    - 1 RRU = 1 strongly consistent read, or 2 eventually consistent reads, for items up to 4 KB in size.
    - 1 WRU = 1 write, for items up to 1 KB in size.
    - per table  (depends on region)
        - 40,000 RRU
        - 40,000 WRU
    - per account  (depends on region)
        - no applicable
    - Minimum throughput for any table or global secondary index  (depends on region)
        - no applicable


- Partition
    - Adaptive capacity activates within 5‑30 minutes to help mitigate short‑term workload imbalance issues. However, each partition is still subject to the hard limit of 1000 WCU and 3000 RCU


## Global secondary index
[Improving Data Access with Secondary Indexes \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)

- you define an alternate key for the index (partition key and sort key)
- You also define the attributes that you want to be projected

## Local secondary index
- Partition key is the same as base table
- You can define an alternate key for the sort_key


## API

#### UpdateItem
- [UpdateItem \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html)
- [DynamoDB — Boto 3 Docs 1\.9\.181 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.update_item)

```
table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)
```

#### Throttled error
- [Resolve Issues with Throttled DynamoDB Tables](https://aws.amazon.com/premiumsupport/knowledge-center/throttled-ddb/)
- Throughput exceeds the current capacity for one or more global secondary indexes. DynamoDB is automatically scaling your index so please try again shortly
- [Designing Partition Keys to Distribute Your Workload Evenly \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-uniform-load.html)
- [Best Practices for DynamoDB \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)

#### Shard and Partition
- [How to perform ordered data replication between applications by using Amazon DynamoDB Streams \| AWS Database Blog](https://aws.amazon.com/blogs/database/how-to-perform-ordered-data-replication-between-applications-by-using-amazon-dynamodb-streams/)

- When you enable a stream on a DynamoDB table, DynamoDB creates at least one shard per partition.
- Shards in DynamoDB streams are collections of stream records.
- For example, event source mappings that read from a stream do not scale beyond the number of shards in the stream
    - [AWS Lambda Function Scaling \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/scaling.html)

#### Read capacity unit comsumption
- [Managing Throughput Settings on Provisioned Tables \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html#ItemSizeCalculations.Reads)


- Query
    - If query returns 41KB data, it rounds up to the next 4KB multiple.
    - 44 KB / 4 KB = consumed RCU in case of strongly consistent data
    - 44 KB / 8 KB = consumed RCU in case of eventually consistent data


#### Retention period of stream
- [DynamoDB Streams Use Cases and Design Patterns \| AWS Database Blog](https://aws.amazon.com/blogs/database/dynamodb-streams-use-cases-and-design-patterns/)
- [GetShardIterator \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html)

- 24 hours
- For every DynamoDB partition, there is a corresponding shard and a Lambda function poll for events in the stream (shard). Based on the batch size you specify, it fetches the records, processes it, and then fetches the next batch.


#### Dynamo db stremaing with KCL
- https://aws.amazon.com/blogs/big-data/processing-amazon-dynamodb-streams-using-the-amazon-kinesis-client-library/

The solution is to use KCL to consume the dynamo db stream.
AFIK, the KCL does not allow us to modify the retention period of dynamo db stream or any configuration.
If you use Lambdas to consume the event, there is no benefit.
If you're already familiar with KCL and new to other service, this might be a solution.

#### Checking the number of shards

```
aws dynamodbstreams describe-stream --stream-arn streamarn | jq '.StreamDescription.Shards | length'
```


#### Permissions
In provisioned, you need permissios to create SNS topic `dynamodb` when you change the WCU/RCU  after creation of dynamo db table.

```
User: ... is not authorized to perform: SNS:CreateTopic on resource: ...:dynamodb (Service: AmazonSNS; Status Code: 403; Error Code: AuthorizationError; Request ID: )
```


#### Error

Projection type is `INCLUDE`.
non_key_attributes contais table primary key and table sort key


```
a key attribute, primary key, is part of a list of non-key attributes, primary_key,sort_key, which is not allowed since all key attributes are added automatically and this configuration causes stack creation failure
```

ProjectionType is `INCLUDE`


```
dynamodb_table One or more parameter values were invalid: ProjectionType is INCLUDE, but NonKeyAttributes is not specified (Service: AmazonDynamoDBv2; Status Code: 400; Error Code: ValidationException; Request ID: )
```

#### Check if stream is eneabled or not
`describe-table` returns `StreamSpecification` key if stream is enabled.

```
        "StreamSpecification": {
            "StreamEnabled": true,
            "StreamViewType": "NEW_IMAGE"
        },
```

## Restore Dynamo DB
- [Restoring a DynamoDB Table to a Point in Time \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.Tutorial.html)

```
aws dynamodb update-continuous-backups \
    --table-name Music \
    --point-in-time-recovery-specification PointInTimeRecoveryEnabled=True 
```

Check if the PITR is enabled or not.

```
aws dynamodb describe-continuous-backups \
--table-name Music
```

Restore table

```
aws dynamodb restore-table-to-point-in-time \
    --source-table-name Music \
    --target-table-name MusicMinutesAgo \
    --use-latest-restorable-time

aws dynamodb restore-table-to-point-in-time \
    --source-table-name cloud-pipeline-db-backup-1x0-us-makus4-db \
    --target-table-name cloud-pipeline-db-backup-1x0-us-makus4-restore-db  \
    --use-latest-restorable-time
```

#### Error throttled exception

```
[ERROR] ClientError: An error occurred (ThrottlingException) when calling the UpdateItem operation (reached max retries: 9): Throughput exceeds the current capacity of your table or index. DynamoDB is automatically scaling your table or index so please try again shortly. If exceptions persist, check if you have a hot key: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html
```

## Loggging
- [Logging DynamoDB Operations by Using AWS CloudTrail \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/logging-using-cloudtrail.html)

## ARNs
- [DynamoDB API Permissions: Actions, Resources, and Conditions Reference \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/api-permissions-reference.html)

- `arn:aws:dynamodb:region:account-id:table/*`
- `arn:aws:dynamodb:region:account-id:table/table-name`
- `arn:aws:dynamodb::account-id:global-table/*`
- `arn:aws:dynamodb::account-id:global-table/global-table-name`
- `arn:aws:dynamodb:region:account-id:table/table-name/index/*`
- `arn:aws:dynamodb:region:account-id:table/table-name/index/index-name`
- `arn:aws:dynamodb:region:account-id:table/table-name/backup/*`
- `arn:aws:dynamodb:region:account-id:table/table-name/backup/backup-name`
- `arn:aws:dynamodb:region:account-id:*`
- `*`
- `arn:aws:dynamodb:region:account-id:table/table-name/stream/*`
- `arn:aws:dynamodb:region:account-id:table/table-name/stream/stream-label`


## Reference
* [DynamoDB Core Components \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)
