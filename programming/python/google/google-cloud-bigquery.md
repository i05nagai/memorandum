---
title: google-cloud-bigquery
---

## google-cloud-bigquery
BigQueryのpython用のwrapper

2.7系でしか動かない。

```
pip install --upgrade google-cloud-bigquery
gcloud auth application-default login
```

* [python-docs-samples/quickstart.py at master · GoogleCloudPlatform/python-docs-samples · GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/bigquery/cloud-client/quickstart.py)

## Usage
* [BigQuery — google-cloud 988e2c2 documentation](https://googlecloudplatform.github.io/google-cloud-python/latest/bigquery/usage.html)


## API
* [Jobs  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs)


* JobConfig
    * create_dsiposition
        * `CREATE_IF_NEEDED`
            * default
        * `CREATE_NEVER`
            * 存在しなかったらerror
    * write_disposition
        * `WRITE_TRUNCATE`
            * tableが存在したら、上書き
        * `WRITE_APPEND`
            * tableが存在したら追記する
        * `WRITE_EMPTY`
            * default
            * tableが存在してnot emptyならerror

* [BigQuery Client — google-cloud 0.24.1 documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/bigquery-client.html#google.cloud.bigquery.client.Client.run_async_query)

```python
from google.cloud import bigquery
job_name = "my_sample_job"
query_str = "select * from table_name"
# Instantiates a client
client = bigquery.Client(project="project")
query = client.run_sync_query(query_str)
query.run()

# list of tuples
# tuple is values of row in table
rows = query.rows
token = query.page_token
while True:
    do_something_with(rows)
    if token is None:
        break
    rows, total_count, token = query.fetch_data(page_token=token)
```

* `bigquery._helper.Row`

```python
result = 
print(result[0].field_to_index)
```

## Environment
* [Google Application Default Credentials  |  Google Identity Platform  |  Google Developers](https://developers.google.com/identity/protocols/application-default-credentials)


* `GOOGLE_APPLICATION_CREDENTIALS`
    * path to credential file

## Refrence
* [BigQuery クライアント ライブラリ  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/libraries?hl=ja#client-libraries-install-python)
* [API Client Library for Python  |  Google Developers](https://developers.google.com/api-client-library/python/?hl=ja)
* [BigQuery Client — google-cloud 0.24.1 documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/bigquery-client.html)
* [API Client Library for Python  |  Google Developers](https://developers.google.com/api-client-library/python/?hl=ja)
* [BigQuery Client Libraries  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python)
* [BigQuery Client — google-cloud 0.24.1 documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/bigquery-client.html)
* [BigQuery Client — google-cloud 0.24.1 documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/bigquery-client.html)
* [BigQuery クライアント ライブラリ  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/libraries?hl=ja#client-libraries-install-python)
* [python-docs-samples/quickstart.py at master · GoogleCloudPlatform/python-docs-samples · GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/bigquery/cloud-client/quickstart.py)



