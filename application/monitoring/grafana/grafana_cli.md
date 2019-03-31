---
title: grafana-cli
---

## grafana-cli


## CLI

```
grafana-cli [global options] command [command options] [arguments...]
```

Manage plugins for grafana

```
grafana-cli plugins  
```

Grafana admin commands

```
grafana-cli admin
```

* `--pluginsDir value`
    * path to the grafana plugin directory
    * (default: "/var/lib/grafana/plugins")
    * `$GF_PLUGIN_DIR`
* `--repo value`
    * url to the plugin repository
    * (default: "https://grafana.com/api/plugins")
    * `$GF_PLUGIN_REPO`
* `--pluginUrl value`
    * Full url to the plugin zip file instead of downloading the plugin from grafana.com/api
    * `$GF_PLUGIN_URL`
* --insecure
    * Skip TLS verification (insecure)
* --debug, -d
    * enable debug logging

## Usage

## Configuration

## Reference
