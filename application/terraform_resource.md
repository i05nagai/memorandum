---
title: Terraform Resource
---

## Terraform Resource
Providerが提供しているResourceの設定について記載

## AWS Provider
* [Provider: AWS - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/index.html)

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

## Terraform
* `backend`
    * remote stateのbackend
    * `gcp`
        * `bucket`
            * bucket名
        * `credentials`
        * `prefix`
            * remote stateの保存先
            * `<prefix>/<name>.tfstate`のfileが作られる
        * `path`
        * `project`
        * `region`
        * `encryption_key`
            * stateのencryptionのための32 byte base64 encoded key

## Reference
