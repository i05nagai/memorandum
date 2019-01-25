---
title: Terraform
---

## Terraform
Terraformの設定ファイルはHCLで記述する。

* `.tf`, `.tf.json`
* fileはdirectoryごとにalphabetic orderで読まれる
* variableの宣言順序は関係ない


## Concepts
* workspace
    * dev/stg/prodなどの環境の切り替えに使われる
    * [State: Workspaces - Terraform by HashiCorp](https://www.terraform.io/docs/state/workspaces.html)
* state
    * [State - Terraform by HashiCorp](https://www.terraform.io/docs/state/purpose.html)
    * 作成したresourceが持つstate
    * stateのimportもできる
        * [Import: Usage - Terraform by HashiCorp](https://www.terraform.io/docs/import/usage.html)
    * terraformのversion
* remote state
    * stateをGCSなどのremoteにもてる
    * teamで共有したり、CIで利用する
    * [State: Remote Storage - Terraform by HashiCorp](https://www.terraform.io/docs/state/remote.html)
* locals
    * [Configuring Local Values - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/locals.html)
    * [Variable cannot contain interpolation? · Issue #14343 · hashicorp/terraform](https://github.com/hashicorp/terraform/issues/14343)
    * variables blockの中でvarは利用できないので、 変数を使って値を生成する際などに利用する。
    * varに書いている定数はだいたい置き換えが可能
* variables
    * resource定義の変数として使う
* outputs
    * resourceの出力結果
* modules
    * 設定fileをmoduleとして共通化できる
* resources
    * terraformが扱うinfrastructure
* resroucde addressing
    * [Internals: Resource Address - Terraform by HashiCorp](https://www.terraform.io/docs/internals/resource-addressing.html)
    * resourceはそれぞれaddressをもつ
        * `[module path][resource spec]`
    * moduleを使っている場合は、moduleで使っているresourceもaddressを持つ
        * `module.A.module.B.module.C...`
    * countを使っている場合は番号がつく。
* data sources
    * resourceを作成も管理しないが、参照だけしたい場合に使う
    * 作成はしないが管理したい場合は、state importを使う


## Resource
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

## DataSource
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


## Tips

### General needs
terraform周りでよくあるやりたいこと

* dev/stg/prodでresourceを分けて管理
    * workspaceを使う
* dev/stg/prodでresourceを作る作らないを選択
    * countを使う
* dev/stg/prodで共通のresourceを選択
    * commonというworkspaceを作る
* serviceごとでresourceの作成を選択
    * serviceごとのresourceをdirectory/moduleに分ける
* serviceごとで共通のresourceを作成する
    * coreというdirectory/moduleに作成する

### to create resource if only specified environment
environmentごとにresourceの作成/不作成を決める。

```tf
locals {
    flag = {
        # important that the value is exclusive
        env_dev = "${var.env == "dev" ? 1 : 0}"
        env_stg = "${var.env == "stg" ? 1 : 0}"
        env_prod = "${var.env == "prod" ? 1 : 0}"
    }
}

# only created if env is dev
resource "google_kms_key_ring_iam_binding" "container_builder" {
  count = "${local.flag["env_dev"]}"
  ...
}
# if env is dev or stg
resource "google_kms_key_ring_iam_binding" "container_builder" {
  # must be 0 <= local.flag["env_dev"] + local.flag["env_stg"] <= 1
  count = "${local.flag["env_dev"] + local.flag["env_stg"] }"
  ...
}
```

### Rename resource with state
以下のcommandでstateのrenameができる。
configurationを書き換えて、stateをrenameすればOK

```
terraform state mv SOURCE DESTINATION
```

### Debug
CLIの実行時に環境変数を設定することで、実行することで、logの出力を変更できる

* `TF_LOG`
    * TRACE, DEBUG, INFO, WARN or ERROR
    * defualt: INFO
    * TRACE is the most verbose
* `TF_LOG_PATH`
    * logの出力先
    * `/dev/stdout`
* `[apply|plan] -parallelism=0`
    * disable parallelism

```
TF_LOG=DEBUG TF_LOG_PATH=/tmp/terraform.log terraform apply -parallelims=0
```

## override
* `_override`で終わる`.tf`か`override.tf`のファイルで設定の上書きができる。

### Rename workspace / move state to another workspace
* [Improvement Command: terraform workspace rename · Issue #16072 · hashicorp/terraform](https://github.com/hashicorp/terraform/issues/16072)

```sh
# pull and export current state in workspace
terraform state pull > remote_state.tfstate
# create new workspace with exported state
terraform workspace new -state= remote_state.tfstate <new_workspace_name>
# show state
terraform state list
# delete old workspace if you want
terraform workspace delete <old_workspace_name>
```

### Automation
* [Running Terraform in Automation - Guides - Terraform by HashiCorp](https://www.terraform.io/guides/running-terraform-in-automation.html)

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
        * `GOOGLE_CREDENTIALS`でcredentialsを設定できる
    * http
    * manta
    * s3
        * you need to create bucket before `terraform init`
    * swift
    * terraform enterprise
* backendのblockの中に書く項目はbackendごとに異なる
* backendの設定でinterpolationは使えない
* terraform init時の`-backend-config=""` で設定する

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
remote stateの場合はbackendのfile上にsensitiveなdataが保存される。

## Workspace
* [State: Workspaces - Terraform by HashiCorp](https://www.terraform.io/docs/state/workspaces.html)
* [Naming - Workspaces - Terraform Enterprise - Terraform by HashiCorp](https://www.terraform.io/docs/enterprise/workspaces/naming.html)
    * enterpriseで例としてあがっているnaming

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

moduleの呼び出し方


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

**Moduleの作り方**

* [Creating Modules - Terraform by HashiCorp](https://www.terraform.io/docs/modules/create.html)

最小のstandard module structure

* `main.tf`
    * moduleのentrypoint
    * simpleな構成の場合は、すべてのresource定義が含まれる
* `variables.tf`
    * moduleのvariable定義
* `outputs.tf`
    * moduleのoutputs定義

```
.
├── README.md
├── main.tf
├── variables.tf
├── outputs.tf
```

より複雑な場合、moduleはNestできる。

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

いつmoduleを使うべきか

* [Part 3.2: From Semi-Automation to Infrastructure as Code - Terraform Recommended Practices - Terraform by HashiCorp](https://www.terraform.io/docs/enterprise/guides/recommended-practices/part3.2.html#3-create-your-first-module)


## Environment Variables

Terraformのvairableをenvironment varibleから読み込める。
`TF_VAR_<variable name>`

```
export TF_VAR_region=us-west-1
export TF_VAR_ami=ami-049d8641
export TF_VAR_alist='[1,2,3]'
export TF_VAR_amap='{ foo = "bar", baz = "qux" }'
```

## Error

#### design

workspaces

* `dev`
* `prod`
* `stg`

directory

* `variables.tf`
    * workspaceごとの値を定義
* `locals.tf`
    * workspaceごとの差異を吸収して、必要な変数を定義
* `main.tf`
    * modulesの呼び出し
    * resourceは定義しない
* `script/`
    * `terraform/`
        * `import.sh`
            * 全てのworkspaceで共通で使われるresourceをimportするscript
        * `import/`
            * import用のfile
* `core/`
    * 全てのserviceでshareするresource
    * `aws/`
        * service内で`terraform.workspace`は使わない。変数としてうけとる。環境を変数として受けて、環境にあわせたresourceを返す
        * `variables.tf`
    * `gcp/`
* `<service1>/`
    * `aws/`
    * `gcp/`
* `<service2>/`
    * `aws/`
    * `gcp/`
* `immutables/`
    * 参照するが殆ど変更しないもの
    * `data` resourceが使えるものは使うが、何らかの理由で変更する可能性がある
    * `<serviceA>/`
        * `aws/`
        * `gcp/`

```sh
$ terraform worksapce select dev
# imoprt resources shared with all worksapce
$ import.sh
$ terraform plan
```

* `import.sh`を使わない場合は、workspaceで共有するresouce用のworkspace `core`, `common`を作る方法がある。
    * この場合は、`prod`, `dev`などで`core`のresourceを参照できなくなる。
    * 実際参照するためには、stateのimportが必要になるので、`import.sh`を使う方法と同じになる。
    * `dev`をuserごとに作る場合は、`dev<username>`のworkspaceを作っても良いが、一部resourceしか使わず殆どのresourceを共有する場合は、fileに`<workspace><username>`のresourceを追加してtask runnerでtargetを制御する方法で良い。
* task runnerでのtargetの制御はある程度は必須。
* workspacesをdev/stg/prodなどで分ける場合は、どのresourceをどのworkspaceで使うかどうかはあらかじめ設計しておく必要がある

## Best practices
* [Terraform職人入門: 日々の運用で学んだ知見を淡々とまとめる - Qiita](https://qiita.com/minamijoyo/items/1f57c62bed781ab8f4d7)
    * よくまとまっている
* [Terraform Best Practices in 2017 - Qiita](https://qiita.com/shogomuranushi/items/e2f3ff3cfdcacdd17f99)
    * directory設計のpractice
* [best-practices/terraform at master · hashicorp/best-practices](https://github.com/hashicorp/best-practices/tree/master/terraform)
    * officialのbest practice
    * workspaceなどの導入により、deprecatedになっている


```
- core/
-- gcp/
-- aws/
- service1/
-- gcp/
-- aws/
- serivce2/
-- gcp/
-- aws/
- main.tf
- provider.tf
- backend.tf
- variables.tf
- locals.tf
```

* dev/stg/prodで共通のresourceを使う場合
* dev/stg/prodで異なるresourceを使う場合
    * workspaceで分けていればprefixをid(name)に含めてworkspaceごとに管理すればOK
* serviceで異なるresourceを使う場合
    * serviceの各directoryに
* serviceで共通のresourceを使う場合
    * core/commonという名前のdirectory(service)を使う
    * networkと


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

## Reference
* [Configuration Syntax - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/syntax.html)
* [Terraform職人入門: 日々の運用で学んだ知見を淡々とまとめる - Qiita](https://qiita.com/minamijoyo/items/1f57c62bed781ab8f4d7)
* [chroju - Qiita](https://qiita.com/chroju)
* [Terraform moduleは何が嬉しいのか · the world as code](https://chroju.github.io/blog/2017/12/27/how_to_use_terraform_modules/)
