---
title: zip
---

## zip
You need to delete existing zip file to re-create zip files.
Otherwise, zip command updates the existing zip file.


## CLI

## Usage
Show detailed help message

```
zip -h2
```

Create zip from directory excluding directories.

```
# exclude __pycache__ directory and *dist-info directory
zip -q -r -9 zipfilename.zip directoryname -x '**__pycache__**' *.pyc '*dist-info*'
```

## Configuration

## Reference
