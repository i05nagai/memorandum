---
title: syslog
---

## syslog
send messages to the system logger
logrotationは自分で設定する。

defaultで存在するlog file

* cron
* messages
* maillog
* secure

## CLI
restart

```
systemctl restart rsyslog
```

logger commandでlog messageを生成できる。

```
logger -p <facility>.<priority> -t <tag> message
```

## Configuration
defaultでは以下のいずれか。

* `/etc/syslog.conf`
* `/etc/rsyslog.conf`

```
<facility>.<priority>[;<facility>.<priority>] output
```

例えば

```
cron.* /var/log/cron
```

* facility
    * `cron`
    * kern
    * user
    * mail
    * daemon
    * auth
    * syslog
    * lpr
    * news
    * uucp
    * atuthpriv
    * ftp
* priority (severity)
    * `*`
    * emerg(panic)
        * systemが利用できない
    * alert
        * 即座に対応が必要
    * crit
        * critial
    * err (error)
    * warning (warn)
    * notice
        * 重要な情報
    * info
    * debug
    * `none`
        * facilityを無効にする
* output
    * `/var/log/cron`

`;` 区切りで複数かける。

## Facility
message soruce

* auth,authpriv
    * 認証系(usなど)
* cron
* daemon
* kern
    * from kernel
* lpr
    * from printer
* mail
    * from system mail
* syslog
    * syslogの機能関係
* local0~7
    * 独自設定

## Priority

* emerg
    * 致命的状態
* alert
    * 早急な対処が必要
* crit
    * 危険な状態
* err
    * 一般的エラー
* warning
    * 一般的警告
* notice
    * 重要な通知
* info
    * システムからの情報
* debug
    * デバッグ情報
* none
    * ファシリティの無効化 ログの除外

## Output
* filename
    * ファイルに出力
* @hostname
    * リモートホストのsyslogデーモンへ出力する。
* username
    * ユーザの端末に出力する。
* `/dev/console`
    * コンソールへ出力する。
* `*` 全てにユーザ端末へ出力する。


## Module
接頭辞でmoduleの種類が分かる。

[Modules — rsyslog 8.33-20180209-f13323d documentation](http://www.rsyslog.com/doc/v8-stable/configuration/modules/index.html)

* om
    * output module
* im
    * input module
* pm
    * parser module
* mm
    * message modification module
* sm
    * string generator modules
* lm
    * library module
* other module

moduleの読み込みは以下のようにする。

```
$ModLoad imjournal
```

## Configuration
`/etc/syslogd.conf`



## Reference
* [syslog\(3\): send messages to system logger \- Linux man page](https://linux.die.net/man/3/syslog)
* [【初心者でもすぐわかる】syslogとは？とsyslogの設定方法](https://eng-entrance.com/linux-log-syslog)
* [必読！ログファイルとディレクトリ | Think IT（シンクイット）](https://thinkit.co.jp/article/711/1)
* [syslogを押さえよう！ | Think IT（シンクイット）](https://thinkit.co.jp/article/724/1)
