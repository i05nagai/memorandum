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



## Reference
* [DynamoDB Core Components \- Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)
