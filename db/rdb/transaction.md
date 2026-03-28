---
title: Transaction
---

## Transaction


## Isolation


### Dirty Read isolation( ANSI Read Uncommitted)

With Dirty Read, the reader can read a row that has not been committed to the database and might be eliminated or changed during a rollback

- User1 starts a transaction.
- User1 inserts row A.
- User2 reads row A.
- User1 rolls back row A.

User2 gets uncommited row A.


### Committed Read isolation (ANSI Read Committed)
WIth Committed Read, the reader checks for locks before returning a row. By checking for locks, the reader cannot return any uncommitted rows.


### Cursor Stability isolation
A reader with Cursor Stability isolation acquires a shared lock on the row that is currently fetched.
This action assures that no other user can update the row until the user fetches a new row.

### repeatable read isolation
https://www.ibm.com/docs/en/informix-servers/14.10.0?topic=level-repeatable-read-isolation

With Repeatable Read, the database server locks all rows examined (not just fetched) for the duration of the transaction.
Repeatable Read is useful during any processing in which multiple rows are examined, but none must change during the transaction. 

use Repeatable Read isolation for tables when the database server can use an index to access a table.
If an index exists and the optimizer chooses a sequential scan instead, you can use directives to force use of the index. However, forcing a change in the query path might negatively affect query performance.


#### Serializable isolation
https://www.postgresql.org/docs/current/transaction-iso.html


## Reference


