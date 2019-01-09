---
title: Tensorflow source code core
---

## Tensorflow source code core

* `PerPartitionExecutorsAndLib`
    * DirectSession
* `ExecutorsAndKeys`
* `Session`
* `DirectSession`
    * `DirectSession::CreateExecutors`
    * `DirectSession::CreateGraphs`
* `GraphExecutionState`
    * `graph_execution_state.h`
    * `GraphExecutionState::BuildGraph`
    * `GraphExecutionState::OptimizeGraph`
    * `static GraphExecutionState::MakeForPrunedGraph`
    * `static GraphExecutionState::MakeForBaseGraph`
        * Call `GraphExecutionState::InitBaseGraph`
    * `GraphExecutionState::InitBaseGraph`
        * `ConvertGraphDefToGraph`

* `TensorStore`
    * `session_state.h`
    * `std::unordered_map<string, TensorAndKey> tensors_`
        * a map from tensor string to tensor
* `Tensor`
* `TTypes<typename T, int NDIMS = 1, typename IndexType = Eigen::DenseIndex>`
    * `tensor_types.h`

* `Executor`
    * `executor.h`
* `ExecutorBarrier`
    * A class to help run multiple executors in parallel and wait until all of them are complete.
    * `executor.h`
* `ExecutorFactory`
    * `executor_factory.h`

* `ConvertGraphDefToGraph`
    * `graph_constructor.cc`
* `GraphConstructor`
    * `Graph* g_`
    * `graph_constructor.cc`
    * `GraphConstructor::TryImport`
    * `GraphConstructor::MakeNode`
        * Make node from `NodeDef`
    * `GraphConstructor::MakeEdge`
        * Make node from `EdgeDef`
* `Graph`
    * `Graph::AllocateNode`
        * Call `Node::Initialize` for actual initializaiton
    * `Graph::AddControlEdge`
    * `Graph::AddEdge`
* `Node`
    * `Node::Initialize`
    * `Node::GetNodeClassForOp`
    * `Node::kNodeClassTable`
* `NodeClass`
    * enum to label the type of the node


* `InOutTypesForNode`
    * `node_def_util.cc`
* `AddArgToSig`
    * `node_def_util.cc`
* `GetNodeAttr(`

* `grappler::GrapplerItem`

* `OpRegistrationDataFactory`
* `OpRegistry::RegisterAlreadyLocked`
    * Create `OpDef` by calling `OpRegistrationDataFactory`
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
    * `types.pb.h`
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
* `Env`
    * `env.h`

## Tape
* `TensorTape = gtl::FlatMap<int64, int64>`
    * Map from tensor_id to internally-defined operation-id of the operation which produced this tensor.
    * A value of -1 means that the tensor was directly watched and not the result of any operation in the tape.
    * `c/eager/tape.h`
* `OpTape`
    * `c/eager/tape.h`

## Session

## Device
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


## test
* `test::graph::Var`
    * `core/graph/testlib.h`


## OpKernel
* `OpKernel`
* `VariableOp`
    * `variable_ops.h`
* `ApplyGradientDescentOp`
    * `training_ops.cc`
* `GetInputTensorFromVariable`
    * `training_op_helpers.h`
* `functor::ApplyGradientDescent<Device, T>()`
    * `training_ops.cc`
* `OpKernelConstruction`
* `OpKernelContext`
    * `op_kernel.h`


## Registered Operators
* `Variable`
    * `state_ops.h`


## cc
* `Output`
    * ops.h
* `Operation`
    * ops.h

## Reference
* [Adding a New Op  \|  TensorFlow](https://www.tensorflow.org/guide/extend/op)
