---
title: bazel buildifier
---

## bazel buildifier
Bazel BUILD filer formatter.

Install

```
go get github.com/bazelbuild/buildtools/buildifier
```

```
brew install buildifier
```

## Usage

```
buildifier -showlog -mode=check $(find . -type f \( -iname BUILD -or -iname BUILD.bazel \))
```


## Reference
* [bazelbuild/buildtools: A bazel BUILD file formatter and editor](https://github.com/bazelbuild/buildtools)
