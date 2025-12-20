---
title: wrench
---

## wrench

## CLI

Create database with tables described in schema file

```
wrench create
```

Drop database

```
wrench drop
```

Equivalent to drop and then create

```
wrench reset
```

Load schema from server to file

```
wrench load
```

Apply DDL file to database

```
wrench apply
```

Migrate database

```
wrench migrate
```

- create
    - Create a set of sequential up migrations in directory
- up
    - Apply all or N up migrations
- version
    - Print current migration version
- set
    - Set version V but don't run migration (ignores dirty state)


Truncate all tables without deleting a database

```
wrench truncate
```

Apply DDL file to database

```
wrench instance
```

Generate the autocompletion script for the specified shell

```
wrench completion
```

- `--credentials_file string`
    - Specify Credentials File
- `--database string`
    - Cloud Spanner database name (optional. if not set, will use `$SPANNER_DATABASE_ID` value) (default "identification")
- `--directory string`
    - Directory that schema file placed (required)
- `--instance string`
    - Cloud Spanner instance name (optional. if not set, will use `$SPANNER_INSTANCE_ID value`) (default `local-instance`)
- `--project string`
    - GCP project id (optional. if not set, will use `$SPANNER_PROJECT_ID` or `$GOOGLE_CLOUD_PROJECT` value) (default `local-project`)
- `--schema_file string`
    - Name of schema file (optional. if not set, will use default 'schema.sql' file name)
- `--timeout duration`
    - Context timeout (default 1h0m0s)


## fail condition

- if the schema file is empty, wrench migrate up will fail

### dirty
If the `wrench migraiton up` fails, the version will be dirty state.
If the version is dirty, you cannot run `wrench migration up` again until you fix the dirty state.

```
wrench migraiont set <dirty-version>

wrench migraiont set $(wrench migration version)
```

will fix the dirty state.


## Reference
