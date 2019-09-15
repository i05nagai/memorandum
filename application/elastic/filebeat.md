---
title: filebeat
---

## filebeat

## Install

```
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.2.1-linux-x86_64.tar.gz
tar xzvf filebeat-7.2.1-linux-x86_64.tar.gz
```

## CLI

```
filebeat [flags]
filebeat [command]
```

* `-E, --E setting=value`
    * Configuration overwrite
* -M, --M setting=value
    * Module configuration overwrite
* -N, --N
    * Disable actual publishing for testing
* -c, --c string
    * Configuration file, relative to path.config (default "filebeat.yml")
* --cpuprofile string
    * Write cpu profile to file
* -d, --d string
    * Enable certain debug selectors
* -e, --e
    * Log to stderr and disable syslog/file output
* --httpprof string
    * Start pprof http server
* --memprofile string
    * Write memory profile to this file
* --modules string
    * List of enabled modules (comma separated)
* --once
    * Run filebeat only once until all harvesters reach EOF
* --path.config string   Configuration path (default "")
* --path.data string     Data path (default "")
* --path.home string     Home path (default "")
* --path.logs string     Logs path (default "")
* --plugin pluginList    Load additional plugins
* --strict.perms         Strict permission checking on config files (default true)
* -v, --v                    Log at INFO level


This will enroll in Kibana Beats Central Management.
If you pass an enrollment token it will be used. You can also enroll using a username and password combination.

```
filebeat enroll <kibana_url> [<enrollment_token>] [flags]
```

* --force             Force overwrite of current configuraiton, do not prompt for confirmation
* --password string   Method to read the password to use when enrolling without token (stdin or env:VAR_NAME) (default "stdin")
* --username string   Username to use when enrolling without token (default "elastic")

Export current config or index template

```
filebeat export [command]
```

* config
    * Export current config to stdout
* dashboard
    * Export defined dashboard to stdout
* ilm-policy
    * Export ILM policy
* index-pattern
    * Export kibana index pattern to stdout
* template
    * Export index template to stdout

Generate Filebeat modules, filesets and fields.yml

```
filebeat generate [command]
```

* fields
    * Generates a new fields.yml file for fileset
* fileset
    * Generates a new fileset
* module
    * Generates a new module


```
filebeat keystore [command]
```

* add         Add secret
* create      Create keystore
* list        List keystore
* remove      Remove secret


Manage configured modules

```
filebeat modules [command]
```

* disable     Disable one or more given modules
* enable      Enable one or more given modules
* list        List modules



Run filebeat

```
filebeat run [flags]
```

* -N, --N                   Disable actual publishing for testing
* --cpuprofile string   Write cpu profile to file
* --httpprof string     Start pprof http server
* --memprofile string   Write memory profile to this file
* --modules string      List of enabled modules (comma separated)
* --once                Run filebeat only once until all harvesters reach EOF



This command does initial setup of the environment:

* Index mapping template in Elasticsearch to ensure fields are mapped.
* Kibana dashboards (where available).
* ML jobs (where available).
* Ingest pipelines (where available).
* ILM policy (for Elasticsearch 6.5 and newer).


```
filebeat setup [flags]
```

* --dashboards         Setup dashboards
* --index-management   Setup all components related to Elasticsearch index management, including template, ilm policy and rollover alias
* --machine-learning   Setup machine learning job configurations
* --modules string     List of enabled modules (comma separated)
* --pipelines          Setup Ingest pipelines



Test config

```
filebeat test [command]
```

* config
    * Test configuration settings
* output
    * Test filebeat can connect to the output by using the current settings


## Usage

## Configuration

## Reference
