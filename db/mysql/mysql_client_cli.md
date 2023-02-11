---
title: mysql-client cli
---

## mysql-client cli

## Install
Alpine linux

```
apk add mysql-client
```

For Amazon linux,

## CLI

* `-h, --host=name`
    * Connect to host.
* `--skip-column-names, -N`
    * no print columun name
* `-u, --user=name`
    * User for login if not current user.
* `-v, --verbose`
    * Write more. (-v -v -v gives the table output format).
* ` -P, --port=#`
* `-t, --table`
    * Output in table format.
* `--tee=name`
    * Append everything into outfile. See interactive help (\h)


## Usage

#### Connect to mysql

```
mysql -u username -p -P port -h hostname
```

#### Run sql

```
mysql -u username -P port -h hostname database < file.sql
```

## Reference
