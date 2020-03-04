---
title: Amazon CloudWatch
---

## Amazon CloudWatch

## Services
* [AWS Services That Publish CloudWatch Metrics \- Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html)

## Metrics filter
- [Searching and Filtering Log Data \- Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
- [Filter and Pattern Syntax \- Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html)

Aamazon CloudWatch allow us to create the metric from logs by filtering json .

#### Extract fields from JSON outputs.

```
{ $.field_name = *}
```

Then you can refer to this field with `$.field_name` in Metric Vlaue.


#### API
[put\-metric\-filter — AWS CLI 1\.16\.193 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/logs/put-metric-filter.html)

```
put-metric-filter
--log-group-name <value>
--filter-name <value>
--filter-pattern <value>
--metric-transformations <value>
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```

```
# for metric-transformations
[
  {
    "metricName": "string",
    "metricNamespace": "string",
    "metricValue": "string",
    "defaultValue": double
  }
  ...
]
```

#### Metric  filter
- [Filter and Pattern Syntax \- Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html)

## Reference
