---
title: Apache Flink
---

## Apache Flink


## Concetps
- DataFrame API
    - how to implement a simple DataStream application and how to extend it to be stateful and use timers
- Table API
    - The Table API Flink’s language-embedded, relational API to write SQL-like queries in Java or Scala which are automatically optimized similar to SQL queries.


## JVM memory
https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/memory/mem_setup_tm/

- JVM heap
    - Framework heap
    - Task heap
- Off heap memory
    - Managed memory
        1. streaming jobs can use it for RocksDB state backend.
        2. both streaming and batch jobs can use it for sorting, hash tables, caching of intermediate results.
        3. both streaming and batch jobs can use it for executing User Defined Functions in Python processes.
    - Direct memory
        - Framework off-heap
        - Task Off-heap
        - Network
    - JVM Metaspace
    - JVM Overhead


## backpressue
- https://flink.apache.org/2021/07/07/backpressure.html

## Windows
https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/operators/windows/


Assigners

Window functions

Triggers

- Each window functions has the default trigger: EventTimeTrigger which triggers the window functions after the watermark passes the end of window.

Evictors

## Error
Class class com.klarna.cloudpipeline.decisionengines.AccountLimitRecord cannot be used as a POJO type because not all fields are valid POJO fields, and must be processed as GenericType. Please read the Flink documentation on \"Data Types & Serialization\" for details of the effect on performance.


## Serialization
- https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/fault-tolerance/serialization/types_serialization/

## Flink vs Spark
- [Apache Showdown: Flink vs\. Spark](https://engineering.zalando.com/posts/2016/03/apache-showdown-flink-vs.-spark.html)

## Flink on Kubernets

#### Upgrades
https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-release-1.3/docs/custom-resource/job-management/


## State
https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/fault-tolerance/state/


- `ValueState<T>`
    - This keeps a value that can be updated and retrieved (scoped to key of the input element as mentioned above, so there will possibly be one value for each key that the operation sees). The value can be set using update(T) and retrieved using T value().
- `ListState<T>`
    - This keeps a list of elements. You can append elements and retrieve an Iterable over all currently stored elements. Elements are added using add(T) or addAll(List<T>), the Iterable can be retrieved using Iterable<T> get(). You can also override the existing list with update(List<T>)
- `ReducingState<T>`
    - This keeps a single value that represents the aggregation of all values added to the state. The interface is similar to ListState but elements added using add(T) are reduced to an aggregate using a specified ReduceFunction.

- `AggregatingState<IN, OUT>`
    - This keeps a single value that represents the aggregation of all values added to the state. Contrary to ReducingState, the aggregate type may be different from the type of elements that are added to the state. The interface is the same as for ListState but elements added using add(IN) are aggregated using a specified AggregateFunction.
- `MapState<UK, UV>`
    - This keeps a list of mappings. You can put key-value pairs into the state and retrieve an Iterable over all currently stored mappings. Mappings are added using put(UK, UV) or putAll(Map<UK, UV>). The value associated with a user key can be retrieved using get(UK). The iterable views for mappings, keys and values can be retrieved using entries(), keys() and values() respectively. You can also use isEmpty() to check whether this map contains any key-value mappings.


- `StateTtlConfig.UpdateType.OnCreateAndWrite`
- `StateTtlConfig.UpdateType.OnReadAndWrite`

Cleanup of Expired State


- `disableCleanupInBackground`
- `cleanupFullSnapshot`


When is the Time-to-Live reset?

By default, the expiration time of a state entry is updated when the state is modified. Optionally, It can also be updated on read access at the cost of an additional write operation to update the timestamp.


Which time semantics are used for the Time-to-Live timers?

If the flink job does not access to the state for TTL time. The state will be removed.


## Time semantics

- Event time
- Processing time
- ingestion time


## Watermarks

- BoundedOutOfOrder


Watermark generators

- A periodic generator
    - usually observes the incoming events via onEvent() and then emits a watermark when the framework calls onPeriodicEmit().
- A puncutated generator
    - will look at events in onEvent() and wait for special marker events or punctuations that carry watermark information in the stream. When it sees one of these events it emits a watermark immediately. Usually, punctuated generators don’t emit a watermark from onPeriodicEmit().


## Checkpoint/Savepoint
Checkpoint and savepiont are handled by the same classes

Scheduler execute checkpointing

- Checkpiont Request goes to a request queue and the request to be executed is chosen from the queue.
- Then it triggers `flink.runtime.checkpoint.CheckpointCoordinater::startTriggeringCheckpoint`
    - Create pending checkpoints
    - Do pending checkpoints in `flink.runtime.checkpoint.OperatorCoordinatorCheckpoints::triggerAndAcknowledgeAllCoordinatorCheckpointsWithCompletion`
    - Do pending checkpoints in `flink.runtime.checkpoint.OperatorCoordinatorCheckpoints::triggerCoordinatorCheckpoint`
        - `state` is `byte[]`


- Coordinator to restore an operator from checkpont
    - `RecreateOnResetOperatorCoordinator.java`
- `SourceCoordinator`


## Reference
- [Benchmarking Streaming Computation Engines at\.\.\. \| Yahoo Engineering](https://yahooeng.tumblr.com/post/135321837876/benchmarking-streaming-computation-engines-at)
