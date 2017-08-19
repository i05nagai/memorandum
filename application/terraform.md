---
title: Terraform
---

## Terraform
Terraformの設定ファイルはHCLで記述する。


```
brew install terraform
```

## Use on docker
* [hashicorp/terraform - Docker Hub](https://hub.docker.com/r/hashicorp/terraform/)

Hashicorpが提供しているdocker imageがある。。

```
docker run -i -t hashicorp/terraform:light plan main.tf
```

fullはrepositoryのsource code全て含まれている。
developmentとdebugはこちらが役にたつ。

```
docker run -i -t hashicorp/terraform:full plan main.tf
```

## Syntax
基本はHCLで記述する。

* true/false
* `${var.foo}` で変数参照
* commentは`#`
* 数字は10進数、`0x`をつけると16進数
* 配列とmapはjsonと同じ
* 完全なjson形式のformatも記述可能

```tf
variable "ami" {
  description = "the AMI to use"
}
```

は以下と等価

```
variable = [{
  "ami": {
    "description": "the AMI to use",
  }
}]
```

```
resource "aws_instance" "web" {
  ami               = "${var.ami}"
  count             = 2
  source_dest_check = false

  connection {
    user = "root"
  }
}
```

以下と等価？

```
resource = [{
    "aws_instance": {
        "web":  {
          ami               = "${var.ami}"
          count             = 2
          source_dest_check = false

          connection {
            user = "root"
          }
        }
    }
}]
```

### Available Variables
* `${}`
* `${var.amis["us-east-1"]}`
* `${var.subnets}`
    * subnetsがlistの場合、listとして変数を参照
* `${var.subnets[idx]}`
    * listのidx番目
* `${self.private_ip_address}`
    * selfをつけるとresourceの変数

### override
* `_override`で終わる`.tf`か`override.tf`のファイルで設定の上書きができる。

### Resource
* [Configuring Resources - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/resources.html)

`TYPE`, `NAME`の組で記載する。
この2つの組は一意である必要がある。
`TYPE`はproviderとresourceのmapをする際に考慮される。
resourceの中に記載するのは`TYPE`にmatchするproviderの設定である。
`NAME`はわかりやすい名前ならなんでも良い。


```
resource TYPE NAME {
    CONFIG ...
    [count = COUNT]
    [depends_on = [NAME, ...]]
    [provider = PROVIDER]

    [LIFECYCLE]

    [CONNECTION]
    [PROVISIONER ...]
}
```

Resourceごとにexportされる外部から参照できる属性がある。

### DataSource
* [Configuring Data Sources - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/data-sources.html)

data sourceは例えば、既存のinstanceの情報を取得してterraformに提供する。



### Provider Configuration
* [Configuring Providers - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/providers.html)

ResourceはProviderにmapされる。
mapの規則は文字の先頭からの最長一致。
resourceが`aws_instances`であれば、`aws`のproviderを定義していれば`aws`にmapされる。
providerごとに、認証の情報やendpointの情報を必要とする場合がある。
versionの指定もできる。

```
provider "aws" {
  version = "~> 1.0"

  access_key = "foo"
  secret_key = "bar"
  region     = "us-east-1"
}
```

resourceの中で明示的にproviderを指定できる。
aliasで設定の異なる同じproviderを作成することもできる。

```
# The default provider
provider "aws" {
  # ...
}

# West coast region
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

resource "aws_instance" "foo" {
  provider = "aws.west"

  # ...
}
```

### Variables
* [Configuring Variables - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/variables.html)

```
variable NAME {
  [type = TYPE]
  [default = DEFAULT]
  [description = DESCRIPTION]
}
```

* `type`
    * string, map, list
* `default`はNAMEで参照した場合に利用される値

## CLI

* `terraform init`
    * directoryの初期化
    * 他のコマンドと違って、何回実行しても結果は同じ
* terraform apply
    * terraformの設定を適用する
    * `-var 'foo=bar'`
        * 実行時に変数の定義ができる
        * credentialの設定などに便利

## Tips

### Input Variables
* [Input Variables - Terraform by HashiCorp](https://www.terraform.io/intro/getting-started/variables.html)

以下の形式で渡すか、`.tfvars`のファイルに変数を記載する。

```
$ terraform plan \
  -var 'access_key=foo' \
  -var 'secret_key=bar'
```

```
access_key = "foo"
secret_key = "bar"
```

その場合は以下のtf-varでファイルを指定する。

```
$ terraform plan \
  -var-file="secret.tfvars" \
  -var-file="production.tfvars"
```

### Output Variables
* [Output Variables - Terraform by HashiCorp](https://www.terraform.io/intro/getting-started/outputs.html)

terraformの使用者に変数の情報を表示する。
`terraform output`で参照できるようになる。
`terraform apply`時にoutputの結果が表示される。

```
output "ip" {
  value = "${aws_eip.ip.public_ip}"
}
```

## Providers
Provicerごとにそれぞれ、DataSourceとResoruceを提供している。

### AWS
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
* `aws_eip`
    * [AWS: aws_eip - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/r/eip.html)
    * `vpc`
        * EIPがVPCの中ならtrue
    * `instance`
        * EIPを割り当てるEC2 instance ID
* `aws_eip_association`
    * [AWS: aws_eip_association - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/r/eip_association.html)
    * `instance_id`
    * `allocation_id`


## Provisioner
* [Provisioners - Terraform by HashiCorp](https://www.terraform.io/docs/provisioners/index.html)

instanceなどを立ち上げた後に、設定をする際に用いる。
provisonerのblockは複数記述できる。

* Creation time provisoner
    * resourceの作成時に一度だけ実行される
    * resourceのupdateでは実行されない
    * creation time provionerでfailすると状態は`tainted`になる
* Destroy time provisioner
    * provisonerのblockで`when = destory`を指定するとdestory time provionerになる

### chef

### local-exec
terraformが動いているmachineで、コマンドを実行する。
terraformの変数が使えるので、結果の出力などに使える？

```
resource "aws_instance" "web" {
  # ...

  provisioner "local-exec" {
    command = "echo ${self.private_ip_address} > file.txt"
  }

  provisioner "local-exec" {
    command = "echo ${self.private_ip_address} > file.txt"
    when = destroy
    on_failure = ["continue"|"fail"]
  }
}
```

### remote-exec
各resourceでcommandを実行する。
file provisionerでfileをcopyしてresource上でfileを実行するなどに使える。
commandのListを渡すのが`local-exec`との違い。

```
resource "aws_instance" "web" {
  # ...

  provisioner "remote-exec" {
    inline = [
      "puppet apply",
      "consul join ${aws_instance.web.private_ip}",
    ]
  }
}
```

* `inline`
* `script`
    * terraformが実行されているmachineのFileをcopyして、実行する
    * fileは実行後には削除される
* `scripts`
    * terraformが実行されているmachineのFileをcopyして、実行する
    * fileは上から順番に実行される
    * fileは実行後には削除される


### File Provisoner
file、directoryをcopyする。

### null Provisoner
特定のresourceに紐付かないが、triggerに応じてProvisonを実行する。


## Reference
* [Configuration Syntax - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/syntax.html)
