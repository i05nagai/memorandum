---
title: Cloud SQL MySQL
---

## Cloud SQL MySQL
MySQL5.6, MySQL5.7にのみ対応している。
First Generation, Second Generationがあるが、Secondを使えば良い

## Connecting from GKE

## Replication and Manging instance

### Creating and Managing On-Demand and Automatic Backups

### Restoring an Instance

## Connection
* Authorized netowrks
    * Cloud SQL Proxyを使わない場合はCIDRで接続可能なIP addressを指定する
* Cloud SQL Proxy
    * [About the Cloud SQL Proxy  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/sql-proxy)
    * Porxy client/server経由で通信する
    * Cloud SQL Proxyを使う場合は、SSLの設定は不要
    * javaのexecutableをinstallする
    * client側にproxy clientを動かし続けておく必要がある
        * docker imageがある`gcr.io/cloudsql-docker/gce-proxy:1.11`
        * https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/master/cloudsql/mysql_wordpress_deployment.yaml
* SSL
    * [Configuring SSL for Instances  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/configure-ssl-instance)
    * ssl key pairの管理が必要

## Cloud SQL Proxy
* [About the Cloud SQL Proxy  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/sql-proxy)

Authorized netowkrsやSSLの設定なしでsecureに接続する方法
Second generationのみ。

* Secure connections
    * TLS 1.2 with a 128-bit AES cipher
* Easier connection management

How the Cloud SQL Proxy works

* proxy serverがinstanceの前にたち、clientはproxy clientにlocalでつなげる
* proxy clinetとproxy serverがdataのやりとり
* `clinet <-> proxy client <--over network-> proxy server <-> instance`

Installng the Cloud SQL Proxy

For Linux

```
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy
```

* service accountの情報
    * `Cloud SQL Client` の Roleが必要
* proxy user account/password


In production

* Reducing Cloud SQL Proxy output
    * `-verbose=false`
* How failover affects the Cloud SQL Proxy


## Concepts

### Backup

* What backups provide
    * restore, recover
    * binary logが必要になる場合もある
* What backups cost
    * 7 automated backup for each instance
    * second generationではbackup storageにcostがかかる
    * 

### Restoring instance
* [Overview of Restoring an Instance  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-restore)

* restoreでcurrent dataは全て消える
* restore中はconnection不可
* high availability configuration (failover replica), replicaがある場合は先に全てのreplicaを削除して、restore後にreplicaを作り直す必要がある

Tips and requirements for restoring to a different instance

* different GCP projectのinstanceにはrestoreできない
* must be same generation
* must be same datanbase version
* The storage capacity of the target instance must be at least as large as the capacity of the instance being backed up.
* backup target instance must be RUNNABLE
* can be different tier

Overview of point-in-time recovery

* recover a specific point time
* binary logging and automated backup must be enable
* point-in-itme recovery always create a new instance

* binary logging
    * a slight reduction in write perfomance
    * read performance is unaffected
    * need to restart if enable/disable
    * enable -> disable delete all existing binary logs

## Log
Stackdriverにlogが転送される。

operational logs

* the time of operation completed in you local timezone
* type of operation
* the status of the operation
* A message describing the outcome the operation.

## Pricing
For lowa

* instance
    * depends on instance type
* storage
    * 0.17USD per GB/month for SSD storage capacity
    * 0.09USD per GB/month for HDD storage capacity
    * 0.08USD per GB/month for backups (used)
* network
    * ingress: free
    * egress:
        * to GCE
            * same region: free
            * between regions within North America: 0.12USD/GB
            * between regions outside of North America: 0.12USD/GB
        * to Other Google Products
            * intra continental: free
            * inter continental: 0.12USD/GB
    * IPv4 address: 0.01USD/hour while idle


## Cloud SQL Proxy CLI
* [About the Cloud SQL Proxy  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/sql-proxy#flags)

```
docker run --rm -it gcr.io/cloudsql-docker/gce-proxy:1.11 /cloud_sql_proxy --help
```

* `-max_connections`
    * default 0
    * 0 means no limit
* `-credential_file`
* `-check_region`
* `-instances=my-project:my-region:my-instance=tcp:3306`
    * `-instances=<connection-name>=<port>`
    * `<port>` はproxy serverのlisten port
    * `-instances=my-project:my-region:my-instance=tcp:0.0.0.0:3306`
        * proxyをhostする場合は

Usage

```
docker run --rm -it \
    gcr.io/cloudsql-docker/gce-proxy:1.11 \
    /cloud_sql_proxy \
    -credential_file=/path/to/credential.json \
    -instances=my-project:my-region:my-instance=tcp:0.0.0.0:3306
```


## Importing data
* [Importing Data into Cloud SQL  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/import-export/importing)
* [Exporting Data for Import into Cloud SQL  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/import-export/creating-sqldump-csv#sqldump)
    * You need GCS to import data



Export data from existing MySQL.

* `--ignore-table [VIEW1] [VIEW2]`
    * VIEW must be ignored
* `--set-gtid-purged=OFF`
* `--skip-triggers`
* `--hex-blob`

```
mysqldump \
    --databases [DATABASE_NAME] \
    -h [INSTANCE_IP] \
    -u [USERNAME] \
    -p \
    --skip-triggers \
    --set-gtid-purged=OFF \
    --hex-blob --default-character-set=utf8 > data.sql

# if you want to rename databases name before importing
cat data.sql | sed -e 's/[DATABASE_NAME]/[NEW_DATABSE_NAME]/' > data.sql
```

Import dumped data


```
gsutil mb gs://<bucket-name>/

# upload dumped data
gsutil cp data.sql gs://<bucket-name>/data.sql

# get service account for Cloud SQL instance
gcloud sql instances describe <instance-name> | grep serviceAccountEmailAddress | cut -f 2 -d ' '

# add permissions
gsutil acl ch -u <service-account>:W gs://<bucket-name>/
gsutil acl ch -u <service-account>:R gs://<bucket-name>/data.sql

# --database=<databse-name> option may not work
# you need to check dumped sql file
gcloud sql import sql \
    <instance-name> \
    gs://<bucket-name>/data.sql \
    --database=<databse-name>

gsutil rb -f gs://<bucket-name>/
```

If you see following error, you need to check

* permissions is added properly,
* or the file exists in GCS

```
Do you want to continue (Y/n)?  y

Importing data into Cloud SQL instance...failed.
ERROR: (gcloud.sql.import.sql) ERROR_RDBMS
```


## Import/Export best branctice
* [Best Practices for Importing and Exporting Data  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/import-export/)

## Reference
* [Cloud SQL for MySQL Documentation  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/)
