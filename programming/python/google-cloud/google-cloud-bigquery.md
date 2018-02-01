---
title: google-cloud-bigquery
---

## google-cloud-bigquery
BigQueryのpython用のwrapper

2.7系でしか動かない。

```
pip install --upgrade google-cloud-bigquery
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


## Refrence
* [BigQuery クライアント ライブラリ  |  BigQuery  |  Google Cloud Platform](https://cloud.google.com/bigquery/docs/reference/libraries?hl=ja#client-libraries-install-python)
* [API Client Library for Python  |  Google Developers](https://developers.google.com/api-client-library/python/?hl=ja)
* [BigQuery Client — google-cloud 0.24.1 documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/bigquery-client.html)



