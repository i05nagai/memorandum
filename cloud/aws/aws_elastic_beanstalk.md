---
title: AWS Elastic Beanstalk
---

## AWS Elastic Beanstalk



## EBの環境が削除できなくなったとき
* https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-delete-stack-fails

AWS CloudFormation で削除できなかったリソースがあったために、スタックが DELETE_FAILED 状態である場合は、
RetainResources パラメーターで AWS CloudFormation が削除できない当該リソースを指定し、削除を再実行します。
AWS CloudFormation は、保持されたリソースを残してスタックを削除します。


## Reference
* [AWS Elastic Beanstalk – Deploy Web Applications](https://aws.amazon.com/elasticbeanstalk/)
