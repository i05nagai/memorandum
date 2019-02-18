---
title: Application Auto Scaling
---

## Application Auto Scaling


## ScalingPolicy

* `ScalableDimension`
    * ecs:service:DesiredCount - The desired task count of an ECS service.
* `ServiceNamespace`
    * valid valiues: `ecs`
* `TargetTrackingScalingPolicyConfiguration`
    * ScaleOutCooldown
* `StepScalingPolicyConfiguration`
    * `AdjustmentType`
    * `Cooldown`
    * `MetricAggregationType`
        * The aggregation type for the CloudWatch metrics
        * `Average`, `Minimum`, `Maximum`
    * `MinAdjustmentMagnitude`
    * `StepAdjustments`
* `StepAdjustment`
    * `MetricIntervalLowerBound`
    * `ScalingAdjustment`
    * `MetricIntervalUpperBound`

## Reference
* https://docs.aws.amazon.com/autoscaling/application/APIReference/Welcome.html
