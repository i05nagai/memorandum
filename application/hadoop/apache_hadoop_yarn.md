---
title: Apache Hadoop YARN
---

## Apache Hadoop YARN
The fundamental idea of YARN is to split up the functionalities of resource management and job scheduling/monitoring into separate daemons.

* global ResourceManager (RM)
* per-application ApplicationMaster (AM)

## Concepts
* application
    * either a single job or a DAG of jobs.
* ResourceManager
    * the ultimate authority that arbitrates resources among all the applications in the system
    * components
        * Scheduler
        * ApplicationsManager
* Scheduler
    * allocating resources to the various running applications subject to familiar constraints of capacities, queues etc.
    * pure scheduler in the sense that it performs no monitoring or tracking of status for the application
    * it offers no guarantees about restarting failed tasks either due to application failure or hardware failures
    * based on the abstract notion of a resource Container which incorporates elements such as memory, cpu, disk, network etc.
    * scheduler is pluggable
        * CapacityScheduler 
        * FairScheduler
* ApplicationManager
    * responsible for accepting job-submissions, negotiating the first container for executing the application specific ApplicationMaster
    * provides the service for restarting the ApplicationMaster container on failure
* ApplicationMaster
    * responsibility of negotiating appropriate resource containers from the Scheduler, tracking their status and monitoring for progress.
* YARN Timeline Server
    * [Apache Hadoop 2.8.2 – The YARN Timeline Server](https://hadoop.apache.org/docs/r2.8.2/hadoop-yarn/hadoop-yarn-site/TimelineServer.html)
    * Persisting application specifc information
    * persisting 
* NodeManager
    * per-machine framework
    * responsible for containers, monitoring their resource usage (cpu, memory, disk, network)
    * reporting the same to the ResourceManager/Scheduler.


## Reference
* [Apache Hadoop 2.9.1 – Apache Hadoop YARN](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html)
