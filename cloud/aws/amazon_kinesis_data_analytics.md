---
title: Amazon Kinesis Data Analytics
---

## Amazon Kinesis Data Analytics
With Amazon Kinesis Data Analytics, you can process and analyze streaming data using standard SQL.
Common use cases are

* Generate time-series analytics
* Feed real-time dashboards
* Create real-time metrics

## State backend
RocksDBStateBackend is used.

[rocksdb \- RocksDBStateBackend in Flink: how does it works exactly? \- Stack Overflow](https://stackoverflow.com/questions/58644940/rocksdbstatebackend-in-flink-how-does-it-works-exactly)

## API


#### Describe application
```
{
    "ApplicationDetail": {
        "ApplicationARN": "<arn>",
        "ApplicationDescription": "<description>",
        "ApplicationName": "<arn>",
        "RuntimeEnvironment": "FLINK-1_11",
        "ServiceExecutionRole": "<arn>",
        "ApplicationStatus": "RUNNING",
        "ApplicationVersionId": 15,
        "CreateTimestamp": 1635248936.0,
        "LastUpdateTimestamp": 1636993761.0,
        "ApplicationConfigurationDescription": {
            "ApplicationCodeConfigurationDescription": {
                "CodeContentType": "ZIPFILE",
                "CodeContentDescription": {
                    "CodeMD5": "<md5>",
                    "CodeSize": 74033626,
                    "S3ApplicationCodeLocationDescription": {
                        "BucketARN": "<arn>",
                        "FileKey": "<key>"
                    }
                }
            },
            "RunConfigurationDescription": {
                "ApplicationRestoreConfigurationDescription": {
                    "ApplicationRestoreType": "RESTORE_FROM_LATEST_SNAPSHOT"
                },
                "FlinkRunConfigurationDescription": {
                    "AllowNonRestoredState": false
                }
            },
            "FlinkApplicationConfigurationDescription": {
                "CheckpointConfigurationDescription": {
                    "ConfigurationType": "DEFAULT",
                    "CheckpointingEnabled": true,
                    "CheckpointInterval": 60000,
                    "MinPauseBetweenCheckpoints": 5000
                },
                "MonitoringConfigurationDescription": {
                    "ConfigurationType": "CUSTOM",
                    "MetricsLevel": "OPERATOR",
                    "LogLevel": "INFO"
                },
                "ParallelismConfigurationDescription": {
                    "ConfigurationType": "DEFAULT",
                    "Parallelism": 1,
                    "ParallelismPerKPU": 1,
                    "CurrentParallelism": 1,
                    "AutoScalingEnabled": true
                }
            },
            "EnvironmentPropertyDescriptions": {
                "PropertyGroupDescriptions": [
                    {
                        "PropertyGroupId": "<group-id>",
                        "PropertyMap": {
                            "<key1>": "<value1>"
                        }
                    }
                ]
            },
            "ApplicationSnapshotConfigurationDescription": {
                "SnapshotsEnabled": false
            },
            "VpcConfigurationDescriptions": [
                {
                    "VpcConfigurationId": "3.1",
                    "VpcId": "<vpc-id>",
                    "SubnetIds": [
                        "<subnet-id>"
                    ],
                    "SecurityGroupIds": [
                        "<securitygroup-id>"
                    ]
                }
            ]
        },
        "CloudWatchLoggingOptionDescriptions": [
            {
                "CloudWatchLoggingOptionId": "2.1",
                "LogStreamARN": "<log-arn>"
            }
        ],
        "ApplicationMaintenanceConfigurationDescription": {
            "ApplicationMaintenanceWindowStartTime": "22:00",
            "ApplicationMaintenanceWindowEndTime": "06:00"
        },
        "ApplicationVersionUpdatedFrom": 14,
        "ConditionalToken": "<token>",
        "ApplicationMode": "STREAMING"
    }
}
```

```
{
    "ApplicationDetail": {
        "ApplicationARN": "<arn>",
        "ApplicationName": "<applicationname>",
        "RuntimeEnvironment": "FLINK-1_11",
        "ServiceExecutionRole": "<arn>",
        "ApplicationStatus": "READY",
        "ApplicationVersionId": 1,
        "CreateTimestamp": 1636999825.0,
        "LastUpdateTimestamp": 1636999825.0,
        "ApplicationConfigurationDescription": {
            "FlinkApplicationConfigurationDescription": {
                "CheckpointConfigurationDescription": {
                    "ConfigurationType": "DEFAULT",
                    "CheckpointingEnabled": true,
                    "CheckpointInterval": 60000,
                    "MinPauseBetweenCheckpoints": 5000
                },
                "MonitoringConfigurationDescription": {
                    "ConfigurationType": "CUSTOM",
                    "MetricsLevel": "APPLICATION",
                    "LogLevel": "INFO"
                },
                "ParallelismConfigurationDescription": {
                    "ConfigurationType": "CUSTOM",
                    "Parallelism": 1,
                    "ParallelismPerKPU": 1,
                    "CurrentParallelism": 1,
                    "AutoScalingEnabled": true
                }
            },
            "ApplicationSnapshotConfigurationDescription": {
                "SnapshotsEnabled": false
            }
        },
        "CloudWatchLoggingOptionDescriptions": [
            {
                "CloudWatchLoggingOptionId": "1.1",
                "LogStreamARN": "<arn>"
            }
        ],
        "ApplicationMaintenanceConfigurationDescription": {
            "ApplicationMaintenanceWindowStartTime": "22:00",
            "ApplicationMaintenanceWindowEndTime": "06:00"
        },
        "ConditionalToken": "<token>",
        "ApplicationMode": "STREAMING"
    }
}
```

## Tips

#### Error

```
Received response status [FAILED] from custom resource. Message returned: Kinesis Analytics currently supports only 1 VPC configuration(s) (RequestId: <request-id>)
```




## Reference
* [What Is Amazon Kinesis Data Analytics? \- Amazon Kinesis Data Analytics](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html)
