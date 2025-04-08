---
title: go CLI
---

## go CLI

## clean
* `-i`
    * delete installed archive/binary
* `-n`
    * dry-run

## doc

```
go doc [-u] [-c] [package|[package.]symbol[.methodOrField]]
```

* -c
    * symbol matching honors case (paths not affected)
* -cmd
    * show symbols with package docs even if package is a command
* -u
    * show unexported symbols as well as exported

## tool

```
go tool [-n] command [args...]
```

- `-n`
    - dry run


## go generate
To convey to humans and machine tools that code is generated, generated source should have a line that matches the following regular expression (in Go syntax):

```
        ^// Code generated .* DO NOT EDIT\.$
```


### Usage
Show documentation for current package

```
go doc
```

## Tips


go getでgetしたものを削除

```
go get github.com/prasmussen/gdrive
```

の場合以下で削除のdry-run.
`-n`を抜けば実行する。

```
go clean -i -n github.com/prasmussen/gdrive
```


## Reference
* [Removing packages installed with go get - Stack Overflow](https://stackoverflow.com/questions/13792254/removing-packages-installed-with-go-get)
