---
title: Apache Kafka
---

## Apache Kafka
A distributed streaming platform.

* Building real-time streaming data pipelines that reliably get data between systems or applications
* Building real-time streaming applications that transform or react to the streams of data


kafka
16cpu core, 32gb, 3TB(raid10)
9 node

## Term
* leader
    * is the node responsible for all reads and writes for the given partition. Each node will be the leader for a randomly selected portion of the partitions.
* replicas
    * is the list of nodes that replicate the log for this partition regardless of whether they are the leader or even if they are currently alive.
* isr
    * is the set of "in-sync" replicas. This is the subset of the replicas list that is currently alive and caught-up to the leader.


## TLS
- [Security Tutorial — Confluent Platform](https://docs.confluent.io/current/tutorials/security_tutorial.html#generating-keys-certs)


## Performance
- [Benchmarking Apache Kafka: 2 Million Writes Per Second \(On Three Cheap Machines\) \| LinkedIn Engineering](https://engineering.linkedin.com/kafka/benchmarking-apache-kafka-2-million-writes-second-three-cheap-machines)


## Reference
* [Apache Kafka](https://kafka.apache.org/)
* [Top 5 Apache Kafka Books \| Complete Guide To Learn Kafka \- DataFlair](https://data-flair.training/blogs/apache-kafka-books/)
* [Install and Configure Apache Kafka on Ubuntu 16\.04 \| ProfitBricks DevOps Central](https://devops.profitbricks.com/tutorials/install-and-configure-apache-kafka-on-ubuntu-1604-1/)
