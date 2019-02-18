---
title: datadog agent
---

## datadog agent

## CLI

```
agent <command>
```

* check
    * Run the specified check
* config
    * Print the runtime configuration of a running agent
* configcheck
    * Print all configurations loaded & resolved of a running agent
* diagnose
    * Execute some connectivity diagnosis on your system
* flare
    * Collect a flare and send it to Datadog
* health
    * Print the current agent health
* help
    * Help about any command
* hostname
    * Print the hostname used by the Agent
* import
    * Import and convert configuration files from previous versions of the Agent
* integration
    * Datadog integration manager

#### agent jmx

```
agent jmx list <collected>
```

* collected
    * List attributes that will actually be collected by your current instances configuration.
* everything
    * List every attributes available that has a type supported by JMXFetch.
* limited
    * List attributes that do match one of your instances configuration but that are not being collected because it would exceed the number of metrics that can be collected.
* matching
    * List attributes that match at least one of your instances configuration.
* not-matching
    * List attributes that don’t match any of your instances configuration.

* launch-gui  starts the Datadog Agent GUI
* run         Run the Agent
* status      Print the current status
* stop        Stops a running Agent
* tagger-list Print the tagger content of a running agent
* version     Print the version info


## Configuration file
https://docs.datadoghq.com/agent/faq/agent-configuration-files/?tab=agentv6

* `/datadog-agent/conf.d/<NAME>.d/`

## Autodiscovery
* https://docs.datadoghq.com/agent/autodiscovery/?tab=docker

Template variables

* `%%host%%`
* `%%host_<NETWORK NAME>%%`
* `%%port%%`


#### Reload configuration
https://github.com/DataDog/dd-agent/pull/1983

```
kill -SIGUSR2 PID
```


## Reference
* https://docs.datadoghq.com/agent/?tab=agentv6
