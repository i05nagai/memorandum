---
title: Apache HTTP
---

## Apache HTTP

## Config


## Module
モジュールはデフォルトで利用可能なものもある。
公式ドキュメントのステータスが

Install mod_wsgi

```
apt-get install libapache2-mod-wsgi
```

### log_config
* [mod_log_config - Apache HTTP サーバ バージョン 2.4](https://httpd.apache.org/docs/current/ja/mod/mod_log_config.html)


### logio
* [mod_logio - Apache HTTP サーバ バージョン 2.2](http://httpd.apache.org/docs/2.2/ja/mod/mod_logio.html)

* このモジュールはリクエストごとに受け取ったバイト数と 送信したバイト数のロギングを行なう機能を提供します。 記録される数字はリクエストのヘッダとレスポンスの本体を 反映した、実際にネットワークで受け取ったバイト値です。 入力では SSL/TLS の前に、出力では SSL/TLS の後に数えるので、 数字は暗号による変化も正しく反映したものになります。
* デフォルトでは入っていない

### mod_rewrite
* [Apacheのmod_rewriteモジュールの使い方を徹底的に解説 | OXY NOTES](http://oxynotes.com/?p=7392)

mod_rewriteを利用することでURLを書き換えやリダイレクトを指定することができます。

PHPでパラメータを追加して動的なURLを作成している場合、URLは以下のようになります。

```
http://example.com/?p=123
```

mod_rewriteを利用すれば以下のような静的なURLでアクセスすることが可能になります。

```
http://example.com/123/
```

## Reference
