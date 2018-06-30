---
title: Terraform Syntax
---

## Terraform Syntax
Terraform Configuration Syntax.

## Syntax
基本はHCLで記述する。

* true/false
    * boolean
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

### Interpolation syntax
* [Interpolation Syntax - Terraform by HashiCorp](https://www.terraform.io/docs/configuration/interpolation.html)

`${}`で変数や関数を参照でき、Resource内で使える。

* `"${path.module}"`
    * module path
* `"${path.cwd}"`
    * working dir
* `"${path.root}"`
    * root module dir
* `"${var.subnets}"`
    * subnetsがlistの場合、listとして変数を参照
* `"${var.foo}"`
    * `foo`という名前のstring variableのreference
* `"${var.foo["hoge"]}"`
    * `foo`という名前のmap variableの`hoge` key の値
* `"${var.foo[idx]}"`
    * `foo`という名前のlist variableの`idx` 番目の値
* `"${self.foo}"`
    * 同じresource内の`foo`というvariableの値
* `"${resource_type.resource_name.attribute}"`
    * resourceの`resource_type` typeの`resource_name`という名前がついたresourceの`attribute`の値
* `"${data.data_type.data_name.attribute}"`
    * dataの`data_type` typeの`data_name`という名前がついたdataの`attribute`の値
* `"${data.data_type.data_name.0.attribute}"`
* `"${var.env == "production" ? var.prod_subnet : var.dev_subnet}"`
    * if文
* `"${lookup(map, key [, default])}"`
    * keyがあればkeyの値を出力、なければdefault
    * defaultが省略されているか、keyがないときerror

### count
* [Terraform tips & tricks: loops, if-statements, and gotchas](https://blog.gruntwork.io/terraform-tips-tricks-loops-if-statements-and-gotchas-f739bbae55f9)

terraformにおけるfor文

```terraform
resource "resource_type" "resource_name" {
    count = 3
}
```

countをifの用に使う

```terrafomr
# if var.create_eip = true => count is 0 => does not create
# if var.create_eip = false => count is 1 => create
resource "aws_route53_record" "example" {
  count = "${1 - var.create_eip}"
  zone_id = "A1B2CDEF3GH4IJ"
  name = "foo.example.com"
  type = "A"
  ttl = 300
  records = ["${aws_instance.example.public_ip}"]
}
```

`data "template_file"`でstringのifができる。

```terraform
data "template_file" "user_data_shell" {
  count = "${var.use_shell_script_user_data}"
  template = <<-EOF
              #!/bin/bash
              run-microservice.sh
              EOF
}
data "template_file" "user_data_cloud" {
  count = "${1 - var.use_shell_script_user_data}"
  template = <<-EOF
              #cloud-config
              runcmd:
                - run-microservice.sh
              EOF
}

# if var.use_shell_script_user_data = true => user_data_cloud = empty
# if var.use_shell_script_user_data = false => user_data_shell = etpty
resource "aws_instance" "example" {
  ami = "${var.ami}"
  instance_type = "${var.instance_type}"
  user_data = "${element(concat(data.template_file.user_data_shell.*.rendered, data.template_file.user_data_cloud.*.rendered), 0)}"
  
  tags {
    Name = "${var.service_name}"
  }
}
```

null_data_soruceを使う

```
# map[string]
data "null_data_source" "values" {
    count = 1
    inputs = {
        key = ""
    }
}
# ${data.null_data_soruce.values.*.outputs}

```

## Reference
