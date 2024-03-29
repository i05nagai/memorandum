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
    * `{rest-api-id}.execute-api.{region}.amazonaws.com`
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
- [Build an API Gateway API with Lambda Integration \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html)

* Lambda Proxy
* Lambda Custom
* Lambda Errors in API Gateway



## Creating a REST API

* API endpoint


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


## Enable logging in cloud watch
- [Enable CloudWatch Logs for API Gateway REST API or WebSocket API Troubleshooting](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-cloudwatch-logs/)
- [View API Gateway Log Events in the CloudWatch Console \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/view-cloudwatch-log-events-in-cloudwatch-console.html)

For a REST API, the log group's name is in this format: `API-Gateway-Execution-Logs_apiId/stageName`
For a WebSocket API, the log group's name is in this format: `/aws/apigateway/apiId/stageName`.

Additionally, `/aws/apigateway/welcome` log group might be create

#### Private endpoint
- [Introducing Amazon API Gateway Private Endpoints \| AWS Compute Blog](https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/)
- [Troubleshoot Connection Issues with API Gateway Private API Endpoints](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-private-endpoint-connection/)
- [Create a Private API in Amazon API Gateway \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html#apigateway-private-api-create-interface-vpc-endpoint)
- [How to Invoke a Private API \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html#w20aac13c16c28c11)


Check if the private DNS is enabled

- Go to endpints in VPC page
- Check VPC endpoint for API gateway. service name would be `com.amazonaws.<region>.execute-api` 
- 

How to invoke privaite api

- private DNS enabled on VPC endpoint
    - 


- private DNS disabled on VPC endpoint


Accessing from another account

[Access an API Gateway Private REST API in Another Account Using an Interface Endpoint](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-private-cross-account-vpce/)

- In account A, you want to call private API in account B

- In account A,
    - Create a VPC endpoint with Private DNS name enabled
- In account B,
    - Create a Private API
    - Give Resource based policy to allow VPC endpoint you created in account A


If you cannot access to endpoint, you will get `Nmae or Service not found`.
If api gateway rejects the access, you will get `403 Forbidden`

- VPC peering is not needed.

## Permisson
- [Control Access to an API with IAM Permissions \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html)
- [Create and attach an API Gateway resource policy to an API \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies-create-attach.html)


## Lambda integration
- [Set up Lambda proxy integrations in API Gateway \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)

## Invoke

Invoke public endpoint

```
curl -v -X "PUT" -H "Content-Type: application/json" \
  -d "@data.json" \
  'https://<rest-api-id>.execute-api.eu-west-1.amazonaws.com/path'
```


## Errors
- [Resolve API Gateway “Missing Authentication Token” errors](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-authentication-token-errors/)
- https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/

If body is empty, check if your request actually has body.


## Reference
* [What Is Amazon API Gateway? \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
* [Building Serverless APIs with the Amazon API Gateway and AWS AppSync \- Speaker Deck](https://speakerdeck.com/danilop/building-serverless-apis-with-the-amazon-api-gateway-and-aws-appsync?slide=14)
* [Creating an Edge\-Optimized Custom Domain Name \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-edge-optimized-custom-domain-name.html)
* [Create a REST API with Lambda Integrations in Amazon API Gateway \- Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-getting-started-with-rest-apis.html)
