---
title: bq
---

## bq
bq command.


## create partitioned table from query resulst

```
cat query.sql | bq query \
  --nouse_legacy_sql \
  --destination_table "project_id:dataset_id.destination_table" \
  --time_partitioning_field field_name
```

## Reference

