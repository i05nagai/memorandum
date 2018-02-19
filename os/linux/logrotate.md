---
title: logrotate
---

## logrotate

## Install

```
sudo yum install logrotate
```


## Usage

```
logrotate -d /path/to/conf
```

* `-d`
    * dryrun

logの状態を確認する。

```
cat /var/lib/logrotate.status
```

## Configuration

* daily
* missingok
    * 指定したlog fileがなくてもエラーを出力しない
* compress
* delaycompress
    * compressと一緒に指定する
* dateext
    * logのrotate時に日付の接尾辞をつける
* `include /etc/logrotate.d`
    * include

```
# ローテーション周期を1週間ごとに
weekly

# 4世代ログをのこす
rotate 4

# ローテーション後に空のファイルを作成する
create

# ログファイルのサフィックス指定、この場合は日付がスタンプされる。
dateext

include /etc/logrotate.d

# /var/log/wtmpファイル設定
/var/log/wtmp {
    monthly
    create 0664 root utmp
    rotate 1
}
```


## Reference
* [logrotate入門 - Qiita](http://qiita.com/zom/items/c72c7bac63462225971b)
* [logrotate の delaycompress - ngの日記](http://ngyuki.hatenablog.com/entry/20111205/p1)
* [【初心者でもすぐわかる】syslogとは？とsyslogの設定方法](https://eng-entrance.com/linux-log-syslog)

