# MySQL

## インストール
[pages](http://promamo.com/?p=2933)

## ファイル
* `/etc/my.cnf`に設定ファイルがある。

## grant
[title](http://www.dbonline.jp/mysql/user/index6.html)
```mysql
GRANT ALL PREVILEDGES ON database.table TO 'user'@'host' IDENTIFIED BY '[pass]' WITH GRANT OPTION;
```

* [pass]つきのユーザを作成

権限の種類は以下
* [title](http://www.dbonline.jp/mysql/user/index5.html)
