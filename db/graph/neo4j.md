---
title: neo4j
---

## neo4j


## Configuration
https://neo4j.com/docs/operations-manual/2025.01/configuration/
https://neo4j.com/docs/operations-manual/2025.01/configuration/configuration-settings/


#### File locations
https://neo4j.com/docs/operations-manual/2025.01/configuration/file-locations/

- `NEO4J_HOME`

## CLI

```
neo4j console
```
Start server in console.

```
neo4j restart  
```

Restart the server daemon.


```
neo4j start [-h] [--expand-commands] [--verbose]
```

Start server as a daemon.

- `--expand-commands`
    - Allow command expansion in config value evaluation.


```
neo4j status
```

Get the status of the neo4j server process.

```
neo4j stop
```

Stop the server daemon.

## Reference
- https://neo4j.com/free-graph-database/
- https://github.com/neo4j/docker-neo4j
