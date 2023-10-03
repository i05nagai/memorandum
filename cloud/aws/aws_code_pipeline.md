---
title: AWS CodePipeline
---

## AWS CodePipeline

## Concepts
https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html

- Pipelines
- artifacts
    - Your source code is an example of an artifact.
- Stages
    - A stage is a logical unit you can use to isolate an environment and to limit the number of concurrent changes in that environment.
    - Each stage contains actions that are performed on the application artifacts.
    - e.g. build stage, deployment stage
- Actions
    - stage consists of multiple actions
    - An action is a set of operations performed on application code and configured so that the actions run in the pipeline at a specified point.
    - Valid CodePipeline action types are source, build, test, deploy, approval, and invoke.
    - https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers
- RunOrder
    - The default is 1. The value must be a positive integer (natural number).
    - To specify a serial sequence of actions, use the smallest number for the first action and larger numbers for each of the rest of the actions in sequence.
    - To specify parallel actions, use the same integer for each action you want to run in parallel.

## Qotas
- https://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html

- Custom actions: 24 hours
- Maximum number of total pipelines per Region in an AWS account: 1000
- Maximum number of actions per pipeline: 500
- Maximum number of parallel actions in a stage: 50
- Maximum number of sequential actions in a stage: 50
- Number of actions in a stage: 1-50
- Number of stages in a pipeline: 2-50


## Reference
- https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html
