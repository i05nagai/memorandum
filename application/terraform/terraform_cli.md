---
title: Terraform CLI
---

## Terraform CLI

## Install
For OSX

```
brew install terraform
```

to use mulptile version of terraforms

```
$ brew install tfenv
```

For ubuntu 16.04,

```
TERRAFORM_VERSION=0.11.7
cd /tmp
curl -L -O https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip
cp terraform /usr/local/bin
```

## CLI

* `terraform init`
    * directoryの初期化
    * 他のコマンドと違って、何回実行しても結果は同じ
    * `-input=false`
        * inputのpromptをださないようにする
* `terraform plan`
* `terraform apply`
    * terraformの設定を適用する
    * resourceの作成
    * `terraform plan`+実行
    * `-var 'foo=bar'`
        * 実行時に変数の定義ができる
        * credentialの設定などに便利
    * `-out=path`
        * binary形式で実行計画が出力される
    * `-state=statefile`
        * default は `terraform.tfstate`
* `terraform destroy`
    * resourceの停止
* `terraform workspace`
    * workspaceの切り替え管理
* `terraform fmt`
    * formatter
    * go fmtと同じようなもの

```
terraform fmt -diff -write=true -list=true .
```

* `terraform validate [dir]`
    * dirctoryのtf fileをcheck
* terraform import

stateをimportできる。
対応するconfig fileが存在する必要がある。
resource addressとIDを指定する。
idに何を指定するかはresourceによる。

```
terraform import <resource-address> <reousrce-id>
terraform import aws_instance.example i-abcd1234
```

管理しているresourceの状態の一覧

```
terraform state list
```

stateのidやparameterなどを見る。
idが見れるので、別のworkspaceで同じstateをimportする際に便利。

```
terraform state show <resource-address>
```

## Usage

## Configuration

## Makefile

```make
TERRAFORM_VARIABLE = TF_VAR_somelist=\'["ami-abc123", "ami-bcd234"]\'
TERRAFORM_VARIABLE = TF_VAR_aws='{default.aws_access_key="${AWS_IAM_ACCESS_KEY_ID}", default.aws_secret_key="${AWS_IAM_SECRET_KEY}"}'
TERRAFORM_BIN = ${TERRAFORM_VERSION} @terraform

create-s3:
    ${TERRAFORM_BIN} apply -target=....
```

Then export varaiebls as

```
export AWS_IAM_ACCESS_KEY_ID=""
export AWS_IAM_ACCESS_KEY=""
make create-s3
```


## Reference
