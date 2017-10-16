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
oauth2のcredintialを扱う。

```
gcloud auth GROUP | COMMAND [GCLOUD_WIDE_FLAG …]
```


* Google Cloud SDKに対するauthorizationを行う

* GROUP
    * application-default

* Commands
    * active-service-account
    * list
    * login
    * revoke

```
gcloud config set account <service-account@gmail.com> 
```

で設定したアカウントに

```
gcloud auth login
```

でログインできる。
ログインすると、`~/.config/gcloud/credentials`にアクセスに必要なcredentialが書き込まれる。
gcloudはこのcredentialを使ってアクセスする。
中身は、アクセス用のjsonファイル。
gcloud auth loginはbrowserが起動するが、CLIでcredentialの生成もできる。

```
gcloud auth activate-service-account service_account_email --key-file /path/to/key_file.json
```


## Reference
* [gcloud  |  Cloud SDK  |  Google Cloud Platform](https://cloud.google.com/sdk/gcloud/reference/)

