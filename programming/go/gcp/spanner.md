---
title: spanner
---

## spanner

- Not stopping a RowIterator that is returned by Query, Read and other methods. Always use RowIterator.Stop() to ensure that the RowIterator is always closed.
- Not closing a ReadOnlyTransaction when you no longer need it. Always call ReadOnlyTransaction.Close() after use, to ensure that the ReadOnlyTransaction is always closed.


## Reference
- https://pkg.go.dev/cloud.google.com/go/spanner#section-readme
