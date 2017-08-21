---
---

## apt-get

```
apt-get autoclean
apt-get clean
```

`/var/cache/apt/archives`にキャッシュされていて、アプリを削除した後もキャッシュは残る。
`apt-get autoclean`では、この`/var/cache/apt/archives`にキャッシュされていてシステムにはインストールされていない`.deb`ファイルが削除され、`apt-get clean`では`/var/cache/apt/archives`にキャッシュされている全てのパッケージが削除される。


## Reference
* [NetWalker覚書～へなちょこおたくメモ～: apt-get autocleanやapt-get cleanで不要なキャッシュを削除する](http://toshi-netwalker.blogspot.jp/2010/02/apt-get-autocleanapt-get-clean.html)
