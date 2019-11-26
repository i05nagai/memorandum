---
title: hdfs
---

## hdfs
* [Apache Hadoop 2.6.0 - HDFS Commands Guide](https://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html#dfs)

## CLI

```
hdfs [--config confdir] [--loglevel loglevel] COMMAND
  dfs                  run a filesystem command on the file systems supported in Hadoop.
  classpath            prints the classpath
  namenode -format     format the DFS filesystem
  secondarynamenode    run the DFS secondary namenode
  namenode             run the DFS namenode
  journalnode          run the DFS journalnode
  zkfc                 run the ZK Failover Controller daemon
  datanode             run a DFS datanode
  debug                run a Debug Admin to execute HDFS debug commands
  dfsadmin             run a DFS admin client
  haadmin              run a DFS HA admin client
  fsck                 run a DFS filesystem checking utility
  balancer             run a cluster balancing utility
  jmxget               get JMX exported values from NameNode or DataNode.
  mover                run a utility to move block replicas across
                       storage types
  oiv                  apply the offline fsimage viewer to an fsimage
  oiv_legacy           apply the offline fsimage viewer to an legacy fsimage
  oev                  apply the offline edits viewer to an edits file
  fetchdt              fetch a delegation token from the NameNode
  getconf              get config values from configuration
  groups               get the groups which users belong to
  snapshotDiff         diff two snapshots of a directory or diff the
                       current directory contents with a snapshot
  lsSnapshottableDir   list all snapshottable dirs owned by the current user Use -help to see options
  portmap              run a portmap service
  nfs3                 run an NFS version 3 gateway
  cacheadmin           configure the HDFS cache
  crypto               configure HDFS encryption zones
  storagepolicies      list/get/set block storage policies
  version              print the version
```

### dfs
Hadoop fs command.

* `-ls <path>`
    * 
* `-appendToFile`
* `-copyFromLocal from to`
* `-cp from to`
* `-copyToLocal from to`


## Usage

```
hdfs -ls hdfs:///var/log/
```

#### dfsadmin
[Apache Hadoop 2\.7\.1 – HDFS Commands Guide](https://hadoop.apache.org/docs/r2.7.1/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html#dfsadmin)

Update the fsimage and remove editlogs if conditions are met.
See related configuration.

- dfs.namenode.num.extra.edits.retained
- dfs.namenode.num.checkpoints.retained

```
hdfs dfsadmin -safemode enter
hdfs dfsadmin -saveNamespace
hdfs dfsadmin -safemode leave
```

Roll edit logs. Just rolling in progress edit logs. So it doesn't update the fsimage and delete the editlogs.


```
hdfs dfsadmin -rollEdits
```

```
hdfs dfsadmin -report
```


- query: Query the current rolling upgrade status.
- prepare: Prepare a new rolling upgrade.
- finalize: Finalize the current rolling upgrade.

```
hdfs dfsadming -rollingUpgrade [<query>|<prepare>|<finalize>]
```


#### getconf
- [hdfs getconf command examples \- Fibrevillage](http://fibrevillage.com/storage/646-hdfs-getconf-command-examples)

```
hdfs getconf -confKey fs.defaultFS
hdfs getconf -confKey yarn.resourcemanager.address
```


## Reference
