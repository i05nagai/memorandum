---
title: Tensorflow source code core
---

## Tensorflow source code core


* `FunctionLibraryDefinition`
    * operators
* `Arena`
    * This class is "thread-compatible": different threads can access the arena at the same time without locking, as long as they use only const methods.
* `ProfileNode`
    * core/profiler?
    * profiler node
* `EdgeSet`
    * `edgeset.h`
* `Const`
    * `const_op.h`
* `Const`
* `Scope`
    * `scope.h`
    * A `Scope` object represents a set of related TensorFlow ops that have thesame properties such as a common name prefix.
    * A Scope object is a container for TensorFlow Op properties. Op constructors get a Scope object as a mandatory first argument and the constructed op acquires the properties in the object.
    * has graph
    * `GetUniqueNameForOp`
* `Scope::Impl`
    * `scope_internal.h`
* `NodeDef`
* `Node`
    * `graph.h`
    * Need to call `Initialize` with NodeProperty, id, cost_id.
    * `in_edges_`
    * `out_edges_`
* `NodeBuilder`
    * `node_builder`
* `NodeDefBuilder`
    * `node_def_builder.h`
    * helper for creating `NodeDef`
* `NodeProperties`
    * `graph.cc`
    * Has `OpDef`, `NodeDef`, `DataTypeSlice` for inputs, `DataTypeSlice` for outputs
* `NodeOut`
* `OpDef`
* `StringPiece`
    * `stringpiece.h`
    * class for string slice?
* `Input`
    * `ops.h`
    * generated from Tensor, Output, a scalar
* `Output`
    * `ops.h`
    * Represents a tensor value produced by an Operation.
* `DataTypeVector`
    * `type.h`
    * `gtl::InlinedVector<DataType, 4>`
        * `DataType`
* `DataType`
    * `type.pb.h` ?
    * enum
* `ClientSession`
* `SessionOptions`
    * `session_options.h`
    * Has `Env`
    * Has `target`
        * `local`
        * `ip:host`
* `SessionFactory`
    * `session_factory.h`
* `DirectoSessionFactory`
    * `direct_session.h`
    * child of SessionFactory
* `DeviceFactory`
    * `device_factory.cc`
* `FactoryItem`
    * struct
  * Has `std::unique_ptr<DeviceFactory> factory;`
  * Has `int priority`
* `ThreadPoolDeviceFactory`
    * `threadpool_device_factory.cc`
    * for CPU
* `ThreadPoolDevice`
    * `threadpool_device.cc`
    * Instantiated by `TreadPoolDeviceFactory`
* `DeviceMgr`
    * `device_mgr.cc`
* `Env`
    * `env.h`




## Reference
