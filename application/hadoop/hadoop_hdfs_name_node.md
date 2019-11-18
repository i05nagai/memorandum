---
title: Hadoop HDFS NameNode
---

## Hadoop HDFS NameNode


## HA
- [Apache Hadoop 3\.2\.1 – HDFS High Availability](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithNFS.html)

- `dfs.namenode.shared.edits.dir`
    - the location of the shared storage directory
    - This is where one configures the path to the remote shared edits directory which the Standby NameNodes use to stay up-to-date with all the file system changes the Active NameNode makes. You should only configure one of these directories. This directory should be mounted r/w on the NameNode machines. The value of this setting should be the absolute path to this directory on the NameNode machines. For example:

## Reference

