---
title: Percona
---

## Percona
Discover how to better monitor, secure, and optimize your MySQL, PostgreSQL, or MongoDB database environments on any infrastructure.

## Percona Toolkit


#### pt-kill
https://docs.percona.com/percona-toolkit/pt-kill.html


- `pt-kill all`
    - all targets
- `--kill`
    - Kill the connection for matching queries.
- `--busy-time 10`
    - query longer than 10 sec
- `--port 3306`
    - kj
- `h=<host-name>,u=<user>`
- `--ignore-user xxx`
    - ignore xxx user in database
- `--victims [all|oldest|all-but-oldest]`
    - Which of the matching queries in each class will be killed. After classes have been matched/filtered, this option specifies which of the matching queries in each class will be killed (or printed, etc.).
- `--print`
    - print to output

## Reference
- https://www.percona.com/
