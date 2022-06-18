---
title: MySQL
---

# MySQL

## Install
[pages](http://promamo.com/?p=2933)

For alpine linux

```
apk add mysql
```

### For CentOS
For 5.6

* [【シンプル】CentOS6にMySQL5.6をyumで簡単にインストールする手順 | 田舎に住みたいエンジニアの日記](http://blog.ybbo.net/2014/01/22/%E3%80%90%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%80%91centos6%E3%81%ABmysql5-6%E3%82%92yum%E3%81%A7%E7%B0%A1%E5%8D%98%E3%81%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B/)

```
sudo yum install mysql
sudo yum install mysql-devel
sudo yum install mysql-server
sudo yum install mysql-utilities
```

rootへのpassの設定は以下。
デフォルトはpassなし。

```
/usr/libexec/mysql55/mysqladmin -u root password 'new-password'
/usr/libexec/mysql55/mysqladmin -u root -h ip-172-19-252-55 password 'new-password'
```

bash_historyに記録されるので、mysqlに接続後に以下を実行

```
mysql> update mysql.user set password=password('root用の任意パスワード') where user = 'root';
mysql> flush privileges; ← 変更を反映
mysql> exit;
```

* [CentOS 6.x に MySQL 5.7をyumで簡単にインストールする - Qiita](http://qiita.com/UmedaTakefumi/items/924cdce7cfff083bf492)
* [MySQL :: A Quick Guide to Using the MySQL Yum Repository](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/)
    * Officialのyum repositoryの追加方法

### For Amazon Linux

For 5.7

* [サーバー AmazonLinuxにMySQL5.7をインストールする - YoheiM .NET](http://www.yoheim.net/blog.php?q=20160402)

以下でyum repositoryの追加

```
sudo yum -y install http://dev.mysql.com/get/mysql57-community-release-el6-7.noarch.rpm
```

追加されているかの確認。

```
yum repolist enabled | grep "mysql.*-community.*"
```

こんな感じなら良さそう。

```
mysql-connectors-community/x86_64       MySQL Connectors Community         29+7
mysql-tools-community/x86_64            MySQL Tools Community                47
mysql57-community/x86_64                MySQL 5.7 Community Server          183
```

また、packageの確認は以下で、version 5.7なら良い。

```
yum info mysql-community-server
```

```
sudo yum install mysql-community-server
```

でインストールされる。

起動は

```
sudo service mysqld start
```

rootの初期passwordは`/var/log/mysqld.log`に記載されている。
接続は

```
mysql -u root -p -P 3306 -h localhost
```

で、rootの初期パスワードで接続できる。
passwordの変更は

```sql
ALTER USER root@localhost IDENTIFIED BY 'NewPass123?&!';
```

serviceの停止は

```
sudo service mysqld stop
```


## Configuration
* `/etc/my.cnf`に設定ファイルがある。

## grant
[title](http://www.dbonline.jp/mysql/user/index6.html)

```sql
GRANT ALL PREVILEDGES ON database.table TO 'user'@'host' IDENTIFIED BY '[pass]' WITH GRANT OPTION;
```

* [pass]つきのユーザを作成

権限の種類は以下

* [title](http://www.dbonline.jp/mysql/user/index5.html)

## Uninstall

### Amazon Linux
* [DBの中身もろとも消したいときの、Mysql-server の完全削除 - Qiita](http://qiita.com/rojiuratech/items/80dda65d832b407322f1)

```
yum remove mysql
yum remove mysql-utilities
yum remove mysql-server mysql-devel
rm -rf /var/lib/mysql
```

### 5.6と5.7の違い
* [第10回　yum, rpmインストールにおけるMySQL 5.6とMySQL 5.7の違い：MySQL道普請便り｜gihyo.jp … 技術評論社](http://gihyo.jp/dev/serial/01/mysql-road-construction-news/0010)

## Docker
* [library/mysql - Docker Hub](https://hub.docker.com/_/mysql/)

officialのdocker imageがある。
versinを指定して取得可能。

```
docker pull mysql:5.7.18
```

DB serverとしてのimageもあるが、mysql clientとしても使うことができる。

* `some.mysql.host`
    * serverのhost
* `some.mysql.user`
    * serverのuser

```
docker run -it --rm mysql:5.7.18 mysql -hsome.mysql.host -usome-mysql-user -p
```

docker imageの設定に用いる環境変数

* MYSQL_ROOT_PASSWORD='pass'

```
MYSQL_DATABASE
MYSQL_USER
MYSQL_PASSWORD
```

sql fileやshellを実行したい場合は`/docker-entrypoint-initdb.d`にMountする。
serverのconfを変更したい場合は、`/etc/mysql/conf.d`にMountする。
`/etc/mysql/my.cnf`は`/etc/mysql/conf.d`以下の`.cnf`fileをincludeする。

```
docker run -it --rm -v /my/custom:/etc/mysql/conf.d mysql:5.7.18 mysql -hsome.mysql.host -usome-mysql-user -p
```

DBのdataをmountする場合は、`/var/lib/mysql`にMountする。
mountするvolumeが空でないと以下のerrrorがでる。

```
[ERROR] --initialize specified but the data directory exists. Aborting.
```

以下のsiteを見て適宜修正する。

[MySQL 5.7のmysqld --initializeと鶏卵問題 - (ひ)メモ](http://d.hatena.ne.jp/hirose31/20161004/1475582156)


## SQL
* https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html#sqlmode_no_zero_date


## sqlmode
* `NO_ZERO_DATE`
    * `0000-00-00 00:00:00`がだめ
* `NO_ZERO_IN_DATE`
    * 年月日にzeroを含むとだめ
    * `1990-00-01 11:11:11`はだめ

## Error

#### Invalid default value for datetime
```
Cause: com.mysql.jdbc.exceptions.jdbc4.MySQLSyntaxErrorException: Invalid default value for
```

* https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html#sqlmode_no_zero_date
    * sql_modeの`NO_ZERO_DATE`外す

#### Invalid GIS data provided to function st_astext.
* [MySQL: Invalid GIS data provided to function st_geometryfromtext - Stack Overflow](https://stackoverflow.com/questions/34524031/mysql-invalid-gis-data-provided-to-function-st-geometryfromtext)
* [MySQL spatial geometry validate wkt - Stack Overflow](https://stackoverflow.com/questions/39285560/mysql-spatial-geometry-validate-wkt)
    * The query changed to invalid query in MySQL 5.7?

`ST_isValid(col)`でGeometry型がvalidかどうか判定できるので、invalidならNULLにするなどの対応で回避はできる。

```
IF(ST_isValid(col) = 1, ASTEXT(col), NULL)
```

## Reference
* [MySQL/ユーザの作成・変更・削除 - 調べる.DB](http://db.just4fun.biz/?MySQL/%E3%83%A6%E3%83%BC%E3%82%B6%E3%81%AE%E4%BD%9C%E6%88%90%E3%83%BB%E5%A4%89%E6%9B%B4%E3%83%BB%E5%89%8A%E9%99%A4)
