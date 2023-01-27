---
title: Bigtable
---

## Bigtable


## concepts

- instance
    - instance contains clusters
    - a table belongs to an instance
    - Bigtable instances that have only 1 cluster do not use replication
    -  If you add a second cluster to an instance, Bigtable automatically starts replicating your data by keeping separate copies of the data in each of the clusters' zones and synchronizing updates between the copies.
- cluster
    - cluster contains nodes
    - each cluster has at least 1 node
- nodes
- application profile
    - once you create an instance, application profile is stored
- table
    - Each table has only one index, the row key, from the lowest to the highest byte string. 
- row key
    - Row keys are sorted in big-endian byte order (sometimes called network byte order), the binary equivalent of alphabetical order.
- column family
    - Column families are not stored in any specific order.
    - Columns are grouped by column family and sorted in lexicographic order within the column family
- garbage collection
    - Garbage collection is the automatic, ongoing process of removing expired and obsolete data from Bigtable tables.
- garbage collection policy
    -  a set of rules you create that state when data in a specific column family is no longer needed.

## Schema

## Column family

#### storage
Columns that are not used in a Bigtable row do not take up any space in that row. Each row is essentially a collection of key/value entries, where the key is a combination of the column family, column qualifier and timestamp. If a row does not include a value for a specific column, the key/value entry is simply not present.

#### consistency
- Single-cluster Bigtable instances provide strong consistency.
- By default, instances that have more than one cluster provide eventual consistency, but for some use cases they can be configured to provide read-your-writes consistency or strong consistency, depending on the workload and app profile settings.

## Garbage collection

- It can take up to a week before data that is eligible for garbage collection is actually deleted.
- Garbage collection occurs on a fixed schedule that does not vary based on how much data needs to be deleted. Until the data is deleted, it appears in read results


## Limitations
- https://cloud.google.com/bigtable/quotas



## Reference



