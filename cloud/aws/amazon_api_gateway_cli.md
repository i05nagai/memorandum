---
title: Amazon API gateway CLI
---

## Amazon API gateway CLI

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

* [Method \- Amazon API Gateway API Reference](https://docs.aws.amazon.com/apigateway/api-reference/resource/method/)

```
aws apigateway
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
* `--request-parameters (map)`
    * A key-value map defining required or optional method request parameters  that  can  be  accepted by API Gateway. A key defines a method request parameter name matching the pattern of
    * `method.request.{location}.{name}`
        * location
            * `querystring`, `path`, `header`, `name`
    * The value associated with the key  is  a  Boolean  flag  indicating  whether the parameter is required (true ) or optional (false ).
    * The method request  parameter names  defined  here  are  available in Integration to be mapped to integration request parameters or body-mapping templates.

```
aws apigateway put-integration \
    --rest-api-id $API \
    --resource-id $RESOURCE \
    --http-method POST \
    --type AWS \
    --integration-http-method POST \
--uri arn:aws:apigateway:$REGION:lambda:path/2015-03-31/functions/arn:aws:lambda:$REGION:$ACCOUNT:function:LambdaFunctionOverHttps/invocations
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

## Reference
* [Amazon API Gateway Version 2 API Reference \- Amazon API Gateway](https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/api-reference.html)
