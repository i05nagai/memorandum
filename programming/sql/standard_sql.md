## standards SQL

## Bigquery
* [Functions & Operators  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)

### Extract
UTC+0からJSTに変更する場合は以下で良い。

```sql
SELECT
    EXTRACT(DATETIME FROM TIMESTAMP "2008-12-25 15:30:00" AT TIME ZONE "Asia/Tokyo")
```

`TIMESTAMP "2008-12-25 15:30:00"`の部分は、TIMESTAMP型のcolumn_nameに変更できる。

