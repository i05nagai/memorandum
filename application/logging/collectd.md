---
title: collectd
---

## collectd

```
yum install epel-release
yum install collectd
```

```
add-apt-repository -y ppa:signalfx/collectd-release \
add-apt-repository -y ppa:signalfx/collectd-plugin-release \
apt-get update \
# Install
apt-get install -y \
    # Install SignalFx Plugin
    signalfx-collectd-plugin \
    # Install collectd
    collectd \
```

## CLI
Following command runs collectd process in the backgroud.

```
collectd
```

* `-C <file>`
    * Configuration file.
    * Default: /etc/collectd/collectd.conf
* `-t`
    * Test config and exit.
* `-T` 
    * Test plugin read and exit.
* `-P <file>`
    * PID-file
    * Default: /var/run/collectd.pid
* `-f`
    * Don't fork to the background.
* `-B`
    * Don't create the BaseDir
* `-h`
    * Display help (this message)

## Plugins
* [lebauce/docker-collectd-plugin: docker-collectd-plugin](https://github.com/lebauce/docker-collectd-plugin)
    * Network bandwidth
    * Memory usage
    * CPU usage
    * Block IO
* df
    * disk spaceを収集する
    * `/proc`, `/dev`は集計の対象にしない

## Configuraton
`/etc/collectd.conf`

## Docker
* [signalfx/docker-collectd: Collectd within a Docker image](https://github.com/signalfx/docker-collectd)



## Reference
* [Documentation – collectd – The system statistics collection daemon](https://collectd.org/documentation.shtml)
* [Start page – collectd – The system statistics collection daemon](https://collectd.org/)
* [collectdの設定方法 - Qiita](https://qiita.com/28tomono/items/33d3520e81f39fe2f96f)
