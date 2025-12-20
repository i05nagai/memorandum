---
title: Postgresql
---

## Postgresql


## Trigger
https://www.postgresql.org/docs/current/sql-createtrigger.html

- The trigger can be specified to fire
    - before the operation is attempted on a row (before constraints are checked and the INSERT, UPDATE, or DELETE is attempted);
    - or after the operation has completed (after constraints are checked and the INSERT, UPDATE, or DELETE has completed);
    - or instead of the operation (in the case of inserts, updates or deletes on a view).
- If the trigger fires before or instead of the event, the trigger can skip the operation for the current row, or change the row being inserted (for INSERT and UPDATE operations only).
- If the trigger fires after the event, all changes, including the effects of other triggers, are “visible” to the trigger.

## Reference
