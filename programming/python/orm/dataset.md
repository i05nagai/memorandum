---
title: dataset
---

## dataset
OR mapper

```
pip install dataset
```

## Usage

```
import dataset

db = dataset.connect('sqlite:///:memory:')

table = db['sometable']
table.insert(dict(name='John Doe', age=37))
table.insert(dict(name='Jane Doe', age=34, gender='female'))

john = table.find_one(name='John Doe')
```

## Reference
* [pudo/dataset: Easy-to-use data handling for SQL data stores with support for implicit table creation, bulk loading, and transactions.](https://github.com/pudo/dataset)
* [怠惰な人のための超お手軽 ORマッパー dataset - Qiita](https://qiita.com/shoma/items/59c9c907e8f217ab7b14)
