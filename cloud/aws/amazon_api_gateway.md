---
title: Amazon API Gateway
---

## Amazon API Gateway

* API Gateway offers the way to manage API key and access control

## Concepts
* API Gateway
* API Gateway API
* API deployment
* API developer
* API endpoints
    * `{rest-api-id}.execute-api.{region}.amazonaws.co`
    * Edge-optimized API endpoint
        * best for geographically distributed clients.
        * API requests are routed to the nearest CloudFront Point of Presence (POP)
        * Edge-optimized APIs capitalize the names of HTTP headers (for example, Cookie).
    * Regional API endpoint
        * A regional API endpoint is intended for clients in the same region
        * When a client running on an EC2 instance calls an API in the same region, or when an API is intended to serve a small number of clients with high demands, a regional API reduces connection overhead
        * Regional and private APIs pass all header names through as-is.
    * Private API endpoint
        * an API endpoint that can only be accessed from your Amazon Virtual Private Cloud (VPC) using an interface VPC endpoint,
* API key
    * An alphanumeric string that API Gateway uses to identify an app developer who uses your API. 
* API owner
* API stage
    * Each stage is a snapshot of the API and is made available for client apps to call.
* App developer
* Integratin request
* Integration response
* Private API
* Private integration
* Proxy integration
* Usage plan
* Mapping template



## Lambda integration
* Lambda Proxy
* Lambda Custom
* Lambda Errors in API Gateway

## Creating a REST API

* API endpoint


## CLI
* [apigateway — AWS CLI 1\.16\.89 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/apigateway/index.html)

```
# create rest-api
# return api-id for created endpoint
aws apigateway create-rest-api \
    --name <name> \
    --description (string) \
    --clone-from (string) \
    --binary-media-types (list) \
```

```
aws apigateway create-resource \
    --rest-api-id <value> \
    --parent-id <value> \
    --path-part <value>
```

* `--rest-api-id`
* `--parent-id`
    * The parent resource's identifier.
* `--path-part`
    * The last path segment for this resource.


```
aws apigateway get-resources \
    --rest-api-id <value>
```

```
  put-method
--rest-api-id <value>
--resource-id <value>
--http-method <value>
--authorization-type <value>
[--authorizer-id <value>]
[--api-key-required | --no-api-key-required]
[--operation-name <value>]
[--request-parameters <value>]
[--request-models <value>]
[--request-validator-id <value>]
[--authorization-scopes <value>]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```

* `--http-method`
    * PUT, POST,
* `--authorization-type`
    * This is fine for testing but in production you should use either the key-based or role-base authentication.
    * NONE
    * AWS_IAM
        * using AWS IAM permissions
    * CUSTOM
        * using a custom authorizer
    * COGNITO_USER_POOLS
        * using a Cognito user pool.


```
aws apigateway put-integration \
    --rest-api-id $API \
    --resource-id $RESOURCE \
    --http-method POST \
    --type AWS \
    --integration-http-method POST \
--uri arn:aws:apigateway:$REGION:lambda:path/2015-03-31/functions/arn:aws:lambda:$REGION:$ACCOUNT:function:LambdaFunctionOverHttps/invocations
{
```

* [put\-integration — AWS CLI 1\.16\.89 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/apigateway/put-integration.html)
* `--type`
    * HTTP
    * AWS
        * Lamdab
    * MOCK
    * HTTP_PROXY
    * AWS_PROXY
* `--uri (string)`
    * `HTTP` or `HTTP_PROXY`
        * [Uniform Resource Identifier \- Wikipedia](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)
        * For a private HTTP integration, the URI is not used for routing
    * `AWS_PROXY` or `AWS`
        * `arn:aws:apigateway:{region}:{subdomain.service|service}:path|action/{service_api}`
            * `{Region}`
                * the API Gateway region
            * `{service}`
                * the name of the integrated AWS service
                * e.g. `s3`, `lambda`
            * `{subdomain}`
            * `{service_api}`
            * `path`
            * `action`
                * Action={name}{p1}={v1}p2={v2}...

