---
title: mysql cli
---

## mysql cli

## Install
Ubuntu

```
apt install mysql-server
```

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
https://dev.mysql.com/doc/refman/8.0/en/server-options.html

- `--binlog-cache-size=#`
    - The size of the transactional cache for updates to transactional engines for the binary log. If you often use transactions containing many statements, you can increase this to get more performance
- `--binlog-max-flush-queue-time=#`
    - The maximum time that the binary log group commit will keep reading transactions before it flush the transactions to the binary log (and optionally sync, depending on the value of sync_binlog).
- `--default-time-zone=name`
    - Set the default time zone.
- `--socket=path`
    - On Unix, this option specifies the Unix socket file to use when listening for local connections. The default value is /tmp/mysql.sock. If this option is given, the server creates the file in the data directory unless an absolute path name is given to specify a different directory. On Windows, the option specifies the pipe name to use when listening for local connections that use a named pipe. The default value is MySQL (not case-sensitive).
- `--skip-networking`
- `--daemonize`
- `--skip-grant-tables`
    - it causes the server not to read the grant tables in the mysql system schema, and thus to start without using the privilege system at all. This gives anyone with access to the server unrestricted access to all databases.


#### Start mysql server

```
mysqld -D
```

#### Stop mysql server

```
mysqld stop
```

## Reference

