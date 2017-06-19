---
title: BigQuery
---

## BigQuery


## 制限
* [割り当てポリシー  |  BigQuery のドキュメント  |  Google Cloud Platform](https://cloud.google.com/bigquery/quota-policy?hl=ja)


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

## Query Plan Explanation
* [Query Plan Explanation  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/query-plan-explanation)

* query実行時に7日間保持される

WEEB UIとAPI JSONで名前が違う。

* Stage x
    * 
* Input
    * stageで読まれた行数
* Output
    * stageで書かれた行数
* <img src="https://cloud.google.com/bigquery/images/explain-waitRatioAvg.png">
    * 各workerがscheduleされるまでに待った、時間の平均
* <img src="https://cloud.google.com/bigquery/images/explain-waitRatioMax.png">
    * 各workerがscheduleされるまでに待った、時間の最大
* <img src="https://cloud.google.com/bigquery/images/explain-readRatioAvg.png">
    * 各workerがreadするのにかかった時間の平均
* <img src="https://cloud.google.com/bigquery/images/explain-readRatioMax.png">
    * 各workerがreadするのにかかった時間の最大
* <img src="https://cloud.google.com/bigquery/images/explain-computeRatioAvg.png">
    * 各workerが計算にかかった時間の平均
* <img src="https://cloud.google.com/bigquery/images/explain-computeRatioMax.png">
    * 各workerが計算にかかった時間の最大
* <img src="https://cloud.google.com/bigquery/images/explain-writeRatioAvg.png">
    * 各workerがwriteにかかった時間の平均
* <img src="https://cloud.google.com/bigquery/images/explain-writeRatioMax.png">
    * 各workerがwriteにかかった時間の最大

画像中の`AVG`と`MAX`は実際には表示されない。


## Reference

