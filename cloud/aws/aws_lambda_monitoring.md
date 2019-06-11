---
title: AWS Lambda Monitoring
---

## AWS Lambda Monitoring


## Metrics
- https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-metrics.html

- Invocations
- Errors
- DeadLetterErrors
- Duration
- Throttles
- IteratorAge
- ConcurrentExecutions
- UnreservedConcurrentExecutions

## Throttle
- [Managing Concurrency \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)

On reaching the concurrency limit associated with a function, any further invocation requests to that function are throttled, i.e. the invocation doesn't execute your function.

## Reference
- [Lambda Error Hound: Chase Down Serverless Log Messages \- CloudProse \- Trek10 Blog](https://www.trek10.com/blog/lambda-error-hound/)
- [How to monitor Lambda functions \| Datadog](https://www.datadoghq.com/blog/how-to-monitor-lambda-functions/)
