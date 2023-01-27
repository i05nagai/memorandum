---
title: Debezium
---

## Debezium


## MySQL Connector
https://debezium.io/documentation/reference/stable/connectors/mysql.html


- `database.include.list`
- `database.server.id`
    - unique id of connector
- `include.schema.changes`
    - Flag that specifies if the connector should generate events for DDL changes and emit them to the fulfillment schema change topic for use by consumers.

Performance

- https://reorchestrate.com/posts/debezium-performance-impact/
- Dumping is done with
    - https://github.com/shyiko/mysql-binlog-connector-java/blob/dd710a5466381faa57442977b24fceff56a0820e/src/main/java/com/github/shyiko/mysql/binlog/network/protocol/command/DumpBinaryLogGtidCommand.java
    - https://github.com/shyiko/mysql-binlog-connector-java/blob/dd710a5466381faa57442977b24fceff56a0820e/src/main/java/com/github/shyiko/mysql/binlog/network/protocol/command/DumpBinaryLogCommand.java
- https://hevodata.com/learn/using-mysql-binlog/#:~:text=The%20mysqlbinlog%20command%20displays%20the,which%20the%20logs%20are%20required.


## Schema changes
- https://debezium.io/blog/2016/04/15/parsing-ddl/



## Transformations
https://debezium.io/documentation/reference/stable/transformations/index.html
https://docs.confluent.io/platform/current/connect/transforms/regexrouter.html#regexrouter


#### org.apache.kafka.connect.transforms.RegexRouter
Update the record’s topic using the configured regular expression and replacement string.

Examples

Drop `soe-` from the topic

```
"transforms": "dropPrefix",
"transforms.dropPrefix.type": "org.apache.kafka.connect.transforms.RegexRouter",
"transforms.dropPrefix.regex": "soe-(.*)",
"transforms.dropPrefix.replacement": "$1"
```


## Reference
