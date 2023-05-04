---
title: gsutil
---

## gsutil


## Permissions
- https://cloud.google.com/storage/docs/access-control/iam-gsutil

## gsutil cp
[cp \- Copy files and objects  \|  Cloud Storage  \|  Google Cloud](https://cloud.google.com/storage/docs/gsutil/commands/cp)

If both the source and destination are GCS, gsutil copies data in the cloud.
Copies spanning locations and/or storage classes cause data to be rewritten in the cloud.

```
gsutil cp <from> <to>
```

* `-r`
    * recursive
* `-m`
    * copying in parallel

```
gsutil cp -m gs://path/to/file[1-9].csv gs://path/to/
```

## gsutil notification
[notification \- Configure object change notification  \|  Cloud Storage  \|  Google Cloud](https://cloud.google.com/storage/docs/gsutil/commands/notification)

The notification command is used to configure Google Cloud Storage support for sending notifications to Cloud Pub/Sub as well as to configure the object change notification feature.

```
gsutil notification
```

```
gsutil notification create \
    -t <topic-name> \
    -f json <bucket-name>
```

## Reference
