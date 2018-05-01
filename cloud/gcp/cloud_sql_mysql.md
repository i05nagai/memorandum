---
title: Cloud SQL MySQL
---

## Cloud SQL MySQL
MySQL5.6, MySQL5.7にのみ対応している。
First Generation, Second Generationがあるが、Secondを使えば良い


`'root'@'%'`

## Connecting from GKE

## Replication and Manging instance

### Creating and Managing On-Demand and Automatic Backups

### Restoring an Instance

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
## Reference
* [Cloud SQL for MySQL Documentation  |  Cloud SQL for MySQL  |  Google Cloud](https://cloud.google.com/sql/docs/mysql/)
