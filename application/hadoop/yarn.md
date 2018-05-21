---
title: yarn
---

## yarn
CLI for Apache Hadoop YARN.

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

```
usage: yarn logs -applicationId <application ID> [OPTIONS]

general options are:
 -am <AM Containers>             Prints the AM Container logs for this
                                 application. Specify comma-separated
                                 value to get logs for related AM
                                 Container. For example, If we specify -am
                                 1,2, we will get the logs for the first
                                 AM Container as well as the second AM
                                 Container. To get logs for all AM
                                 Containers, use -am ALL. To get logs for
                                 the latest AM Container, use -am -1. By
                                 default, it will only print out syslog.
                                 Work with -logFiles to get other logs
 -appOwner <Application Owner>   AppOwner (assumed to be current user if
                                 not specified)
 -containerId <Container ID>     ContainerId. By default, it will only
                                 print syslog if the application is
                                 runing. Work with -logFiles to get other
                                 logs.
 -help                           Displays help for all commands.
 -logFiles <Log File Name>       Work with -am/-containerId and specify
                                 comma-separated value to get specified
                                 container log files. Use "ALL" to fetch
                                 all the log files for the container.
 -nodeAddress <Node Address>     NodeAddress in the format nodename:port
```

## Usage
Show applications

```
yarn application -list
```

Show processes

```
yarn top
```

## Reference


