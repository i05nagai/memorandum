---
title: spanner
---

## spanner


## Transaction

### read-write transaction

- Read-write transactions with serializable isolation
    - The transaction returns values that reflect a consistent snapshot at the transaction's commit timestamp.
    - Empty rows or ranges remain empty at commit time.
    - The transaction commits all writes at the transaction's commit timestamp.
    - No transaction can see the writes until after the transaction commits.
- Read-write transactions with repeatable read isolation




### read-only transactino


### partitioned 



## Isolation

### serializable isolation


### repeatable read isolation
https://docs.cloud.google.com/spanner/docs/isolation-levels#repeatable-read


## Reference
