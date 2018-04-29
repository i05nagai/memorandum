---
title: ubuntu
---

## ubuntu
* package mangaer
    * apt-get

## Create a bootable USB stick on Windows
* https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows#0

* Rufus

## Tips

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

## apt-get
versionを指定してinstall

```
sudo apt-get install nginx=1.8.0-1
```

## ubuntu in Dockerで日本語表示
* [Docker＋Ubuntuで日本語入力できないのを解決した](http://blog.nocorica.jp/2017/01/docker-ubuntu-japanese-input/)

## LVM
* http://piro791.blog.so-net.ne.jp/2008-11-04


## DiskSpace
* https://help.ubuntu.com/community/DiskSpace

For non-GPT disk

* swap
    * size of RAM
* /
    * the rest of the disk

For GPT disk,
`sudo parted -l`

* BIOS-boot or EFI
* swap
    * size of RAM
* /
    * required
    * Mount point: /
    * minimum 8GB
    * recommended: 15GB
* swap
    * recommended
    * mount point: none
    * size of RAM
    * https://help.ubuntu.com/community/SwapFaq
* /boot
    * sometiems required
    * 250MB - 1GB
    * 100GBより多くlocateされていると、`/boot`が見えないことがあるのでたまに分けて作る必要がある
* BIOS boot
    * Mount point: none
    * no filesystem
    * GRUB2のcore
    * EFI mode以外でBIOSが動いている場合必要
    * 1MB
* EFI partition
    * Mount pont: /boot/efi
    * installerが自動でinstallする
    * FAT/FAT32
    * EFI partiton, ESP contain some boot files
    * 2011 year の後のcomputers
    * 100MB - 250MB

Optional partitions

* /home
    * EXT4
    * 
* /srv
    * less than 100MB
    * serverの場合は
* /opt
* /tmp
    * swapと同じsize
* /dev
    * do not partition
* /mnt
    * do not partition
* /media
    * do not partition

## Swap
* https://help.ubuntu.com/community/SwapFaq

Disable swap

https://askubuntu.com/questions/214805/how-do-i-disable-swap

```
sudo swapoff -a
```

delete `fstab`

## Tips

### Change shell
* https://superuser.com/questions/119179/how-can-i-change-shell-in-ubuntu

sudoなしの`chsh`を実行すれば良い。


## Reference
* [Ubuntuサーバー管理チートシート - Qiita](http://qiita.com/shunichi/items/c7744878f5c02eaab18d)
