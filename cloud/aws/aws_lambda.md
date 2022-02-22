---
title: AWS Lambda
---

## AWS Lambda

Use case

* Invoke lambda function over HTTPS
    * [Using AWS Lambda with Amazon API Gateway \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-on-demand-https.html)
    * In many cases, lambda functions are invoked from some event sources.
    * Amazon API Gateway enables AWS lambda to have custom REST APIs and endpoints

* Supported Language
    * Node.js
    * Java
    * C#
    * Python
    * Go
    * Powershell


## CLI

```
aws lambda
```

```
aws lambda create-function \
    --function-name CreateThumbnail \
    --zip-file fileb://deploy-package.zip \
    --handler index.handler \
    --runtime python3 \
    --role role-arn \
    --timeout 10 \
    --memory-size 1024
```

```
aws lambda invoke
          --function-name <value>
          [--invocation-type <value>]
          [--log-type <value>]
          [--client-context <value>]
          [--payload <value>]
          [--qualifier <value>]
          outfile <value>
#
aws lambda invoke \
    --function-name CreateThumbnail \
    --invocation-type Event \
    --payload file://inputfile.txt outputfile.txt
```

```
aws lambda add-permission \
          --function-name <value>
          --statement-id <value>
          --action <value>
          --principal <value>
          [--source-arn <value>]
          [--source-account <value>]
          [--event-source-token <value>]
          [--qualifier <value>]
          [--revision-id <value>]
          [--cli-input-json <value>]
          [--generate-cli-skeleton <value>]
# Example
aws lambda add-permission \
    --function-name CreateThumbnail \
    --principal s3.amazonaws.com \
    --statement-id some-unique-id \
    --action "lambda:InvokeFunction" \
    --source-arn arn:aws:s3:::sourcebucket \
    --source-account bucket-owner-account-id
```

* `--function-name <value>`
    * format
        * `MyFunction`
        * `arn:aws:lambda:us-west-2:123456789012:function:MyFunction`
        * `123456789012:function:MyFunction`
* `--statement-id <value>`
    * A unique statement identifier.
* `--action <value>`
    * The AWS Lambda action you want to  allow  in  this  statement.
    * Each Lambda  action is a string starting with lambda: followed by the API name
* `--principal <value>`
    * The  principal  who is getting this permission

```
aws lambda get-policy
          --function-name <value>
          [--qualifier <value>]
          [--cli-input-json <value>]
          [--generate-cli-skeleton <value>]
#
aws lambda get-policy \
    --function-name function-name
```

## Concepts
* BatchSize
    * The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.
    * The default for Amazon Kinesis and Amazon DynamoDB is 100 records.
    * Both the default and maximum for Amazon SQS are 10 messages.

## Python
* [AWS Lambda Function Handler in Python \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/python-programming-model-handler-types.html)

```
# event is dict
def handler_name(event, context):
    return some_value
```

* `event`
    * AWS Lambda uses this parameter to pass in event data to the handler. This parameter is usually of the Python dict type. It can also be list, str, int, float, or NoneType type.
* `context`
    * AWS Lambda uses this parameter to provide runtime information to your handler. This parameter is of the LambdaContext type.
    * [AWS Lambda Context Object in Python \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html)

* [AWS Lambda Deployment Package in Python \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)


```
mkdir deploy-package
cd deploy-package
pip install -r ../requirements.txt --target .
zip -r9 ../function.zip .
cd ../
# add your code
zip -g function.zip function.py
# upload
aws lambda update-function-code --function-name python37 --zip-file fileb://function.zip
```

Logging

* The following Python statements generate log entries
    * Logger functions in the logging module 
    * print statements.
* Both print and logging.* functions write logs to CloudWatch Logs but the logging.* functions write additional information to each log entry, such as time stamp and log level.
* Finding log
    * In the AWS Lambda console
    * In the response header, when you invoke a Lambda function programmatically
        * If you invoke a Lambda function programmatically, you can add the LogType parameter to retrieve the last 4 KB of log data that is written to CloudWatch Logs
        * `x-amz-log-results`
    * In CloudWatch Logs

Error

* If your Lambda function raises an exception, AWS Lambda recognizes the failure and serializes the exception information into JSON and returns it.

