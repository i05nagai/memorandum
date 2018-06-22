---
title: godoc
---

## godoc
One of Go tools.

## Install

```
go get -u golang.org/x/tools/cmd/godoc
```

## CLI

```
godoc [flag] package [name ...]
```

* `-http=ip:port`
    * by default `:6060`
    * `127.0.0.1` if you omit ip address

## Usage
Show documentation of `<pkg>` or `<pkg>.<func>`

```
godoc <pkg>
godoc <pkg> <func>
```

```
godoc -http=:6060
```

## Reference
* [Godoc: documenting Go code \- The Go Blog](https://blog.golang.org/godoc-documenting-go-code)
* [golang/tools: Go Tools](https://github.com/golang/tools)
* [godoc \- GoDoc](https://godoc.org/golang.org/x/tools/cmd/godoc)
* [tools/godoc at master · golang/tools](https://github.com/golang/tools/tree/master/godoc)
* [Go Documentation: godoc, go doc, godoc\.org, and go/doc—Which One’s Which? · Whipperstacker](http://whipperstacker.com/2015/09/30/go-documentation-godoc-godoc-godoc-org-and-go-doc/)