```
  put-method-response
--rest-api-id <value>
--resource-id <value>
--http-method <value>
--status-code <value>
[--response-parameters <value>]
[--response-models <value>]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```

* [put\-method\-response — AWS CLI 1\.16\.89 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/apigateway/put-method-response.html)
* set the HTTP method response to specific content-type.
* This is the response type that your API method returns
* `--status-code`
* `--response-models (map)`
    * `application/json=Empty`
    * Specifies the Model resources used for the response's content type
    *  a content type as the key
        * `application/json`
    *  a Model name as the value
        * `Empty`


```
put-integration-response
--rest-api-id <value>
--resource-id <value>
--http-method <value>
--status-code <value>
[--selection-pattern <value>]
[--response-parameters <value>]
[--response-templates <value>]
[--content-handling <value>]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```

* [put\-integration\-response — AWS CLI 1\.16\.89 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/apigateway/put-integration-response.html)
    * set the HTTP method integration response to content-type
    * This is the response type that Lambda function returns.
* `--http-method`
* `--status-code`
* `--response-`


```
  create-stage
--rest-api-id <value>
--stage-name <value>
--deployment-id <value>
[--description <value>]
[--cache-cluster-enabled | --no-cache-cluster-enabled]
[--cache-cluster-size <value>]
[--variables <value>]
[--documentation-version <value>]
[--canary-settings <value>]
[--tracing-enabled | --no-tracing-enabled]
[--tags <value>]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```

* [create\-stage — AWS CLI 1\.16\.89 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-stage.html)
* `--stage-name`


```
  create-deployment
--rest-api-id <value>
[--stage-name <value>]
[--stage-description <value>]
[--description <value>]
[--cache-cluster-enabled | --no-cache-cluster-enabled]
[--cache-cluster-size <value>]
[--variables <value>]
[--canary-settings <value>]
[--tracing-enabled | --no-tracing-enabled]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```

* [create\-deployment — AWS CLI 1\.16\.89 Command Reference](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-deployment.html)
    * Creates a Deployment resource, which makes a specified RestApi callable over the internet.
    * `--stage-name`
    * `--rest-api-id`
    * `--stage-name`

## Deploy a REST API
* [Deploying a REST API in Amazon API Gateway \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html)


## Monitoring
* https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html

Amazon API Gateway sends metric datat to Cloudwatch every minute
Metrics

* 4xx Error
* 5xx Error
* CacheHitCount
* CacheMissCount
* Count
* IntegratinoLatency
* Latency

Filtering dimensions


* ApiName
* ApiName, Method, Resource, Stage
* ApiName, Stage


## Pricing
[Amazon API Gateway – Pricing](https://aws.amazon.com/api-gateway/pricing/)

Example of pricing.
Price is based on 

* API calls
    * First 333 million per month
        * 3.50 usd per million
    * Next 667 million
        * 2.80 usd per million
    * Next 19 billion
        * 2.38 usd per million
    * Over 20 billion
        * 1.51 usd per million
* Caching
    * 0.5 GB
        * 0.02 USD per hour
    * 1.6 GB
        * 0.038 usd per hour
    * 6.1 GB
        * 0.20 usd per hour
    * 13.5 GB
        * 0.25 usd per hour
    * 28.4 GB
        * 0.50 usd per hour
    * 58.2 GB
        * 1.00 usd per hour
    * 118.0 GB
        * 1.90 usd per hour
    * 237.0 Gb
        * 3.80 usd per hour
* Transfer data
    * if you use other AWS services, the requests forwarded by API Gateway incurs costs in AWS service which receives the request, depending on the AWS service

## Reference
* [What Is Amazon API Gateway? \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
* [Building Serverless APIs with the Amazon API Gateway and AWS AppSync \- Speaker Deck](https://speakerdeck.com/danilop/building-serverless-apis-with-the-amazon-api-gateway-and-aws-appsync?slide=14)
