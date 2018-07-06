---
title: Bazel CLI
---

## Bazel CLI


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
    * pass to complier
    * e.g. `--copt="-g0" --copt="-fpic"`

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

## Configuration

## Reference
