---
title: Apache2
---

## Apache2



## Modules

## core
* [core - Apache HTTP Server Version 2.4](https://httpd.apache.org/docs/2.4/mod/core.html)

* AcceptFilter
* AcceptPathInfo
* AccessFileName
* AddDefaultCharset
* AllowEncodedSlashes
* AllowOverride
* Directory
    * directiveをgroup化して指定したdirectory以下にのみ適用する
    * directoryの指定にはwild cardが使える
    * Directory directiveのnestは不可

```
<Directory "/usr/local/httpd/htdocs">
  Options Indexes FollowSymLinks
</Directory>
```

* Files
    * filenameに言っつする全てのファイルに適用する
    * FilesとDirectoryの組み合わせも可能

```
<Directory /var/web/dir1>
    <Files private.html>
    Order allow,deny
    Deny from all
    </Files>
</Directory>
```

* Location
    * directieをgroup化して指定したURL以下にのみ適用する

```
<Directory "/URL">
  Options Indexes FollowSymLinks
</Directory>
```

* Options
    * `Options +ExecCGI`
        * 付与
    * `Options -ExecCGI`
        * 除外
    * 特定のdirectoryでserverの機能をON/OFFする
    * ExecCGI
        * CGIの実行を許可
    * FollowSymLinks
        * symbolic linkをfollowする
    * Includes
    * Indexes
        * directoryに対応するfileを検索する
    * MultiViews
        * User Agentをみてcontentsを変えるcontents negotiationを行うためのoption
        * 英語であれば、英語版が、日本語であれば日本語版が表示される

* `DirectoryIndex`

```
<Directory "/path/to/directory">
    DirectoryIndex index.cgi
</Directory>
```

* SetHandler
    * 指定したfileをhandlerで処理するようにする


### mod_alias
* [mod_alias - Apache HTTP Server Version 2.4](https://httpd.apache.org/docs/current/mod/mod_alias.html)
    * URLとfilesystemのpathをmapする
    * 同じaliasが複数定義された場合は、ある順序に従って優先順位がきまる
    * AliasとRedirectはRedirectが先に適用される
    * RedirectにMatchする場合は、Aliasは評価されない
    * その他順番は、configファイルで先に現れた方が適用される
    * なので、subdirectoryを含む設定は、含まない設定より前に現れる必要がある


* `Alias`
* AliasMatch
* Redirect
* RedirectMatch
* RedirectPermanent
* RedirectTemp
* `ScriptAlias`
    * filesystemのpathがcgi contentsのみを含む場合に利用する

以下と

```
ScriptAlias "/cgi-bin/" "/web/cgi-bin/"
```

以下は等価

```
Alias "/cgi-bin/" "/web/cgi-bin/"
<Location "/cgi-bin">
    SetHandler cgi-script
    Options +ExecCGI
</Location>
```

* ScriptAliasMatch

### mod_wsgi
* https://qiita.com/arc279/items/df28bd100cc2f72fad3c

```
WSGIScriptAlias /wsgi-scripts/ /web/wsgi-scripts/
```

は以下と等価。
Aliasのmerge ruleとWSGIScriptAliasのMerge ruleは異なるので、他のaliasがある場合はAliasを使って、`Location`や`Directive`で指定した方が良い。

```
Alias /wsgi-scripts/ /web/wsgi-scripts/
<Location /wsgi-scripts>
SetHandler wsgi-script
Options +ExecCGI
</Location>
```

例えば、

```
Alias /image /path/to/hoge/hoge.wsgi
<Directory "/path/to/hoge">
    SetHandler wsgi-script
    Options +ExecCGI
    Require all granted
</Directory>
```

## CLI
a2ensite

a2dissite

* [a2dissite(8) — apache2 — Debian jessie — Debian Manpages](https://manpages.debian.org/jessie/apache2/a2dissite.8.en.html)

## Tips

```
 Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
```

```
ServerName localhost
```

### .htaccess
* [Apache HTTP Server Tutorial: .htaccess files - Apache HTTP Server Version 2.4](https://httpd.apache.org/docs/current/howto/htaccess.html)
    * 設定の変更をdirectory baseで行うファイル
    * `.htaccess` fileは serverを遅くするので極力使わない方が良い
    * `.htaccess`が置かれたdirectoryの`<Directory>`内の設定を上書きできる
        * 上書きを禁止したい場合は`AllowOverride No`をを`<Directory>`に記載しておく

## Reference
