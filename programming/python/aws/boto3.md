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


## Reference
* [Boto 3 Documentation — Boto 3 Docs 1.4.4 documentation](https://boto3.readthedocs.io/en/latest/)
