---
title: Terraform
---

## Terraform
Terraformの設定ファイルはHCLで記述する。

* `.tf`, `.tf.json`
* fileはdirectoryごとにalphabetic orderで読まれる
* variableの宣言順序は関係ない

## Install
For OSX

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
resource "resource_type" "resource_name" {
  attribute1 = "${var.ami}"
  attribute2 = 2
  attribute3 = false

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

          connection: {
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


```
data "data_type" "data_name" {
}
```


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

### Local values
* [Configuring Local Values - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/locals.html)
* [Variable cannot contain interpolation? · Issue #14343 · hashicorp/terraform](https://github.com/hashicorp/terraform/issues/14343)

variables blockの中でvarは利用できないので、 変数を使って値を生成する際などに利用する。
varに書いている定数はだいたい置き換えが可能



### Variables
* [Configuring Variables - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/variables.html)
    * variablesの中でvarのinterpolationは使えない
    * local valueを使う

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

## Debug
CLIの実行時に環境変数を設定することで、実行することで、logの出力を変更できる

* `TF_LOG`
    * TRACE, DEBUG, INFO, WARN or ERROR
    * defualt: INFO
    * TRACE is the most verbose
* `TF_LOG_PATH`
    * logの出力先
    * `/dev/stdout`
* `[apply|plan] -parallelism=0`
    * 出力が見づらくなるsync

## CLI

* `terraform init`
    * directoryの初期化
    * 他のコマンドと違って、何回実行しても結果は同じ
    * `-input=false`
        * inputのpromptをださないようにする
* terraform apply
    * terraformの設定を適用する
    * `-var 'foo=bar'`
        * 実行時に変数の定義ができる
        * credentialの設定などに便利
    * `-out=path`
        * binary形式で実行計画が出力される
    * `-state=statefile`
        * default は `terraform.tfstate`
* `terraform fmt`
    * formatter

```
terraform fmt -diff -write=true -list=true .
```

* `terraform validate [dir]`
    * dirctoryのtf fileをcheck

stateをimportできる。
対応するconfig fileが存在する必要がある。
resource addressとIDを指定する。
idに何を指定するかはresourceによる。

```
terraform import <resource-address> <reousrce-id>
terraform import aws_instance.example i-abcd1234
```

## Resroucde Addressing
* [Internals: Resource Address - Terraform by HashiCorp](https://www.terraform.io/docs/internals/resource-addressing.html)

moduleを使っている場合は、moduleで使っているresourceもaddressを持つ
countを使っている場合は番号がつく。


## Tips

### Automation
* [Running Terraform in Automation - Guides - Terraform by HashiCorp](https://www.terraform.io/guides/running-terraform-in-automation.html)

* [Part 3.2: From Semi-Automation to Infrastructure as Code - Terraform Recommended Practices - Terraform by HashiCorp](https://www.terraform.io/docs/enterprise/guides/recommended-practices/part3.2.html#3-create-your-first-module)
    * いつmoduleを使うべきか

### Locals


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

## DataSource
* `data`ではじまる


```
data "template_file" "example" {
  template = "$${hello} $${world}!"
  vars {
    hello = "goodnight"
    world = "moon"
  }
}
```

* `template_file`
    * 内部的に文字列を描画してfileに持つ

## Providers
Provicerごとにそれぞれ、DataSourceとResoruceを提供している。

Providerは

* GCP
* AWS
* など

## State
terraformが実際のinfrastructureとresourceとの対応をとるためのmeta dataのこと。
terraform applyを一度実行すると、state 管理用のファイルが作られる。
defaultでは`terraform.tfstate`がlocalに作られる。
state fileはただのJson file.
backupの作成を自動で行う。
localの場合はplain textで保存されるので、passwordなどは暗号化されていない。

**Remote State**

* backendとして以下が使える
    * [Backend: Supported Backend Types - Terraform by HashiCorp](https://www.terraform.io/docs/backends/types/index.html)
    * artifactory
    * azurerm
    * consul
    * etcd
    * gcs
    * http
    * manta
    * s3
    * swift
    * terraform enterprise
* backendのblockの中に書く項目はbackendごとに異なる

```
terraform {
  backend "consul" {
    address = "demo.consul.io"
    path    = "example_app/terraform_state"
  }
}
```

以下のように設定を空欄にしておけば実行時にconfigを指定可能。

```
terraform {
  backend "consul" {}
}
```

```
$ terraform init \
    -backend-config="address=demo.consul.io" \
    -backend-config="path=example_app/terraform_state"
```


**Sensitive data**

State fileにはpasswordなどのsensitive dataが保存される可能性がある。
remote stateの場合はmemoryにのみstateが保存される。



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

## Workspace
* [State: Workspaces - Terraform by HashiCorp](https://www.terraform.io/docs/state/workspaces.html)

0.10から追加された機能で、異なるstateを保持できる。
production, staging, development環境で異なるinfrastructureの管理をする場合などに利用する。

```
terraform workspace new name_of_workspace
```

workspaceの名前は以下から取得できる。

```tf
resource "aws_instance" "example" {
  tags {
    Name = "web - ${terraform.workspace}"
  }

  # ... other arguments
}
```

workspace名に応じてifなどで条件をつけることもできる。

```tf
resource "aws_instance" "example" {
  count = "${terraform.workspace == "default" ? 5 : 1}"

  # ... other arguments
}
```

## Modules
以下のmoduleのsourceとして利用できる
    * [Module Sources - Terraform by HashiCorp](https://www.terraform.io/docs/modules/sources.html)
    * [Terraform Module Registry](https://registry.terraform.io/?_ga=2.60555309.1863698067.1515572881-174552816.1502194891)に登録されているmodule
    * local file
        * `source = './path/to/module'`
    * GitHub
    * BitBucket
    * Git, Mercurial
    * HTTP URL
    * S3 bucket

moduleの呼び出し。


```tf
module "module_name" {
  # source of module
  source  = "hashicorp/consul/aws"
  version = "0.0.5"
  name = "module_name"

  # input variable for module
  servers = 3
}

output "output_name" {
  # module_output_name is output name defined in the module
  value = "${module.moduel_name.module_output_name}"
}
```

最小のstandard module structure

* `main.tf`
    * moduleのentrypoint
    * simpleな構成の場合は、すべてのresource定義が含まれる

```
.
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
```

より複雑な場合

```
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
├── ...
├── modules/
│   ├── nestedA/
│   │   ├── README.md
│   │   ├── variables.tf
│   │   ├── main.tf
│   │   ├── outputs.tf
│   ├── nestedB/
│   ├── .../
├── examples/
│   ├── exampleA/
│   │   ├── main.tf
│   ├── exampleB/
│   ├── .../
```

## Environment Variablaeso

Terraformのvairableをenvironment varibleから読み込める。
`TF_VAR_<variable name>`

```
export TF_VAR_region=us-west-1
export TF_VAR_ami=ami-049d8641
export TF_VAR_alist='[1,2,3]'
export TF_VAR_amap='{ foo = "bar", baz = "qux" }'
```

## Error

### netrpc
以下のようなerrorが出たらterraformのversionをあげる。
providerが古いterraformに対応していない可能生がある。
それかproviderのversionを指定する。

```
provider.terraform: dial unix ....|netrpc: connect: no such file or directory
```


## Interpolation syntax
* [Interpolation Syntax - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/interpolation.html)

`${var.foo}`で変数や関数を参照でき、Resource内で使える。

* `${var.foo}`
    * `foo`という名前のstring variableのreference
* `${var.foo["hoge"]}`
    * `foo`という名前のmap variableの`hoge` key の値
* `${var.foo[idx]}`
    * `foo`という名前のlist variableの`idx` 番目の値
* `${self.foo}`
    * 同じresource内の`foo`というstring variableの値
* `${resource_type.resource_name.attribute}`
    * resourceの`resource_type` typeの`resource_name`という名前がついたresourceの`attribute`の値
* `${data.data_type.data_name.attribute}.`
    * `resource`の
* `${data.data_type.data_name.0.attribute}.`
* `"${var.env == "production" ? var.prod_subnet : var.dev_subnet}"`

* `lookup(map, key [, default])`
    * keyがあればkeyの値を出力、なければdefault
    * defaultが省略されていれば、keyがないときerror

## count
* [Terraform tips & tricks: loops, if-statements, and gotchas](https://blog.gruntwork.io/terraform-tips-tricks-loops-if-statements-and-gotchas-f739bbae55f9)

## Reference
* [Configuration Syntax - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/syntax.html)
* [Terraform職人入門: 日々の運用で学んだ知見を淡々とまとめる - Qiita](https://qiita.com/minamijoyo/items/1f57c62bed781ab8f4d7)
* [chroju - Qiita](https://qiita.com/chroju)
* [Terraform moduleは何が嬉しいのか · the world as code](https://chroju.github.io/blog/2017/12/27/how_to_use_terraform_modules/)
