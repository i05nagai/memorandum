---
title: yarn
---

## yarn
CLI for Apache Hadoop YARN.

* application id
    * `application_<unix_time>_xxxx`
        * `xxxx` is application number
    * `xxxx` is counted up by each `spark-submit` execution
* application attemp id
    * `appattempt_<unix_time>_xxxx_yyyyyy`
        * `<unix_time>` is application id's unix epoch time
        * `yyyyyy` is attemp number
* container id
    * [ContainerId \(Apache Hadoop Main 2\.9\.2 API\)](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/yarn/api/records/ContainerId.html)
    * e.g. `container_<unix_time>_xxxx_zz_wwwwww`
    * `zz`
        * attemptID
    * `wwwwww`
        * container ID
* AM
    * application master
    * master node?
* AM container id
    * container for application master
* RM
    * resource maanger
* queue
    * `default` by default

## CLI

```
Usage: yarn [--config confdir] [COMMAND | CLASSNAME]
  CLASSNAME                             run the class named CLASSNAME
 or
  where COMMAND is one of:
  resourcemanager                       run the ResourceManager
                                        Use -format-state-store for deleting the RMStateStore.
                                        Use -remove-application-from-state-store <appId> for
                                            removing application from RMStateStore.
  nodemanager                           run a nodemanager on each slave
  timelineserver                        run the timeline server
  rmadmin                               admin tools
  sharedcachemanager                    run the SharedCacheManager daemon
  scmadmin                              SharedCacheManager admin tools
  version                               print the version
  jar <jar>                             run a jar file
  application                           prints application(s)
                                        report/kill application
  applicationattempt                    prints applicationattempt(s)
                                        report
  container                             prints container(s) report
  node                                  prints node report(s)
  queue                                 prints queue information
  logs                                  dump container logs
  classpath                             prints the class path needed to
                                        get the Hadoop jar and the
                                        required libraries
  cluster                               prints cluster information
  daemonlog                             get/set the log level for each
                                        daemon
  top                                   run cluster usage tool
```

### nodemanager

### application

```
yarn application [option]
```

* `-appStates RUNNING`
    * `ALL,NEW,NEW_SAVING,SUBMITTED,ACCEPTED,RUNNING,FINISHED,FAILED,KILLED`

### applicationattemp

```
yarn applicationattempt <option>
```

* `-fail <Application Attempt ID>`
    * Fails application attempt.
* `-list <Application ID>`
    * List application attempts for application.
* `-status <Application Attempt ID>`
    * Prints the status of the application attempt.

### logs
PySparkなどでstderrのlogを見る場合などに使える。
applicationIdは何らかの方法で調べる必要がある。

```
yarn logs -applicationId <application ID> [OPTIONS]
```

* `-am <AM Containers>`
    * Prints the AM Container logs for this application. Specify comma-separated
                                 value to get logs for related AM
                                 Container. For example, If we specify -am
                                 1,2, we will get the logs for the first
                                 AM Container as well as the second AM
                                 Container. To get logs for all AM
                                 Containers, use -am ALL. To get logs for
                                 the latest AM Container, use -am -1. By
                                 default, it will only print out syslog.
                                 Work with -logFiles to get other logs
* `-appOwner <Application Owner>`
    * AppOwner (assumed to be current user if not specified)
* `-containerId <Container ID>`
    * ContainerId. By default, it will only print syslog if the application is runing. Work with -logFiles to get other logs.
* `-logFiles <Log File Name>`
    * Work with -am/-containerId and specify comma-separated value to get specified container log files.
    * Use "ALL" to fetch all the log files for the container.
* `-nodeAddress <Node Address>`
    * NodeAddress in the format nodename:port

### container
List containers for application attempt.

```
yarn container
```

* `-list <Application Attempt ID>`
* `-signal <container ID [signal command]>`
    * by default,  OUTPUT_THREAD_DUMP
    * OUTPUT_THREAD_DUMP
    * GRACEFUL_SHUTDOWN
    * FORCEFUL_SHUTDOWN
* `-status <Container ID>`
    * print status of the container

Output

* Container-Id
* Start Time
* Finish Time
* State
* Host
* Node Http Address
* LOG-URL

### node

```
yarn node <option>
```

* `-all`
    * use with `-list`
* `-showDetails`
    * use with `-list`
* `-list`
* `-state <States>`
    * use with `-list` to filter lists
    * `<States>` are comma-separated
    * NEW
    * RUNNING
    * UNHEALTHY
    * DECOMMISSIONED
    * LOST
    * REBOOTED
    * DECOMMISSIONING
    * SHUTDOWN
* `-status <NodeId>`
    * Prints the status report of the node

Output

* node id
* node state
* Node-Http-Address
* Number-of-Running-Containers

Usage

List all nodes

```
yarn node -all -list
```

### daemonlog

```
yarn dameonlog <option>
```

* `-getlevel <host:httpPort> <name>`
* `-setlevel <host:httpPort> <name> <level>`

## Usage
Show all applications

```
yarn application -list -appStates ALL
```

Show application attemps

```
yarn applicationattempt -list <appllication-id>
```

Show containers in applicationattempt

```
yarn container -list <applicationattempt-id>
```

Show (stdout/stderr) logs of applicationattempt

```
yarn logs -applicationId <application-id>
```

Show (stdout/stderr) logs of container

```
yarn logs -applicationId <application-id> -containerId <container-id>
```

Show application status

```
yarn application -status <application-id>
```


Show processes

```
yarn top
```

## Reference


