---
title: Terraform Resource AWS
---

## Terraform Resource AWS

Resource

* `aws_instance`
    * `ami`
    * `availability_zone`
    * `disable_api_termination`
        * trueだとEC2 Instance Termination Protectionをenableにする
        * trueだとprotectionをつける
    * `instance_type`
    * `key_name`
    * `vpc_security_group_ids`
    * `subnet_id`
    * `associate_public_ip_address`
        * trueだとPublic IPに関連付ける
    * `tags`
    * `volume_tags`
    * `root_block_device`
    * `ebs_block_device`
    * `tags`
        * tagつける
    * `volume_tags`
        * volumeにtagをつける
* `aws_db_instance`
    * `identifier`
    * `allocated_storage`
        * storageの容量をGBで指定
    * `storage_type`
    * `engine`
    * `engine_version`
    * `name`
        * DB名、省略するとDBを作らない
    * `password`
        * master DB userのpassword
        * logとstate fileに記録される可能性がある
    * `username`
        * master DB userのusername
    * `skip_final_snapshot`
        * RDS terminate時にDBのsnapshotを保存するかを指定
        * defaultはfalse
        * falseの場合は`final_snapshot_identifier`を指定する必要がある
    * `final_snapshot_identifier`
        * `final_snapshot`時のsnapshotの名前
    * `tags`
        * tagを記載
    * `copy_tags_to_snapshot`
        * snapshotにtagをcopy
        * `final_snapshot_identifier`を指定している必要がある
* `aws_eip`
    * [AWS: aws_eip - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/r/eip.html)
    * Elastic IPを作成する
    * `vpc`
        * EIPがVPCの中ならtrue
    * `instance`
        * EIPを割り当てるEC2 instance ID
* `aws_route53_zone`
    * `terraform import RESOURCE_ADDR Z4KAPRWWNC7JR`
        * `ZONEID`
* `aws_route53_route`
    * `terraform import RESOURCE_ADDR Z4KAPRWWNC7JR_dev.example.com_NS_dev`
        * `ZONEID_RECORDNAME_TYPE_SET-IDENTIFIER`
            * SET-IDENTIFIERはない場合は省略可能

```
$ terraform import aws_eip.bar eipalloc-00a10e96
```

* `aws_eip_association`
    * [AWS: aws_eip_association - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/r/eip_association.html)
    * 取得したElasticp IPをEC2 instanceと割り当てるときに使う
    * `aws_eip` resourceと一緒に使うことが多い
    * `instance_id`
    * `allocation_id`


* `aws_iam_policy`
    * [AWS: aws\_iam\_policy \- Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/d/iam_policy.html)
    * `arn`
        * required
    * `name`
    * `description`
    * `policy`
    * `path`


* `aws_iam_policy_document`
    * compatible to JSON of IAM policy
    * `statement`
        * `sid`
        * `effect`
            * `Allow`, `Deny`
        * `actions`
        * `principals`
            * `type`
                * For AWS accounts this is "AWS"
            * `identifiers`
                * When type is "AWS", these are IAM user or role ARNs
        * `test`
        * `variable`
        * `values`
* `aws_iam_role_policy_attachment`
    * Attaches a Managed IAM Policy to an IAM role
    * [AWS: aws\_iam\_role\_policy\_attachment \- Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html)
    * `role`
    * `policy_arn`


* `aws_s3_bucket_notification`
    * `lambda_function`
        * lambda function
        * `id`
        * `lambda_function_arn`
        * `events`
        * `filter_prefix`
            * Specifies object key name prefix.
        * `filter_suffix`
            * Specifies object key name suffix.
    * `topic`
        * SNS topic
        * `id`
            * optional
        * `topic_arn`
        * `events`
        * `filter_prefix`
        * `filter_suffix`
    * `queue`
        * SQS queue
        * `id`
            * optional
        * `queue_arn`
        * `events`
        * `filter_prefix`
        * `filter_suffix`


* https://www.terraform.io/docs/providers/aws/r/acm_certificate.html

## LoadBalancer
* https://www.terraform.io/docs/providers/aws/r/lb_listener.html
* https://www.terraform.io/docs/providers/aws/r/lb.html


## ECS
https://www.terraform.io/docs/providers/aws/r/ecs_service.html

## AWS IAM Policy
* [AWS IAM Policy Documents with Terraform \- Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html)


You need to define IAM policy with JSON texts.
Using JSON texts in terraform configuration file causes additional formatting of JSON texts and mainting JSON syntax.
The recommended approach is to use `aws_iam_policy_document` data source.

* Native Terraform configuration - no need to worry about JSON formatting or syntax
* Policy layering - create policy documents that combine and/or overwrite other policy documents
* Built-in policy error checking


## Reference
* [Provider: AWS - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/index.html)
