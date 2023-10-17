---
title: AWS Code Build
---

## AWS Code Build


## Pricing
- https://aws.amazon.com/codebuild/pricing/


## Queue
If the build project does not have a concurrent build limit set, builds are queued if the number of running builds reaches the concurrent build limit for the platform and compute type.
The maximum number of builds in a queue is five times the concurrent build limit.

## Quotas
- https://docs.aws.amazon.com/codebuild/latest/userguide/limits.html

- Quotas for the maximum number of concurrent running builds vary, depending on the compute type.
    - For some platforms and compute types, the default is 20

- Concurrently running builds for ARM/Large environment
    - 1
    - account level
- Concurrently running builds for ARM/Small environment
    - 1
    - account level
- Concurrently running builds for Linux GPU Large environment
    - 0
    - account level
- Concurrently running builds for Linux GPU Small environment
    - 0
    - account level
- Concurrently running builds for Linux/2XLarge environment
    - 0
    - account level
- Concurrently running builds for Linux/Large environment
    - 1
    - account level
- Concurrently running builds for Linux/Medium environment
    - 1
    - account level
- Concurrently running builds for Linux/Small environment
    - 1
    - account level
- Concurrently running builds for Windows Server 2019/Large environment
    - 1
    - account level
- Concurrently running builds for Windows Server 2019/Medium environment
    - 1
    - account level
- Concurrently running builds for Windows/Large environment
    - 1
    - account level
- Concurrently running builds for Windows/Medium environment
    - 1
    - account level

## Queue Error

```
Error calling startBuild: Cannot have more than 1 builds in queue for the account (Service: AWSCodeBuild; Status Code: 400; Error Code: AccountLimitExceededException; Request ID: ; Proxy: null)
````


## Reference
- https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html
