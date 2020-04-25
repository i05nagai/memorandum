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

### location of .desktop
* `/usr/share/applications`

### install gcc-4.6 and g++-4.6
`/etc/apt/sources.list`に以下を追加し、

* `apt-get update`
* sudo apt-get install gcc-4.6
* sudo apt-get install g++-4.6

```
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

```
cat id_rsa.pub >> /path/to/user/home/.ssh/authorized_keys
```

`authorized_keys`と`id_rsa.pub`などは`chmod 600 authorized_keys`で権限を設定しておく。

#### rootのsshd設定
`/root/.ssh`に配置する。

## Managing user

### Add user
```
sudo adduser USER
```

`useradd`はホームディレクトリなどは指定しないと作られない。

useraddの場合は

```
useradd user_name -m -d /home/user_name -p encripted_password
```

* `encripted_password`は暗号化されたパスワードを指定する
    * perlが使える場合は下記で'passowrd'を'keyword'で暗号化したpasswordが使える
    * `perl -e "print(crypt('password', 'keyword'));"`

### Delete user

```
sudo userdel -r USER
```

### show users

```
ls /etc/passwd
```

### add sudo previledge to user
`user_name`に`sudo`権限をつける。
sudoで求められるpasswordは、suするユーザのpasswordではなく、sudoを実行したユーザのpasswordである。

```
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

### Use japanese input method
* [Ubuntu 16\.10でibus\-mozcを使用する \- Sickly Life Blog](https://sicklylife.hatenablog.com/entry/2016/11/22/192850)

For Ubuntu 16.04,

fcitx+mozcの組み合わせで良い。
設定の方法は、 `Settings`->`Text Entry`->`input method`->`fcitx`を選択。
keyboard iconを右clickすると`fcitx`のconfigurationが開く。
`Global config`のtabで`Trigger input method`があるので、これを`Shift+space`などに割り当てる。

`xmodmap`の設定が反映されない場合があるが、window managerをi3に変更したら修正された。
fcitxのofficial documentによれば、`4.9.2`からは`$HOME/.Xmodmap`が存在すればその設定を反映させるらしい。
keyboard周りは設定の反映にlogoutなどが必要な場合もあるので、window managerに変更する過程のlogoutで適用されたかもしれない。

### shutdown/logout is very slow
[Slow shutdown on Ubuntu 16\.04 LTS \(Stopping thermal daemon/running fit make remote CUPS printers\) \- Ask Ubuntu](https://askubuntu.com/questions/760952/slow-shutdown-on-ubuntu-16-04-lts-stopping-thermal-daemon-running-fit-make-remo)

```
systemctl disable cups-browsed.service
```

### Delete amazon
* [How to Remove the Amazon Application from Ubuntu](https://www.lifewire.com/remove-amazon-application-from-ubuntu-4134329)

### Change keybindings like Emacs
* [gtk \- How do I change my gnome Ubuntu key\-binding work as emacs? \- Super User](https://superuser.com/questions/345452/how-do-i-change-my-gnome-ubuntu-key-binding-work-as-emacs)
* [Ubuntu で key\-theme を emacs にしたときにテキストを全選択する方法 \- Qiita](https://qiita.com/ledmonster/items/f37c86a1b9fc408f0b9b)

Keybinds are defined in `/usr/share/themes/Emacs/gtk-3.0` or `/usr/share/themes/Emacs/gtk-2.0-key/gtkrc`
Get current key theme.

```
gsettings get org.gnome.desktop.interface gtk-key-theme "Emacs"
```

Set current theme to Emacs

```
gsettings set org.gnome.desktop.interface gtk-key-theme "Emacs"
```

You can change to default keybinds by

```
gsettings set org.gnome.desktop.interface gtk-key-theme "Default"
```

### Backlight
* [grub2 \- What is the difference between GRUB\_CMDLINE\_LINUX and GRUB\_CMDLINE\_LINUX\_DEFAULT in /etc/default/grub \- Ask Ubuntu](https://askubuntu.com/questions/575651/what-is-the-difference-between-grub-cmdline-linux-and-grub-cmdline-linux-default)
* [echo xx \| sudo tee /sys/class/backlight/intel\_backlight/brightness](https://askubuntu.com/questions/471847/brightness-fn-key-shortcut-doesnt-work-on-asus-laptop)

Chagne backlight brightness from CLI

```
# check backlight device
$ ls -la /sys/class/backlight

# check max value of brightness
$ sudo cat /sys/class/backlight/intel_backlight/max_brightness

# change value of brightness
$ echo 5000 | sudo tee /sys/class/backlight/intel_backlight/brightness

# get current brightness
$ cat /sys/class/backlight/intel_backlight/brightness
```

```
sudo vim /etc/default/grub
```

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash acpi_backlight=vendor"
```

Execute

```
sudo update-grab
```

## Function keys
- [Enable Fn Keys on HP Essential Laptops & Ubuntu 16\.04 \| UbuntuHandbook](http://ubuntuhandbook.org/index.php/2018/02/enable-fn-keys-hp-ubuntu-16-04/)
- [Set F\-Keys primary instead of special keys on Lenovo \- Ask Ubuntu](https://askubuntu.com/questions/404275/set-f-keys-primary-instead-of-special-keys-on-lenovo)
- [How to get special keys to work \- ThinkWiki](http://www.thinkwiki.org/wiki/How_to_get_special_keys_to_work)


## Reference
* [Ubuntuサーバー管理チートシート - Qiita](http://qiita.com/shunichi/items/c7744878f5c02eaab18d)
