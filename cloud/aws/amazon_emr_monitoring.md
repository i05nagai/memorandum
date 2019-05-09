---
title: Amazon EMR Monitoring
---

## Amazon EMR Monitoring


## Metrics

- MissingBlocks
    - The number of blocks in which HDFS has no replicas. These might be corrupt blocks.
    - Use cases: Monitor cluster health
- CapacityRemainingGB
    - The amount of remaining HDFS disk capacity.
    - Use cases: Monitor cluster progress, Monitor cluster health
- MRUnhealthyNodes
    - The number of nodes available to MapReduce jobs marked in an UNHEALTHY state.
    - Equivalent to YARN metric `mapred.resourcemanager.NoOfUnhealthyNodes`.
    - Use cases: Monitor cluster progress
- MRTotalNodes
    - the number of nodes presently available to MR jobs
    - Equivalent to YARN metrics `mapred.resourcemanager.TotalNodes.`
- HDFSUtilization
    - The percentage of HDFS storage currently used
- MemoryTotalMB
    - The total amount of memory in the cluster.
    - Monitor cluster progress
- MemoryReservedMB
- MemoryAvailableMB
- YARNMemoryAvailablePercentage
    - MemoryAvailableMB / MemoryTotalMB
- MemoryAllocatedMB
    - The amount of memory allocated to the cluster
- TotalLoad
    - The current, total number of readers and writers reported by all DataNodes in a cluster.
- HDFSBytesRead
- HDFSBytesWritten
- MemoryTotalMB


Dimenstion

- JobFlowId
    - cluster ID
- JobId
    - The identifier of a job within a cluster

## Reference
- [Monitor Metrics with CloudWatch \- Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.html)
