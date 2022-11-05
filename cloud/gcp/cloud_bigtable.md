---
title: Cloud Bigtable
---

## Cloud Bigtable

- KVS
- Each table has only one index, the row key. 
- Rows are sorted lexicographically by row key,
- Column families are not stored in any specific order.
- Columns are grouped by column family and sorted in lexicographic order within the column family. 
- All operations are atomic at the row level
- Ideally, both reads and writes should be distributed evenly ac
- Bigtable tables are sparse.

## HDD or SSD
- You expect to store at least 10 TB of data.
- You will not use the data to back a user-facing or latency-sensitive application.
- Your workload falls into one of the following categories:
    - Batch workloads with scans and writes, and no more than occasional random reads of a small number of rows or point reads.
    - Data archival, where you write very large amounts of data and rarely read that data.

## Reference
- [Bigtable overview  \|  Cloud Bigtable Documentation  \|  Google Cloud](https://cloud.google.com/bigtable/docs/overview)
