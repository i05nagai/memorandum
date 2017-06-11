---
title: Amazon Linux
---

## Amazon Linux



## Tips
### First thing frist

```
sudo yum update
```


### Add user

```
sudo adduser <username>
cd /home
sudo su username
cd username
mkdir .ssh
touch .ssh/authorized_keys
```

authorized_keysにログインするユーザのpublic keyを貼り付ける。
必要なら複数のkeyを貼り付けてOK
最後に、

```
chmod 600 .ssh/authorized_keys
```

にして終わり。
defaultのec2-userを削除したい場合は、

```
sudo userdel -r ec2-user
```

で良い。
ファイルの所有者は間違ったら以下で変更できる。


```
sudo chown -R username username/.ssh
```


## Reference
