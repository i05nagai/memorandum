---
title: openssl
---
## openssl


## self signed certification
以下で、10年間有効な自己署名証明書が作れる。

```ssh
openssl genrsa 2048 > server.key
openssl req -new -key server.key > server.csr
openssl x509 -days 3650 -req -signkey server.key < server.csr > server.crt
```

* certificate file
    * server.crt
* certificate key file
    * server.key

* [オレオレ証明書をopensslで作る（詳細版） - ろば電子が詰まっている](http://d.hatena.ne.jp/ozuma/20130511/1368284304)


## Reference


