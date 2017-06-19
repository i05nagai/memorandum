## mysqlclient

```
pip install mysqlclient
```

import名は異なるので注意。

```python
import MySQLdb
```

Installには、`mysql_config.h`が必要。
OSXの場合は、以下でOK。

```
brew install mysql
```

## API

接続とcursorの作成。
cursorとconnは必ずcloseする。

```python
conn = MySQLdb.connect(
    user="user_name",
    passwd="passowrd",
    host="hostname",
    db="db_name"
)
cursor = conn.cursor()
cursor.close()
conn.close()
```

データベースへの変更を保存する

```python
conn.commit()
```

テーブル作成

```python
sql = "create table test (id int, content varchar(32))"
cursor.execute(sql)
```

テーブル一覧の取得

```ptyhon
sql = "show tables"
cursor.execute(sql)
```

レコードの登録

```python
sql = "insert into test values (%s, %s)"
c.execute(sql, (1, 'hoge'))
datas = [
    (2, 'foo'),
    (3, 'bar')
]
c.executemany(sql, datas)
```

レコード一覧の取得

```python
sql = "SELECT * FROM test"
c.execute(sql)
for row in c.fetchall():
    print("Id: {0}, Content: {1}".format(row[0], row[1]))
```

レコードの削除

```python
sql = "DELETE FROM test WHERE id=%s"
c.execute(sql, (2,))
```

## Reference
* [PythonからMySQLを使う - mas9612の雑記](http://mas9612.hatenablog.com/entry/2016/07/13/215316)
