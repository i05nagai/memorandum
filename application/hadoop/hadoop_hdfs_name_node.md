---
title: Hadoop HDFS NameNode
---

## Hadoop HDFS NameNode

- [A Guide to Checkpointing in Hadoop \- Cloudera Blog](https://blog.cloudera.com/a-guide-to-checkpointing-in-hadoop/)
    - How metadata are created
- [Actual use of FSimage and Edits log? \- Cloudera Community](https://community.cloudera.com/t5/Support-Questions/Actual-use-of-FSimage-and-Edits-log/td-p/166077)
- [What is SafeMode in Hadoop \| Tech Tutorials](https://netjs.blogspot.com/2018/02/what-is-safemode-in-hadoop-hdfs.html)


## HA
- [Apache Hadoop 3\.2\.1 – HDFS High Availability](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSHighAvailabilityWithNFS.html)
- [Apache Hadoop 3\.2\.1 – HDFS Users Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)
- [Deploying HDFS on a Cluster \| 5\.4\.x \| Cloudera Documentation](https://docs.cloudera.com/documentation/enterprise/5-4-x/topics/cdh_ig_hdfs_cluster_deploy.html)


    - To update automatically fsimage, we need secondby namenode.
    - The behavior of the Secondary NameNode is controlled by the following parameters in hdfs-site.xml.
        - dfs.namenode.checkpoint.check.period
        - dfs.namenode.checkpoint.txns
        - dfs.namenode.checkpoint.dir
        - dfs.namenode.checkpoint.edits.dir
        - dfs.namenode.num.checkpoints.retained


- `dfs.namenode.shared.edits.dir`
    - the location of the shared storage directory
    - This is where one configures the path to the remote shared edits directory which the Standby NameNodes use to stay up-to-date with all the file system changes the Active NameNode makes. You should only configure one of these directories. This directory should be mounted r/w on the NameNode machines. The value of this setting should be the absolute path to this directory on the NameNode machines. For example:

## Reference

