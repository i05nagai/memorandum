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

## Qotas
- https://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html

- Custom actions: 24 hours
- Maximum number of total pipelines per Region in an AWS account: 1000


## Reference
- https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html
