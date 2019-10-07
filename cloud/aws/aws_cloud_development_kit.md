---
title: AWS Cloud Development Kit
---

## AWS Cloud Development Kit

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

## Reference
- [What Is the AWS CDK? \- AWS Cloud Development Kit \(AWS CDK\)](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
