---
title: /var/log
---

## /var/log

`/var/log`以下のdirectory/file

Login情報

* wtmp
    * binary
    * `/usr/bin/last` command
    * login情報の記録
    * system loginの成功の記録
    * username, login terminal, login host, login time,
    * 再起動は、`reboot` というusernameで記録される
* btmp
    * binary
    * `/usr/bin/lastd` command
    * root権限が必要
    * login情報の記録
    * system loginの失敗の記録
    * username, login terminal, login host, login time,
    * 再起動は、`reboot` というusernameで記録される
* lastlog
    * binary
    * `/usr/bin/lastlog`
    * userのlast login time
* faillog
    * binary
    * `/usr/bin/faillog`
    * architectureに依存しているfile形式
    * loginの失敗の記録
    * userごとのloginの失敗回数
    * 最大失敗回数を指定でき、認証にpam_tally moduleを使っている場合は、accountのLockなどがでっきる
* tallyog
    * binary
    * `/usr/bin/taillog`
    * userごとのloginの失敗回数
    * architectureに依存しないfile形式


syslogを利用したlog

* boot.log
    * system起動時のlog
    * serviceの起動時のmessage
* cron
    * cronのlog
    * cronやatdのclock daemon
* maillog
    * mail systemのLog
    * MTAが処理したmailの記録
* secure
    * 認証関連のlog
    * sshdやsudoのLog
* spoofer
    * UUCPのlog
    * Unix to Unix CoPyのlog
* messages
    * 上以外のsyslogのmessage


その他のlog

* acpid
    * acpiidのlog
    * power buttonが押されたときのacpi event eventを処理するacpidのlog
* anaconda.log
    * installerのLog
    * `/root/install.log`, `/root/install.log.syslog`にも記録される
* anaconda.syslog
    * installerのLog
* dmesg
    * system起動時からfilesystemがmountされるまでののdmesgの内容
* rpmpkgs
    * install済みのrpm packages
* yum.log
    * yumのLog

log directory

* audit/
    * auditdのlog
* conman/
    * commandのLog
* conman.old/
    * commandのLotateずみのlog
* cups/
    * cupsのLog
* httpd/
    * apache httpd
* mail/
    * mail system
* news/
    * news system
* pm/
    * pm-utils
* ppp/
    * pppd
* prelink/
    * prelink
* samba/
    * samba
* squid/
    * squid
* vbox/
    * vbox


## Reference
* [必読！ログファイルとディレクトリ | Think IT（シンクイット）](https://thinkit.co.jp/article/711/1)
