---
title: Tensorflow
---

## Tensorflow


## Build with bazel
* [C\+\+ API  \|  TensorFlow](https://www.tensorflow.org/api_guides/cc/guide)

* 1. `git clone `
* 2. `mkdir tensorflow/workspace`
* 3.  Create `tensorflow/workspace/BUILD` and save with

```bzl
load("//tensorflow:tensorflow.bzl", "tf_cc_binary")

tf_cc_binary(
    name = "workspace",
    srcs = ["code.cc"],
    copts = [
            "-O3",
            "-g",
            ],
    deps = [
        "//tensorflow/cc:cc_ops",
        "//tensorflow/cc:client_session",
        "//tensorflow/core:tensorflow",
    ],
)
```

* 4. Implement in `tensorflow/workspace/code.cc`

```cpp
#include "tensorflow/cc/client/client_session.h"
#include "tensorflow/cc/ops/standard_ops.h"
#include "tensorflow/core/framework/tensor.h"

int main() {
  using namespace tensorflow;
  using namespace tensorflow::ops;
  Scope root = Scope::NewRootScope();
  // Matrix A = [3 2; -1 0]
  auto A = Const(root, { {3.f, 2.f}, {-1.f, 0.f} });
  // Vector b = [3 5]
  auto b = Const(root, { {3.f, 5.f} });
  // v = Ab^T
  auto v = MatMul(root.WithOpName("v"), A, b, MatMul::TransposeB(true));
  std::vector<Tensor> outputs;
  ClientSession session(root);
  // Run and fetch v
  TF_CHECK_OK(session.Run({v}, &outputs));
  // Expect outputs[0] == [19; -3]
  LOG(INFO) << outputs[0].matrix<float>();
  return 0;
}
```

* 5. Build your code with

```
# in root of tensorflow repository
# for debugging
bazel build --copt "-g" //tensorflow/workspace
bazel run //tensorflow/workspace
```

## Examples
* [tensorflow\-cpp/app\.cc at master · jhjin/tensorflow\-cpp](https://github.com/jhjin/tensorflow-cpp/blob/master/app.cc)
* [tensorflow/models: Models and examples built with TensorFlow](https://github.com/tensorflow/models)

## Reference
* [A few notes on using the Tensorflow C\+\+ API](https://jacobgil.github.io/deeplearning/tensorflow-cpp)
