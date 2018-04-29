---
title: terraform provisioner
---

## terraform provisioner
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

### file
terraformのmachineにあるfile/directoryをresourceにuploadする。

```tf
resource "aws_instance" "web" {
  # Copies all files and folders in apps/app1 to D:/IIS/webapp1
  provisioner "file" {
    source      = "apps/app1/"
    destination = "D:/IIS/webapp1"
  }
}
```

### habitat
Habitat supervisorをresourceにinstallする。


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

