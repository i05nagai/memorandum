---
title: AWS Cloud Development Kit
---

## AWS Cloud Development Kit

## Concepts

- App
- Stack
    - Within the app, you typically define one or more stacks, which are the unit of deployment, analogous to AWS CloudFormation stacks
- pattern
    - the AWS Construct Library includes even higher-level constructs, which we call patterns
    - e.g. https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-ecs-patterns.ApplicationLoadBalancedFargateService.html
- Constructs


## Bootstrapping
Bootstrapping your AWS Environment
Before you can use the AWS CDK you must bootstrap your AWS environment to create the infrastructure that the AWS CDK CLI needs to deploy your AWS CDK app. Currently the bootstrap command creates only an Amazon S3 bucket.

You incur any charges for what the AWS CDK stores in the bucket. Because the AWS CDK does not remove any objects from the bucket, the bucket can accumulate objects as you use the AWS CDK. You can get rid of the bucket by deleting the CDKToolkit stack from your account.

```
cdk bootstrap aws://<account-num>/us-east-1
```



## Permissions
In CDK v2, 

To bootstrap

```
cdk boostrap --cloudformation-execution-policies 
```

## CLI

```
apt-get install python3-venv
npm install -g aws-cdk
```

Lists all stacks in the app

```
cdk list [STACKS..]
cdk ls [STACKS..]
```

Synthesizes and prints the CloudFormation template for this stack

```
cdk synthesize [STACKS..]
cdk synth [STACKS..]
```

Deploys the CDK toolkit stack into an AWS  environment

```
cdk bootstrap [ENVIRONMENTS..]
```

Deploys the stack(s) named STACKS into your AWS account

```
cdk deploy [STACKS..]
```

* --app, -a
    * REQUIRED: command-line for executing your app or a cloud assembly directory (e.g. "node bin/my-app.js")
* --context, -c
    * Add contextual string parameter (KEY=VALUE)
* --plugin, -p
    * Name or path of a node package that extend the CDK features. Can be specified multiple times
* --trace
    * Print trace for stack warnings
    * default: false
* --strict
    * Do not construct stacks with warnings
* --ignore-errors
    * Ignores synthesis errors, which will likely produce an invalid output
    * default: false
* --json, -j
    * Use JSON output instead of YAML when templates are printed to STDOUT
    * default: false
* --verbose, -v
    * Show debug logs
    * default: false
* --profile
    * Use the indicated AWS profile as the default environment
* --proxy
    * Use the indicated proxy. Will read from HTTPS_PROXY environment variable if not specified.
* --ec2creds, -i
    * Force trying to fetch EC2 instance credentials. Default: guess EC2 instance status
* --version-reporting
    * Include the "AWS::CDK::Metadata" resource in synthesized templates
    * default: true
* --path-metadata
    * Include `aws:cdk:path` CloudFormation metadata for each resource
    * default: true
* --asset-metadata
    * Include `aws:asset:*` CloudFormation metadata for resources that user assets
    * default: true
* --role-arn, -r
    * ARN of Role to use when invoking CloudFormation
* --toolkit-stack-name
    * The name of the CDK toolkit stack
* --staging
    * Copy assets to the output directory (use --no-staging to disable, needed for local debugging the source files with SAM CLI)
    * default: true
* --output, -o
    * Emits the synthesized cloud assembly into a directory (default: cdk.out)
* --no-color            Removes colors and other style from console output
    * default: false
* --version
    * Show version number
* --build-exclude, -E
    * Do not rebuild asset with the given ID. Can be specified multiple times.
    * default: []
* --exclusively, -e
    * Only deploy requested stacks, don't include dependencies
* --require-approval
    * What security-sensitive changes need manual approval
    * [choices: "never", "any-change", "broadening"]
* --ci
    * Force CI detection. Use --no-ci to disable CI autodetection.
    * default: false
* --tags, -t
    * Tags to add to the stack (KEY=VALUE)
* -h, --help
    * Show help

Destroy the stack(s) named STACKS

```
cdk destroy [STACKS..]
```

Compares the specified stack with the deployed stack or a local template file, and returns with status 1 if any difference is found

