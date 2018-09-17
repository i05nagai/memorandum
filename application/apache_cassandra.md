---
title: Apache Cassandra
---

## Apache Cassandra

## Install
For ubuntu,

```
echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -
sudo apt-get update
sudo apt-get install cassandra
```

## Reference
* [Apache Cassandra](http://cassandra.apache.org/)
