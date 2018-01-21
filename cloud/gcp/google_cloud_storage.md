---
title: Google Cloud Storage
---

## Google Cloud Storage
google-cloud-sdkをインストールするとインストールされる`gsutil`を使う。

* Bucket名はGCS全体でunique
* Bucket名は、小文字、hyphen, underscore, 3-63文字、という制限がある
* google-cloud-sdkのgsutilがstorage用のCUI

* storage class
    * Multi Regional
        * 世界中で広く使われる場合
        * Web全般？
    * Regional
        * データの分析など一部の値域で使われる
    * Nealine
        * accessが殆どないもの
        * 月に1回くらい
    * Coldline
        * accessが殆どないもの
        * 年に1回くらい

## Upload

```
gsutil cp arcanine.png gs://hoge/sinmetal.png
```

## Change ACL

```
gsutil acl ch -u AllUsers:R gs://hoge/sinmetal.png
```

## Log
* [Access Logs & Storage Logs  |  Cloud Storage Documentation  |  Google Cloud Platform](https://cloud.google.com/storage/docs/access-logs)
* [Cloud Audit Logging with Cloud Storage  |  Cloud Storage Documentation  |  Google Cloud Platform](https://cloud.google.com/storage/docs/audit-logs)


Audito logと`access & storage log`の使い分け

* audit log
    * 多くの場合、audit logが推奨される
    * Cloud Audit Logging tracks access on a continuous basis.
    * Cloud Audit Logging produces logs that are easier to work with.
    * Cloud Audit Logging can monitor many of your Google Cloud Platform services, not just Cloud Storage.
* access & storage logを使いたい場合
    * You want to track access for public objects.
    * You use Access Control Lists (ACLs) to control access to your objects.
    * You want your logs to include latency information, or the request and response size of individual HTTP requests.
    * You want to track the amount of data stored in your buckets.


### Audit logso
* Admin activity logs
    * admin activity logs are recorded by default
    * free
* Data access logs
    * Stackdriverでenableにする
    * Stacdriverのlogの合計使用量が50GB/mounthを超えると利用料金が発生する


```bash
$ gcloud projects get-iam-policy [PROJECT_ID] > /tmp/policy.yaml
$ cat /tmp/policy.yaml
bindings:
- members:
  - user:colleague@example.com
  role: roles/editor
- members:
  - user:myself@example.com
  role: roles/owner
etag: BwVM-FDzeYM=
version: 1

# edit policy.yaml
$ vim /tmp/policy.yaml
$ cat /tmp/policy.yaml
auditConfigs:
- auditLogConfigs:
  - logType: DATA_WRITE
  - logType: DATA_READ
  service: storage.googleapis.com
bindings:
- members:
  - user:colleague@example.com
  role: roles/editor
- members:
  - user:myself@example.com
  role: roles/owner
etag: BwVM-FDzeYM=
version: 1

# update
$ gcloud projects set-iam-policy [PROJECT_ID] /tmp/policy.yaml
```

### access & storage logs

```
gsutil mb gs://bucket-to-store-log
# give write permission to GCS
gsutil acl ch -g cloud-storage-analytics@google.com:W gs://bucket-to-store-log
gsutil defacl set project-private gs://bucket-to-store-log
gsutil logging set on -b gs://bucket-to-store-log [-o log_object_prefix ] gs://bucket-to-be-logged
```

* `log_object_prefix`
    * logのprefix

```bash
#!/bin/bash

################################################################################
# Requirements:
#   gcloud
################################################################################

bucket_to_store_log="gs://bucket_to_store_log"

for bucket_url in $(gsutil ls | grep -v ${bucket_to_store_log} ); do
  log_prefix=$(echo $bucket_url | sed 's/gs:\/\///')
  echo "gsutil logging set on -b ${bucket_to_store_log} -o ${log_prefix} ${bucket_url}"
  gsutil logging set on -b ${bucket_to_store_log} -o ${log_prefix} ${bucket_url}
done
```

**BigQueryでの分析**

StorageにためたlogをbigQueryで分析できるようにする。
GCPからschemaが提供されている。

* [Access Logs & Storage Logs  |  Cloud Storage Documentation  |  Google Cloud Platform](https://cloud.google.com/storage/docs/access-logs#format)
* http://storage.googleapis.com/pub/cloud_storage_usage_schema_v0.json
    * storage_usage
* http://storage.googleapis.com/pub/cloud_storage_storage_schema_v0.json
    * storage_storage

BigQueryへのloadは`*`がつかえるので、一括してLoadできる。

```
$ bq load --skip_leading_rows=1 dataset.table_usage \
      gs://example-logs-bucket/example-bucket_usage_2014_* \
      ./cloud_storage_usage_schema_v0.json
$ bq load --skip_leading_rows=1 dataset.table_storage \
      gs://example-logs-bucket/example-bucket_storage_2014_* \
      ./cloud_storage_storage_schema_v0.json
```

## CLI


```
gsutil mb gs://example-logs-bucket
```

* `mb`
    * make bucket

Get list of buckets

```
gsutil ls
```

Show objects in buckets

```
gsutil ls gs://bucket
```

* `-r`
    * recursive

bucketのloggingが設定されているか。

```
gsutil logging get gs://bucket
```

## Reference
* [Google Cloud Storageで適当にファイルを公開する方法 - Qiita](http://qiita.com/sinmetal/items/81395ce5fdaeb6e69310)


