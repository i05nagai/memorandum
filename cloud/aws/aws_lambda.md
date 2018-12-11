---
title: AWS Lambda
---

## AWS Lambda

* Language
* Node.js
* Java
* C#
* Python
* Go
* Powershell

## Concepts
* BatchSize
    * The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.
    * The default for Amazon Kinesis and Amazon DynamoDB is 100 records.
    * Both the default and maximum for Amazon SQS are 10 messages.
            

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

## Reference
* [Best Practices for Working with AWS Lambda Functions \- AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
* [Building Serverless APIs with the Amazon API Gateway and AWS AppSync \- Speaker Deck](https://speakerdeck.com/danilop/building-serverless-apis-with-the-amazon-api-gateway-and-aws-appsync?slide=5)
