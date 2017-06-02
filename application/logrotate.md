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

        
## conf

* daily
* missingok
    * 指定したlog fileがなくてもエラーを出力しない
* compress
* delaycompress
    * compressと一緒に指定する
* dateext
    * logのrotate時に日付の接尾辞をつける


## Reference
* [logrotate入門 - Qiita](http://qiita.com/zom/items/c72c7bac63462225971b)
* [logrotate の delaycompress - ngの日記](http://ngyuki.hatenablog.com/entry/20111205/p1)
