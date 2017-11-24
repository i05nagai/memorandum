---
title: Google Data Studio
---

## Google Data Studio


## Pricing
Google Data Studio is free of charge for Google Cloud Platform customers.


## Stackdriver

```sql
SELECT
  timestamp
  AS Date,
  resource.labels.project_id
  AS ProjectId,
  protopayload_auditlog.serviceName
  AS ServiceName,
  protopayload_auditlog.methodName
  AS MethodName,
  protopayload_auditlog.status.code
  AS StatusCode,
  protopayload_auditlog.status.message
  AS StatusMessage,
  protopayload_auditlog.authenticationInfo.principalEmail
  AS UserId,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobName.jobId
  AS JobId,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobConfiguration.query.query
  AS Query,
  protopayload_auditlog.servicedata_v1_bigquery.jobQueryResponse.job.jobConfiguration.query.destinationTable.projectId
  AS DestinationTableProjectId,
  protopayload_auditlog.servicedata_v1_bigquery.jobQueryResponse.job.jobConfiguration.query.destinationTable.datasetId
  AS DestinationTableDatasetId,
  protopayload_auditlog.servicedata_v1_bigquery.jobQueryResponse.job.jobConfiguration.query.destinationTable.tableId
  AS DestinationTableId,
  protopayload_auditlog.servicedata_v1_bigquery.jobQueryResponse.job.jobConfiguration.query.createDisposition
  AS CreateDisposition,
  protopayload_auditlog.servicedata_v1_bigquery.jobQueryResponse.job.jobConfiguration.query.writeDisposition
  AS WriteDisposition,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobConfiguration.dryRun
  AS DryRun,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatus.state
  AS JobState,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatus.error.code
  AS JobErrorCode,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatus.error.message
  AS JobErrorMessage,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.createTime
  AS JobCreateTime,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.startTime
  AS JobStartTime,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.endTime
  AS JobEndTime,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.billingTier
  AS BillingTier,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.totalBilledBytes
  AS TotalBilledBytes,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.totalProcessedBytes
  AS TotalProcessedBytes,
  protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.totalBilledBytes / 1000000000
  AS TotalBilledGigabytes,
  (protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.totalBilledBytes / 1000000000) / 1000
  AS TotalBilledTerabytes,
  ((protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.job.jobStatistics.totalBilledBytes / 1000000000) / 1000) * 5
  AS TotalCost,
  1 AS Queries
FROM `PROJECT_ID.YOUR_DATASET_HERE.cloudaudit_googleapis_com_data_access_*`
WHERE
  protopayload_auditlog.serviceName = 'bigquery.googleapis.com'
  AND protopayload_auditlog.methodName = 'jobservice.jobcompleted'
  AND protopayload_auditlog.servicedata_v1_bigquery.jobCompletedEvent.eventName = 'query_job_completed'
```


## cachsing 
* [How Data Studio caches data - Data Studio (Beta) Help](https://support.google.com/datastudio/answer/7020039?hl=en&ref_topic=7441387)

以下の2種類ある。
結果がcacheを使用している場合は、以下が左下に表示される。

<img src="https://lh3.googleusercontent.com/lXeThrcoG_LsQT3a7rCiZAyj2Wm9vuS76T4mlY0JE-_vMJ0GLoL_UW5wmaUrS7wvVIhm=w20">

12時間ごとにcacheが更新される。
Refresh dataで明示的に更新も可能。

* Query cache
    * dimensionや期間を指定したqueryごとに結果がcacheされる
    * query cacheで見つからないときは、prefetch cacheを見に行く
* Prefetch cache (smart cache)
    * prefetchでデータを取得しqueryの結果を分析する
    * BigQueryのようにquery scanの容量ごとに料金がかかる場合はprefechで料金がかかる
    * reportが10日開かれない場合は自動でoffになる

Prefetch cacheのon/off

* Edit your report.
* Select the File > Report settings menu.
* In the Report Settings panel on the right, check or uncheck the Enable cache checkbox.

## Reference
* [Data Studio - Beautiful Data Visualization  |  Google Cloud Platform](https://cloud.google.com/data-studio/)
* [Visualize Spend Over Time with Data Studio  |  Google Cloud Billing API Documentation  |  Google Cloud Platform](https://cloud.google.com/billing/docs/how-to/visualize-data)
* [BigQueryにエクスポートしたGCPの課金データを可視化してみる - Qiita](https://qiita.com/tora470/items/0a3879426d6acc9f0d14)
