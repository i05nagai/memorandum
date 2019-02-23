---
title: MySQL Monitoring
---

## MySQL Monitoring

## Tips

#### buffer pool
MySQL’s default storage engine, InnoDB, uses an area of memory called the buffer pool to cache data for tables and indexe
Buffer pool metrics are resource metrics as opposed to work metrics, and as such are primarily useful for investigating (rather than detecting) performance issues
If database performance starts to slide while disk I/O is rising, expanding the buffer pool can often provide benefits.

## Reference
* https://www.datadoghq.com/blog/monitoring-mysql-performance-metrics/#buffer-pool-usage

