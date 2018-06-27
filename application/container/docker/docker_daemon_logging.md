---
title: Docker daemon logging
---

## Docker daemon logging
* [Configure and troubleshoot the Docker daemon | Docker Documentation](https://docs.docker.com/config/daemon/#read-the-logs)


## Logging driver
* `/var/log/containers`


| Driver     | Description                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------|
| none       | No logs will be available for the container and docker logs will not return any output.                 |
| json-file  | The logs are formatted as JSON. The default logging driver for Docker.                                  |
| syslog     | Writes logging messages to the syslog facility. The syslog daemon must be running on the host machine.  |
| journald   | Writes log messages to journald. The journald daemon must be running on the host machine.               |
| gelf       | Writes log messages to a Graylog Extended Log Format (GELF) endpoint such as Graylog or Logstash.       |
| fluentd    | Writes log messages to fluentd (forward input). The fluentd daemon must be running on the host machine. |
| awslogs    | Writes log messages to Amazon CloudWatch Logs.                                                          |
| splunk     | Writes log messages to splunk using the HTTP Event Collector.                                           |
| etwlogs    | Writes log messages as Event Tracing for Windows (ETW) events. Only available on Windows platforms.     |
| gcplogs    | Writes log messages to Google Cloud Platform (GCP) Logging.                                             |
| logentries | Writes log messages to Rapid7 Logentries.                                                               |

## log tag
containerのmessageを識別するためのtag
defaultでは12 charのcontainer ID.
tagの指定には以下の値を利用できる。

```
--log-opt tag="{{.ImageName}}/{{.Name}}/{{.ID}}"
```

出力は、`hello-world/foobar/5790672ab6a0`として付与される。

```
Aug  7 18:33:19 HOSTNAME hello-world/foobar/5790672ab6a0[9103]: Hello from Docker.
```

| Markup           | Description                                          |
|------------------|------------------------------------------------------|
| {{.ID}}          | The first 12 characters of the container ID.         |
| {{.FullID}}      | The full container ID.                               |
| {{.Name}}        | The container name.                                  |
| {{.ImageID}}     | The first 12 characters of the container’s image ID. |
| {{.ImageFullID}} | The container’s full image ID.                       |
| {{.ImageName}}   | The name of the image used by the container.         |
| {{.DaemonName}}  | The name of the docker program (docker).             |

## json-file
* [JSON File logging driver | Docker Documentation](https://docs.docker.com/v17.09/engine/admin/logging/json-file/)

log-opt

* `--log-opt max-size=10m`
    * rotateされるlogのsize
    * default -1でunlimited
* `--log-opt max-file=3`
    * defautl 1
    * rotateされた時に残るfileの数
* `--log-opt labels=production_status,geo`
* `--log-opt env=os,customer`
* `--log-opt env-regex=^(os|customer).`

```json
{"log":"2014/09/25 21:15:03 Got request with path wombat\\n",
 "stream":"stderr",
  "time":"2014-09-25T21:15:03.499185026Z"}
```

* log
    * 出力されたlog
* stream
    * stdout/stderr
* time
    * logの出力された時間

## Reference
