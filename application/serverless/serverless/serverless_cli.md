---
title: serverless CLI
---

## serverless CLI

Deploy a Serverless service

```
severless deploy <subcommand>
```

* deploy function
    * Deploy a single function from the service
* deploy list
    * List deployed version of your Serverless Service
* deploy list functions
    * List all the deployed functions and their versions
* --conceal
    * Hide secrets from the output (e.g. API Gateway key values)
* --stage / -s
    * Stage of the service
* --region / -r
    * Region of the service
* --package / -p
    * Path of the deployment package
* --verbose / -v
    * Show all stack events during deployment
* --force
    * Forces a deployment to take place
* --function / -f
    * Function name. Deploys a single function (see 'deploy function')
* --aws-s3-accelerate
    * Enables S3 Transfer Acceleration making uploading artifacts much faster.


```
serverless config credentials <option>
```

* --provider / -p (required)
    * Name of the provider. Supported providers: "spotinst"
* --key / -k (required)
    * Access key for the provider
* --secret / -s (required)
    * Secret key for the provider
* --profile / -n
    * Name of the profile you wish to create. Defaults to "default"
* --overwrite / -o
    * Overwrite the existing profile configuration in the credentials file


## Configuration


```
${opt:some_option}
```

## Errors

#### Trying to populate non string value into a string for variable . Please make sure the value of the property is a string.

```
sls deploy -s dev # OK
sls deploy -stage=dev # NG
sls deploy --stage=dev # OK
```

## Reference

