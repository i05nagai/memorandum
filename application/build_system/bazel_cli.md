---
title: Bazel CLI
---

## Bazel CLI
You can query with `bazel query` command.

## CLI
```
<target name>
:<target name>
//<package name>
//<package name>:<target name>
```

Builds the specified targets.

```
bazel build //<package name>:<target name>
```

* `-c opt`
    * Use optimized builds for C++ code
* `--copt cc-option`
    * pass to gcc complier
    * e.g. `--copt="-g0" --copt="-fpic"`
* `--cxxopt=<a string>`
* `--host_cxxopt=<a string>`
    * Additional options to pass to gcc for host tools. 


```
bazel test
```

* `--copt -g`
* `--compilation_mode=fastbuild|opt|dbg`
    * `fastbuild`
        * `-gmlt -Wl,-S`
    * `opt`
        * `-O2 -DNDEBUG`
    * `dbg`
* `--test_output=errors|all`
    * `errors`
        * show the output from failed tests
    * `all`
        * show you the outputs from all the tests
* `--collect_code_coverage`
    * run gcov
    * https://github.com/bazelbuild/bazel/issues/1118
    * https://github.com/bazelbuild/bazel/issues/5128
        * 0.15.2 has problems, but it will be fixed in 0.16

```
bazel clean
```

```
bazel run //<package name>:<target name>
```

Fetches external repositories that are prerequisites to the targets.

```
bazel fetch
```

Analyzes build profile data.

```
bazel analyze-profile
```

Canonicalizes a list of bazel options.

```
bazel canonicalize-flags
```

Removes output files and optionally stops the server.

```
bazel clean
```

Generates code coverage report for specified test targets.

```
bazel coverage
```

* c++
    * lcov is needed

Loads, analyzes, and queries the specified targets w/ configurations.

```
bazel cquery
```

Dumps the internal state of the bazel server process.

```
bazel dump
```

Displays runtime info about the bazel server.

```
bazel info
```

Prints the license of this software.

```
bazel license
```

Installs targets to mobile devices.

```
bazel mobile-install
```

Prints the command line args for compiling a file.

```
bazel print_action
```

Executes a dependency graph query.

```
bazel query
```

Runs the specified target.

```
bazel run
```

Stops the bazel server.

```
bazel shutdown
```

Builds and runs the specified test targets.

```
bazel test
```

## Usage
[bazel query 'foo/\.\.\.' \-\-output package](https://docs.bazel.build/versions/master/query-how-to.html#What_packages_exist_beneath_foo_)

```
bazel query 
```

## Configuration

## Reference
