---
title: RDS
---

## RDS

## Backup

### Create Snapshot
RDSのstorageのsnapshotを作成して、backupを作成できる。
Single AZの場合は、snapshotのためにI/Oが中断される。
Multi AZの場合は、stand byの時にbackupが作成されるので、この中断はない。
中断時間はsize/specにより、数秒から数分。

snapshotはRDSのdashboardのsnapshotから確認できる。

### Restore from snapshot
snapshotからの復元ができる。
復元時に異なるstorage typeを選べるが、その場合は移行に追加の時間がかかる。

## MySQL




## Reference
* [Amazon RDS での MySQL - Amazon Relational Database Service](http://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)
