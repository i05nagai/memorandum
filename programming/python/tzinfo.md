---
title: tzinfo
---

## tzinfo
pythonのtzinfoはUTCのみ存在する。
third party libraryの`pytz`で他のtimezoneのtzinfoを利用できる。
基本的に、pythonでdatetime objectでtzinfoを指定しない`naive`なdatetimeは、UTCと思って良い。
`naive`なdatetimeから`aware`なdatetimeでUTCに変換する場合は、timezoneとして`+00:00`がつくだけ。

```

```

unixtimeからdatetimeへの変換については、defaultでは`naive`なので、UTCでのdatetimeが作られると思って良い。

* 入力
    * unixtimeで2017/1/1/00:00:00のデータ
* 出力
    * UTCで2017/1/1/00:00:00

* 入力
    * 日本時刻で2017/1/1/00:00:00のデータ
* 出力
    * UTCで2017/1/1/00:00:00
        * 正しい結果にするには、2017/12/31/15:00:00に減算が必要

## Reference
* [8.1. datetime — Basic date and time types — Python 3.6.2 documentation](https://docs.python.org/3/library/datetime.html#tzinfo-objects)
