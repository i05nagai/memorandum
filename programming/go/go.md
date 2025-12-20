---
title: Go
---

## Go

## Install
For ubuntu
* [Ubuntu · golang/go Wiki](https://github.com/golang/go/wiki/Ubuntu)

```
sudo apt-get install golang-go
```

or

```
$ sudo add-apt-repository ppa:gophers/archive
$ sudo apt-get update
$ sudo apt-get install golang-1.10-go
$ sudo apt-get install golang-1.10-go
$ echo 'export PATH="/usr/lib/go-1.10/bin:$PATH"' >> ~/.zshrc
```


For OSX

```
brew install go
```

```
sudo apt-get install golang-1.8-go
```

From tar

```
curl -L -O https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.9.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
export GOPATH="/opt/local/go"
```

## Package manager
* [PackageManagementTools · golang/go Wiki · GitHub](https://github.com/golang/go/wiki/PackageManagementTools)

`dep`が一応officialのpackage manager

* `$GOPATH`
    * defaultはgo 1.8から`$HOME/go`


## API server
* [7 Frameworks To Build A REST API In Go | Nordic APIs |](https://nordicapis.com/7-frameworks-to-build-a-rest-api-in-go/)

## Packaging
* variables in a package is initialized when the package is imported
    * [Effective Go - The Go Programming Language](https://golang.org/doc/effective_go.html#init)
* `func init()` in a file is used for initializing a package
    * is called after all the variable declarations in the package have evaluated their initializers, and those are evaluated only after all the imported packages have been initialized.


## Enum
`iota` operator

```go
const (
    _           = iota // ignore first value by assigning to blank identifier
    KB float64  = 1 << (10 * iota)
    MB
    GB
    TB
    PB
    EB
    ZB
    YB
)
```

## Naming convention
https://appliedgo.net/spotlight/conventions-in-go/

- Functions that panic should have “Must” in their name

* package name
    * lower case
    * `src/encoding/base64`
    * `encoding/base64`
    * mixedCap or underscore
        * [Package names \- The Go Blog](https://blog.golang.org/package-names)

## Method
* recieverを定義できるのは`type`で定義した型だけ
* 同じpackage内で宣言されている必要がある
* recieverがpointer typeの場合はrecieverの値を買い換えることができる

```go
func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}
```

Type assert

* interfaceが(string)型をもっていればcastできる
* interfaceが(string)型をもっていればcastできなければ、panic
* second return valueをつけた場合はpanicにはならない

```go
	var i interface{} = "hello"

	s := i.(string)
	fmt.Println(s)

	s, ok := i.(string)
	fmt.Println(s, ok)
```
Type switch

```go
	switch v := i.(type) {
	case int:
		fmt.Printf("Twice %v is %v\n", v, v*2)
	case string:
		fmt.Printf("%q is %v bytes long\n", v, len(v))
	default:
		fmt.Printf("I don't know about type %T!\n", v)
	}
```

```
type MyStruct struct {

}

// sum of interface
type ErrorWithErrorMessage interface {
	error
	errorMessager
}
```

## Tips

### Project structure Standard 
* [golang\-standards/project\-layout: Standard Go Project Layout](https://github.com/golang-standards/project-layout)


* `/cmd/`
    * main applicatoin
    * executables
* `/internal/`
    * private applicatoin and library code
    * `app/`
    * `pkg/`
* `/pkg/`
    * library code used by external application
* `/vendor/`
    * application dependency
* `/api/`
    * open API/Swagger
    * protocol definition
    * json schema file
* `/web/`
    * web applicatoin specific
    * static web assets
    * server side template
    * SPA
* `/configs/`
* `/init/`
* `/scripts/`
* `/build/`
    * `ci/`
        * scripts for ci
* `/deployments/`
    * e.g. docker-compose, kubernetes/helm, mesos, terraform
* `/test/`
    * `data/`
* `/docs/`
* `/tools/`
* `/examples/`
* `/third_party/`
* `/githooks/`
* `/assets/`


`src/` is not needed.


## Conventions
https://go.dev/doc/effective_go#names

- pacakge name
- interface name
    - one-method interfaces are named by the method name plus an -er suffix or similar modification to construct an agent noun: Reader, Writer, Formatter, CloseNotifier etc.
- Finally, the convention in Go is to use MixedCaps or mixedCaps rather than underscores to write multiword names.
    
### nil in pointer
https://go.dev/doc/faq#nil_error

```

```

### How can I guarantee my type satisfies an interface?¶

```go
type T struct{}
var _ I = T{}       // Verify that T implements I.
var _ I = (*T)(nil) // Verify that *T implements I.
```

### Defer

```go
func b() {
    for i := 0; i < 4; i++ {
        defer fmt.Print(i)
    }
}
// Output: 3210
```

```go
func c() (i int) {
    defer func() { i++ }()
    return 1
}
// Output: 2

func c() (i int) {
    i = 4
    defer func() { i++ }()
    return 1
}
// Output: 2
```

### Defer, Panic, and Recover
https://go.dev/blog/defer-panic-and-recover

```go
package main

import "fmt"

func main() {
    f()
    fmt.Println("Returned normally from f.")
}

func f() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered in f", r)
        }
    }()
    fmt.Println("Calling g.")
    g(0)
    fmt.Println("Returned normally from g.")
}

func g(i int) {
    if i > 3 {
        fmt.Println("Panicking!")
        panic(fmt.Sprintf("%v", i))
    }
    defer fmt.Println("Defer in g", i)
    fmt.Println("Printing in g", i)
    g(i + 1)
```

```go
// jsonError is an error wrapper type for internal use only.
// Panics with errors are wrapped in jsonError so that the top-level recover
// can distinguish intentional panics from this package.
type jsonError struct{ error }

func (e *encodeState) marshal(v any, opts encOpts) (err error) {
	defer func() {
		if r := recover(); r != nil {
			if je, ok := r.(jsonError); ok {
				err = je.error
			} else {
				panic(r)
			}
		}
	}()
	e.reflectValue(reflect.ValueOf(v), opts)
	return nil
}
```


### Enum, variant type, tagged union
https://gobyexample.com/enums

```go
type ServerState int

const (
    StateIdle ServerState = iota
    StateConnected
    StateError
    StateRetrying
)
```

## Go code reviews
https://go.dev/wiki/CodeReviewComments


## When to use pointers
https://medium.com/@meeusdylan/when-to-use-pointers-in-go-44c15fe04eac
https://www.reddit.com/r/explainlikeimfive/comments/35zbyc/eli5_stack_vs_heap/


- Copying large structs
- Mutability
    - The only way to mutate a variable that you pass to a function is by passing a pointer.


## value/pointer Receiver

- value receiver
    - the Scale method operates on a copy of the original Vertex value. (This is the same behavior as for any other function argument.)

```go
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale1(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func (v Vertex) Scale2(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
    {
        v := Vertex{3, 4}
        v.Scale1(10)
        fmt.Println(v.Abs())
        // 50
    }
    {
        v := Vertex{3, 4}
        v.Scale2(10)
        fmt.Println(v.Abs())
        // 5
    }
}
```

## Slices and array
https://go.dev/blog/slices-intro

## Go directory structure
- `go help gopath`
- https://ido50.net/content/dont-put-all-your-code-in-internal.html
- https://go.dev/doc/modules/managing-dependencies
- https://www.bytesizego.com/blog/golang-internal-package
- https://github.com/google/exposure-notifications-server
- https://medium.com/@as27/internal-folder-133a4867733c

```
The Go path is used to resolve import statements.
It is implemented by and documented in the go/build package.

The GOPATH environment variable lists places to look for Go code.
On Unix, the value is a colon-separated string.
On Windows, the value is a semicolon-separated string.
On Plan 9, the value is a list.

If the environment variable is unset, GOPATH defaults
to a subdirectory named "go" in the user's home directory
($HOME/go on Unix, %USERPROFILE%\go on Windows),
unless that directory holds a Go distribution.
Run "go env GOPATH" to see the current GOPATH.

See https://golang.org/wiki/SettingGOPATH to set a custom GOPATH.

Each directory listed in GOPATH must have a prescribed structure:

The src directory holds source code. The path below src
determines the import path or executable name.

The pkg directory holds installed package objects.
As in the Go tree, each target operating system and
architecture pair has its own subdirectory of pkg
(pkg/GOOS_GOARCH).

If DIR is a directory listed in the GOPATH, a package with
source in DIR/src/foo/bar can be imported as "foo/bar" and
has its compiled form installed to "DIR/pkg/GOOS_GOARCH/foo/bar.a".

The bin directory holds compiled commands.
Each command is named for its source directory, but only
the final element, not the entire path. That is, the
command with source in DIR/src/foo/quux is installed into
DIR/bin/quux, not DIR/bin/foo/quux. The "foo/" prefix is stripped
so that you can add DIR/bin to your PATH to get at the
installed commands. If the GOBIN environment variable is
set, commands are installed to the directory it names instead
of DIR/bin. GOBIN must be an absolute path.

Here's an example directory layout:

    GOPATH=/home/user/go

    /home/user/go/
        src/
            foo/
                bar/               (go code in package bar)
                    x.go
                quux/              (go code in package main)
                    y.go
        bin/
            quux                   (installed command)
        pkg/
            linux_amd64/
                foo/
                    bar.a          (installed package object)

Go searches each directory listed in GOPATH to find source code,
but new packages are always downloaded into the first directory
in the list.

See https://golang.org/doc/code.html for an example.

GOPATH and Modules

When using modules, GOPATH is no longer used for resolving imports.
However, it is still used to store downloaded source code (in GOPATH/pkg/mod) and compiled commands (in GOPATH/bin).
```

### Internl Directories

Code in or below a directory named "internal" is importable only
by code in the directory tree rooted at the parent of "internal".
Here's an extended version of the directory layout above:

    /home/user/go/
        src/
            crash/
                bang/              (go code in package bang)
                    b.go
            foo/                   (go code in package foo)
                f.go
                bar/               (go code in package bar)
                    x.go
                internal/
                    baz/           (go code in package baz)
                        z.go
                quux/              (go code in package main)
                    y.go


The code in z.go is imported as "foo/internal/baz", but that import statement can only appear in source files in the subtree rooted at foo. The source files foo/f.go, foo/bar/x.go, and foo/quux/y.go can all import "foo/internal/baz", but the source file crash/bang/b.go cannot.

See https://golang.org/s/go14internal for details.


### Vendor Directories

Go 1.6 includes support for using local copies of external dependencies to satisfy imports of those dependencies, often referred to as vendoring.
Code below a directory named "vendor" is importable only by code in the directory tree rooted at the parent of "vendor", and only using an import path that omits the prefix up to and including the vendor element.
Here's the example from the previous section, but with the "internal" directory renamed to "vendor" and a new foo/vendor/crash/bang directory added:

```
    /home/user/go/
        src/
            crash/
                bang/              (go code in package bang)
                    b.go
            foo/                   (go code in package foo)
                f.go
                bar/               (go code in package bar)
                    x.go
                vendor/
                    crash/
                        bang/      (go code in package bang)
                            b.go
                    baz/           (go code in package baz)
                        z.go
                quux/              (go code in package main)
                    y.go
```

The same visibility rules apply as for internal, but the code in z.go is imported as "baz", not as "foo/vendor/baz".
Code in vendor directories deeper in the source tree shadows code in higher directories. Within the subtree rooted at foo, an import of "crash/bang" resolves to "foo/vendor/crash/bang", not the top-level "crash/bang".
Code in vendor directories is not subject to import path checking (see 'go help importpath').
When 'go get' checks out or updates a git repository, it now also updates submodules.
Vendor directories do not affect the placement of new repositories being checked out for the first time by 'go get': those are always placed in the main GOPATH, never in a vendor subtree.


## Environment variables
https://go.dev/ref/mod#private-modules
https://go.dev/ref/mod#environment-variables

```
go help environment
```

- GOPROXY
    - list of module proxy URLs. The go command will attempt to download modules from each server in sequence. The keyword direct instructs the go command to download modules from version control repositories where they’re developed instead of using a proxy.
- GOPRIVATE
    — list of glob patterns of module path prefixes that should be considered private. Acts as a default value for GONOPROXY and GONOSUMDB.
- GONOPROXY
    — list of glob patterns of module path prefixes that should not be downloaded from a proxy. The go command will download matching modules from version control repositories where they’re developed, regardless of GOPROXY.
- GONOSUMDB
    — list of glob patterns of module path prefixes that should not be checked using the public checksum database, sum.golang.org.
- GOINSECURE
    - list of glob patterns of module path prefixes that may be retrieved over HTTP and other insecure protocols.
- GOENV
    - The go command and the tools it invokes consult environment variables for configuration.
    - If an environment variable is unset or empty, the go command uses a sensible default setting.
    - To see the effective setting of the variable <NAME>, run `go env <NAME>`.
    - To change the default setting, run `go env -w <NAME>=<VALUE>`.
    - Defaults changed using `go env -w` are recorded in a Go environment configuration file stored in the per-user configuration directory, as reported by os.UserConfigDir.
    - The location of the configuration file can be changed by setting the environment variable `GOENV`, and `go env GOENV` prints the effective location, but `go env -w` cannot change the default location.


## Generics
- https://go.dev/blog/intro-generics




## Reference
* [Documentation - The Go Programming Language](https://golang.org/doc/)
* [Effective Go - The Go Programming Language](https://golang.org/doc/effective_go.html)
* [Essential Go - a free Go programming book](http://www.programming-books.io/essential/go/)
