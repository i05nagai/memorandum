---
title: Trino
---

## Trino


## Syntax
- https://trino.io/docs/current/sql.html


#### date
https://trino.io/docs/current/functions/datetime.html


```
timestamp '2012-08-08 01:00'
timestamp '2012-10-31 01:00 UTC'
timestamp '2012-10-31 01:00 UTC' AT TIME ZONE 'America/Los_Angeles'
interval '29' hour
```

From date to date

```
date_trunc(second, timestamp '2001-08-22 03:04:05.100')
# 2001-08-22 03:04:05.100
```

Add

```
date_add('second', 86, TIMESTAMP '2020-03-01 00:00:00');
```

## Reference
- https://trino.io/
