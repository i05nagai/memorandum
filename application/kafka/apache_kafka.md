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


## topic replication
https://community.cloudera.com/t5/Community-Articles/Kafka-0-9-Configuration-Best-Practices/ta-p/246962#:~:text=The%20replication%20factor%20for%20the,request%20for%20the%20offsets%20topic.

## Configuration
- offsets.topic.replication.factor
    - the number of replica for a partition which brokers replicate as a backup
- `client.id.prefix`
- `client.id`
- `group.id`
    - A unique string that identifies the consumer group this consumer belongs to.
    - This property is required if the consumer uses either the group management functionality by using subscribe(topic) or the Kafka-based offset management strategy.
- `group.instance.id`
    - A unique identifier of the consumer instance provided by the end user.
- `max.poll.interval.ms`
- `partition.discovery.interval.ms`
- `auto.offset.reset`
- `enable.auto.commit`
- `restart-strategy`
    - `exponential-delay`
- `taskmanager.registration.timeout`
- `queryable-state.proxy.ports`
- `heartbeat.interval`
- `heartbeat.timeout`
- `web.timeout`
- `web.submit.enable`
- `web.cancel.enable`
- `state.backend`
    - `rocksdb`
- `state.checkpoints.dir`
- `state.savepoints.dir`
- `state.backend.rocksdb.localdir`
- `state.backend.incremental`
- `state.backend.rocksdb.thread.num`
- `state.backend.rocksdb.checkpoint.transfer.thread.num`
- `jobmanager.execution.failover-strategy`
    - region
- `isolation.level`
    - `read_committed`
        - consumer.poll() will only return transactional messages which have been committed.
        - Non-transactional messages will be returned unconditionally in either mode.
    - `read_uncommitted`
        - consumer.poll() will return all messages, even transactional messages which have been aborted.
        - Non-transactional messages will be returned unconditionally in either mode.


## Cleanup
- https://docs.confluent.io/platform/current/installation/configuration/topic-configs.html#ak-topic-configurations-for-cp

- `cleanup.policy=compact`
    - The “compact” policy will enable log compaction, which retains the latest value for each key. 
- `cleanup.policy=delete`
    -  The “delete” policy (which is the default) will discard old segments when their retention time or size limit has been reached. 

- `retention.ms`
    - default: 7days
    - If set to -1, no time limit is applied.

## Compacted topic
- https://towardsdatascience.com/log-compacted-topics-in-apache-kafka-b1aa1e4665a7
- https://developer.confluent.io/learn-kafka/architecture/compaction/
- Log compaction is a mechanism to give finer-grained per-record retention, rather than the coarser-grained time-based retention. The idea is to selectively remove records where we have a more recent update with the same primary key. This way the log is guaranteed to have at least the last state for each key.

`cleanup.policy=compact` 

## Segments

- `segment.bytes`
- `segment.ms`


## Tomstones
- https://medium.com/@damienthomlutz/deleting-records-in-kafka-aka-tombstones-651114655a16



## Consumer

## Consumer group

As a consumer in the group reads messages from the partitions assigned by the coordinator, it must commit the offsets corresponding to the messages it has read. If the consumer crashes or is shut down, its partitions will be re-assigned to another member, which will begin consumption from the last committed offset of each partition.
If the consumer crashes before any offset has been committed, then the consumer which takes over its partitions will use the reset policy.

## TLS
- [Security Tutorial — Confluent Platform](https://docs.confluent.io/current/tutorials/security_tutorial.html#generating-keys-certs)


## Performance
- [Benchmarking Apache Kafka: 2 Million Writes Per Second \(On Three Cheap Machines\) \| LinkedIn Engineering](https://engineering.linkedin.com/kafka/benchmarking-apache-kafka-2-million-writes-second-three-cheap-machines)


## Reference
* [Apache Kafka](https://kafka.apache.org/)
* [Top 5 Apache Kafka Books \| Complete Guide To Learn Kafka \- DataFlair](https://data-flair.training/blogs/apache-kafka-books/)
* [Install and Configure Apache Kafka on Ubuntu 16\.04 \| ProfitBricks DevOps Central](https://devops.profitbricks.com/tutorials/install-and-configure-apache-kafka-on-ubuntu-1604-1/)
