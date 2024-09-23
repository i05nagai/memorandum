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
* package name
    * lower case
    * `src/encoding/base64`
    * `encoding/base64`
    * mixedCap or underscore
        * [Package names \- The Go Blog](https://blog.golang.org/package-names)

## Method
* In general, all methods on a given type should have either value or pointer receivers, but not a mixture of both
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


## Module

```
go mod init package
```

## Reference
* [Documentation - The Go Programming Language](https://golang.org/doc/)
* [Effective Go - The Go Programming Language](https://golang.org/doc/effective_go.html)
* [Essential Go - a free Go programming book](http://www.programming-books.io/essential/go/)
