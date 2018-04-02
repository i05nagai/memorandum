---
title: cron
---

## cron

起動しているか確認

```
service crond status
# runinngと出ればOK
```

登録されているcronを確認表示

```
crontab -l
```

currentuserのcronの設定の編集。
editorが立ち上がる。

```
crontab -e
```

特定のuserのcronの設定

```
crontab -u user_name -l
```

## usage

```
分 時 日 月 曜日 コマンド
```

## Configuration
`/etc/crontab`に`root`の設定をおく。

```
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
```

各userごとの設定は、 `/var/spool/cron/username`におかれる。


## Reference

