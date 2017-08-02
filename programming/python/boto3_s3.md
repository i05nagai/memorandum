---
title: Boto3 S3
---

## Boto3 S3

```python
import boto3

s3 = boto3.resource('s3')
s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')
```

* copy
    S3からS3へのcopy
* download_file
    * fileのdowload

```python
s3 = boto3.client('s3')
s3.client.download_file(bucket, key, to_path)
```

upload files from local to S3.

```python
import boto3

path_to_local_file = '/tmp/hello.txt'
bucket_name = 'mybucket'
bucket_key = 'key/hello.txt'
s3 = boto3.client('s3')
s3.upload_file(path_to_local_file, bucket_name, bucket_key)
```

create bucket

```python
import boto3

bucket_name = 'mybucket'
s3 = boto3.client('s3')
s3.create_bucket(Bucket=bucket_name)
```

## Reference
* [Amazon S3 Examples — Boto 3 Docs 1.4.5 documentation](https://boto3.readthedocs.io/en/latest/guide/s3-examples.html)
