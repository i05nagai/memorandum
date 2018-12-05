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
    * Regional API endpoint
    * Private API endpoint
* API key
    * An alphanumeric string that API Gateway uses to identify an app developer who uses your API. 
* API owner
* API stage
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
