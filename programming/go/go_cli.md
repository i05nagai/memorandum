---
title: go CLI
---

## go CLI

## build


-C dir
        Change to dir before running the command.
        Any files named on the command line are interpreted after
        changing directories.
        If used, this flag must be the first one in the command line.

- `-a`
    - force rebuilding of packages that are already up-to-date.
- `-n`
    - print the commands but do not run them.
- `-p n`
    - the number of programs, such as build commands or test binaries, that can be run in parallel.
    - The default is GOMAXPROCS, normally the number of CPUs available.
- `-race`
    - enable data race detection.
    - Supported only on linux/amd64, freebsd/amd64, darwin/amd64, darwin/arm64, windows/amd64, linux/ppc64le and linux/arm64 (only for 48-bit VMA).
- `-msan`
    - enable interoperation with memory sanitizer.
    - Supported only on linux/amd64, linux/arm64, linux/loong64, freebsd/amd64 and only with Clang/LLVM as the host C compiler.
    - PIE build mode will be used on all platforms except linux/amd64.
- `-asan`
    - enable interoperation with address sanitizer.
    - Supported only on linux/arm64, linux/amd64, linux/loong64.
    - Supported on linux/amd64 or linux/arm64 and only with GCC 7 and higher or Clang/LLVM 9 and higher.
    - And supported on linux/loong64 only with Clang/LLVM 16 and higher.
- `-cover`
    - enable code coverage instrumentation.
- `-covermode set,count,atomic`
    - set the mode for coverage analysis.
    - The default is "set" unless -race is enabled, in which case it is "atomic".
    - The values:
        - set: bool: does this statement run?
        - count: int: how many times does this statement run?
        - atomic: int: count, but correct in multithreaded tests; significantly more expensive.
        - Sets -cover.
- `-coverpkg pattern1,pattern2,pattern3`
    - For a build that targets package 'main' (e.g. building a Go executable), apply coverage analysis to each package whose import path matches the patterns.
    - The default is to apply coverage analysis to packages in the main Go module.
    - See 'go help packages' for a description of package patterns.
    - Sets -cover.
- `-v`
    - print the names of packages as they are compiled.
- `-work`
    - print the name of the temporary work directory and do not delete it when exiting.
- `-x`
    - print the commands.
- `-asmflags '[pattern=]arg list'`
    - arguments to pass on each go tool asm invocation.
- `-buildmode mode`
    - build mode to use. See 'go help buildmode' for more.
- `-buildvcs`
    - Whether to stamp binaries with version control information ("true", "false", or "auto"). By default ("auto"), version control information is stamped into a binary if the main package, the main module containing it, and the current directory are all in the same repository.
    - Use -buildvcs=false to always omit version control information, or -buildvcs=true to error out if version control information is available but cannot be included due to a missing tool or ambiguous directory structure.
- `-compiler name`
    - name of compiler to use, as in runtime.Compiler (gccgo or gc).
- `-gccgoflags '[pattern=]arg list'`
    - arguments to pass on each gccgo compiler/linker invocation.
- `-gcflags '[pattern=]arg list'`
    - arguments to pass on each go tool compile invocation.
- `-installsuffix suffix`
    - a suffix to use in the name of the package installation directory, in order to keep output separate from default builds.
    - If using the -race flag, the install suffix is automatically set to race or, if set explicitly, has _race appended to it.
    - Likewise for the -msan and -asan flags. Using a -buildmode option that requires non-default compile flags has a similar effect.
- `-json`
    - Emit build output in JSON suitable for automated processing.
    - See 'go help buildjson' for the encoding details.
- `-ldflags '[pattern=]arg list'`
    - arguments to pass on each go tool link invocation.
- `-linkshared`
    - build code that will be linked against shared libraries previously created with -buildmode=shared.
- `-mod mode`
    - module download mode to use: readonly, vendor, or mod.
    - By default, if a vendor directory is present and the go version in go.mod is 1.14 or higher, the go command acts as if -mod=vendor were set.
    - Otherwise, the go command acts as if -mod=readonly were set.
    - See https://golang.org/ref/mod#build-commands for details.
- `-modcacherw`
    - leave newly-created directories in the module cache read-write instead of making them read-only.
- `-modfile file`
    - in module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the module root directory.
    - A file named "go.mod" must still be present in order to determine the module root directory, but it is not accessed. When -modfile is specified, an alternate go.sum file is also used: its path is derived from the -modfile flag by trimming the ".mod" extension and appending ".sum".
- `-overlay file`
    - read a JSON config file that provides an overlay for build operations.
    - The file is a JSON struct with a single field, named 'Replace', that maps each disk file path (a string) to its backing file path, so that a build will run as if the disk file path exists with the contents given by the backing file paths, or as if the disk file path does not exist if its backing file path is empty.
    - Support for the -overlay flag has some limitations: importantly, cgo files included from outside the include path must be in the same directory as the Go package they are included from, and overlays will not appear when binaries and tests are run through go run and go test respectively.
- `-pgo file`
    - specify the file path of a profile for profile-guided optimization (PGO).
    - When the special name "auto" is specified, for each main package in the build, the go command selects a file named "default.pgo" in the package's directory if that file exists, and applies it to the (transitive) dependencies of the main package (other packages are not affected).
    - Special name "off" turns off PGO. The default is "auto".
- `-pkgdir dir`
    - install and load all packages from dir instead of the usual locations.
    - For example, when building with a non-standard configuration, use -pkgdir to keep generated packages in a separate location.
- `-tags tag,list`
    - a comma-separated list of additional build tags to consider satisfied during the build.
    - For more information about build tags, see 'go help buildconstraint'. (Earlier versions of Go used a space-separated list, and that form is deprecated but still recognized.)
- `-trimpath`
    - remove all file system paths from the resulting executable.
    - Instead of absolute file system paths, the recorded file names will begin either a module path@version (when using modules), or a plain import path (when using the standard library, or GOPATH).
- `-toolexec 'cmd args'`
    - a program to use to invoke toolchain programs like vet and asm.
    - For example, instead of running asm, the go command will run 'cmd args /path/to/asm <arguments for asm>'.
    - The TOOLEXEC_IMPORTPATH environment variable will be set, matching 'go list -f {{.ImportPath}}' for the package being built.


## env
Env prints Go environment information.

By default env prints information as a shell script (on Windows, a batch file). If one or more variable names is given as arguments, env prints the value of each named variable on its own line.


```
usage: go env [-json] [-changed] [-u] [-w] [var ...]
```

- `-u`
    - The -u flag requires one or more arguments and unsets the default setting for the named environment variables, if one has been set with 'go env -w'.
- `-w`
    - write environment variables to the go env configuration file
    - The -w flag requires one or more arguments of the form NAME=VALUE and changes the default settings of the named environment variables to the given values.
- `-changed`
    - The -changed flag prints only those settings whose effective value differs from the default value that would be obtained in an empty environment with no prior uses of the -w flag.
- `-json`
    - The -json flag prints the environment in JSON format instead of as a shell script.



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
