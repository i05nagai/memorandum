---
title: cypher-shell
---

## cypher-shell

```
cypher-shell [-h] [-a ADDRESS] [-u USERNAME] [--impersonate IMPERSONATE] [-p PASSWORD] [--encryption {true,false,default}] [-d DATABASE] [--access-mode {read,write}] [--enable-autocompletions]
                [--format {auto,verbose,plain}] [-P PARAM] [--non-interactive] [--sample-rows SAMPLE-ROWS] [--wrap {true,false}] [-v] [--driver-version] [-f FILE] [--change-password]
                [--log [LOG-FILE]] [--history HISTORY-BEHAVIOUR] [--notifications] [--idle-timeout IDLE-TIMEOUT] [--fail-fast | --fail-at-end] [cypher]
```

- `--fail-fast`
    - Exit and report failure on the first error when reading from a file (this is the default behavior).
- `--fail-at-end`
    - Exit and report failures at the end of the input when reading from a file.
- `--enable-autocompletions`
    - Whether to enable Cypher autocompletions inside the CLI. Completions can only be enabled for neo4j 5 and later. (default: false)
- `--format {auto,verbose,plain}`
    - Desired output format. Displays the results in tabular format if you use the shell interactively and with minimal formatting if you use it for scripting.  `verbose` displays results in tabular format and prints statistics.  `plain` displays data with minimal formatting. (default: auto)
- `-P PARAM`, `--param PARAM`
    - Add a parameter to this session. Example: `-P {a: 1}` or `-P {a: 1, b: duration({seconds: 1})}`. This argument can be specified multiple times. (default: [])
- `--non-interactive`
    - Force non-interactive mode. Only useful when auto-detection fails (like on Windows). (default: false)
- `--sample-rows SAMPLE-ROWS`
    - Number of rows sampled to compute table widths (only for format=VERBOSE). (default: 1000)
- `--wrap {true,false}`
    - Wrap table column values if column is too narrow (only for format=VERBOSE). (default: true)
- `--driver-version`
    - Print Neo4j Driver version and exit. (default: false)
- `-f FILE`, `--file FILE`
    - Pass a file with Cypher statements to be executed. After executing all statements, Cypher Shell shuts down.
- `--change-password`
    - Change the neo4j user password and exit. (default: false)
- `--log [LOG-FILE]`
    - Enable logging to the specified file, or standard error if the file is omitted.
- `--history HISTORY-BEHAVIOUR`
    - File path of a query and a command  history  file  or  `in-memory`  for  in-memory  history.  Defaults  to  <user  home>/.neo4j/.cypher_shell_history. Can also be set using the environment variable NEO4J_CYPHER_SHELL_HISTORY.
- `--notifications`
    - Enable notifications in interactive mode. (default: false)
- `--idle-timeout IDLE-TIMEOUT`
    - Closes the application after the specified amount of idle time in  interactive  mode.  You can specify the duration using the format `<hours>h<minutes>m<seconds>s`,
    - for example `1h` (1 hour), `1h30m` (1 hour 30 minutes), or `30m` (30 minutes).

## Reference
- https://neo4j.com/docs/operations-manual/2025.01/tools/cypher-shell/
