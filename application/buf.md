---
title: buf
---

## buf


```
brew install bufbuild/buf/buf
```

## CLI

```
buf build
```

```
buf generate
```

#### breaking

```
buf breaking
```

```
buf breaking proto --against "ssh://git@github.com/<your-org>/<your-repo>.git#branch=main,subdir=proto"
buf breaking --against '.git#branch=main,subdir=proto'
```

- `--against string`
    - Required. The source, module, or image to check against. 
    - [binpb,dir,git,json,mod,protofile,tar,txtpb,yaml,zip]
    - `'.git#branch=main,subdir=proto'`
- `--against-config string`
    - The buf.yaml file or data to use to configure the against source, module, or image
- `--config string`
    - The buf.yaml file or data to use for configuration
- `--disable-symlinks`
    - Do not follow symlinks when reading sources or configuration from the local filesystem
    - By default, symlinks are followed in this CLI, but never followed on the Buf Schema Registry
- --error-format string
    - The format for build errors or check violations printed to stdout. Must be one of [text,json,msvs,junit,github-actions] (default "text")
- --exclude-imports
    - Exclude imports from breaking change detection.
- --exclude-path strings
    - Exclude specific files or directories, e.g. "proto/a/a.proto", "proto/a"
    - If specified multiple times, the union is taken
* --limit-to-input-files
    * Only run breaking checks against the files in the input When set, the against input contains only the files in the input Overrides --path
* `--path strings`
    * Limit to specific files or directories, e.g. "proto/a/a.proto", "proto/a"
    * If specified multiple times, the union is taken

#### lint
https://buf.build/docs/lint/rules/

```
buf lint
```

- MINIMAL
    - 
- STANDARD
- BASIC

```
bu
```



## Reference
- https://buf.build/docs/cli/
