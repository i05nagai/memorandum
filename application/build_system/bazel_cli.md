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

* Inherits all options from `bazel build`.
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
bazel coverage <target>
```

* Inherits all options from `bazel test`.
* For c++ coverage report, you need to install
    * `lcov`
    * `gcov`
* log file
    * log files are generated in `bazel-testlogs/.../test.log`
* coverage
    * coverage report are generated in `bazel-testlogs/.../coverage.dat`
        * lcov coverage data
* `--coverage_support=<a build target label>`
    * Location of support files that are required on the inputs of every test action that collects code coverage. Defaults to '//tools/test: coverage_support'. 
* `--coverage_report_generator=<a build target label>`
    * Location of the binary that is used to generate coverage reports.
    * This must currently be a filegroup that contains a single file, the binary. Defaults to '//tools/test:coverage_report_generator'. 
* `--[no]collect_code_coverage`
    * (a boolean; default: "false")
    * If specified, Bazel will instrument code (using offline instrumentation where possible) and will collect coverage information during tests.
    * Only targets that match `--instrumentation_filter` will be affected.
    * Usually this option should not be specified directly - 'bazel coverage' command should be used instead. 
* `--[no]experimental_cc_coverage`
    * (a boolean; default: "false")
    * If specified, Bazel will use gcov to collect code coverage for C++ test targets.
    * This option only works for gcc compilation.
* `--[no]experimental_java_coverage`
    * (a boolean; default: "false")

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
