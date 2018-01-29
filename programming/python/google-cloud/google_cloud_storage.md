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

## Reference
* [Storage — google-cloud 62972c4 documentation](https://googlecloudplatform.github.io/google-cloud-python/latest/storage/client.html)
