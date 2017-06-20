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

## Partitioned Table
* [分割テーブル  |  BigQuery のドキュメント  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/partitioned-tables?hl=ja)

Partitionは各テーブル最大2000個


### Best Practice

タイムゾーンへの問題


`_PARTITIONTIME`への演算はさける。
以下のSQLより2番目の方が高速な場合がある。

```sql
#standardSQL
/* Can be slower */
SELECT
  field1
FROM
  mydataset.table1
WHERE
  TIMESTAMP_ADD(_PARTITIONTIME, INTERVAL 5 DAY) > TIMESTAMP("2016-04-15")
```

```sql
#standardSQL
/* Often performs better */
SELECT
  field1
FROM
  mydataset.table1
WHERE
  _PARTITIONTIME > TIMESTAMP_SUB(TIMESTAMP('2016-04-15'), INTERVAL 5 DAY)
```



## Creating and Updating Date-Partitioned Tables
* [Creating and Updating Date-Partitioned Tables  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/creating-partitioned-tables#example)

Partitioned Tableの一種で、日付でpartitionを分けたものをDate-Parittioned tableという。
以下で作成する。

```
bq mk --time_partitioning_type=DAY --time_partitioning_expiration=259200 mydataset.table1
```

* `--time_partitioning_type=DAY`
    * 日付でpartitionを分割
* `--time_partitioning_expiration`
    * paritionのデータが消えるまでの時間、秒で指定

以下で既存のtableの設定を確認できる。

```
bq show --format=prettyjson mydataset.table2
```

出力は以下のようになる。

```json
{
  ...
  "tableReference": {
    "datasetId": "mydataset",
    "projectId": "myproject",
    "tableId": "table2"
  },
  "timePartitioning": {
    "expirationMs": "2592000000",
    "type": "DAY"
  },
  "type": "TABLE"
}
```

基本的にtbaleへのデータの挿入日が、partitionの日付となる。
明示的に、paritionnの日付を指定する場合は、以下のようにpartitionの日付を明示する。

```
bq query
    --use_legacy_sql=false \
    --allow_large_results \
    --replace \
    --noflatten_results \
    --destination_table 'mydataset.temps$20160101' \
    'SELECT stn,temp from `bigquery-public-data.noaa_gsod.gsod2016` WHERE mo="01" AND da="01" limit 100'
```

## Querying Date Partitioned Tables
* [Querying Date-Partitioned Tables  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)


Partitioned tableに対しては、queryが走査するpartitionを指定することができる。

```sql
SELECT
    *
FROM
    
WHERE
  _PARTITIONTIME BETWEEN TIMESTAMP('2016-01-01') AND TIMESTAMP('2016-01-02');
```

## Reference

