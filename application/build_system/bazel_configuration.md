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

## Conditional build rule
* https://docs.bazel.build/versions/master/configurable-attributes.html#defaults


## Function
* [Functions \- Bazel](https://docs.bazel.build/versions/master/be/functions.html#exports_files)

* `licenses(license_types)`
* `exports_files([label, ...], visibility, licenses)`
* `glob(include, exclude=[], exclude_directories=1)`
* `select`
    * makes a rule attribute configurable
    * debug/release build
    * control conditional execution by CLI options and `config_setting`

```
select(
    {conditionA: valuesA, conditionB: valuesB, ...},
    no_match_error = "custom message"
)
# bazel build //pkg:target --crosstool_top=//crosstoolsw/windows
config_setting(
    name = "conditionA",
    values = {
        "crosstool_top": "//crosstools/windows",
    },
)
# bazel build //pkg:target --crosstool_top=//crosstools/darwin
config_setting(
    name = "conditionB",
    values = {
        "crosstool_top": "//crosstools/darwin",
    },
)
# usage
sh_binary(
    name = "myrule",
    srcs = select({
        ":conditionA": ["myrule_a.sh"],
        ":conditionB": ["myrule_b.sh"],
        "//conditions:default": ["myrule_default.sh"]
    })
)
```

## Label
https://docs.bazel.build/versions/master/skylark/lib/Label.html#Label

* `Label("//tools:default")`
    * parse target
    * `Label("//pkg/foo:abc").name == "abc"`
    * `str(Label("//pkg/foo:abc")) == "abc"`
    * `Label("//pkg/foo:abc").package == "pkg/foo"`
    * `Label("//foo/bar:baz").relative(":quux") == Label("//foo/bar:quux")`
    * `Label("@repo//pkg/foo:abc").workspace_root == "external/repo"`


## Reference
* [Workspace Rules \- Bazel](https://docs.bazel.build/versions/master/be/workspace.html)
