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

### C/C++

```
```

## Directory structure


## Reference
