---
title: gcloud
---

## gcloud

* GROUP
    * alpha
    * app
    * auth
    * beta
    * components
    * compute

## gcloud auth

利用中のaccountの一覧

```
gcloud auth list
```

user accountでaccountを認証.
browserが立ち上がるので`your@email`のccountでgoogleにloginする。

```
gcloud auth login your@email
```

service accountの認証。
key-fileは必須。

```
gcloud auth activate-service-account your_service_account@email --key-file=/path/to/keyfile.json
```

認証したアカウントの認証を取り消す

```
gcloud auth revoke your@email
```

emailを省略した場合のaccountを指定する。

```
gcloud config set account <service-account@gmail.com> 
```

ログインすると、`~/.config/gcloud/credentials`にアクセスに必要なcredentialが書き込まれる。
gcloudはこのcredentialを使ってアクセスする。
中身は、アクセス用のjsonファイル。
gcloud auth loginはbrowserが起動するが、CLIでcredentialの生成もできる。
service accountを使う場合は以下のcommandでkey fileを指定すれば良い。
`service_account@email`はkeyfileのaccountを指定する。

```
gcloud auth activate-service-account service_account@email --key-file /path/to/key_file.json
```

service accountのaccess tokenを取得する。

```
echo $(gcloud auth activate-service-account service_account@email --key-file /path/to/key_file.json; gcloud auth print-access-token)
```

## CLi

Update gcloud

```
gcloud components update
```

## Tips

### Warning googleapiclient.discovery_cache
以下のようなwarningがでる。

```
googleapiclient.discovery_cache init.py:autodetect:44 | file_cache is unavailable when using oauth2client >= 4.0.0
```

以下でlogを抑制できる

```
import logging
logging.getLogger('google.auth._default').setLevel(logging.ERROR)
```

### Warning

```
import logging
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
```

## Docker
* [google/cloud-sdk - Docker Hub](https://hub.docker.com/r/google/cloud-sdk/)
* `~/.config`がvolumeになっているので、一度認証すれば二回目移行は認証不要



## Reference
* [gcloud  |  Cloud SDK  |  Google Cloud Platform](https://cloud.google.com/sdk/gcloud/reference/)

