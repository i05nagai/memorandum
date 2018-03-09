---
title: Nginx
---

## Nginx


```
sudo nginx <options>
```

* `-t`
    * 設定ファイルの構文check
    * 起動せずにcheckのみを行う
* `-c nginx.conf`
    * path to nginx.conf
* `-g settings`
    * 設定を上書き
    * 上書き可能なのはmain contextのdirectiveだけ

```
sudo nginx -g "pid /var/run/test_nginx.pid"
```

* `-p prefix`
    * prefix pathを指定

master processの制御は、`-s`か killコマンドで行う。

* `-s signal`
    * master processにsignalを送る
    * reload
        * 設定ファイルの再読込
    * reopen
        * log fileを開く
    * quit
        * 現在のrequest処理が終了してから終了
    * stop
        * requestの処理を待たずに終了

```
nginx -s [stop|quit|reload|reopen]
```

killの場合はo

```
kill -s QUIT `cat /var/run/nginx.pid`
```

* stop = TERM, INT
* quit = QUIT
* reload = HUP
* reopen = USR1

packageでinstallした場合は、serviceとして起動できる。

```
sudo service nginx start
sudo service nginx stop
sudo service nginx restart
sudo service nginx reload
sudo service nginx configtest
sudo service nginx upgrade
```

* upgrade
    * 無停止で実行バイナリを差し替える
    * 同時起動しゆるかやに移行するので、requestの取りこぼしがない

systemdを使っている場合は

```
sudo systemctl enable nginx.service
sudo systemctl start nginx.service
sudo systemctl stop nginx.service
```

## Configuration
`nginx.conf`がdefaultの名前。
場所は起動時か、ビルド時に指定する。

設定ファイルのpathを確認

```
nginx -V
```

### directives
* `include filename|filemask`
    * filemaskの場合は読み込み順を指定できない
    * includeはcontextを考慮して読み込まれる

```conf
# relative path from path to nginx.conf
include mine.types;
# absolute path
include /etc/nginx/mime.types;
# filemask
include sites-enabled/*.conf
```

* `http {}`
* `server {}`

* `listen address[:port] [default_server] [ssl] [http2 | spdy];`
    * server contextで使う
    * defaultは`*:80`で80が使えない場合は、`*:8000`
* `server_name host_name ...;`
    * server context
    * virtual serverで指定するホスト名を指定する
* `error_page`
    * error pageのhtmlを指定する

```
error_page 404 /404.html
error_page 500 502 503 504 /50x.html
error_page 404 = 200 /empty.gif
error_page 404 = /error.php
```

* `allow address|CIDR|unix:|all;`
    * `CIDR`
        * `192.0.2.0/24`
    * `unix:`
        * 全てのunix socket
    * 上から順に評価され、denyとallowの先にmatchしたruleが優先される
* `deny address|CIDR|unix:|all;`
    * 上から順に評価され、denyとallowの先にmatchしたruleが優先される

white list form

```
location /restricted {
    allow 192.0.2.1;
    allow 192.0.2.2;
    deny all;
}
```

black list form

```
location /restricted {
    deny 192.0.2.1;
    deny 192.0.2.100;
    allow all;
}
```

white listとbacl listの組み合わせ。
192.0.2.1以外の192.0.2.0/24を許可。
それ以外を拒否。

```
location /restricted {
    deny 192.0.2.1;
    allow 192.0.2.0/24;
    deny all;
}
```

* `auth_basic`
* `auth_basic_user_file filepath`
    * basic認証のユーザ名とpasswordを記述したfileを指定
    * passwordファイルはApache HTTPの`.htpasswd`と互換性がある
    * formatは以下
    * `password`の暗号化は`openssl passwd passsowrd`で暗号化できる
    * apacheに付属しているhtpasswdのコマンドでもできる
        * `htpasswd -c filepath username`
        * filepathにusernameのデータを作成する

```
# comment
# passwordは暗号化したpassword
username:password
username:password:comment
```

* `limit_conn_zone keyname zone=zonename:size;`
    * http context
    * 同時connection数をcountするためのzoneの作成
    * `$binary_remote_addr`を使うとbinary表現でremote addressのtableをつくる
        * `$remote_addr`は15byte
* `limit_conn zonename num_max_connextion;`
    * http, server, location context
    * 同時connection数を制限する
    * 以下の例では`addr_limit`を100connectionに制限
    * connectionを超えた場合は503を返す

```
http {
    limit_conn_zone $binary_remote_addr zone=addr_limit:10m;
    server {
        location / {
            limit_conn addr_limit 100;
        }
    }
}
```

時間あたりのrequest数の制限

* `limit_req_zone keyname zone=zonename:size rate=RATEr/s;`
    * http context
    * request数のrateを記録するためのzoneを作成する
* `limit_req zone=zonename [burst=BURSTVALUE] [nodelay];`
    * http, server, location context
    * 時間あたりのrequest数を制限する
    * 以下ではremote addressごとに10r/sまで許可、それを超えた場合はburstで50r/sまでqueueに追加される。それを超えた場合は503が戻る

```
http {
    limit_req_zone $binary_remote_addr zone=addr_limit:10m rate=10r/s;
    server {
        location /download/ {
            limit_req zone=addr_limit burst=50;
        }
    }
}
```

* `return status_code [string];`
    * server, location, if context
    * 特定のstatus code pageを返す
    * 以下はredirectの例

