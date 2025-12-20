---
title: neo4j-admin
---

## neo4j-admin
Neo4j database administration tool.

```
neo4j-admin [-hV] [--expand-commands] [--verbose] [COMMAND]

      --expand-commands   Allow command expansion in config value evaluation.
  -h, --help              Show this help message and exit.
  -V, --version           Print version information and exit.
      --verbose           Prints additional information.
```

#### database 
Database-specific administration tasks.


#### dbms
DBMS-wide (for single and clustered environments) administration tasks.

```
neo4j-admin dbms set-initial-password <password>
```

- `<password>`
    - password for user neo4j

```
neo4j-admin dbms set-default-admin
```

#### server
Server-wide administration tasks.


#### backup
Backup-specific administration tasks.

## Environment variables:

- NEO4J_CONF
    Path to directory which contains neo4j.conf.
- NEO4J_DEBUG
    - Set to anything to enable debug output.
- NEO4J_HOME
    - Neo4j home directory.
- HEAP_SIZE
    - Set JVM maximum heap size during command execution. Takes a number and a unit, for example 512m.
- JAVA_OPTS
    - Used to pass custom setting to Java Virtual Machine executing the command. Refer to JVM documentation about the exact format. This variable is incompatible with HEAP_SIZE and takes precedence over HEAP_SIZE.

## Reference

