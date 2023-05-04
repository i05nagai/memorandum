---
title: Apache Flink Metrics
---

## Apache Flink Metrics


## Tasks
https://nightlies.apache.org/flink/flink-docs-master/docs/ops/metrics/

- inputFloatingBuffersUsage
    - An estimate of the floating input buffers usage. (ignores LocalInputChannels)
    - If an input is floating, it will be "high impedance"
- outPoolUsage
    - An estimate of the output buffers usage. The pool usage can be > 100% if overdraft buffers are being used.
- Metaspace.Used
    - The amount of memory currently used in the Metaspace memory pool (in bytes).
- Direct.MemoryUsed	
    - The amount of memory used by the JVM for the direct buffer pool (in bytes).
- Managed.Used	
    - The amount of managed memory currently used.
- Mapped.MemoryUsed	
    - The amount of memory used by the JVM for the mapped buffer pool (in bytes).
- NonHeap.Max	
    - The maximum amount of non-heap memory that can be used for memory management (in bytes).
- AvailableMemorySegments
    - The number of unused memory segments.	
- ClassesLoaded
    - The total number of classes loaded since the start of the JVM.

## Reference
- https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/ops/metrics/
