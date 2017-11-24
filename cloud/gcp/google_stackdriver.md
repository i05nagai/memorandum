---
title: Google Stackdriver
---

## Google Stackdriver


## Analyze billing


## Pricing
2017 年 12 月 1 日から50GBの無料制限を超えて受信したlogに対する課金が始まる。
Defaultで有効になっている監査logは常に無料で、超過計算の対象にならない。

* Basic tier
* Premium tier

* Free logs
    * Cloud Audit Logging
    * Excluded logs
        * manually excluded logs



### Calculating your logs allotment


## Audit logging
* [Google Cloud Audit Logging  |  Stackdriver Logging  |  Google Cloud Platform](https://cloud.google.com/logging/docs/audit/#data_access_logs)

**Activity logs**

logの保存期間は400日。

* App Engine
* Application Identity
    * OAuth 2.0 のクライアントの ID とブランドを監査します。
* BigQuery
* Cloud IAM
    * サービス アカウントの API を監査します。
* Cloud Resource Manager
    * プロジェクトの API を監査します。
* Cloud Dataflow
* Cloud Dataproc
* Cloud Deployment Manager
* Cloud DNS
* Cloud SQL
* Cloud Storage
    * リクエスト / レスポンスの情報はまだ含まれていません。
* Compute Engine シリアルポート アクセス
* Container Engine
* Stackdriver Debugger
* Stackdriver Logging

**Data access log**

logの保存期間は無料で7日、premiumで30日。
project ownerとprivate log 閲覧者がみることができる。
defaultで有効になっているlogは
利用可能なservice

* BigQuery
    * defaultでloggingは有効


**Audit logのexport**

1. Create export
2. 

## Export logs

* 必要な権限
    * Stackdriverのexportの設定権限
    * Stackdriverからの書き込み先の権限
        * CLIからexportを実行する場合は、CLIのaccountが書き込みの権限を持っている必要がある
        * Web UIからexportを設定する場合は、`cloud-logs@google.com`に書き込み先の書き込み権限を付与する
* export先の指定
    * [Exporting Logs in the API  |  Stackdriver Logging  |  Google Cloud Platform](https://cloud.google.com/logging/docs/api/tasks/exporting-logs?hl=en_US&_ga=2.93541725.-1335872466.1495156691#about_sinks)
    * `storage.googleapis.com/[BUCKET_ID]`
    * `bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET_ID]`
    * `pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]`

To bigquery

* 出力先の選定
    * datasetの横のdropdown menuから`share dataset`を選択す
    * add userで `メールでグループ化` `Can edit`
    * `notify people by email` をoff

* resource.labels.project_id
    * project ID
* protopayload_auditlog.serviceName
    * ServiceName,
* protopayload_auditlog.methodName
    * MethodName
* protopayload_auditlog.status.code
    * StatusCode
* protopayload_auditlog.status.message
    * StatusMessage
* protopayload_auditlog.authenticationInfo.principalEmail
    * accountのemail
    * service accountの場合はservice accountのemail
* protopayload_auditlog.servicedata_v1_bigquery.jobQueryRequest.query
* protopayload_auditlog.servicedata_v1_bigquery.jobInsertRequest.resource.jobConfiguration.query.query
* protopayload_auditlog.servicedata_v1_bigquery.jobQueryResponse.job.jobConfiguration.query.query

## Reference

