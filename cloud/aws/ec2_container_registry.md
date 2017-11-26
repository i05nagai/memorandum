---
title: EC2 Container Registry
---

## EC2 Container Registry

## Push to ECR

get login command

```
aws ecr get-login --no-include-email --region <region>
```

`docker login`commandが出力されるので実行する。


* region
    * ap-northeast-1
        o
```
docker tag <image_name>:latest <repository_host>/<repository_name>/<image_name>:<tag>
```

* `<repository_host>`
* `<repository_name>`

## Reference