```
cdk diff [STACKS..]
```

Returns all metadata associated with this stack

```
cdk metadata [STACK]
```

Create a new, empty CDK project from a template. Invoked without TEMPLATE, the app template will be used.

```
cdk init [TEMPLATE]
```

```
cdk init -l python
```

Manage cached context values

```
cdk context
````

Opens the reference documentation in a browser [aliases: doc]

```
cdk docs
```

Check your set-up for potential problems

```
cdk doctor
```

## CLI

```
cdk init sample-app --language=python
```

## API

#### Custom Resource
Custom Resouce with `on_delete` does not work without adding `on_create` (possibly either `on_create`/`on_update`).

```python
custom_resources.AwsCustomResource(
    self, "master_rule_remover",
    on_delete=custom_resources.AwsSdkCall(
        service="EC2",
        action="revokeSecurityGroupIngress",
        parameters={
            "GroupId": security_group_master.security_group_id,
            "IpProtocol": "tcp",
            "FromPort": 0,
            "ToPort": 65535,
        }
    )
)
```

When you deploy the stack, you observe the following error

```
Invalid PhysicalResourceId
```

#### LazyValue
- [Python: implementing IStepFunctionsTask causes jsii to throw "Don't know how to convert object to JSON" · Issue \#5410 · aws/aws\-cdk](https://github.com/aws/aws-cdk/issues/5410)

```python
@jsii.implements(core.IStringProducer)
class Producer:

    def produce(self, context: core.IResolveContext) -> Optional[str]:
        return "some-lazy-value"

    def __init__(self):
        super().__init__()

core.Lazy.string_value(producer=Producer())
```

`jsii` has an issue of copying object.

```python
    copy.deepcopy({
    "deployment_config": aws_codedeploy.LambdaDeploymentConfig.ALL_AT_ONCE,
    })
```

#### iam condition

```
aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "tag:GetResources",
            ],
            resources=[
                f"*",
            ],
            conditions={
                ""
            }
        )
```

## Staging buckets

- `<bucket-name>/cdk/<stack-name>/<hash>.yml`


## Metadata

```
FileAssetMetadataEntry(
    artifact_hash_parameter='AssetParameters1111111111111111111111111111111111111111111111111111111111111111ArtifactHash970BE98F',
    id='1111111111111111111111111111111111111111111111111111111111111111',
    packaging='file',
    path='asset.1111111111111111111111111111111111111111111111111111111111111111.whl',
    s3_bucket_parameter='AssetParameters1111111111111111111111111111111111111111111111111111111111111111S3Bucket18CC822F',
    s3_key_parameter='AssetParameters1111111111111111111111111111111111111111111111111111111111111111S3VersionKeyC8F8CC56',
    source_hash='1111111111111111111111111111111111111111111111111111111111111111')
```

## Plugin
Currenlty, plugin feature supports only handling credentials.

- [GitHub](https://aws.amazon.com/blogs/devops/cdk-credential-plugin/)


## Java
- https://github.com/xiaod-dev/demo-CDK-gradle-project

## Lifecycle
[Apps \- AWS Cloud Development Kit \(AWS CDK\)](https://docs.aws.amazon.com/cdk/latest/guide/apps.html#lifecycle)


IResolvable will be resolved 

- (1) during `prepare` phase if it's `CfnReference`
- (2) during `synthesis` phase otherwise

## Bundling images

- PYTHON_3_7: `public.ecr.aws/sam/build-python3.7`

## Metadata
Some metadata in a node is not added at the Aspect phase.
For instance, `cd:asset:path` is not available.


## Error

#### cdk deploy fails when the stack is being update

```
<stack> failed: Error [ValidationError]: Stack:arn:aws:cloudformation:eu-west-1:<account>:stack/<stack> is in CREATE_IN_PROGRESS state and can not be updated.
```

## Reference
- [What Is the AWS CDK? \- AWS Cloud Development Kit \(AWS CDK\)](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [AWS CDK Tools \- AWS Cloud Development Kit \(AWS CDK\)](https://docs.aws.amazon.com/cdk/latest/guide/tools.html)
