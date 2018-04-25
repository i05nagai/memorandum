---
title: Google Stackdriver Logging
---

## Google Stackdriver Logging
loggingはfluentdが使われている。

## Customize Logging
* [Installing the Logging Agent  |  Stackdriver Logging  |  Google Cloud](https://cloud.google.com/logging/docs/agent/installation#installing_the_logging_agent)

`/etc/google-fluentd/config.d/`にfluentdのconfigがある。
`/var/log/google-fluentd/google-fluentd.log`にfluetndのLogがはかれる。

## Pricing
Start at June 30, 2018

* Stackdriver Logging
    * free
        * First 50 GB/project
    * price
        * 0.50USD/GB

## Reference

