---
title: Google Cloud Storage CLI
---

## Google Cloud Storage CLI


## CLI

Upload

```
gsutil cp arcanine.png gs://hoge/sinmetal.png
```

Change ACL

```
gsutil acl ch -u AllUsers:R gs://hoge/sinmetal.png
```

Make bucket

```
gsutil mb gs://example-logs-bucket
```

Get list of buckets

```
gsutil ls
```

Show objects in buckets

```
gsutil ls gs://bucket
```

* `-r`
    * recursive

bucketのloggingが設定されているか。

```
gsutil logging get gs://bucket
```

Delete all bucket objects

```
gsutil rm -r gs://bucket
```

Delete bucket.
The bucket need to be empty

```
gsutil rb gs://bucket
```

## Reference
