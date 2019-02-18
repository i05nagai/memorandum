---
title: Amazon Elastic Container Service
---

## Amazon Elastic Container Service

## Service

#### LoadBalancer
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html

* ALB L7 LB
    * Application Load Balancers allow containers to use dynamic host port mapping
    * Application Load Balancers support path-based routing and priority rules
* ELB L4 LB

## Configuration

#### logConfiguration
* https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LogConfiguration.html
    * https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html
        * `awslogs`


log configuration options
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html#create_awslogs_logdriver_options

* `awslogs-create-group`
* `awslogs-datetime-format`
* `awslogs-region`
* `awslogs-group`
    * required
* `awslogs-stream-prefix`

```json
"logConfiguration": {
    "logDriver": "awslogs",
    "options": {
        "awslogs-group": "group"
    }
}
```

Amazon ECS container instances requires the following permissions

* `logs:CreateLogStream`
* `logs:PutLogEvents`

## Container agent
* https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html
* https://github.com/aws/amazon-ecs-agent
    * Github



```
"Source": "/etc/ecs",
"Source": "/cgroup",
"Destination": "/sys/fs/cgroup",
"Source": "/etc/pki",
"Destination": "/etc/pki",
"Source": "/proc",
"Destination": "/host/proc",
"Source": "/var/run",
"Destination": "/var/run",
"Source": "/var/run",
"Destination": "/var/run",
"Source": "/var/log/ecs",
"Destination": "/log",
"Source": "/var/lib/ecs/data",
"Destination": "/data",
"Source": "/var/cache/ecs",
"Destination": "/var/cache/ecs",
"Source": "/var/lib/ecs",
"Destination": "/var/lib/ecs",
"Source": "/var/lib/ecs",
"Destination": "/var/lib/ecs",
"Source": "/run/docker/plugins",
"Destination": "/run/docker/plugins",
"Source": "/etc/docker/plugins",
"Destination": "/etc/docker/plugins",
"Source": "/usr/lib/docker/plugins",
"Destination": "/usr/lib/docker/plugins",
```

##### Environment variables
* https://github.com/aws/amazon-ecs-agent#environment-variables

* `ECS_AGENT_CONFIG_FILE_PATH`
    * https://github.com/aws/amazon-ecs-agent/issues/409
* `ECS_IMAGE_CLEANUP_INTERVAL`
    * The time interval between automated image cleanup cycles. If set to less than 10 minutes, the value is ignored.
* `ECS_ENGINE_TASK_CLEANUP_WAIT_DURATION`
    * Time to wait to delete containers for a stopped task. If set to less than 1 minute, the value is ignored.
* `ECS_UPDATES_ENABLED`
* `ECS_AGENT_CONFIG_FILE_PATH=/etc/ecs/ecs.config.json`
* `ECS_UPDATE_DOWNLOAD_DIR=/var/cache/ecs`
* `ECS_CLUSTER`
    * The cluster this agent should check into.
* `ECS_ENABLE_TASK_IAM_ROLE_NETWORK_HOST=true`
    * Whether to enable IAM Roles for Tasks when launched with host network mode on the Container Instance
* `ECS_ENABLE_TASK_ENI=true`
    * Whether to enable task networking for task to be launched with its own network interface
* `ECS_ENGINE_TASK_CLEANUP_WAIT_DURATION=1m`
* `ECS_LOGFILE=/log/ecs-agent.log`
    * The location where logs should be written. Log level is controlled by ECS_LOGLEVEL.
* `ECS_LOGLEVEL`
* `ECS_DATADIR=/data`
* `ECS_ENABLE_AWSLOGS_EXECUTIONROLE_OVERRIDE=true`
* `ECS_AVAILABLE_LOGGING_DRIVERS=[\"json-file\",\"syslog\",\"awslogs\",\"none\"]`
* `ECS_ENABLE_TASK_IAM_ROLE=true`
* `SSL_CERT_DIR=/etc/pki/tls/certs`

#### Debug

```
echo "ECS_LOGLEVEL=debug" >> /etc/ecs/ecs.config
docker logs -f ecs-agent
```

#### Error1
* https://github.com/aws/amazon-ecs-agent/issues/294


Internet cannot be reacheable from the VPC.
Check route table settings.


#### Error2: ECS was unable to assume the role 
https://stackoverflow.com/questions/48997463/ecs-unable-to-assume-role



## Reference
* https://medium.com/@pahud/ulimit-of-nofile-in-amazon-ecs-optimized-ami-6790aedee582
