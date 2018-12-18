---
title: Terraform Resource
---

## Terraform Resource
Providerが提供しているResourceの設定について記載


## Terraform
* `backend`
    * remote stateのbackend
    * `gcp`
        * `bucket`
            * bucket名
        * `credentials`
        * `prefix`
            * remote stateの保存先
            * `<prefix>/<name>.tfstate`のfileが作られる
        * `path`
        * `project`
        * `region`
        * `encryption_key`
            * stateのencryptionのための32 byte base64 encoded key

## Reference
