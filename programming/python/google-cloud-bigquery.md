---
title: google-cloud-bigquery
---

## google-cloud-bigquery
BigQueryのpython用のwrapper

```
pip install --upgrade google-cloud-bigquery
gcloud auth application-default login
```

## API

* [BigQuery Client — google-cloud 0.24.1 documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/bigquery-client.html#google.cloud.bigquery.client.Client.run_async_query)

```python
from google.cloud import bigquery
job_name = "my_sample_job"
query_str = "select * from table_name"
# Instantiates a client
client = bigquery.Client(project="project")
query = client.run_sync_query(job_name,  query_str)
query.run()

rows = query.rows
token = query.page_token
while True:
    do_something_with(rows)
    if token is None:
        break
    rows, total_count, token = query.fetch_data(page_token=token)
```


## Reference
* [API Client Library for Python  |  Google Developers](https://developers.google.com/api-client-library/python/?hl=ja)
* [BigQuery Client Libraries  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python)
* [BigQuery Client — google-cloud 0.24.1 documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/bigquery-client.html)
* [BigQuery Client — google-cloud 0.24.1 documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/bigquery-client.html)
* [BigQuery クライアント ライブラリ  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/libraries?hl=ja#client-libraries-install-python)
* [python-docs-samples/quickstart.py at master · GoogleCloudPlatform/python-docs-samples · GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/bigquery/cloud-client/quickstart.py)

