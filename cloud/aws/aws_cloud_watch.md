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

#### Metric filter
- [Filter and Pattern Syntax \- Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html)

## Cloudwatch agent
- [Installing the CloudWatch Agent Using the Command Line \- Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/installing-cloudwatch-agent-commandline.html)
- [Download and Configure the CloudWatch Agent Using the Command Line \- Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.html)

```
https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
```

#### Configuration
[Create the CloudWatch Agent Configuration File with the Wizard \- Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.html)
There is a command to generate configuration with the Wizard.

```
amazon-cloudwatch-agent-config-wizard
```

- [Manually Create or Edit the CloudWatch Agent Configuration File \- Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html)
    - Configuration examples and description

Recommended path is `/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json`

#### Metrics
- [Metrics Collected by the CloudWatch Agent \- Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html)

#### Comparison operator
The specified static value (metric) will be used as a operand.
If GreaterThanOrEqualToThreshold is specified, it will be `metric >= threshold`.
This is same for Cloud fomration template and API.



#### Tips
- [Troubleshoot a Unified CloudWatch Agent That's Not Pushing Log Events](https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-push-logs-with-unified-agent/)
- [CloudWatch Logs Agent Reference \- Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html)
- [Troubleshooting the CloudWatch Agent \- Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/troubleshooting-CloudWatch-Agent.html#CloudWatch-Agent-options-help)
- [CloudWatch Agent Configuration File: Logs Section](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-common-scenarios.html)
- [Collecting Metrics and Logs from Amazon EC2 Instances and On\-Premises Servers with the CloudWatch Agent \- Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

## Cloudwatch Log
- [Streaming CloudWatch Logs to Kinesis Data Streams](https://aws.amazon.com/premiumsupport/knowledge-center/streaming-cloudwatch-logs/)
- [Using CloudWatch Logs Subscription Filters \- Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs//SubscriptionFilters.html#FirehoseExample)

## Retention date of metrics
- [Amazon CloudWatch FAQs \- Amazon Web Services \(AWS\)](https://aws.amazon.com/cloudwatch/faqs/)

- from the previous 14 days to 15 months
- Data points with a period of less than 60 seconds: 3 hours
- 1 minute: 14 days
- 5 minutes: 63 days
- 1 hour: 455 days
- if you request for 1-minute data from 5 months back, the UI will automatically change the granularity to 1-hour and the GetMetricStatistics API will not return any output.

## Reference
