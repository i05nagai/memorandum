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


#### Datadog metric and Cloud watch metric
* aws.lambda.iterator_age
    * iterator age
    * 1 sec
    * average
* aws.lambda.invocation
    * invocation
    * 1 sec
    * sum
* aws.lambda.duration
    * duration average
    * 5 min?
    * Average
* aws.lambda.duration.maximum
* aws.dynamodb.consumed_write_capacity_units
    * sum of ConsumedWriteCapacityUnit in 1 sec / 60 sec
    * To make it equal to table metrics, you need to add `globalsecondaryindexname: none`. Otherwise it contains ConsumedWriteCapacityUnit for global secondary index
* aws.dynamodb.consumed_read_capacity_units
    * sum of ConsumedReadCapacityUnit in 1 sec / 60 sec
    * To make it equal to table metrics, you need to add `globalsecondaryindexname: none`. Otherwise it contains ConsumedReadCapacityUnit for global secondary index
* aws.dynamodb.system_error
    * sum of BatchWriteItem SystemError
* aws.dynamodb.user_error
    * this metrics shows the number of user errors in the AWS accounts
* aws.dynamodb.write_throttle


Custom metrics

AWS custom metrics are collected if you check the checkbox in AWS integration.
The name of metrics in datadog will be normalized.
e.g. `-` -> `_`. `<namespace>.<metric_name>`


## Dashboard JSON
- [Graphing with JSON](https://docs.datadoghq.com/dashboards/graphing_json/)

```json
DASHBOARD_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
        "layout_type": {"enum": ["ordered", "free"]},
        "is_read_only": {"type": "boolean"},
        "template_variables": {"type": "array", "items": TEMPLATE_VARIABLE_SCHEMA},
        "notify_list": {"type": "array", "items": {"type": "string"}},
        "widgets": {
            "type": "array",
            "items": WIDGET_SCHEMA
        }
    },
    "required": ["title", "layout_type", "widgets"],
}
```


### Widget
- [Widget JSON schema](https://docs.datadoghq.com/dashboards/graphing_json/widget_json/)


```
{ (...)
  "widgets": [
    {
      "definition": {
        "markers": [
          {
            "display_type": "ok dashed",
            "label": "OK",
            "value": "0 < y < 50"
          },
          {
            "display_type": "error dashed",
            "label": "ALERT",
            "value": "y > 80"
          },
          {
            "display_type": "warning dashed",
            "label": "WARNING",
            "value": "50 < y < 80"
          }
        ],
        "requests": [(...)],
        "title": "CPU with markers",
        "type": "timeseries"
      },
(...)
},
```

###
- [Request JSON schema](https://docs.datadoghq.com/dashboards/graphing_json/request_json/)


## Reference
* [How to monitor Google Kubernetes Engine with Datadog](https://www.datadoghq.com/blog/monitor-google-kubernetes-engine/)