```
location /closed/ {
    return 301 http://new-sizete.example.com/
}
```

* `rewrite regexp replacee [flag];`
    * server, location, if context
    * request URIを書き換える
    * 正規表現はPCREが利用できる
    * flag
        * `last`
            * URIを書き換えたあとこのcontextの`ngx_http_rewrite_module`処理を終了し、再度マッチングを行う
        * `break`
            * URIを下記ケアたあとこのcontextの`ngx_http_rewrite_module`処理を終了する
        * `redirect`
            * 302 によるredirectを行う
        * `permanent`
            * 301 によるredirectを行う

```
#
rewrite ^/images/([^/]+)/(.+\.jpg)$ /contents/$1/jpg/$2;
#
rewrite ^/images/(?<dir>[^/]+)/(?<name>.+\.jpg)$ /contents/$dir/jpg/$name;
```

* `if (condition) { }`
    * server, location context
    * conditionを満たした場合block内の処理を実行
    * 以下はiPhone用の設定
    * ANDとかORは使えないので、一度変数に`set`する
    * 利用できる演算子
        * `$a = "b"`
        * `$a - b`
            * 正規表現match
        * `$a -* b`
            * 正規表現match
        * `-f path`
            * 指定したpathにファイルが存在するか
        * `-d path`
            * directoryかどうか
        * `-e path`
            * pathがfileかsymbolic linkかどうか
        * `-x path`
            * pathが実行形式かどうか

```
location / {
    if ($http_user_agent - "iPhone") {
        return 301 http://mobile.example.com;
    }
}
```

* `set $variablename value;`
    * server, location, if
    * nginxのvariableに代入
    * ANDの例

```
location / {
    set $redirect_to_mobile = 0
    if ($http_user_agent - "iPhone") {
        set $redirect_to_mobile 1;
    }
    if ($http_user_agent - "iPod") {
        set $redirect_to_mobile 1;
    }
    if ($http_user_agent - "iPad") {
        set $redirect_to_mobile 1;
    }
    if ($redirect_to_mobile) {
        set $redirect_to_mobile 1;
    }
}
```

* `valid_referers none|blocked|server_names|referer_pattern`
    * server, location context
    * referesに注意
    * 有効なreferのpattern
    * matchの結果は`$invalid_referer`にsetされる

```
location /images {
    valid_referers *.www.example.com ~www[0-9]*.exampe.com;

    if ($invalid_referer) {
        return 403;
    }
}
```

* `gzip on|off;`
    * http, server, location, locaiton context
    * gzip圧縮を有効/無効にする
    * 以下が基本的な設定

```
location / {
    gzip on;
    gzip_types text/css text/javascript
        application/x-javascript application/javascript
        application/json;
    gzip_min_length 1k;
    gzip_disable "msie6";
}
```

* `gzip_types mime_type`
    * http, server, location context
    * gzip 圧縮対象のmime type
* `gzip_min_length minimum_body_size;`
    * http, server, location context
    * gzip圧縮対象となるfileの最小sizeを指定
* `gzip_disable regexp;`
    * http, server, location context
    * gzip 圧縮を無効にするuser agentのpatternを指定する
    * `"msie6"`は特別な意味をもち、`MSIE [4-6]\.(?!.*SV1)`と同等だが高速になる
* `gzip_static on|off|always;`
    * http, server, location context
    * build時に`--with-http_gzip_static_module`が必要
    * gzip圧縮済みのファイルの転送を有効
* `gunzip on|off;`
    * http, server, location context
    * clientがgzip圧縮に対応していない場合、serverで解凍して返す
* `ssl_certificate path_to_cert`
    * http, server context
    * server certificate
* `ssl_certificate_key path_to_private_key`
    * http, server context
    * server certificate key
* `ssl_password_file path_to_passphrasefile`
    * http, server context
    * server certificateのpass phraseを保存んしたfile
* `ssl_ciphers 暗号化suitelist`
    * http, server context
    * HTTPS 通信で利用する暗号化スイートのリストを指定する
* `ssl_prefer_server_ciphers on|off;`
    * http, server context
    * 有効にするとserver側で設定した暗号化suiteの利用が優先される
* `ssl_dhparam dhparam_file_path`


TLS sessionとOCSP staplingの確認は以下のコマンドでｄきる。

```
openssl s_client -connect www.example.com:443 -tls1 -status < /dev/null
```

Session cacheの確認は以下から可能

* [GitHub - vincentbernat/rfc5077: Various tools for testing RFC 5077](https://github.com/vincentbernat/rfc5077)

```
./rfc5077-client -4 www.example.com
```


### HTTPS fundamental configuration
* [Security/Server Side TLS - MozillaWiki](https://wiki.mozilla.org/Security/Server_Side_TLS)
* [Configuring HTTPS servers](http://nginx.org/en/docs/http/configuring_https_servers.html)

基本的な設定

```
server {
    listen 443 ssl;
    server_name secure.example.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/cert.key;
    ssl_password_file /etc/nginx/ssl/cert.password;
}
```

* OpenSSLのversion check
* SSLv3の無効化
* 暗号化suiteを明示的に指定
* DH parameter fileを指定
* SHA-2(SHA-256) server証明書を利用


## Docker
* [library/nginx - Docker Hub](https://hub.docker.com/_/nginx/)



## Reference
