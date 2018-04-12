---
title: Flask-Blueprint
---

## Flask-Blueprint
* 特定のURL以下`/api`の実装を別のfileに分けることができる。

`api.py`で以下のように登録する。
file内でappが使える。


```python
from flask import Blueprint

app = Blueprint("api", __name__, url_prefix="/api")
```

* [API — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/api/#flask.Blueprint)
    * 指定可能なoption
    * `flask.Blueprint(name, import_name, static_folder=None, static_url_path=None, template_folder=None, url_prefix=None, subdomain=None, url_defaults=None, root_path=None)`
    * `url_prefix=None`

## Reference
* [Modular Applications with Blueprints — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/blueprints/)
* [Flaskで大きいアプリケーションを作るときのTips - Qiita](https://qiita.com/Alice1017/items/a6b6500e60f2a0334e44)
