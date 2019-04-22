---
title: git-cat-file
---

## git-cat-file
Provide content or type and size information for repository objects.

- blob
- commit
- tree
- tag

## CLI

```
git cat-file (-t [--allow-unknown-type]| -s [--allow-unknown-type]| -e | -p | <type> | --textconv | --filters ) [--path=<path>] <object>
git cat-file (--batch | --batch-check) [ --textconv | --filters ] [--follow-symlinks]
```

## Usage

Show type of git object

```
git cat-file -t <git-object>
```

## Configuration

## Reference
