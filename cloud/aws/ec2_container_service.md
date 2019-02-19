---
title: EC2 Container Service
---

## EC2 Container Service
ECSの利用料金はかからない。
使用しているinstanceなどの利用料金がかかる。


## terms
* task definition
    * set of container similar to Pod in Kubenetes
    * the number of CPU and reserved memory
    * definition of docker image
    * GUIかjson fileで指定
    * taskをrunするときは、いずれかのclusterに属す必要がある
* service
    * service must be incldued by cluster
* task
* logConfiguration


## Placement strategy
https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PlacementStrategy.html

* `field`
    * `spread`
        * `instanceId`
        * `attribute:ecs.availability-zone`
    * `type=binpack`
        * `cpu`, `memory`
    * `random`
        * not used
* `type`
    * `random`, `spread`, `binpack`

## Container definition
https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html

## Task definition
* [タスク定義パラメーター - Amazon Elastic Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_definition_parameters.html)
* https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskDefinition.html


awslogs log driver

dockerのdriverにawslogs log deriverを指定すればCloud watch にlogを送信できる。
cloudwatchはlog groupごとにlogを管理しているが、aws logs logdriverではlog groupの作成はできないので自分で作成する。
事前にlog groupは作成しておく。
logdriverのoptionにいかを追加する。

```
                "options": {
                    "awslogs-group": "awslogs-mysql",
                    "awslogs-region": "ap-northeast-1",
                    "awslogs-stream-prefix": "awslogs-example"
                }
```

Network mode

Docker run で利用可能なnetworkmode と同じ
defaultは`bridge`.
noneにした場合port指定はできず、接続できない。
hostにした場合にnetworkのperformanceは最大限になる。

## Service
* [サービス - Amazon Elastic Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs_services.html)


## Networking
* https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html

awsvpc

* containers that belong to the same task can communicate over the localhost interface


## Cluster
* [Amazon ECS クラスター - Amazon Elastic Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ECS_clusters.html)

* container instanceは1つのclusterに属す
* region固有

## Container instance
* http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/launch_container_instance.html

clusterにcontainer instanceを登録する必要がある。
登録されているinsntaceに対してcontainerがdeployされる。
EC2で事前に起動しておく必要がある。

EC2instanceの作成と同じようにする。
但し以下を設定すうｒ．

* ami-cb3a8cad
* AWSServiceRoleForECS

ECS用のROLEを作成する。
新しく作る場合は以下を設定して作る

* use case
    * ECS
    * EC2 Role for EC2 Container Service 
* polycies
    * AmazonEC2ContainerServiceforEC2Role
* role
    * role名は任意

container instanceを起動して、数分するとdefault clusterに登録される。
default以外のclusterに登録したい場合は、EC2の環境変数の設定が必要。
EC2の`Advanced detail`->` user data`に以下のscriptを設定する。
一度EC2を起動して、既存のclusterに登録されている場合は、`deregisiter-container-instance`で登録を消す必要がある。

```
#!/bin/bash
echo ECS_CLUSTER=your_cluster_name >> /etc/ecs/ecs.config
```

```
aws ecs list-container-instances --cluster default
```


## Task Scheduling
* run task

* task placement
    * AZ balanced spread
        * AZ間AZ内のcontainer instance間でtaskを分散
    * AZ balanced BinPack
        * 利用可能な最小目盛でAZ間およびcontainer instance間でtaskを分散
    * BinPack
        * CPU/memoryの最小利用可能量に基いてtaskを配置
    * One Task Per Instance
        * container instanceのserviceから最大1taskを配置
    * Custom
        * 独自配置


## CLI

```
aws ecr get-login --no-include-email --region ap-northeast-1 
```

```
docker build -t airflow-sample .
```

### register-task-definition


### register-task-definition
* http://docs.aws.amazon.com/cli/latest/reference/ecs/register-task-definition.html
* [タスク定義パラメーター - Amazon Elastic Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_definition_parameters.html)


