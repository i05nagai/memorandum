---
title: Elastic Container Registry
---

## Elastic Container Registry

## Pricing
* storage
    * 0.1 USD per GB month
* Data transfer
    * upload
        * 0 USD
    * download
        * First 1GB/month free
        * Up to 10TB/month 

## Push to ECR

get login command

```
aws ecr get-login --no-include-email --region <region>
```

`docker login`commandが出力されるので実行する。


* region
    * ap-northeast-1

```
docker tag <image_name>:latest <repository_host>/<repository_name>/<image_name>:<tag>
```

* `<repository_host>`
* `<repository_name>`


## Reference
