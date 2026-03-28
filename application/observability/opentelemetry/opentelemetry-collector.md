---
title: opentelemetry collector
---

## opentelemetry collector

## Configuration
https://opentelemetry.io/docs/collector/configuration/


## self metrics
https://opentelemetry.io/docs/collector/internal-telemetry/?utm_source=chatgpt.com

## GKE
https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/googlemanagedprometheusexporter/README.md

opentelemetry collector sends internal metrics(metrics of opentelemetry collector itself) when opentelemetry collector is shuting down.
Usually, opentelemetry coolector shutdown service first so that otel cannot sends metrics to otel itself when flushing the internal metrics.
To avoid this issue, for internal metrics we should use prometheus pull model instead of push model.

https://oneuptime.com/blog/post/2026-02-06-google-managed-prometheus-exporter-opentelemetry-collector/view


## Reference
