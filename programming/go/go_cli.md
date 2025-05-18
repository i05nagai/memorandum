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

## go vet

```
go vet [build flags] [-vettool prog] [vet flags] [packages]
```

`go tool vet help`

For more about vet and its flags, see 'go doc cmd/vet'.
For a list of checkers and their flags, see 'go tool vet help'.
For details of a specific checker such as 'printf', see 'go tool vet help printf'.

The -vettool=prog flag selects a different analysis tool with alternative or additional checks.
For example, the 'shadow' analyzer can be built and run using these commands:

```
go install golang.org/x/tools/go/analysis/passes/shadow/cmd/shadow@latest
go vet -vettool=$(which shadow)
```

The build flags supported by go vet are those that control package resolution and execution, such as -C, -n, -x, -v, -tags, and -toolexec.
For more about these flags, see 'go help build'.


## go fmt

## go fix

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
