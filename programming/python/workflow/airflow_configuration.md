---
title: Airlfow Configuration
---

## Airlfow Configuration
description for `airflow.cfg`

## airflow.cfg

```cfg
task_log_reader = file.task
```

* `task_log_reader`
    * [15.9. logging.handlers — Logging handlers — Python 2.7.14 documentation](https://docs.python.org/2/library/logging.handlers.html)
    * [Integration — Airflow Documentation](http://airflow.incubator.apache.org/integration.html?highlight=bigquery)

## Logging to GCS
* [Integration — Airflow Documentation](http://airflow.incubator.apache.org/integration.html?highlight=bigquery#gcp-google-cloud-platform)

## Connection to GCP
* [Apache Airflow: How to add a connection to Google Cloud with CLI](https://medium.com/google-cloud/apache-airflow-how-to-add-a-connection-to-google-cloud-with-cli-af2cc8df138d)
* [google cloud storage - Airflow Remote logging not working - Stack Overflow](https://stackoverflow.com/questions/46293020/airflow-remote-logging-not-working)
    * `googleapis.com/auth/devstorage.full_control `
    * `airflow[gcp_api]`のinstallが必要
        * ` gcloud SDK`が必要
* [How to aggregate data for BigQuery using Apache Airflow | Google Cloud Big Data and Machine Learning Blog  |  Google Cloud Platform](https://cloud.google.com/blog/big-data/2017/07/how-to-aggregate-data-for-bigquery-using-apache-airflow)


## Reference
