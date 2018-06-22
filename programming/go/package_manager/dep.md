---
title: dep
---

## dep

Install

```
go get -u github.com/golang/dep/cmd/dep
```

## CLI

```
dep init
```

* `-gopath`
* `-no-examples`
* `-skip-tools`
* `-v`

```
go status
```

* return exit code 0
    * if all dependencies are in a "good state".
* PROJECT
    * Import path
* CONSTRAINT
    * Version constraint, from the manifest
* VERSION
    * Version chosen, from the lock
* REVISION
    * VCS revision of the chosen version
* LATEST
    * Latest VCS revision available
* PKGS USED
    * Number of packages from this project that are actually used


* -dot
    * output the dependency graph in GraphViz format (default: false)
* -examples
    * print detailed usage examples (default: false)
* -f
    * output in text/template format (default: <none>)
* -json
    * output in JSON format (default: false)
* -missing
    * only show missing dependencies (default: false)
* -old
    * only show out-of-date dependencies (default: false)
* -v
    * enable verbose logging (default: false)


```
dep ensure [-update | -add] [-no-vendor | -vendor-only] [-dry-run] [-v] [<spec>...]
```

* `<import path>[:alt source URL][@<constraint>]`
* -add
    * add new dependencies, or populate Gopkg.toml with constraints for existing dependencies (default: false)
* -dry-run
    * only report the changes that would be made (default: false)
* -examples
    * print detailed usage examples (default: false)
* -no-vendor    update Gopkg.lock (if needed), but do not update vendor/ (default: false)
* -update       update the named dependencies (or all, if none are named) in Gopkg.lock to the latest allowed by Gopkg.toml (default: false)
* -v            enable verbose logging (default: false)
* -vendor-only  populate vendor/ from Gopkg.lock without updating it first (default: false)


## Usage
Create project.
Directory you create projects need to be under a path in `$GOPATH`.

```
$ mkdir -p $GOPATH/src/github.com/me/example
$ cd $GOPATH/src/github.com/me/example
$ dep init
$ ls
Gopkg.toml Gopkg.lock vendor/
```

Add dependent packages

```
dep ensure -add github.com/foo/bar github.com/baz/quux
```

Solve dependency

```
dep ensure
```

Update all packages to the latest allowed by `Gopkg.toml`.

```
dep ensure -update
```

## Configuration
* [dep/Gopkg\.toml\.md at master · golang/dep](https://github.com/golang/dep/blob/master/docs/Gopkg.toml.md)

`Gopkg.toml`

## Reference
* [GitHub - golang/dep: Go dependency management tool](https://github.com/golang/dep)
* [dep · Dependency management for Go](https://golang.github.io/dep/)
