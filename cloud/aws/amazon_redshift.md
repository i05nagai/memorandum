---
title: Amazon Redshift
---

## Amazon Redshift


- Schema
    - schema contains tables

## Query

List schema

```
select * from pg_namespace;
```

List tables

```
select distinct(tablename) from pg_table_def
where schemaname = 'pg_catalog';
```




## Reference
- [Using the Amazon Redshift Data API \- Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html)
