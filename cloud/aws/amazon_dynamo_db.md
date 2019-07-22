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

## Reference
* [DynamoDB Core Components \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)
