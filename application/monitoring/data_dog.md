---
title: DataDog
---

## DataDog

* custom metric
    * refers to a single, unique combination of a metric name, host, and any tags.

## Docker image
* [datadog-agent/Dockerfiles/agent at master · DataDog/datadog-agent](https://github.com/DataDog/datadog-agent/tree/master/Dockerfiles/agent)
* [datadog/docker-dd-agent - Docker Hub](https://hub.docker.com/r/datadog/docker-dd-agent/)
* https://hub.docker.com/r/datadog/agent/tags

## Autodiscovery
* [Using Autodiscovery with Kubernetes and Docker](https://docs.datadoghq.com/agent/autodiscovery/)

## Custom metrics
* https://docs.datadoghq.com/developers/dogstatsd/

The easiest way to get your custom application metrics into Datadog is to send them to DogStatsD.
DogStatsD implements StatsD protrocol and DataDog specific extensions:

* Histogram metric type
* Service Checks and Events
* Tagging


## metrics
https://docs.datadoghq.com/agent/faq/docker-jmx/

```
docker exec -it <agent_container_name> agent configcheck
```

## Graphing
* https://docs.datadoghq.com/graphing/


* Aggregation group
    * for GCP
        * zone
        * project_id
        * 
* Aggregation methods
    * sum
    * min
    * max
    * avg

## Dashboard
* Screenboard
* timeboard

## Python
* https://www.datadoghq.com/blog/monitoring-flask-apps-with-datadog/

## MySQL
* https://www.datadoghq.com/blog/monitoring-mysql-performance-metrics/

Key MySQL Statistics

* Query throughput
* Query execution performance
* Connections
* Buffer pool usage
    * Innodb_buffer_pool_pages_total
        * Total number of pages in the buffer pool
    * Buffer pool utilization
        * Ratio of used to total pages in the buffer pool
    * Innodb_buffer_pool_read_requests
        * Requests made to the buffer pool
    * Innodb_buffer_pool_reads



(1) HTTP500 response 増 -> alert -> 
(2) HTTP500 response 増 -> alert ->



## Tips

#### API key and Application key

* API key
    * allows you to write data
* Application key
    * Requests tha read data requires Application key and `full access`

## Pricing
* [Datadog | Pricing](https://www.datadoghq.com/pricing/)

* Free
    * 1day
    * up to 5 host
* Pro
    * 15USD per host per month billed annually 
    * 18USD per host per month billed monthly
    * dataの保存期間15 month
    * container monitoring: 10 per host
    * custom metrics: 100 per host
* Enterprise
    * 23USD per host per month billed annually 
    * 27USD per host per month billed monthly
    * container monitoring: 20 per host
        * customize可能
    * custom metrics: 200 per host
        * customize可能
    * dataの保存期間15 month


## Reference
* [How to monitor Google Kubernetes Engine with Datadog](https://www.datadoghq.com/blog/monitor-google-kubernetes-engine/)
