---
title: Join
---

## Join





## semi join
with hash join, it's efficient.

## anti join / anti semi join

```
SELECT column1, column2,...FROM table1 
LEFT JOIN table2 ON table1.column_name = table2.column_name
WHERE table2.column_name IS NULL;
```

## Reference

- https://www.geeksforgeeks.org/dbms/difference-between-anti-join-and-semi-join/
