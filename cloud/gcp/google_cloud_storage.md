---
title: Google Cloud Storage
---

## Google Cloud Storage
Use `gsutil` which is installed with `google-cloud-sdk` for CLI.

Restrictions

* Bucket name must be unique over GCS
* Bucket name can contain lower case alphabets, hyphen, underscore and within 3-63 chars.
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


## Versioning

## Lifecycle
* [Object Lifecycle Management  \|  Cloud Storage  \|  Google Cloud](https://cloud.google.com/storage/docs/lifecycle)
    * [Buckets  \|  Cloud Storage  \|  Google Cloud](https://cloud.google.com/storage/docs/json_api/v1/buckets#resource-representations)
    * action
        * `Delete`
        * `SetStorageClass`
    * condition
        * if you specify multiple rules that contains the same action, the action is taken when an object matches the condition in any of the rules
        * `Age`
            * integer
            * the number of days
        * `CreatedBefore`
        * `IsLive`
        * `MatchesStorageClass`
        * `NumberOfNewerVersions`
            * the number of newer versions is `1`


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


#### Audit logs
* Admin activity logs
    * admin activity logs are recorded by default
    * free
* Data access logs
    * Stackdriverでenableにする
    * Stacdriverのlogの合計使用量が50GB/mounthを超えると利用料金が発生する


```
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

#### usage & storage logs

* usage log
    * 1時間ごとに生成される
    * accessがなかった場合は生成されない
    * 15分後に前の1時間のlogが生成される
        * 15分より遅くなる場合もある
    * 1時間に1 log objectとは限らない
    * recordの重複は起こりうる
        * `s_request_id`で判別できる
    * `gs://<bucket_name>/<object_prefix>_usage_<timestamp>_<id>_v0`
    * `gs://example-logs-bucket/example-bucket_usage_2013_06_18_14_00_00_1702e6_v0`
* storage log
    * 1日一回10:00 am PST前に前日分のstorage logが生成される
    * `gs://<bucket_name>/<object_prefix>_storage_<timestamp>_<id>_v0`
    * `gs://example-logs-bucket/example-bucket_storage_2013_06_18_07_00_00_1702e6_v0`

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

**Usage log format**

* time_micros
    * integer
    * he time that the request was completed, in microseconds since the Unix epoch.
* c_ip
    * string
    * The IP address from which the request was made. The "c" prefix indicates that this is information about the client.
* c_ip_type
    * integer
    * The type of IP in the c_ip field:
        * A value of 1 indicates an IPV4 address.
        * A value of 2 indicates an IPV6 address.
* c_ip_region
    * string
    * Reserved for future use.
* cs_method
    * string
    * The HTTP method of this request. The "cs" prefix indicates that this information was sent from the client to the server.
* cs_uri
    * string
    * The URI of the request.
* sc_status
    * integer
    * The HTTP status code the server sent in response. The "sc" prefix indicates that this information was sent from the server to the client.
* cs_bytes
    * integer
    * The number of bytes sent in the request.
* sc_bytes
    * integer
    * The number of bytes sent in the response.
* time_taken_micros
    * integer
    * The time it took to serve the request in microseconds, measured from when the first byte is received to when the response is sent. Note that for resumable uploads, the ending point is determined by the response to the final upload request that was part of the resumable upload.
* cs_host
    * string
    * The host in the original request.
* cs_referer
    * string
    * The HTTP referrer for the request.
* cs_user_agent
    * string
    * The User-Agent of the request. The value is GCS Lifecycle Management for requests made by lifecycle management.
* s_request_id
    * string
    * The request identifier.
* cs_operation
    * string
    * The Cloud Storage operation e.g. GET_Object.
* cs_bucket
    * string
    * The bucket specified in the request. If this is a list buckets request, this can be null.
* cs_object
    * string
    * The object specified in this request. This can be null.

usage log用view

```sql
SELECT
  time_micros
  , TIMESTAMP_MICROS(time_micros) AS time_timestamp
  , c_ip AS ip
  , c_ip_type AS ipv4_or_ipv6
  , c_ip_region AS ip_region
  , cs_method AS http_method
  , cs_uri AS uri
  , sc_status AS http_status
  , cs_bytes AS bytes_request
  , sc_bytes AS bytes_response
  , time_taken_micros
  , cs_host AS host_request
  , cs_referer AS referer
  , cs_user_agent AS user_agent
  , s_request_id AS request_id
  , cs_operation AS operation
  , cs_bucket AS bucket
  , cs_object AS object
FROM
  usage
```

## Pricing
* free usage
    * regional stroage
        * 5GB/motnh
    * class A operation
        * 5,000
    * class B operation
        * 50,000
    * network egress
        * 1GB from North America to each GCP region

For Asia,

* data storage
    * multi regional stroage
        * 0.026USD GB/Month
    * nearline storage
        * 0.007 USD GB /month
    * coldline storage
        * 0.01 USD GB /month
* Free network usage
    * same multi regional/ regional location
    * from narrower region to larger multi-region
        * e.g. `us-east1` to `us`
* Bucket-to-bucket network usage
    * 0-1TB
        * within the same location
            * free
        * different part of multi region
            * 0.01 USD GB/month
        * between worldwide loccaiton
            * 0.12 USD/GB
    * 1-10TB
        * within the same location
            * free
        * different part of multi region
            * 0.01 USD GB/month
        * between worldwide loccaiton
            * 0.11 USD/GB
    * 10+TB
        * within the same location
            * free
        * different part of multi region
            * 0.01 USD GB/month
        * between worldwide loccaiton
            * 0.08 USD/GB

For Asia,

* General network usage
    * 0-1 TB
        * Egress to Worldwide Destinations 
            * 0.12 USD GB/month
        * Egress to Asia Destinations
            * 0.12 USD GB/month
        * Egress to China Destinations 
            * 0.23 USD GB/month
        * Egress to Australia Destinations 
            * 0.19 USD GB/month
        * Ingress
            * free
    * 1-10TB
    * 10+TB

For Asia, Additional cost.
a minimum storage.

* Retrieval and early deletion
    * nearline storage
        * retrieval cost
            * 0.01 USD GB/month
        * minimum storage duration
            * 30 days
    * coldline storage
        * retrieval cost
            * 0.01 USD GB/month
        * minimum storage duration
            * 90 days


## Reference
* [Google Cloud Storageで適当にファイルを公開する方法 - Qiita](http://qiita.com/sinmetal/items/81395ce5fdaeb6e69310)
