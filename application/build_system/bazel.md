---
title: Bazel
---

## Bazel

* workspace
    * Directory contains `WORKSPACE` file
* package
    * a directory within the workspace that contains `BUILD` file

## Install
For OSX,

```
brew install bazel
```

For ubuntu 16.04

```
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install bazel
```

## Data type

```
# str
"string"
# list
[
  "v1",
  "v2",
  "v3",
]
# hash
{
    "key1": "v1",
    "key2": "v2",
    "key3": "v3",
}
```

## Target patterns
[Command\-Line Reference \- Bazel](https://docs.bazel.build/versions/master/command-line-reference.html#target-pattern-syntax)

All target patterns starting with `//` are resolved relative to the current workspace.

## Rules


### Docker
* [bitnami/bazel_containers: poc of bazel bitnami containers](https://github.com/bitnami/bazel_containers)
* [Building deterministic Docker images with Bazel - Bazel](https://blog.bazel.build/2015/07/28/docker_build.html)
* [base-images-docker/dockerfile_build at master · GoogleCloudPlatform/base-images-docker](https://github.com/GoogleCloudPlatform/base-images-docker/tree/master/dockerfile_build)
    * dockerfileのbuildのsample

Dockerfileを使ったbuildはgenruleを使う必要がある。


## Reference
* [bazelbuild/bazel: a fast, scalable, multi-language and extensible build system](https://github.com/bazelbuild/bazel)
* [Bazel - a fast, scalable, multi-language and extensible build system" - Bazel](https://bazel.build/)
* [Benchmarking the Bazel build system on real-life C++ - Nicolò Valigi](https://nicolovaligi.com/benchmark-bazel-build-cpp.html)

