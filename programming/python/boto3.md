---
title: boto3
---

## boto3

```
pip install boto3
```

boto3を使うには、credentialの情報が必要。
credentialの渡し方は、

* botoのscriptで、clientを作成するときに、config引数に必要なparameterを渡す
* 環境変数
* `~/.aws/config`

`~/.aws/config/credential`は、`aws-cli`が入っていれば、`aws configure`で作成できる。


## EMR
* [Boto3でEMR - /var/log/laughingman7743.log](http://laughingman7743.hatenablog.com/entry/2016/02/11/185319)
* [EMR — Boto 3 Docs 1.4.4 documentation](https://boto3.readthedocs.io/en/latest/reference/services/emr.html)

## S3

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
s3.meta.client.download_file(bucket, key, to_path)
```




## Reference
* [Boto 3 Documentation — Boto 3 Docs 1.4.4 documentation](https://boto3.readthedocs.io/en/latest/)