```json
{
  "errorMessage": "I failed!",
  "stackTrace": [
    [
      "/var/task/lambda_function.py",
      3,
      "my_always_fails_handler",
      "raise Exception('I failed!')"
    ]
  ],
  "errorType": "Exception"
}
```

Tracing

* Use AWS X-ray

## Scaling behavior
* [Understanding Scaling Behavior \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/scaling.html)


events (or requests) per second * function duration

* Request Rate

## Limits
* Concurrent executions
    * Defualt limit: 1000
* Function storage per region
    * Default limit: 75GGB

* Function memory allocation
    * 128 MB to 3008 MB, in 64 MB increments.
* Function timeout
    * 900 seconds (15 minutes)
* Function environment variables
    * 4 KB
* Invocation payload (request and response)
    * 6 MB (synchronous)
* 256 KB (asynchronous)
* Deployment package size
    * 50 MB (zipped)
    * 256 MB (unzipped)
* 3 MB (console editor)
* Test events (console editor)
    * 10
* `/tmp` directory storage
    * 512 MB
* File descriptors
    * 1024
* Execution processes/threads
    * 1024


## Best practice
* Function
    * Take advantage of Execution Context reuse to improve the performance of your function
    * Use AWS Lambda Environment Variables to pass operational parameters to your function.
    * Control the dependencies in your function's deployment package
    * Avoid using recursive code 
* Function configuration
    * Do performance testing your Lambda function
    * Do load test your Lambda function
        * to determine an optimum timeout value
    * Use most-restrictive permissions when setting IAM policies
    * Be familiar with AWS Lambda Limits.
    * Delete Lambda functions that you are no longer using
* Alarming and Metrics
    * Use AWS Lambda Metrics and CloudWatch Alarms instead of creating or updating a metric from within your Lambda function code.
    * Leverage your logging library and AWS Lambda Metrics and Dimensions to catch app errors (e.g. ERR, ERROR, WARNING, etc.)
* Stream Event Invokes
    * Test with different batch and record size
    * Increase Kinesis stream processing throughput by adding shards.
* Async Invokes
* Lambda VPC
    * Don't put your Lambda function in a VPC unless you have to.

## Amazon API Gateway
* [Tutorial: Using AWS Lambda with Amazon API Gateway \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-on-demand-https-example.html)



## Debugging
* [Debugging Lambda Functions Locally \- AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging.html)
    * [Debugging Python Functions Locally \- AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-python.html)

### Debugging Lambda Functions Locally
Use `sam` command to debug locally.

For Python,

```
sam init --runtime python3.6 --name python-debugging
cd python-debugging/

# Install dependencies of our boilerplate app
pip install -r requirements.txt -t hello_world/build/

# Install ptvsd library for step through debugging

pip install ptvsd -t hello_world/build/

cp hello_world/app.py hello_world/build/
```

