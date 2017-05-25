---
title: BigQuery
---

## BigQuery


## REST API


## UDF
* [レガシー SQL のユーザー定義関数  |  BigQuery のドキュメント  |  Google Cloud Platform](https://cloud.google.com/bigquery/user-defined-functions?hl=ja)
* [ユーザー定義の関数  |  BigQuery のドキュメント  |  Google Cloud Platform](https://cloud.google.com/bigquery/sql-reference/user-defined-functions?hl=ja)


## column type
* [Data Types  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/data-types#civil-time)

* TIMEZONE
    * timezoneは文字列に含めることができるが、内部的には保存されない
    * timezoneが必要な場合は別途columnを作って保存する

## Public Dataset
* クエリにのみ料金がかかる
* 毎月1TBまでは無料

## Fee

* [料金  |  BigQuery のドキュメント  |  Google Cloud Platform](https://cloud.google.com/bigquery/pricing?hl=ja)

* ストレージ
    * 1GBあたり$ 0.02/month
* 長期保存
    * 1GBあたり$ 0.01/month
* ストリーミングインサート
    * 1GBあたり$ 0.05/month
* クエリ
    * 1TBあたり$ 5

### For free
以下は無料。

* データの読み込み
* データのコピー
* データのエクスポート
* メタデータの操作
    * list, get, patch, update, deleteの呼び出し


## Reference

