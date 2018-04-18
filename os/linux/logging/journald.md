---
title: journald
---

## journald
systemdで標準的なlog管理service.
`/var/run/log/journal` に保存される。
OSを再起動するときえるので、永続化する場合は`/var/log/journal`のdirectoryを作る。
このdirectoryがあれば、こちらに保存される。

* 保存用ディレクトリーの全容量に対して10%以上
* 該当ディレクトリーのファイルシステムの空き容量が15%以下

保存するfile

* systemdのserviceとして起動したdaemonの標準出力／標準エラー出力の内容
* localのprocessがsyslogに出力したmessage
* journald独自のAPI（library関数）に対して出力したメッセージ



`/dev/log`からLogをとって、rsyslogdに渡す。

## CLI
* [journalctl 最低限覚えておくコマンド - Qiita](https://qiita.com/aosho235/items/9fbff75e9cccf351345c)

* `-l, `
* `-o, --output=`
    * short, short-precise, short-iso, short-full, short-monotonic, short-unix, verbose, export, json, json-pretty, json-sse, cat
* `-e --pager-end`
    * pagerの最後にjump
* `-a --all`


lessでlogを表示

```
journalctl
```

lessなし

```
journalctl -l --no-pager
```

特定serviceのLog

```
journalctl -u hoge.service
```

tail -f

```
journalctl -f
```

最近のmessage

```
journalctl -e
journalctl -xe
```

特定のserviceのmessage

```
journalctl -u sshd
journalctl -u httpd
journalctl -u nginx
journalctl -u mysqld
journalctl -u cronie
journalctl -u updatedb
journalctl -u 'up*'
```

## Configuration
`/etc/systemd/journald.conf`

* SystemMaxUse
* RuntimeMaxUse

## Reference
* [RHEL7/CentOS7のjournaldについてのもろもろ - めもめも](http://enakai00.hatenablog.com/entry/20141130/1417310904)
