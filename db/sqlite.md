---
title: sqlite
---

## sqlite


## CLI
```
sqlite3 /path/to/db_file
```

helpを表示

```
.help
```

tableの一覧

```
.tables
```

schemaを表示

```
.schema [table_name]
```

exit

```
.exit
```

change working directory

```
.cd /path/to/dir
```

Execute SQL in file

```
.read /path/to/sql
```


## SQL

```
CREATE INDEX index_name ON table(col1, col2);
```

## Reference
* [The SQLite Query Optimizer Overview](https://sqlite.org/optoverview.html)
