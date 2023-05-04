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
    * 1GBあたり0.02 usd /month
* 長期保存
    * 1GBあたり 0.01 usd /month
* ストリーミングインサート
    * 1GBあたり 0.05 usd /month
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
* [Query Plan Explanation | BigQuery Documentation | Google Cloud Platform](https://cloud.google.com/bigquery/query-plan-explanation)

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

画像中の`AVG`と`MAX`は実際には表示されないので、色で判断する。

## Partitioned Table
* [分割テーブル  |  BigQuery のドキュメント  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/partitioned-tables?hl=ja)
* [Introduction to Partitioned Tables  |  BigQuery  |  Google Cloud](https://cloud.google.com/bigquery/docs/partitioned-tables)

Partitioned ttableは2種類ある

* Tables partitioned by ingestion time
    * load時やstreamingの場合はinsert時の時間でpartition
    * `_PARTITIONTIME`のpeseudo columnが使われる
* Partitioned tables
    * tableのoclumnでpartition
    * `_PARTITIONTIME`はなくても良い
    * `NULL` partitionはpartitionのcolumnにした値がnullのものに対するpartition
        *  parititionのcolumnはNULLABLEでも良い
    * `UNPARTITIONED` allowed range of dataから外れたものの
        * `1960-01-01 and later than 2159-12-31`
    * tableのdetailに、どのcolumnがどう指定されているのか記載される
* shardingとの違い
    * `[TABLE_NAME]_yyyymmdd`でtableを分ける方法をdate-shardingとう
    * partition tableの方がperformanceが良い
    * best practiceはparittioned table

Partitionは各テーブル最大2000個

* Delete partition
    * partitionの削除はtable名の後に`$yyyymmdd`でpartitionを指定して削除できる

```
bq rm 'mydataset.table$20160301'
```

partitionの設定の確認は以下を実行してschemaを見る。

```
bq show --format=prettyjson mydataset.table2
```

以下のように設定がある。

```json
  "timePartitioning": {
    "expirationMs": "2592000000",
    "type": "DAY"
  },
```


## Standard SQL
Castは以下の形式でCASTする。

```sql
CAST(expr AS typename)
```


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

## Streaming
* [Life of a BigQuery streaming insert | Google Cloud Big Data and Machine Learning Blog  |  Google Cloud Platform](https://cloud.google.com/blog/big-data/2017/06/life-of-a-bigquery-streaming-insert)

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
特定のpartitionを指定する場合は、table名の後ろに`$YYYYMMDD`をつけて指定する。

```
bq query \
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

## UserDefineFunction
BigQueryではUDFが使える。
以下はstandard SQLの話。

* in legacy SQL
    * [User-Defined Functions in Legacy SQL  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/user-defined-functions)
* in standard SQL
    * [User-Defined Functions  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions)

UDFの定義は以下の形式で行う。

```sql
CREATE [TEMPORARY | TEMP] FUNCTION function_name ([named_parameter[, ...]])
  RETURNS [data_type]
  LANGUAGE [language]
  AS [external_code]
```

* CREATE [TEMPORARY | TEMP ] FUNCTION
    * TEMPORARYかTEMPが必須
    * named_parameterはうけとるparameterと型を記載
* RETURNS
    * 戻り値の型を記載　
* LANGUAGE
    * UDFの言語を指定
    * 対象言語は以下
        * [User-Defined Functions  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions#supported-external-udf-languages)
        * JSのみ
* AS [external_code]
    * LANGUAGEで指定したコードで実際のUDFを記載　

UDFの例は以下

```sql
CREATE TEMPORARY FUNCTION
    multiplyInputs(x FLOAT64, y FLOAT64)
RETURNS FLOAT64
LANGUAGE js AS
"""
  return x*y;
""";
WITH numbers AS (
SELECT
    1 AS x
    , 5 as y
UNION ALL
SELECT
    2 AS x
    , 10 AS y
UNION ALL
SELECT
    3 AS x
    , 15 AS y
)
SELECT
    x
    , y
    , multiplyInputs(x, y) AS product
FROM
    numbers;
```

BigQueryで対応しているUDFの型の一覧

* ARRAY
* BOOL
* BYTES
* DATE
* FLOAT64
* STRING
* STRUCT
* TIMESTAMP

JSとBigQueryの対応

| BigQuery Data Type | JavaScript Data Type                                                               |
|--------------------|------------------------------------------------------------------------------------|
| ARRAY              | ARRAY                                                                              |
| BOOL               | BOOLEAN                                                                            |
| BYTES              | base64-encoded STRING                                                              |
| FLOAT64            | NUMBER                                                                             |
| STRING             | STRING                                                                             |
| STRUCT             | OBJECT where each STRUCT field is a named field                                    |
| TIMESTAMP          | DATE with a microsecond field containing the microsecond fraction of the timestamp |
| DATE               | DATE                                                                               |

JS UDFのbest practice

* UDFに渡す前に、簡単に入力をフィルタできるなら、queryは早く安くなる
* UDFの中で状態を持たない
* memoryの使用は極力減らす
    * UDFが使えるmemoryが限られている

制限

* 一行あたりのUDFの出力は5MB以下
* 1 userあたり6 JavaScript UDF
* JSのUDFは時間がかかりすぎるとtimeoutする
    * 状況によるが一つの目安は5分程度
* query jobは50のJS UDFのresourceをもつ
* inline codeのblobは32KBまで
* external codeは1MBまで
* DOM objects, `Window`, `Document`, `Node`などはサポートしてない

### Authorized view
Rowやcolumn単位で権限を付与したviewを作れる。
もとのviewにaccess権がなくても可能

```sql
#standardSQL
SELECT c.customer, c.id
FROM `private.customers` c
INNER JOIN (
    SELECT group
    FROM `private.access_control`
    WHERE SESSION_USER() = user_name) g
ON c.allowed_group = g.group
```


## Tips

### Add new columns
* [BigQuery で既存のテーブルにカラムを追加する - Qiita](https://qiita.com/m_doi/items/b367d38bac5565f42c76)

bq commandで行う場合は、既存のschemaに新しいcolumnのschemaを追加したものを用意して、bq updateで更新すれば良い。
追加したcolumnはnullで追加される。

```
bq update project_name:dataset_name.table_name table.json
```

### BigQuery for Datawarehouse practitioner
* [BigQuery for Data Warehouse Practitioners  |  Solutions  |  Google Cloud Platform](https://cloud.google.com/solutions/bigquery-data-warehouse)


### Multiple tablea using a wildcard table
* [Querying Multiple Tables Using a Wildcard Table  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/querying-wildcard-tables)
    * `_TABLE_SUFFIX`でできる

```sql
#standardSQL
SELECT
  max,
  ROUND((max-32)*5/9,1) celsius,
  mo,
  da,
  year
FROM
  `bigquery-public-data.noaa_gsod.gsod19*`
WHERE
  max != 9999.9 # code for missing data
  AND _TABLE_SUFFIX BETWEEN '29'
  AND '40'
ORDER BY
  max DESC
```

### pricing of failed query
* https://cloud.google.com/bigquery/docs/best-practices-costs#limit_query_costs_by_restricting_the_number_of_bytes_billed

* maximum bytes billed でfailした場合は料金はかからない
* You aren't charged for queries that return an error, or for queries that retrieve results from the cache.
* [Pricing  |  BigQuery  |  Google Cloud](https://cloud.google.com/bigquery/pricing#on_demand_pricing)

## Tips

### Visualize geographic data
* [Bridging the gap between data and insights \| Google Cloud Blog](https://cloud.google.com/blog/products/gcp/bridging-the-gap-between-data-and-insights)

* Use BigQuery Geo Viz
    * [BigQuery Geo Viz](http://bigquerygeoviz.appspot.com/)
* Use Google Earth Engine
* Use GeoJSON exntension for jupyter extension
    * https://github.com/jupyterlab/jupyter-renderers/tree/master/packages/geojson-extension

Geo Viz limitation

* Geo Viz can only display up to 2,000 results on a map.
* Geo Viz supports geometry inputs (points, lines, and polygons) in well-known text (WKT) format, stored in a STRING column. You can use BigQuery's geography functions to convert latitude and longitude to WKT.
* Real-time, interactive analysis is handled locally by your browser and is subject to your browser's capabilities.
* Geo Viz does not support sharing visualizations with others, saving a visualization, or downloading a visualization for offline editing.

### Geographic data
Bigquery Support the foloowing formats;

* GeoJSON
* Well-Known text


## Permission

* add writer to your destination dataset's permission list
* `BigQuery Data Editor` role.


## Bigtable external schema
https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#bigtableoptions



```json
{
    "sourceFormat": "BIGTABLE",
    "sourceUris": [
        "https://googleapis.com/bigtable/projects/PROJECT_ID/instances/INSTANCE_ID/tables/TABLE_NAME"
    ],
    "bigtableOptions": {
        "columnFamilies" : [
            {
                "familyId": "FAMILY_ID",
                "type": "INTEGER",
                "encoding": "BINARY",
                "columns": [
                    {
                        "qualifierString": "NAME",
                        "type": "INTEGER",
                        "encoding": "BINARY"
                    }
                ]
            }
        ]
    }
}
```




## Reference
* [How to recover a deleted dataset in BigQuery - Stack Overflow](https://stackoverflow.com/questions/31576636/how-to-recover-a-deleted-dataset-in-bigquery)
* [How to load geographic data like shapefiles into BigQuery](https://medium.com/google-cloud/how-to-load-geographic-data-like-zipcode-boundaries-into-bigquery-25e4be4391c8)
