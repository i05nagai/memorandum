---
title: serverless-plugin-aws-alerts
---

## serverless-plugin-aws-alerts


## Naming
- Alarm name
    - `<lambda-name>-<function-name>-<function-ref>`
        - all of the name is normalized
        - `<function-name>` will be upper camel case
- filter name
    - `<lambda-name>-<function-name><metric>LogMetricFilter(ALERT|OK)-<ref>`
    - `<prefix>-<AlarmName>LogMetricFilter`
- metric name
    - `<lamnda-name>/<Metric>DashLambdaFunction`

## Reference
- [ACloudGuru/serverless\-plugin\-aws\-alerts: A Serverless Framework plugin that creates CloudWatch alarms for functions\.](https://github.com/ACloudGuru/serverless-plugin-aws-alerts)