#### Canary deployments
* [Implementing Canary Deployments of AWS Lambda Functions with Alias Traffic Shifting \| AWS Compute Blog](https://aws.amazon.com/blogs/compute/implementing-canary-deployments-of-aws-lambda-functions-with-alias-traffic-shifting/)

## Test

From console

* Click Test
* Create test events
    * A function can have up to 10 test events. 
* Click Test

#### Permissoins
[Overview of Managing Access Permissions to Your AWS Lambda Resources \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-overview.html)

* Function
    * `arn:aws:lambda:region:account-id:function:function-name`
* Function alias
    * `arn:aws:lambda:region:account-id:function:function-name:alias-name`
* Function version
    * `arn:aws:lambda:region:account-id:function:function-name:version`
* Event source mapping
    * `arn:aws:lambda:region:account-id:event-source-mapping:event-source-mapping-id`

[AWS Lambda Function Versions \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html#versioning-permissions)

Difference between ARNs for resource based poicy

- If you use a qualified function name (such as `helloworld:1`), the permission is valid for invoking the helloworld function version 1 only using its qualified ARN. Using any other ARNs results in a permission error.
- If you use an unqualified function name (such as `helloworld`), the permission is valid only for invoking the helloworld function using the unqualified function ARN. Using any other ARNs, including `$LATEST`, results in a permission error.
- If you use the `$LATEST` qualified function name (such as `helloworld:$LATEST`), the permission is valid for invoking the helloworld function only using its qualified ARN. Using an unqualified ARN results in a permission error.



## Concurrency
[Managing Concurrency \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)


## Layer
Layer is a library for lambda function.

- python
    - directory sturcture
    - `<valid-directory>`
        - `python`
        - `python/lib/python3.7/site-packages`
            - depends on runtime

```
/<valid-directory>/PIL
/<valid-directory>/Pillow-5.3.0.dist-info
```

You can set permissions to layers.

## VPC
* [Configuring a Lambda Function to Access Resources in an Amazon VPC \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/vpc.html)

Guidelines for Setting Up VPC-Enabled Lambda Functions

* If your Lambda function accesses a VPC, you must make sure that your VPC has sufficient ENI capacity to support the scale requirements of your Lambda function. Y
    * `Projected peak concurrent executions * (Memory in GB / 3GB)`
    * Projected peak concurrent execution – Use the information in Managing Concurrency to determine this value.
    * Memory – The amount of memory you configured for your Lambda function.
* The subnets you specify should have sufficient available IP addresses to match the number of ENIs.


## Logging
* [AWS Lambda Function Logging in Python \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html)

- print statements.
- Logger functions in the logging module (for example, logging.Logger.info and logging.Logger.error).


Format of `LambdaHandler` in rootlogger is below.

```
[%(levelname)s] %(asctime)s.%(msecs)dZ %(aws_request_id)s %(message)s
```

```
REPORT RequestId: 11111111-c3cf-4801-894d-111111111111	Duration: 10.00 ms	Billed Duration: 10 ms	Memory Size: 512 MB	Max Memory Used: 83 MB	Init Duration: 1.00 ms
```

- Duration doesn't include init duraiton
- init duration is initialization time of lambda contaner

## Cloudwatch log query
Check memory usage

```
filter @type = "REPORT"
| stats avg(@maxMemoryUsed), max(@maxMemoryUsed), min(@maxMemoryUsed) by bin(5m)
```

Check duration

```
filter @type = "REPORT"
| stats percentile(@duration, 99), avg(@duration), max(@duration), min(@duration) by bin(5m) as bintime
| sort bintime asc
```

Check the log with some error messages

```
filter @type != "REPORT" and @type != "START" and @type != "END"
| filter @message like /(?i)(Exception|error|fail|5\d\d)/
```

Check the log with some error messages removing some unnecessary logs. `5\d\d` is for 5xx request.

```
filter @type != "REPORT" and @type != "START" and @type != "END"
| filter @message not like /(?i)(Exception|error|fail|5\d\d)/
```

Check the log with some error messages removing some unnecessary logs

```
filter @type != "REPORT" and @type != "START" and @type != "END"
| filter @message like /(?i)(Exception|error|fail)/
| filter @message not like /<sometext>/
```

Counting the number logs which contains some text

```
filter @type != "REPORT"
| filter @message like /UpdateItem/
| stats count() by bin(5m) as time
| sort time asc
```

#### Lambda logging twice
* [python \- Getting logs twice in AWS lambda function \- Stack Overflow](https://stackoverflow.com/questions/50909824/getting-logs-twice-in-aws-lambda-function)



## Concurrecies
- https://www.serverlessguru.com/blog/scaling-aws-lambda-to-30k-request-per-second

There are burst limit and concurrencies limt.

## Lambda with Kafka 
- [Using Lambda with self\-managed Apache Kafka \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html)

Permissions

- Describe your Secrets Manager secret.
- Access your AWS Key Management Service (AWS KMS) customer managed key.
- Access your Amazon VPC.

create a secret in secret manager

- (key, value) = (`username`, `<username>`)
- (key, value) = (`password`, `<password>`)


Max batch size is `10,000`.
To preserve message ordering in each partition, the maximum number of consumers is one consumer per partition in the topic.
Every 15 minutes, Lambda evaluates the consumer offset lag of all the partitions in the topic. If the lag is too high, the partition is receiving messages faster than Lambda can process them. If necessary, Lambda adds or removes consumers from the topic.


## Reference
* [Best Practices for Working with AWS Lambda Functions \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
* [Building Serverless APIs with the Amazon API Gateway and AWS AppSync \- Speaker Deck](https://speakerdeck.com/danilop/building-serverless-apis-with-the-amazon-api-gateway-and-aws-appsync?slide=5)
* [How to run Serverless Code – Amazon Web Services \(AWS\)](https://aws.amazon.com/getting-started/tutorials/run-serverless-code/)
