---
title: apt-get
---

## apt-get

## CLI

## Usages
Upgrade the kernel in Ubuntum/ Upgrades the distribution in Debian

```
apt-get dist-upgrade
```

Search package

```
apt-cache search <package>
```

Show all version of `<packages>`

```
apt-cache madison <package>
```

Remove packages

```
apt-get remove <package>
apt-get autoclean
apt-get clean
```

`/var/cache/apt/archives`にキャッシュされていて、アプリを削除した後もキャッシュは残る。
`apt-get autoclean`では、この`/var/cache/apt/archives`にキャッシュされていてシステムにはインストールされていない`.deb`ファイルが削除され、`apt-get clean`では`/var/cache/apt/archives`にキャッシュされている全てのパッケージが削除される。

To see installed package,

```
dpkg -l
```


## Tips

## Reference
* [NetWalker覚書～へなちょこおたくメモ～: apt-get autocleanやapt-get cleanで不要なキャッシュを削除する](http://toshi-netwalker.blogspot.jp/2010/02/apt-get-autocleanapt-get-clean.html)
* [[Ubuntu] apt-get まとめ - Qiita](http://qiita.com/white_aspara25/items/723ae4ebf0bfefe2115c)
