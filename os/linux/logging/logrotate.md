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

動作test

```
logrotate -f /path/to/conf
```

logの状態を確認する。

```
cat /var/lib/logrotate.status
```

## Configuration
* [logrotateスクリプトの調査 | ITログ](https://www2.filewo.net/wordpress/2013/03/31/logrotate%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E3%81%AE%E8%AA%BF%E6%9F%BB/)
* [logrotate.conf - rotates, compresses, and mails system logs - Linux Man Pages (5)](https://www.systutorials.com/docs/linux/man/5-logrotate.conf/)

* daily
* weekly
    * sunday
* monthly
    * 1st day of month
* `size 3M`
    * sizeを超えればrotate
    * 日付の設定は無視される
* `maxsize 3M`
    * 3M こえると日付に関係なくrotate
    * 日付の設定と併用可能
* `minsize 3M`
    * 3Mを超えてかつ、日付の設定時
    * 日付の設定と併用可能
* missingok
    * 指定したlog fileがなくてもエラーを出力しない
* compress
    * rotateした後compressする
    * gzip by default
* compresscmd
    * compress用のcmd
* nocompress
* copytruncate
* `create mode owner group, create owner group`
    * rotateした後すぐに空のfileを作成する
* `copy`
    * copyを作ってoriginalのfileはそのままにする
    * current log fileのsnapshotを作る
* `copytruncate`
    * copyを作った後originalのfileを削除する
    * processがfileを開きっぱなしで、moveではだめなとき
    * truncateするtimingでlogが欠損する可能性がある
* delaycompress
    * compressと一緒に指定する
* dateext
    * logのrotate時に日付の接尾辞をつける
* `dateformat _%Y%m%d`
    * `dateext`の日付の形式
    * only `%Y`, `%m`, `%d`, `%s` are allowed
* `include /etc/logrotate.d`
    * include
* `rotate num`
    * num世代logを残す

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

* postrotate/endscript
    * logfileのrotattionの後実行される
    * `/bin/sh`で間に記載されたscriptを実行する
    * scriptのfirst argumentとして、logfileのabspathが渡される
* prerotate/endscript
* firstaction/endscript
    * wild cardでmatchするlog fileのpatternの最初に一度実行される
    * wild cardを使って以内ならprerotateと同じ
* lastaction/endscript

```
postrotate
    # write script here
endscript
```

## Tips
* [» 書き込み中に削除されたファイルを救出する TECHSCORE BLOG](http://www.techscore.com/blog/2015/12/18/%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF%E4%B8%AD%E3%81%AB%E5%89%8A%E9%99%A4%E3%81%95%E3%82%8C%E3%81%9F%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E6%95%91%E5%87%BA%E3%81%99%E3%82%8B/)

### logrorate open files
* [linux - Logrotate and Open Files - Server Fault](https://serverfault.com/questions/55610/logrotate-and-open-files)

開いているFileをlogrotateする場合は

* copytruncateを使う
* postrotate sattementをつかく

```
/var/log/messages {
    rotate 5
    weekly
    postrotate
        /usr/bin/killall -HUP syslogd
    endscript
}
```

## Reference
* [logrotate入門 - Qiita](http://qiita.com/zom/items/c72c7bac63462225971b)
* [logrotate の delaycompress - ngの日記](http://ngyuki.hatenablog.com/entry/20111205/p1)
* [【初心者でもすぐわかる】syslogとは？とsyslogの設定方法](https://eng-entrance.com/linux-log-syslog)
