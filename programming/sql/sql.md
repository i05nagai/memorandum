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


## Reference