```sh
aws ecs register-task-definition
    --family <value>
    [--task-role-arn <value>]
    [--network-mode <value>]
    --container-definitions <value>
    [--volumes <value>]
    [--placement-constraints <value>]
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

* `--generate-cli-skeleton`
    * json templateを生成できる

Structure of json file

* cpu
* memory
    * MB
* memoryReservation
    * MB
* links(list)
    * same as `docker run --link`
* portMappings
    * same as `docker run --publish`
    * containerPort
    * hostPort
    * protocol
        * tcp/udp
* essential
    * true/false
    * trueならこのcontainerが止まった時に、task内のほかのcontainerもとまる
    * falseなら続行
    * 全てのtaskは1ついじょうのessential containerが必要
* entryPoint
    * `docker run --entrypoint`
* command
    * argument of `docker run`
* environment
    * docker run `--env`
    * name
    * value
* mountPoints
    * `docker run --volumne`
    * sourceVolume
        * name of volumne container
    * containerPath
        * path on the container to mount the host volume
    * readOnly
* volumesFrom
    * sourceContainer
    * readOnly
* linuxParameters
* hostname
    * `docker run --hostname`
* user
    * `docker run --user`
* workingDirectory
    * `docker run --workdir`
* disableNetworking
* privileged
    * `docker run --privileged`
* readonlyRootFilesystem
    * `docker run --read-only`
* dnsServers
    * `docker run --dns`
* dnsSearchDomains
    * `docker run --dns-search`
* extraHosts
* hostname
* ipAddress
    * `docker run --add-host`
* dockerLabels
    * `docker run --label`
    * key
    * value
* ulimits
    * `docker run --ulimits`
    * name
        * "core"|"cpu"|"data"|"fsize"|"locks"|"memlock"|"msgqueue"|"nice"|"nofile"|"nproc"|"rss"|"rtprio"|"rttime"|"sigpending"|"stack",
        "softLimit": integer,
        "hardLimit": integer
    * softLimit
    * hardLimit
* logConfiguration
    * `docker run --log-driver`
    * logDriver
        * nmae of log driver
    * options
        * key
        * value
* family
    * required
    * name of set of tasks
* taskRoleArn
    * Amazon Resource Name
* networkMode
* revision
* volumes
    * name
    * host
        * sourcePath
* status
    * status of the task definition
* requiresAttributes
* placementConstraints
    * 

template

```json
{
    "family": "",
    "taskRoleArn": "",
    "networkMode": "",
    "containerDefinitions": [
        {
            "name": "",
            "image": "",
            "cpu": 0,
            "memory": 0,
            "memoryReservation": 0,
            "links": [
                ""
            ],
            "portMappings": [
                {
                    "containerPort": 0,
                    "hostPort": 0,
                    "protocol": ""
                }
            ],
            "essential": true,
            "entryPoint": [
                ""
            ],
            "command": [
                ""
            ],
            "environment": [
                {
                    "name": "",
                    "value": ""
                }
            ],
            "mountPoints": [
                {
                    "sourceVolume": "",
                    "containerPath": "",
                    "readOnly": true
                }
            ],
            "volumesFrom": [
                {
                    "sourceContainer": "",
                    "readOnly": true
                }
            ],
            "linuxParameters": {
                "capabilities": {
                    "add": [
                        ""
                    ],
                    "drop": [
                        ""
                    ]
                }
            },
            "hostname": "",
            "user": "",
            "workingDirectory": "",
            "disableNetworking": true,
            "privileged": true,
            "readonlyRootFilesystem": true,
            "dnsServers": [
                ""
            ],
            "dnsSearchDomains": [
                ""
            ],
            "extraHosts": [
                {
                    "hostname": "",
                    "ipAddress": ""
                }
            ],
            "dockerSecurityOptions": [
                ""
            ],
            "dockerLabels": {
                "KeyName": ""
            },
            "ulimits": [
                {
                    "name": "",
                    "softLimit": 0,
                    "hardLimit": 0
                }
            ],
            "logConfiguration": {
                "logDriver": "",
                "options": {
                    "KeyName": ""
                }
            }
        }
    ],
    "placementConstraints": [
        {
            "expression": "",
            "type": "memberOf"
        }
    ],
    "volumes": [
        {
            "name": "",
            "host": {
                "sourcePath": ""
            }
        }
    ]
}
```

## create-service
* http://docs.aws.amazon.com/cli/latest/reference/ecs/create-service.html

```sh
  create-service
    [--cluster <value>]
    --service-name <value>
    --task-definition <value>
    [--load-balancers <value>]
    --desired-count <value>
    [--client-token <value>]
    [--role <value>]
    [--deployment-configuration <value>]
    [--placement-constraints <value>]
    [--placement-strategy <value>]
    [--network-configuration <value>]
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

