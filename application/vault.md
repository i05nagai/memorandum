---
title: Vault
---

## Vault

```
brew install vault
```


## Configuration
* listener
    * [TCP - Listeners - Configuration - Vault by HashiCorp](https://www.vaultproject.io/docs/configuration/listener/tcp.html)
    * serverの設定

```
listener "tcp" {
  address = "127.0.0.1:8200"
}
```

* seal
* storage
    * S3, GCS etc

```
storage [NAME] {
  [PARAMETERS...]
}
```

* telemetry

## Reference
* [Vault by HashiCorp](https://www.vaultproject.io/?_ga=2.80492631.1373947065.1521111241-174552816.1502194891)
* [Vault を使ってチーム内のセンシティブな情報を安全に管理する - Qiita](https://qiita.com/munisystem/items/5fe1eead92b946bc5946)
