---
title: Auto Scaling
---

## Auto Scaling


## Terms
* Auto scaling group
* auto scaling group size


## Scaling Group

## Autocaling group
https://docs.aws.amazon.com/autoscaling/ec2/APIReference/Welcome.html

## Amazon EC2 Auto Scaling Lifecycle Hooks
[Amazon EC2 Auto Scaling Lifecycle Hooks \- Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)

* 1. The Auto Scaling group responds to scale-out events by launching instances and scale-in events by terminating instances.
* 2. The lifecycle hook puts the instance into a wait state (Pending:Wait or Terminating:Wait)
* 3. You can perform a custom action using one or more of the following options
* 4. By default, the instance remains in a wait state for one hour, and then the Auto Scaling group continues the launch or terminate process (Pending:Proceed or Terminating:Proceed)


## Dynamic Scaling for Amazon EC2 Auto Scaling
* [Dynamic Scaling for Amazon EC2 Auto Scaling \- Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)


* Target tracking scaling
* Step scaling
* Simple scaling

####  Target tracking scaling
[Target Tracking Scaling Policies for Amazon EC2 Auto Scaling \- Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)

* Not all metrics work for target tracking.

## Reference
* http://docs.aws.amazon.com/autoscaling/latest/userguide/AutoScalingGroup.html
* http://docs.aws.amazon.com/ja_jp/autoscaling/latest/userguide/AutoScalingGroup.html
* https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
