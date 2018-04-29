---
title: OpenSSH
---

## OpenSSH
includeが使えるようになるのは、7.3.pから

## Install

For ubuntu 16.04,

* [Install OpenSSH 7\.3 in Ubuntu 16\.04](https://gist.github.com/stefansundin/0fd6e9de172041817d0b8a75f1ede677)
* [Openssh\-client Download \(DEB\)](https://pkgs.org/download/openssh-client)

```
mkdir -p /tmp/openssh
wget --no-check-certificate https://launchpadlibrarian.net/335526589/openssh-client_7.5p1-10_amd64.deb
wget --no-check-certificate https://launchpadlibrarian.net/298453050/libgssapi-krb5-2_1.14.3+dfsg-2ubuntu1_amd64.deb
wget --no-check-certificate https://launchpadlibrarian.net/298453058/libkrb5-3_1.14.3+dfsg-2ubuntu1_amd64.deb
wget --no-check-certificate https://launchpadlibrarian.net/298453060/libkrb5support0_1.14.3+dfsg-2ubuntu1_amd64.deb
sudo dpkg -i libkrb5support0_1.14.3+dfsg-2ubuntu1_amd64.deb
sudo dpkg -i libkrb5-3_1.14.3+dfsg-2ubuntu1_amd64.deb
sudo dpkg -i libgssapi-krb5-2_1.14.3+dfsg-2ubuntu1_amd64.deb
sudo dpkg -i openssh-client_7.5p1-10_amd64.deb
ssh -V
```

```
mkdir -p /tmp/openssh
cd /tmp/openssh
curl -L -O https://launchpad.net/ubuntu/+archive/primary/+files/openssh_7.6p1.orig.tar.gz
tar xvf openssh_7.6p1.orig.tar.gz
./configure --prefix=/usr                     \
            --sysconfdir=/etc/ssh             \
            --with-md5-passwords              \
            --with-privsep-path=/var/lib/sshd              \
            --with-pam
```


## Reference
