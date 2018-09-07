---
title: Bazel Configuration
---

## Bazel Configuration

## General
* genrule
    * `cmd`のcommandを実行
    * `name`
    * `srcs`
        * `$<`で指定したファイルを参照できる
    * `outs`
        * `$@`で指定したファイルを参照できる
    * `executable`
        * 出力が実行ファイルなら1
    * `output_to_bindir`
        * `bazel-bin` directoryに出力するなら1
    * `cmd`

```
genrule(
  name = "hello",
  srcs = [
    "hello.c",
  ],
  outs = [
    "hello",
  ],
  executable = 1,
  output_to_bindir = 1,
  cmd = "gcc $< -O2 -o $@",
)
```

* `local_repository`
    * remote dependency

```
// You can refer @coworkers_project//foo:bar
local_repository(
    name = "coworkers_project",
    path = "/path/to/coworkers-project",
)
```

* `git_repository`
    * remote dependency
* `http_archive`
    * remote dependency

* `new_local_repository`
    * remote non bazel project
* `new_git_repository`
    * remote non bazel project
* `new_http_archive`
    * remote non bazel project
    * `name`
    * `build_file`
        * The file to use as the BUILD file for this repository.  Either build_file or build_file_content must be specified.
    * `strip_prefix`
        * 

* `exports_files`
    * specifies a list of files belonging to this package that are exported to other packages but not otherwise mentioned in the BUILD file.

### C/C++

```
```

## Directory structure


## Reference
* [Functions \- Bazel](https://docs.bazel.build/versions/master/be/functions.html#exports_files)
* [Workspace Rules \- Bazel](https://docs.bazel.build/versions/master/be/workspace.html)
