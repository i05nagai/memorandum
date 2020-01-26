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
# you may need java8
brew cask install homebrew/cask-versions/java8
```

However, [for some reasons](https://blog.bazel.build/2018/08/22/bazel-homebrew.html), bazel in homebrew core is not updated anymore.
If you want the latest bazel, you need to add a tap maintained by bazel developers

```
# uninstall bazel of homebrew core
brew uninstall bazel
# tap and install
brew tap bazelbuild/tap
brew tap-pin bazelbuild/tap
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
* [Command\-Line Reference \- Bazel](https://docs.bazel.build/versions/master/command-line-reference.html#target-pattern-syntax)
* [Concepts and Terminology \- Bazel](https://docs.bazel.build/versions/master/build-ref.html#name)

All target patterns starting with `//` are resolved relative to the current workspace.

* `<package>:<target>`
* `//foo/bar:wiz`
    * Just the single target '//foo/bar:wiz'.
* `//foo/bar`
    * Equivalent to '//foo/bar:bar'.
* `//foo/bar:all`
    * All rules in the package 'foo/bar'.
* `//foo/...`
    * All rules in all packages beneath the directory 'foo'.
* `//foo/...:all`
    * All rules in all packages beneath the directory 'foo'.
* `//foo/...:*`
    * All targets (rules and files) in all packages beneath the directory 'foo'.
* `//foo/...:all-targets`
    * All targets (rules and files) in all packages beneath the directory 'foo'.
* `@<package-name>`

## Rules
[bazel/tools/build\_defs/repo at master · bazelbuild/bazel](https://github.com/bazelbuild/bazel/tree/master/tools/build_defs/repo)


#### genrule
- [Make Variables \- Bazel](https://docs.bazel.build/versions/master/be/make-variables.html)


### Docker
* [bitnami/bazel_containers: poc of bazel bitnami containers](https://github.com/bitnami/bazel_containers)
* [Building deterministic Docker images with Bazel - Bazel](https://blog.bazel.build/2015/07/28/docker_build.html)
* [base-images-docker/dockerfile_build at master · GoogleCloudPlatform/base-images-docker](https://github.com/GoogleCloudPlatform/base-images-docker/tree/master/dockerfile_build)
    * dockerfileのbuildのsample

Dockerfileを使ったbuildはgenruleを使う必要がある。


## Tips

### Measuring coverage
Use `bazel coverage`.

## Reference
* [bazelbuild/bazel: a fast, scalable, multi-language and extensible build system](https://github.com/bazelbuild/bazel)
* [Bazel - a fast, scalable, multi-language and extensible build system" - Bazel](https://bazel.build/)
* [Benchmarking the Bazel build system on real-life C++ - Nicolò Valigi](https://nicolovaligi.com/benchmark-bazel-build-cpp.html)

