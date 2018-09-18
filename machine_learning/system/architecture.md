---
title: Architecture
---

## Architecture

* Pipeline
    * apache Beam
    * GCP Dataflow

* Kubernetes

* Amazon Lambda
* GCP Cloud Function

* messaging
    * cloud Pub/Sub
* logging
    * fluentd
* monitoring
    * Prometheus
    * DataDog
    * grafana
    * zabbix
* workflow
    * Airflow
    * Luigi
    * Jekins
* BI
    * tableau
    * redash
    * looker
* Streaming
    * Apache Kafka
    * Amazon Kinesis Streams
    * Amazon Kinesis Firehose
    * Apache Spark Streaming
* Data storage
    * GCP BigQuery
    * Amazon S3
    * GCP Cloud Storage
    * Apache Hadoop
* Database
    * MySQL
    * MongoDB
    * PostgreSQL
* Search server
    * Apache Solr
    * Elastic Search
* CI/CD
    * Circle CI
    * Travis CI
    * Spinnaker
* redis
* Amazon DynamoDB
* Amazon Athena
* Amazon Redshift
* Apache Hive


* 1. Data Acquisition
    * streaming
    * batch
* 2. store data
* 3. data processing
* 4. store prcessed data
* 5. train models
    * feature slection
* 6. prediction
* 7. A/B testing

### Service

### Feature Engineering
* why this component exist?
* which component this component communicate to?
* expected inputs
    * streaming
    * batch
* outputs
    * streaming
    * batch
* storage for this components
    * structured knowledge of data such as meaning of the URL
        * for instance, third party URL has information about page information implicitly
        * `http://example.com/items/1/1234`, `/1/` is item category such as clothes or games
* feedback to?

### Model Learning

* reporting
    * measurements of models such as precisions, acuracy 
* feature selection
    * 
* sampling

### Model Prediction

### A/B testing

## Reference
[szilard/ml\-prod: Some thoughts on how to use machine learning in production](https://github.com/szilard/ml-prod)
[Preparing and Architecting for Machine Learning](https://www.gartner.com/binaries/content/assets/events/keywords/catalyst/catus8/preparing_and_architecting_for_machine_learning.pdf)
