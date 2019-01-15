---
title: Architecture
---

## Architecture

* Pipeline
    * Apache Beam
    * GCP Dataflow
* messaging
    * cloud Pub/Sub
    * Apache Kafka
* logging
    * fluentd
* monitoring
    * Prometheus
    * DataDog
    * grafana
    * zabbix
* workflow/job scheduler
    * Apache Airflow
    * Luigi
    * Jekins
    * kuroko2
    * digdag
* BI
    * tableau
    * redash
    * looker
* Streaming
    * Apache Kafka
    * Amazon Kinesis Streams
    * Amazon Kinesis Firehose
    * Apache Spark Streaming
* Batch transfering
    * Embulk
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
    * hyperestraier
    * Apache Solr
    * Elastic Search
* CI/CD
    * Circle CI
    * Travis CI
    * Spinnaker
* Communication
    * slack
    * hipchat
* Provisioning
    * Terraform
    * chef
    * Ansible
* Management of Container
    * Kubernetes
* unclassified so far
    * Amazon Lambda
    * GCP Cloud Function
    * redis
    * Amazon DynamoDB
    * Amazon Athena
    * Amazon Redshift
    * Apache Hive
    * OWASPZAP


* 1. Data Acquisition
    * streaming
    * batch
* 2. store raw data
* 3. data processing
    * feature engineering
* 4. store prcessed data
* 5. learning/training models
    * feature slection
* 6. prediction
* 7. A/B testing

### Service

### Preprocessing
* Renaming
* Filling missing values

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
* what does this component communicate to?

* Rescaling
* Discretization
* Aggregation

### Learning/Training

* reporting
    * measurements of models such as precisions, acuracy 
* feature selection
* sampling

### prediction

### A/B testing


## Reference
* [szilard/ml\-prod: Some thoughts on how to use machine learning in production](https://github.com/szilard/ml-prod)
* [Preparing and Architecting for Machine Learning](https://www.gartner.com/binaries/content/assets/events/keywords/catalyst/catus8/preparing_and_architecting_for_machine_learning.pdf)
* [Designing a learning system](https://people.cs.pitt.edu/~milos/courses/cs2750-Spring03/lectures/class2.pdf)
* [11\_Machine\_Learning\_System\_Design](http://www.holehouse.org/mlclass/11_Machine_Learning_System_Design.html)
* [Meet Michelangelo: Uber's Machine Learning Platform](https://eng.uber.com/michelangelo/)
