---
title: PostgreSQL
---

## PostgreSQL


## CLI

```
psql --user name
```


* `\?`
    * help
* `\c database_name`
    * connect to database
    * currently connected database is shown if you omit arguments
* `\dg`
    * roles
* `\dn`
    * schema
* `\dt`
    * tables

## docker
[library/postgres - Docker Hub](https://hub.docker.com/_/postgres/)

* environment variabless
    * POSTGRES_PASSWORD
    * POSTGRES_USER
    * PGDATA
        * `/var/lib/postgresql/data`
    * POSTGRES_DB
    * POSTGRES_INITDB_ARGS
    * POSTGRES_INITDB_WALDIR

## Reference
- https://habr.com/en/company/postgrespro/blog/649499/
