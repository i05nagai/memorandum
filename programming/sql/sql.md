---
title: SQL
---

## sql


## Tips


### 文字列の比較で、改行を含むかチェック
直接入力もできる。

```sql
'データＡ' || CHR(13) || CHR(10) || 'データＢ'
```

* CR
    * CHR(13)
* LF
    * CHR(10)
* CRLF
    * CHR(13) || CHR(10) 

### NULL終端の削除
以下で削除可能

```sql
REPLACE(text_column, CHAR(0), '')
```

### NULL終端文字の検索
TextにNULL終端文字列が含まれるかどうか。

```sql
SELECT
    *
FROM
    table
WHERE
    text_column LIKE "%\0%"
LIMIT 2
```

### Datetime


## Bigquery
* [Functions & Operators  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)

### Extract
UTC+0からJSTに変更する場合は以下で良い。

```sql
SELECT
    EXTRACT(DATETIME FROM TIMESTAMP "2008-12-25 15:30:00" AT TIME ZONE "Asia/Tokyo")
```

`TIMESTAMP "2008-12-25 15:30:00"`の部分は、TIMESTAMP型のcolumn_nameに変更できる。

## Reference

