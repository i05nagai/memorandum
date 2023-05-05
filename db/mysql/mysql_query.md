---
title: MySQL Query
---

## MySQL Query

## default databases

## information_schema

- `SCHEMATA`
    - schema of databases



#### Change password

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'rootpassword';
```

#### Create database 

```
CREATE DATABASE db_name DEFAULT CHARACTER SET utf8;
```

#### Drop database

```
DROP DATABASE db_name;
```

#### Create user
作成直後は、権限が何もないので、GRANTで権限を付与する

```
CREATE USER user_name@'%' IDENTIFIED BY 'password';
```

* @の後ろは、可能な接続元hostを指定する
* localからしかアクセスしなければ、`@localhost`にする
* `@%`はすべての接続元OK

#### Delete user

```
DROP USER user_name@host;
```

#### Change password

```
SET PASSWORD FOR user_name@localhost = PASSWORD('password');
```

#### List user

```
SELECT Host, User FROM mysql.user;
```

#### Grant previledges on user

```
GRANT ALL PRIVILEGES ON db_name.* TO username@host IDENTIFIED BY 'password';
```

* db_nameのtable全てに対して,ALLの権限を付与
* passwordを`password`にする
    * `IDENTIFIED BY` 以下は省略可

* [権限の種類と設定されている権限の確認(SHOW GRANTS文) - ユーザーの作成 - MySQLの使い方](https://www.dbonline.jp/mysql/user/index5.html)

* [MySQL :: MySQL 5.6 リファレンスマニュアル :: 6.2.4 アクセス制御、ステージ 1: 接続の検証](https://dev.mysql.com/doc/refman/5.6/ja/connection-access.html)
    * hostの書き方
    * subnetmask`user@'192.168.1.%'`で良い
    * もしくは`user@'192.168.1.0/255.255.255.0'`

#### Revoke previledges on user
特定のユーザから権限全部削除

```sql
REVOKE ALL PRIVILEGES ON db_name.* FROM user_name@host;
```

#### Show grant

```sql
SHOW GRANTS FOR user_name@host;
```

出力のみかた

* [権限の設定(GRANT文) - ユーザーの作成 - MySQLの使い方](https://www.dbonline.jp/mysql/user/index6.html)


#### List Database/Table
Databaseの一覧

```
SHOW databases;
```

Tableの一覧

```
SHOW tables;
SHOW tables FROM database_name;
```

#### Change Database

```
USE database_name;
```

#### Show table structure

```
DESC table_name
```

## Limit offset

```
# OFFSET = 1, LIMIT = 2
SELECT * FROM `members` LIMIT 1, 2;
```



#### Show binary logs.

```
show binary logs;
```

## Subquery
Get the second value

```
WITH view1 AS (
    SELECT *
    FROM (
        SELECT
            o.id
            , ROW_NUMBER() OVER (PARTITION BY o.id ORDER BY o.date) AS rn
            , o.item_id
        FROM orders AS o
        )
    WHERE rn = 2
    )
SELECT
    *
FROM users AS u
LEFT JOIN view1 AS o ON o.id = u.id
LEFT JOIN items AS i ON i.item_id = o.item_id
```


## Window functions
- Window functions are available since 8.0.
- in 5.7, `ROW_NUMBER() OVER (PARTITION BY ...)` is available


## Tips
- when you left/right outer join, you need to specify the key of


## Reference
