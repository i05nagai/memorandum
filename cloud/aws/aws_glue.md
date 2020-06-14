---
title: AWS Glue
---

## AWS Glue


## TErm
* AWS Glue Data Catalog
    * The persistent metadata store in AWS Glue. Each AWS account has one AWS Glue Data Catalog.
    * It contains table definitions, job definitions, and other control information to manage your AWS Glue environment.
* classifier
* connection
* crawler
    * A program that connects to a data store (source or target), progresses through a prioritized list of classifiers to determine the schema for your data, and then creates metadata in the AWS Glue Data Catalog.
* database
    * A set of associated table definitions organized into a logical group in AWS Glue.
* Data store, data source, data target
* Development endpoint
    * An environment that you can use to develop and test your AWS Glue scripts.
* job
* notebook server
* Script
    * Code that extracts data from sources, transforms it, and loads it into targets.
    * AWS Glue generates PySpark or Scala scripts. PySpark is a Python dialect for ETL programming.

## Development Endpoints
Running a job takes approx 10-15 min at least since it spins up the cluster and provision them.
To develop ETL script faster, AWS provides an endpoint to instances.
You can attach Notebooks to the endpoint to run the script continuously.

##### Arguments
- [Enable Special Parameters in an AWS Glue Job using AWS CloudFormation](https://aws.amazon.com/premiumsupport/knowledge-center/cloudformation-glue-special-parameters/)
- [Special Parameters Used by AWS Glue \- AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html)


## Logging
- [Enabling Continuous Logging for AWS Glue Jobs \- AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging-enable.html)
    - Logging on 
- [AWS Developer Forums: Custom Cloudwatch Log Group for Glue \.\.\.](https://forums.aws.amazon.com/thread.jspa?messageID=898174)
    - Output of jobs goes to `/aws-glue/jobs/output`
    - Error of jobs goes to `/aws-glue/jobs/error`
- [amazon web services \- Custom Cloudwatch Log Group for Glue job \- Stack Overflow](https://stackoverflow.com/questions/55044341/custom-cloudwatch-log-group-for-glue-job)

## Metrics
- [Monitoring AWS Glue Using Amazon CloudWatch Metrics \- AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.html)


## API
- [DynamicFrame Class \- AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-map)
- [aws\-glue\-libs/awsglue at master · awslabs/aws\-glue\-libs](https://github.com/awslabs/aws-glue-libs/tree/master/awsglue)
    - source code


* update_job
    * There are some mondatory fields to update the parameters
    * `Command`
    * `Role`

## Custom library
- [Adding Python Shell Jobs in AWS Glue \- AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-job-python.html)


## Reference
