---
title: Concurrency
---

## Concurrency


## Coffman condition
Deadlocks happen if and only if the following four conditions satisfy

- (1) Mutual Exclusion:
    - Tasks claim exclusive control of the resources they require 
    - (i.e. No two processes can obtain a resource at the same time.)
- (2) Circular Wait:
    -  A circular chain of tasks exists, such that each task holds one or more resources that are being requested by the next task in the chain 
    - (i.e. A circular chain of tasks exists, such that each task holds one or more resources that are being requested by the next task in the chain)
- (3) Hold and Wait:
    - Once a resource is obtained, a process keeps the resource locked.
    - (i.e. Tasks hold resources already allocated to them while waiting for additional resources)
- (4)No pre-emption:
    - Nothing can force the process to give up a resource.

### Resource Allocation Graph
- If a process is using a resource, an arrow is drawn from the resource node to the process node. I
- If a process is requesting a resource, an arrow is drawn from the process node to the resource node.
- If there is a cycle in the Resource Allocation Graph and each resource in the cycle provides only one instance, then the processes will deadlock.


## Reference
- https://cs341.cs.illinois.edu/coursebook/Deadlock
