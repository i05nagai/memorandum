---
title: apt-get
---

## apt-get

```
apt-get autoclean
apt-get clean
```

`/var/cache/apt/archives`にキャッシュされていて、アプリを削除した後もキャッシュは残る。
`apt-get autoclean`では、この`/var/cache/apt/archives`にキャッシュされていてシステムにはインストールされていない`.deb`ファイルが削除され、`apt-get clean`では`/var/cache/apt/archives`にキャッシュされている全てのパッケージが削除される。

## CLI


* apt-get dist-upgrade
    * インストールされてるカーネルの更新(Ubuntu)/ディストリビューションの更新(Debian)
* dpkg -l [package]
    * インストールされてるパッケージの一覧
* dpkg -L
    * インストールした時のファイルの一覧

Search package

```
apt-cache search <package>
```

Show all version of `<packages>`

```
apt-cache madison <package>
```


## Add repository
* [apt-getで見つからないパッケージを追加する方法(debian, ubuntu両方対応) - Qiita](http://qiita.com/kon_yu/items/8ac350f3951f8534c931)

`apt-add-repository` commandは以下に含まれている。

```
apt-get install -y software-properties-common
```

## Tips

## Reference
* [NetWalker覚書～へなちょこおたくメモ～: apt-get autocleanやapt-get cleanで不要なキャッシュを削除する](http://toshi-netwalker.blogspot.jp/2010/02/apt-get-autocleanapt-get-clean.html)
* [[Ubuntu] apt-get まとめ - Qiita](http://qiita.com/white_aspara25/items/723ae4ebf0bfefe2115c)

