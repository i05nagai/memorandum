## Alpine Linux

## Packages
* [Alpine packages](https://pkgs.alpinelinux.org/packages)
    * packageの一覧

psコマンドでエラー。
ps commandはbusyboxコマンドなので、通常のpsとは違う。
通常のpsで使えるオプションなどを使いたい場合は以下をインストールする。

```
apk --no-cache add procps
```

## apk
* [Alpine Linux package management - Alpine Linux](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management)

```
apk add <package_name>
```

versionを指定する

```
apk add <package_name>=1.2.2
```

cacheなしで追加。
`rm -rf /var/cache/apk/*`と同じ。

```
apk --no-cache add
```

別名を付与してinstall.
`<virtual_name>`で削除できる。

```
apk add --virtual <virtual_name> <package_name>
apk del <virtual_name>
```

packageの削除

```
apk del <package_name>
```

関連するファイルも削除。

```
apk del --purge <package_name>
```

updateする。

```
apk update
```

packageの検索。

```
apk search <package_name>
```

Delete old package

```
apk cache clean -v
```


## Reference
* [Alpine Linux入門 -内部構造とapkでパッケージインストール編- - tehepero note(・ω<)](http://blog.stormcat.io/entry/alpine-entry-apk)
* [Alpine Linuxあるある - Qiita](http://qiita.com/MiCHiLU/items/1e80a5325b2746eaf2d4)
