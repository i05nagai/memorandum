---
title: SQLAlchemy
---

## SQLAlchemy


## sqlite

```
sqlite:///:memory: (or, sqlite://)
sqlite:///relative/path/to/file.db
sqlite:////absolute/path/to/file.db
```

## API

* `column_expression.in_(values)`
    * valuesはlist
* `column_expression.isnot(None)`
    * is not null
* `sql_expression.with_only_columns(columns)`
* `sql_expression.execute()`
    * 戻り値は`ResultProxy`
    * [Working with Engines and Connections — SQLAlchemy 1.2 Documentation](http://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.ResultProxy)
* `result_proxy.fetchone()`
    * 戻り値は`RowProxy`
* `result_proxy.fetchall()`
    * 戻り値はlist of `RowProxy`

* [Using the Session — SQLAlchemy 1.2 Documentation](http://docs.sqlalchemy.org/en/latest/orm/session.html)

## Tips

### Alias
`Table`でTableを作成した場合は、`alias()` instance methodが使える。

```
table = Table(...)
ri = table.alias()
```

`declative_base`でmodelを作った場合は、`sqlalchemy.orm.aliased()`を使う。

```
sqlalchemy.orm.aliased(Model, name='')
```

## fetch as list of dict

```python
for row in query.execute().fetchall():
    print(dict(row.items()))
```

### sub query
* [SQLAlchemyでサブクエリ - chykaのブログ](http://chyka.hatenablog.jp/entry/2016/01/18/011834)

```
subquery = session.query(
        column1,
        column2,
    ).group_by(
        column1,
    ).subquery('sub_query_name')
```

### inner join
* [SQLAlchemyでINNER JOINする方法 - Qiita](https://qiita.com/uokada/items/d81fd930402e3be4aa62)


### Automap
* [Automap — SQLAlchemy 1.2 Documentation](http://docs.sqlalchemy.org/en/latest/orm/extensions/automap.html)

### create session

```
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
```

## Types
* [Column and Data Types — SQLAlchemy 1.2 Documentation](http://docs.sqlalchemy.org/en/latest/core/type_basics.html)

* sqlalchemy.types.BigInteger
    * int
* sqlalchemy.types.Integer
* sqlalchemy.types.String
* sqlalchemy.types.Boolean
* sqlalchemy.types.Date
    * datetime.date
* sqlalchemy.types.DateTime
    * datetime.datetime
* sqlalchemy.types.Float

## Example
Sub query example

```python
import sqlalchemy
import sqlalchemy.orm as orm


db_url = ''
engine = sqlalchemy.create_engine(db_url, echo=True)
metadata = sqlalchemy.MetaData()
metadata.bind = engine
Session = orm.sessionmaker(bind=engine)

table_name1 = sqlalchemy.Table(
    'table_name1',
    metadata,
    Column('id', types.Integer, primary_key=True),
    Column('col11', types.Integer, primary_key=True),
)
table_name2 = sqlalchemy.Table(
    'table_name2',
    metadata,
    Column('id', types.Integer, primary_key=True),
    Column('col21', types.Integer, primary_key=True),
)
# alias
tn1 = table_name1.alias()
tn2 = table_name2.alias()

# sub query
session = Session()
sub_columns = [
    tn1.c.id,
    functions.count(1).label('count'),
]
sub_query = (session
          .query(*sub_columns)
          .group_by(
              tn1.c.id)
          .subquery('sub_query'))
# main query
columns = [
    tn1.c.id.cast(types.Integer),
    tn2.c.id.cast(types.Integer),
    sub_query.c.count.cast(types.Integer),
]
q = (tn1
     .join(
         tn2,
         tn1.c.id == tn2.c.id)
     .join(
         sub_query,
         tn1.c.id == sub_query.c.id)
     .select()
     .with_only_columns(columns)
     .where(
         tn1.c.rid.isnot(None))
     .where(
         tn1
         .c.id.in_([1, 2, 3, 4])))
```

## Reference
* [zzzeek/sqlalchemy: See the development link for contribution guidelines](https://github.com/zzzeek/sqlalchemy)
* [SQLAlchemy - The Database Toolkit for Python](http://www.sqlalchemy.org/)
* [SQLAlchemy Documentation — SQLAlchemy 1.2 Documentation](http://docs.sqlalchemy.org/en/latest/)
* [Python SQLAlchemy Cheatsheet — pysheeet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
* [オブジェクトリレーショナルマッパ　チュートリアル — SQLAlchemy 0.6.5 ドキュメント (和訳)](http://omake.accense.com/static/doc-ja/sqlalchemy/ormtutorial.html)

