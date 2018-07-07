---
title: Tensorflow source code core
---

## Tensorflow source code core


* `FunctionLibraryDefinition`
    * operators
* `Arena`
    * This class is "thread-compatible": different threads can access the arena at the same time without locking, as long as they use only const methods.
* `NodeDef`
* `ProfileNode`
    * core/profiler?
    * profiler node
* `Node`
    * `graph.h`
* `EdgeSet`
    * `edgeset.h`

## Reference
