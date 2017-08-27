---
title: Celery
---

## Celery
Celery は Python で非同期処理をするための Task Queue です。


## Flower
* [Flower - Celery monitoring tool — Flower 1.0.0 documentation](http://flower.readthedocs.io/en/latest/)

CeleryのWebUIのようなもの。
主な機能は以下のようになる。

* celeryのeventの可視化
* workerのremote control
* brokerのmonitoring
* HTTP API
* Authentification
    * Basic Auth
    * GitHub OAuth2
    * Google OpenID

Celery flowerとAirflopwの画面は似ている部分が多い。
以下のscreen shotがわかりやすいが、workerの処理しているtaskのstatusや状態、parameterなどがGUIで確認できる。
また、各workerの設定やmonitoringができる。

* [Screenshots — Flower 1.0.0 documentation](http://flower.readthedocs.io/en/latest/screenshots.html)

Install

```
$ pip install flower
```

Usage

```
flower -A proj --port=5555
```

* `-A`
    * applicationの名前

Celeryから直接lanchする場合は以下のようにする。

```
celery flower -A proj --address=127.0.0.1 --port=5555
```

Taskのfilteringができる使える条件は

* `foo`
    * find all tasks containing foo in args, kwargs or result
* `args:foo`
    * `foo`をargumentに含むものを検索
    * taskのargumentの検索
* `kwargs:foo=bar`
    * `foo`keyの値が`bar`であるものを探す
* `result:foo`
    * resultが`foo`
* `state:FAILURE`
    * sateが`FAILURE`なもの

### Configuration
`flowerconfig.py`に設定を記述する。
変更したい場合は起動時に`flower --conf=celeryconfig.py`で指定する。
環境変数で設定をすることもできる。

Celeryの設定をここで上書きすることもできる。
上書きできるoptionについては`celery --help`で一覧が見れる。


## Reference
* [Celery 3.1 を Django で使う - Qiita](http://qiita.com/seizans/items/a40952248ef2004f1d62)
* [Celery - Distributed Task Queue — Celery 4.0.2 documentation](http://celery.readthedocs.io/en/latest/index.html)