* --cluster
    * 省略するとdefault cluster
    * short name or ARN
* --service-name
* --task-definition
    * name of task definition
* --generate-cli-skeleton
    * json formatのtemplateを作成

```json
{
    "cluster": "",
    "serviceName": "",
    "taskDefinition": "",
    "loadBalancers": [
        {
            "loadBalancerName": "",
            "containerName": "",
            "containerPort": 0
        }
    ],
    "desiredCount": 0,
    "clientToken": "",
    "role": "",
    "deploymentConfiguration": {
        "maximumPercent": 0,
        "minimumHealthyPercent": 0
    }
}
```

* cluster
* serviceName
* taskDefinition
* loadBalancers
    * loadBalancerName
    * containerName
        * load balancerに紐付けるcontainerの名前
        * container definition定義したもの
    * containerPort
        * loadbalancerに関連付けるport
* desiredCount
    * RUNNINGに保つtaskの数
* clientToken
* role
    * load brancerのrole
    * load balancerを使う場合は必須
* deploymentConfiguration
    * deploy時に実行されるtaskの数
    * maximumPercent
        * desiredCountが4, maximumPercentが200%のとき、4つのtaskを終了する前に4つのtaskを作成できる
        * defaultは200%
    * minimumHealthyPercent
        * deploy時にRUNNINGに保つtaskの割合
        * desiredCountが4, minimumHealthyPercentが50%のおき、2つのtaskを開始する前に、きぞんの2つを停止できる
        * consoleでは50%, aws cli, aws sdkでは100%

### create-cluster
* http://docs.aws.amazon.com/cli/latest/reference/ecs/create-cluster.html

```sh
aws ecs create-cluster
    [--cluster-name <value>]
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

clusterを作成するだけ。
cliからinstanceを登録する場合は`register-container-instance`を使用する。

```
aws ecs create-cluster --cluster-name "my_cluster"
```

### register-container-instance

```sh
aws ecs register-container-instance
    [--cluster <value>]
    [--instance-identity-document <value>]
    [--instance-identity-document-signature <value>]
    [--total-resources <value>]
    [--version-info <value>]
    [--container-instance-arn <value>]
    [--attributes <value>]
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

```json
{
    "cluster": "", 
    "instanceIdentityDocument": "", 
    "instanceIdentityDocumentSignature": "", 
    "totalResources": [
        {
            "name": "", 
            "type": "", 
            "doubleValue": null, 
            "longValue": 0, 
            "integerValue": 0, 
            "stringSetValue": [
                ""
            ]
        }
    ], 
    "versionInfo": {
        "agentVersion": "", 
        "agentHash": "", 
        "dockerVersion": ""
    }, 
    "containerInstanceArn": "", 
    "attributes": [
        {
            "name": "", 
            "value": ""
        }
    ]
}
```

* instanceIdentityDocument
* instanceIdentityDocumentSignature
* totalResources

### run-task

```sh
aws ecs run-task
    [--cluster <value>]
    --task-definition <value>
    [--overrides <value>]
    [--count <value>]
    [--started-by <value>]
    [--group <value>]
    [--placement-constraints <value>]
    [--placement-strategy <value>]
    [--network-configuration <value>]
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]
```

```json
{
    "cluster": "", 
    "taskDefinition": "", 
    "overrides": {
        "containerOverrides": [
            {
                "name": "", 
                "command": [
                    ""
                ], 
                "environment": [
                    {
                        "name": "", 
                        "value": ""
                    } ]
            }
        ]
    }, 
    "count": 0, 
    "startedBy": ""
}
```

* cluster
* taskDefinitino
* overrides
* count
* startedBy

### start-task


### register-container-instance
container instanceをclusterに登録する。
Run taskをする前に必要。



## Reference
* [AWS Black Belt Online Seminar 2016 Amazon EC2 Container Service](https://www.slideshare.net/AmazonWebServicesJapan/aws-black-belt-online-seminar-2016-amazon-ec2-container-service)
* * [Running Docker on AWS from the ground up](https://www.ybrikman.com/writing/2015/11/11/running-docker-aws-ground-up/)

