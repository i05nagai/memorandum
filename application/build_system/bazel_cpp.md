---
title: Bazel cpp
---

## Bazel cpp

* `cc_library`
    * `name`
    * `srcs`
        * list of sources
    * `hdrs`
        * list of headers
    * `visibility`


```
cc_library(
    name = "hello-greet",
    srcs = ["hello-greet.cc"],
    hdrs = ["hello-greet.h"],
)
```

* `cc_binary`

```
cc_binary(
    name = "hello-world",
    srcs = ["hello-world.cc"],
    deps = [
        ":hello-greet",
    ],
    copts = ["-O2"],
)
```

## Example
Example repository

```
git clone https://github.com/bazelbuild/examples/
```

```
bazel build //main:hello-world
```

## Reference
* [Build Tutorial \- C\+\+ \- Bazel](https://docs.bazel.build/versions/master/tutorial/cpp.html)
