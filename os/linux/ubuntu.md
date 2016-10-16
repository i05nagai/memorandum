# ubuntu

## tips
### install gcc-4.6 and g++-4.6
`/etc/apt/sources.list`に以下を追加し、
* `apt-get update`
* sudo apt-get install gcc-4.6`
* sudo apt-get install g++-4.6`

```shell
deb     http://archive.ubuntu.com/ubuntu/ trusty universe  
deb-src http://archive.ubuntu.com/ubuntu/ trusty universe
```

## SSH

```
apt-get install ssh
```

`/etc/ssh/sshd_config`を設定する。

```
PermitRootLogin no
```

### server settings
ログインするユーザのディレクトリに`authorized_keys`を追加する。
`id_rsa.pub`を公開鍵とする。

```ssh
cat id_rsa.pub >> /path/to/user/home/.ssh/authorized_keys
```

`authorized_keys`と`id_rsa.pub`などは`chmod 600 authorized_keys`で権限を設定しておく。

#### rootのsshd設定
`/root/.ssh`に配置する。

## Managing user

### Add user
```shell
sudo adduser USER
```

`useradd`はホームディレクトリなどは指定しないと作られない。

useraddの場合は

```shell
useradd user_name -m -d /home/user_name -p encripted_password
```

* `encripted_password`は暗号化されたパスワードを指定する
    * perlが使える場合は下記で'passowrd'を'keyword'で暗号化したpasswordが使える
    * `perl -e "print(crypt('password', 'keyword'));"`

### Delete user

```shell
sudo userdel -r USER
```

### show users

```shell
ls /etc/passwd
```

### add sudo previledge to user
`user_name`に`sudo`権限をつける。
sudoで求められるpasswordは、suするユーザのpasswordではなく、sudoを実行したユーザのpasswordである。

```shell
gpasswd -a user_name sudo
```

## reference
* [Ubuntuサーバー管理チートシート - Qiita](http://qiita.com/shunichi/items/c7744878f5c02eaab18d)
