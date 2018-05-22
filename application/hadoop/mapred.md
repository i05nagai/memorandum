---
title: mapred
---

## mapred
MapReduce command.

## CLI

### job

```
mapred job <command> <args>
```

* `-hisotry <job-id or all>`
    * `all`
* `-submit <job-file>`
* `-status <job-id>`
* `-counter <job-id> <group-name> <counter-name>`
* `-kill <job-id>`
* `-set-priority <job-id> <priority>`
    * Valid values for priorities are: VERY_HIGH HIGH NORMAL LOW VERY_LOW DEFAULT. In addition to this, integers also can be used.
* `-events <job-id> <from-event-#> <#-of-events>`
* `-history <jobHistoryFile>`
* `-list [all]`
* `-list-active-trackers`
* `-list-blacklisted-trackers`
* `-list-attempt-ids <job-id> <task-type> <task-state>`
    * Valid values for <task-type> are MAP REDUCE. Valid values for <task-state> are pending, running, completed, failed, killed
* `-kill-task <task-attempt-id>`
* `-fail-task <task-attempt-id>`
* `-logs <job-id> <task-attempt-id>`


## Usage

## Reference
* [Apache Hadoop 2.7.1 – MapReduce Commands Guide](https://hadoop.apache.org/docs/r2.7.1/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapredCommands.html)
