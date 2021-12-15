---
title: Locust
---

## Locust
An open source load testing tool.

```
pip install locustio
```

## CLI

```
locust
```

- `-f LOCUSTFILE`
    - locustfile
- `--worker`
    - Set locust to run in distributed mode with this process as worker
- `--master-host MASTER_NODE_HOST`
    - Host or IP address of locust master for distributed load testing. Only used when running with --worker. Defaults to 127.0.0.1.
- `--master-port MASTER_NODE_PORT`
    - The port to connect to that is used by the locust master for distributed load testing. Only used when running with --worker. Defaults to 5557.
- `-T TAG`, `--tags TAG`
    - List of tags to include in the test, so only tasks with any matching tags will be executed
- `-E TAG`, `--exclude-tags TAG`
    - List of tags to exclude from the test, so only tasks with no matching tags will be executed
- `--csv CSV_PREFIX`
    - Store current request stats to files in CSV format. Setting this option will generate three files: [CSV_PREFIX]_stats.csv, [CSV_PREFIX]_stats_history.csv and [CSV_PREFIX]_failures.csv
- `--csv-full-history`
    - Store each stats entry in CSV format to _stats_history.csv file. You must also specify the '--csv' argument to enable this.
- `--print-stats`
    - Print stats in the console
- `--only-summary`
    - Only print the summary stats
- `--reset-stats`
    - Reset statistics once spawning has been completed. Should be set on both master and workers when running in distributed mode
- `--html HTML_FILE`
    - Store HTML report file
- `--skip-log-setup`
    - Disable Locust's logging setup. Instead, the configuration is provided by the Locust test or Python defaults.
- `--loglevel LOGLEVEL, -L LOGLEVEL`
    - Choose between DEBUG/INFO/WARNING/ERROR/CRITICAL. Default is INFO.
- `--logfile LOGFILE`
    - Path to log file. If not set, log will go to stdout/stderr
- `--show-task-ratio`
    - Print table of the User classes' task execution ratio
- `--show-task-ratio-json`
    - Print json data of the User classes' task execution ratio
- `--exit-code-on-error EXIT_CODE_ON_ERROR`
    - Sets the process exit code to use when a test result contain any failure or error
- `-s STOP_TIMEOUT, --stop-timeout STOP_TIMEOUT`
    - Number of seconds to wait for a simulated user to complete any executing task before exiting. Default is to terminate immediately. This parameter
- `--equal-weights`
    - Use equally distributed task weights, overriding the weights specified in the locustfile.


## Reference
* [Locust - A modern load testing framework](https://locust.io/)
* [Locust コトハジメ - Qiita](https://qiita.com/yamionp/items/17ffcc465272ad83c490)
