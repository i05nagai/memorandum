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



## Change Streams
https://docs.cloud.google.com/spanner/docs/change-streams#value-capture-type

- OLD_AND_NEW_VALUES
    - Captures both old and new values of a row's modified columns.
- NEW_VALUES
    - Captures only the new values of the non-key columns, but no old values.
- NEW_ROW
    - Captures all new values of watched columns, both modified and unmodified, whenever any of those columns change. No old values are captured.
- NEW_ROW_AND_OLD_VALUES
    - Captures all new values for both modified and unmodified columns, and old values for modified columns.


```
CREATE CHANGE STREAM table2_cs FOR table2;
```


Query Change Stream Data

```
SELECT ChangeRecord FROM READ_SingersNameStream (
  start_timestamp => "2022-05-01T09:00:00Z",
  end_timestamp => NULL,
  partition_token => NULL,
  heartbeat_milliseconds => 10000
);
```

### Format
https://docs.cloud.google.com/spanner/docs/change-streams/details#change_streams_record_format

## Reference
