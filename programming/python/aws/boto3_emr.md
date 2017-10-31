---
title: Boto3 EMR
---

## Boto3 EMR

Create cluster

* [InstanceFleetConfig - Amazon Elastic MapReduce](https://docs.aws.amazon.com/ElasticMapReduce/latest/API/API_InstanceFleetConfig.html)


```python
import boto3


client = boto3.client('emr')
# ?
cluster_name = ''
# if you omit, 
log_uri = ''
# ?
additional_info = ''
#
ami_version = ''
#
release_label = 'emr-5.6.0'
#
instances = {
    #
    'MasterInstanceType': '',
    #
    'SlaveInstanceType': '',
    #
    'InstanceCount': 123,
}
#
configurations = [
    {
        'Classification': 'string',
        'Configurations': {'... recursive ...'},
        'Properties': {
            'string': 'string'
        }
    },
]
#
ebs_configuration = {
    'EbsBlockDeviceConfigs': [
        {
            'VolumeSpecification': {
                'VolumeType': 'string',
                'Iops': 123,
                'SizeInGB': 123
            },
            'VolumesPerInstance': 123
        },
    ],
    'EbsOptimized': True|False
}
#
cloud_watch_alarm_definition = {
    'ComparisonOperator': 'GREATER_THAN_OR_EQUAL'|'GREATER_THAN'|'LESS_THAN'|'LESS_THAN_OR_EQUAL',
    'EvaluationPeriods': 123,
    'MetricName': 'string',
    'Namespace': 'string',
    'Period': 123,
    'Statistic': 'SAMPLE_COUNT'|'AVERAGE'|'SUM'|'MINIMUM'|'MAXIMUM',
    'Threshold': 123.0,
    'Unit': 'NONE'|'SECONDS'|'MICRO_SECONDS'|'MILLI_SECONDS'|'BYTES'|'KILO_BYTES'|'MEGA_BYTES'|'GIGA_BYTES'|'TERA_BYTES'|'BITS'|'KILO_BITS'|'MEGA_BITS'|'GIGA_BITS'|'TERA_BITS'|'PERCENT'|'COUNT'|'BYTES_PER_SECOND'|'KILO_BYTES_PER_SECOND'|'MEGA_BYTES_PER_SECOND'|'GIGA_BYTES_PER_SECOND'|'TERA_BYTES_PER_SECOND'|'BITS_PER_SECOND'|'KILO_BITS_PER_SECOND'|'MEGA_BITS_PER_SECOND'|'GIGA_BITS_PER_SECOND'|'TERA_BITS_PER_SECOND'|'COUNT_PER_SECOND',
    'Dimensions': [
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
}
#
rules = [
    {
        'Name': 'string',
        'Description': 'string',
        'Action': {
            'Market': 'ON_DEMAND'|'SPOT',
            'SimpleScalingPolicyConfiguration': {
                'AdjustmentType': 'CHANGE_IN_CAPACITY'|'PERCENT_CHANGE_IN_CAPACITY'|'EXACT_CAPACITY',
                'ScalingAdjustment': 123,
                'CoolDown': 123
            }
        },
        'Trigger': {
            'CloudWatchAlarmDefinition': cloud_watch_alarm_definition
        }
    },
]
#
instance_groups = [
    {
        'Name': 'string',
        'Market': 'ON_DEMAND'|'SPOT',
        'InstanceRole': 'MASTER'|'CORE'|'TASK',
        'BidPrice': 'string',
        'InstanceType': 'string',
        'InstanceCount': 123,
        'Configurations': configurations,
        'EbsConfiguration': ebs_configuration,
        'AutoScalingPolicy': {
            'Constraints': {
                'MinCapacity': 123,
                'MaxCapacity': 123
            },
            'Rules': rules
        }
    },
]
#
instance_fleets = [
    {
        'Name': 'string',
        'InstanceFleetType': 'MASTER'|'CORE'|'TASK',
        'TargetOnDemandCapacity': 123,
        'TargetSpotCapacity': 123,
        'InstanceTypeConfigs': [
            {
                'InstanceType': 'string',
                'WeightedCapacity': 123,
                'BidPrice': 'string',
                'BidPriceAsPercentageOfOnDemandPrice': 123.0,
                'EbsConfiguration': {
                    'EbsBlockDeviceConfigs': [
                        {
                            'VolumeSpecification': {
                                'VolumeType': 'string',
                                'Iops': 123,
                                'SizeInGB': 123
                            },
                            'VolumesPerInstance': 123
                        },
                    ],
                    'EbsOptimized': True|False
                },
                'Configurations': [
                    {
                        'Classification': 'string',
                        'Configurations': {'... recursive ...'},
                        'Properties': {
                            'string': 'string'
                        }
                    },
                ]
            },
        ],
        'LaunchSpecifications': {
            'SpotSpecification': {
                'TimeoutDurationMinutes': 123,
                'TimeoutAction': 'SWITCH_TO_ON_DEMAND'|'TERMINATE_CLUSTER',
                'BlockDurationMinutes': 123
            }
        }
    },
]
#
bootstrap_actions = [
    {
        'Name': 'string',
        'ScriptBootstrapAction': {
            'Path': 'string',
            'Args': [
                'string',
            ]
        }
    },
]
#
configurations = [
    {
        'Classification': 'string',
        'Configurations': {'... recursive ...'},
        'Properties': {
            'string': 'string'
        }
    },
]

response = client.run_job_flow(
    Name='string',
    LogUri='string',
    AdditionalInfo='string',
    AmiVersion='string',
    ReleaseLabel='string',
    Instances={
        'MasterInstanceType': 'string',
        'SlaveInstanceType': 'string',
        'InstanceCount': 123,
        'InstanceGroups': instance_groups,
        'InstanceFleets': instance_fleets,
        'Ec2KeyName': 'string',
        'Placement': {
            'AvailabilityZone': 'string',
            'AvailabilityZones': [
                'string',
            ]
        },
        'KeepJobFlowAliveWhenNoSteps': True|False,
        'TerminationProtected': True|False,
        'HadoopVersion': 'string',
        'Ec2SubnetId': 'string',
        'Ec2SubnetIds': [
            'string',
        ],
        'EmrManagedMasterSecurityGroup': 'string',
        'EmrManagedSlaveSecurityGroup': 'string',
        'ServiceAccessSecurityGroup': 'string',
        'AdditionalMasterSecurityGroups': [
            'string',
        ],
        'AdditionalSlaveSecurityGroups': [
            'string',
        ]
    },
    BootstrapActions=bootstrap_actions,
    SupportedProducts=[
        'string',
    ],
    NewSupportedProducts=[
        {
            'Name': 'string',
            'Args': [
                'string',
            ]
        },
    ],
    Applications=[
        {
            'Name': 'string',
            'Version': 'string',
            'Args': [
                'string',
            ],
            'AdditionalInfo': {
                'string': 'string'
            }
        },
    ],
    Configurations=configurations,
    VisibleToAllUsers=True|False,
    JobFlowRole='string',
    ServiceRole='string',
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ],
    SecurityConfiguration='string',
    AutoScalingRole='string',
    ScaleDownBehavior='TERMINATE_AT_INSTANCE_HOUR'|'TERMINATE_AT_TASK_COMPLETION',
    CustomAmiId='string',
    EbsRootVolumeSize=123,
    RepoUpgradeOnBoot='SECURITY'|'NONE'
)
```


* Name
    * 必須
* InstanceFleetType
    * 必須


戻り値は以下。

```
{
    'JobFlowId': 'string'
}
```


Add steps

```python
step = {
    'Name': 'string',
    'ActionOnFailure': 'TERMINATE_JOB_FLOW'|'TERMINATE_CLUSTER'|'CANCEL_AND_WAIT'|'CONTINUE',
    'HadoopJarStep': {
        'Properties': [
            {
                'Key': 'string',
                'Value': 'string'
            },
        ],
        'Jar': 'string',
        'MainClass': 'string',
        'Args': [
            'string',
        ]
    }
}
response = client.add_job_flow_steps(
    JobFlowId='string',
    Steps=[step]
)
```

戻り値はstep idのlist

```
{
    'StepIds': [
        'string',
    ]
}
```

## Reference
* [Boto3でEMR - /var/log/laughingman7743.log](http://laughingman7743.hatenablog.com/entry/2016/02/11/185319)
* [EMR — Boto 3 Docs 1.4.4 documentation](https://boto3.readthedocs.io/en/latest/reference/services/emr.html)
