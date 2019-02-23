---
title: BigQuery Standard SQL
---

## BigQuery Standard SQL


```
# if you execute 
CURRENT_TIMESTAMP()
```

## Wildcard Tables
How to filter wildcard tables by date.
The following snippets filters the wildcard tables by date and process only not-filtered tables.

```sql
#standardSQL
CREATE TEMPORARY FUNCTION BetweenCalculationDate(table_suffix STRING) AS (
  table_suffix
  BETWEEN
  FORMAT_TIMESTAMP('%Y%m%d', TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR))
  AND
  FORMAT_TIMESTAMP('%Y%m%d', CURRENT_TIMESTAMP())
);

WITH table AS (
  SELECT
    *
  FROM
    `project.dataset.table_*`
  WHERE
    BetweenCalculationDate(_TABLE_SUFFIX)
)

```

## DML syntax
* [INSERT](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#insert_statement)
    * Column names must be specified
    * Duplicate names are not allowed in the list of target columns.
    * Values must be added in the same order as the specified columns.
    * The number of values added must match the number of specified columns.
    * Values must have a type that is compatible with the target column.

```sql
INSERT
    dataset_name.table_name (col1, col2)
VALUES
    (col1_val1, col2_val1),
    (col1_val2, col2_val2)
```

```sql
INSERT
    dataset_name.table_name (col1, col2)
SELECT
    col1, col2
FROM
    dataset_name2.table_name2
```

* [DELETE](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#delete_statement)

Delete all tables

```sql
DELETE FROM dataset.DetailedInventory WHERE true
```

DELETE with sub query

```sql
DELETE dataset.Inventory i
WHERE i.product NOT IN (SELECT product from dataset.NewArrivals)
```

* [MERGE](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#merge_statement)
    * MERGE statement can combine INSERT, UPDATE, and DELETE operations into a single statement and perform the operations atomically.



## Tips

### Insert into partitioned table
ingestion-timeでpartition tableを作っていない場合は、destination tableでpartitionを指定する必要がある。

```sql
INSERT
    dataset_name.table_name$20170101 (col1, col2)
SELECT
    col1, col2
FROM
    dataset_name2.table_name2
```



## Reference
