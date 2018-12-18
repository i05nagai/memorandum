---
title: AWS
---

## aws

## ec2
接続は以下の方法。

```sh
ssh -i key.pem username@ipaddress
```

* `key.pem`は、key pair作成時にdownloadできる秘密鍵
* `username`は、AMI instanceによって決まるroot userで、`ec2-user`もしくは`root`が多い。
* ipaddressはec2のaddress


## Securities
* Getting AWS account root user credentials is different than getting IAM user credentials. 
    * root user credentials
        * you get credentials, such as access keys or key pairs, from the Security Credentials page in the AWS Management Console
    * IAM user credentials
        * you get credentials from the IAM console.
* root user
    * We strongly recommend that you do not use the root user for your everyday tasks, even the administrative ones
    * adhere to the best practice of using the root user only to create your first IAM user.

* [Best Practices for Managing AWS Access Keys \- Amazon Web Services](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html)

### tips
* SGのinboundは、HTTPの場合はAnywhereじゃないとだめ？
* instance作成後はstatusを`stop`にすればinstance typeを変更できる。


## aws-cli

### zsh用の補完
下記を読み込む。

```zsh
source /usr/local/bin/aws_zsh_completer.sh
```

## Reference
* [Rubyとaws-sdkとcredentials](https://gist.github.com/y13i/bf97e86e9c05f10262cf)
* [AWS General Reference \- Amazon Web Services](https://docs.aws.amazon.com/general/latest/gr/Welcome.html)
