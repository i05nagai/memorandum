---
title: aws-cli
---

## aws-cli

## Install

```
pip install awscli --upgrade --user
```

設定は以下で行う。
AWS Access key IDとAWS Secret Access Keyは用意しておく。

```
aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```

#### aws configure
* [Named Profiles \- AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-multiple-profiles.html)

```
aws configure --profile <user>
aws configure get
# list configurations such as Access Key ID,...
aws configure list
aws configure set

aws configure set --profile <profile-name> aws_access_key_id=
aws configure set --profile <profile-name> aws_secret_access_key
```

You can execute command with this credential by giving `--profile` optoin like

```
aws ec2 describe-instances --profile user2
```


## Tips

#### Named profile
* [Terraform で AWS環境を実運用する上で困ったことと、その対処 - Qiita](https://qiita.com/takumiabe/items/07943f23436aa983f397)

AWSの認証情報に名前をつけてlocalで管理できる。

```
$ aws configure --profile my-profile-name
AWS Access Key ID [None]: xxxxxxxxxx
AWS Secret Access Key [None]: xxxxxxxxxx
Default region name [None]: ap-northeast-1
Default output format [None]: 
```

terraformで利用する場合は以下のようにprofileを指定できる。

```
provider "aws" {
  profile = "my-profile-name"
}
```

#### Error
[InvalidSignatureException: Signature expired · Issue #527 · aws/aws-sdk-js](https://github.com/aws/aws-sdk-js/issues/527)

DockerなどでVMを使っている場合はVMの時間がずれている。
VMの再起動で治る。

```
InvalidSignatureException: Signature expired
```


## Reference
* [aws — AWS CLI 1.11.96 Command Reference](http://docs.aws.amazon.com/cli/latest/reference/)

