---
title: Google Cloud Storage Logging
---

## Google Cloud Storage Logging

## Audit log
* Admin activity logs
   * Admin activity logs are recorded by default.
* Data access logs

## Bucket access log

### Creating buckets to store logs
* `gs://gcs-log`
    * bucket to store access log of buckets

```shell
# Create bucket to store logs
gsutil mb gs://gcs-log
# Add write permission of gs://gcs-log to GCS
gsutil acl ch -g cloud-storage-analytics@google.com:W gs://gcs-log
# Change default ACL for objects of logs
gsutil defacl set project-private gs://gcs-log
```

### Setting up log delivery
To deliver logs of a specific bucket, say `gs://sample-bucket`, you need to execute the following command;

```
gsutil logging set on -b gs://gcs-log -o sample-bucket/ gs://sample-bucket 
```

The below script set up log delivery for all existing buckets except for the bucket to store log (i.e. `gs://gcs-log`)

```bash
#!/bin/bash

################################################################################
# Requirements:
#   gcloud
################################################################################

bucket_to_store_log="gs://gcs-log"

for bucket_url in $(gsutil ls | grep -v ${bucket_to_store_log} ); do
  log_prefix=$(echo $bucket_url | sed 's/gs:\/\///')
  echo "gsutil logging set on -b ${bucket_to_store_log} -o ${log_prefix} ${bucket_url}"
  gsutil logging set on -b ${bucket_to_store_log} -o ${log_prefix} ${bucket_url}
done
```

## Analyzing logs in BigQuery
To load logs in buckets,

```bash
#!/bin/bash

################################################################################
# Requirements:
#  * gsutil
#  * curl
# See:
#  * https://cloud.google.com/storage/docs/access-logs
################################################################################

usage() {
  cat <<EOF
make_table_for_access_logs.sh is a tool for make tables from access logs of a bucket

Usage:
    make_table_for_access_logs.sh <bigquery_dataset>
EOF
}

################################################################################
# Description:
# Globals:
#  DATASET
# Arguments:
#   uri: path to object in the bucket
#   prefix: "storage" or "usage"
# Returns:
#   None
################################################################################
load_data_to_table() {
  local uri=$1
  local prefix=$2
  bq load --skip_leading_rows=1 \
    ${DATASET}.${prefix} \
    ${uri}_${prefix}_* \
    "./cloud_storage_${prefix}_schema_v0.json"
}

# Constants
declare -r BUCKET_NAME_FOR_LOG="gcs-log"
declare -r SCHEMA_FOR_USAGE_LOG="http://storage.googleapis.com/pub/cloud_storage_usage_schema_v0.json"
declare -r SCHEMA_FOR_STORAGE_LOG="http://storage.googleapis.com/pub/cloud_storage_storage_schema_v0.json"
# Arguments
declare -r DATASET=$1
if [ -z ${DATASET+x} ]
then
  usage
  exit 0
fi

# download schema
curl -L -O ${SCHEMA_FOR_USAGE_LOG}
curl -L -O ${SCHEMA_FOR_STORAGE_LOG}
# make tables
bq mk ${DATASET}.usage
bq mk ${DATASET}.storage
# make tables
for uri in $(gsutil ls "gs://${BUCKET_NAME_FOR_LOG}"); do
  bucket_name=$(basename $uri)

  echo "Importing logs in ${uri}"
  load_data_to_table ${uri} "usage"
  load_data_to_table ${uri} "storage"
done
```

View for usage logs

```sql
SELECT
  TIMESTAMP_SECONDS(time_micros) AS timestamp
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

## Reference

