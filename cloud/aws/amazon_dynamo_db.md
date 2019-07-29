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


## Reference
* [DynamoDB Core Components \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)
