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

## CLI
[The Most Common OpenSSL Commands](https://www.sslshopper.com/article-most-common-openssl-commands.html)

Check a Certificate Signing Request (CSR)

```
openssl req -text -noout -verify -in CSR.csr
```

check private key

```
openssl rsa -in privateKey.key -check
```

Check a certificate

```
openssl x509 -in certificate.crt -text -noout
```

Check a PKCS#12 file (.pfx or .p12)

```
openssl pkcs12 -info -in keyStore.p12
```

## PEM file
* [How to SSL - PEM Files](http://how2ssl.com/articles/working_with_pem_files/)
* [How to SSL - OpenSSL tips and common commands](http://how2ssl.com/articles/openssl_commands_and_tips/)


## Reference


