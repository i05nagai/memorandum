---
title: google-cloud-storage
---

## google-cloud-storage

Install

```
pip install --upgrade google-cloud
```

## API

```python
from google.cloud import storage
client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('bucket-id-here')
# Then do other things...
blob = bucket.get_blob('remote/path/to/file.txt')
print(blob.download_as_string())
blob.upload_from_string('New contents!')
blob2 = bucket.blob('remote/path/storage.txt')
blob2.upload_from_filename(filename='/local/path.txt')
```

* blob
    * path
        * `/b/bucket/o/path%2Fto%2Fobject`
        * objectのslashは`%2F`に変換される
    * self_link
        * `https://www.googleapis.com/storage/v1/b/bucket/o/path%2Fto%2Fobject`
        * objectのslashは`%2F`に変換される
    * id
        * `bucket/path/to/object/version_info`
        * `version_info`
            * 時間が数値で記録されている
    * media_link
        * `https://www.googleapis.com/download/storage/v1/b/bucket/o/path%2Fto%2Fobject?generation=<generated_time_mnicros&alt=media`

## Reference
* [Storage — google-cloud 62972c4 documentation](https://googlecloudplatform.github.io/google-cloud-python/latest/storage/client.html)
