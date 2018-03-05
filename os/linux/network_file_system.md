---
title: Network File System
---

## Network File System
* [SettingUpNFSHowTo - Community Help Wiki](https://help.ubuntu.com/community/SettingUpNFSHowTo)
    * NFSv3はrpcbind

## Client
Client

```
sudo apt install nfs-common
```

## Configuration
`/etc/fstab`に以下をかく

```
example.hostname.com:/ubuntu /local/ubuntu nfs rsize=8192,wsize=8192,timeo=14,intr
```

## Server

Install

```
sudo apt install nfs-kernel-server
```

## Configuration
* [Ubuntu Manpage: exports - NFS server export table](http://manpages.ubuntu.com/manpages/xenial/man5/exports.5.html)

`/etc/exports`にNFS clientに公開するdirectoryの設定をかく。

設定の反映は、nfs-serverをrestartするか以下を実行する。

```
sudo exportfs-ra
```

* whitespace separated

```
# sample /etc/exports file
# path host1(options)  host2(options)
/               master(rw) trusty(rw,no_root_squash)
/projects       proj*.local.domain(rw)
/usr            *.local.domain(ro) @trusted(rw)
/home/joe       pc001(rw,all_squash,anonuid=150,anongid=100)
/pub            *(ro,insecure,all_squash)
/srv/www        -sync,rw server @trusted @external(ro)
/foo            2001:db8:9:e54::/64(rw) 192.0.2.0/24(rw)
/build          buildhost[0-9].local.domain(rw)
/ubuntu  *(ro,sync,no_root_squash)
/home    *(rw,sync,no_root_squash)
```

* `secure`
    * `IPPORT_RESERVED(1024)`以下のportを使うときに必要
    * default on
* `rw`
    * read/write
* `ro`
    * read only
* `async`
    * NFS protocolに従わず、changeがcommitされる前にrequestにreplyできる
    * crashなどでdataがlostする可能性がある
* `sync`
    * defualt sync
* user id mapping
    * serverのfileへのaccessはclientのuid/gidを使う
    * `root_squash`
        * uid/gid 0をanonymousへ uid/gidにmapする
    * `no_root_squash`
        * diskless clientで有効
    * `all_squash`
        * 全てのclientのuid/gidをanonymousにMapする



## Reference
* [Network File System (NFS)](https://help.ubuntu.com/lts/serverguide/network-file-system.html)
* [Ubuntu Manpage: rpc.mountd - NFS mount daemon](http://manpages.ubuntu.com/manpages/xenial/man8/mountd.8.html)
