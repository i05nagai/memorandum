---
title: Prometheus
---

## Prometheus


## StatsD metrics
https://dev.to/kirklewis/metrics-with-prometheus-statsd-exporter-and-grafana-5145



## On Kubernetes
* [Kubernetes monitoring with Prometheus in 15 minutes](https://itnext.io/kubernetes-monitoring-with-prometheus-in-15-minutes-8e54d1de2e13)
* [The Prometheus Operator: Managed Prometheus setups for Kubernetes | CoreOS](https://coreos.com/blog/the-prometheus-operator.html)

## PromQL
https://prometheus.io/docs/prometheus/latest/querying/basics/
https://promlabs.com/promql-cheat-sheet/


#### Functions
https://prometheus.io/docs/prometheus/latest/querying/functions/#rate


- `rate()`
    - per sec average
    - The range in a `rate` query should be at least four times the scrape interval.
    - Scrape interval is the interval in which Prometheus server scrapes



## Reference
* [Overview | Prometheus](https://prometheus.io/docs/introduction/overview/)
* [Prometheus on Kubernetes](http://marselester.com/prometheus-on-kubernetes.html)
