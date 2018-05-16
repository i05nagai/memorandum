---
title: mysqldump
---

## mysqldump

```
Usage: mysqldump [OPTIONS] database [tables]
OR     mysqldump [OPTIONS] --databases [OPTIONS] DB1 [DB2 DB3...]
OR     mysqldump [OPTIONS] --all-databases [OPTIONS]
```

* `--quick`
    * Don't buffer query, dump directly to stdout.
* `--single-transaction`
    * Creates a consistent snapshot by dumping all tables in a single transaction.
    * Works ONLY for tables stored in storage engines which support multiversioning (currently only InnoDB does);
    * the dump is NOT guaranteed to be consistent for other storage engines.
    * While a --single-transaction dump is in process, to ensure a valid dump file (correct table contents and binary log position), no other connection should use the following statements: ALTER TABLE, DROP TABLE, RENAME TABLE, TRUNCATE TABLE, as consistent snapshot is not isolated from them.
    * Option automatically turns off --lock-tables.  --dump-date
    * Put a dump date to the end of the output.
* `--replace`
* `--opt`
    * Same as --add-drop-table, --add-locks, --create-options, --quick, --extended-insert, --lock-tables, --set-charset, and --disable-keys. 
    * default on
    * --skip-optでoff
* `--add-locks`
* `--create-options`
* `--disable-keys`
* `--add-drop-table`
* `-C, --compless`
* `--compact`
    * Give less verbose output (useful for debugging).
    * Disables structure comments and header/footer constructs.
    * Enables options --skip-add-drop-table --skip-add-locks --skip-comments --skip-disable-keys --skip-set-charset.
* `--extended-insert`
* `--lock-tables`
* `--set-charset`
* `--lock-all-tables`
* `--master-data`
* `--ignore-table=[DB名].[テーブル名]`
* `-R, --routines`
* `-u`
* `-p`
* `-P, --port`
* `--dump-datea`


## Usage
稼働中のDBへのdump

```
mysqldump --quick --single-transaction > hoge
```

dataのdump

```
# データベース
$ mysqldump -u USER_NAME -p -h HOST_NAME DB_NAME > OUTPUT_FILE_NAME

#テーブル
$ mysqldump -u USER_NAME -p -h HOST_NAME DB_NAME TABLE_NAME > OUTPUT_FILE_NAME

#テーブルの定義とデータのダンプ
$ mysqldump -u USER_NAME -p -h HOST_NAME -A -n > OUTPUT_FILE_NAME 
```

## Reference
* [mysqldumpまとめ - Qiita](https://qiita.com/PlanetMeron/items/3a41e14607a65bc9b60c)
