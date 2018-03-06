---
title: Go
---

## Go

## Install
to OSX

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

## Reference
* [Documentation - The Go Programming Language](https://golang.org/doc/)
* [Effective Go - The Go Programming Language](https://golang.org/doc/effective_go.html)
* [Essential Go - a free Go programming book](http://www.programming-books.io/essential/go/)
