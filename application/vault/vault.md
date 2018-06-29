---
title: Vault
---

## Vault
For OSX,

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

## Docker
* https://hub.docker.com/_/vault/

Running for development

```
docker run --cap-add=IPC_LOCK -e 'VAULT_DEV_ROOT_TOKEN_ID=myroot' -e 'VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:1234' vault
```

* `VAULT_DEV_ROOT_TOKEN_ID`
    * This sets the ID of the initial generated root token to the given value
* `VAULT_DEV_LISTEN_ADDRESS`
    * This sets the IP:port of the development server listener (defaults to 0.0.0.0:8200)

Running as server

```
docker run --cap-add=IPC_LOCK -e 'VAULT_LOCAL_CONFIG={"backend": {"file": {"path": "/vault/file"}}, "default_lease_ttl": "168h", "max_lease_ttl": "720h"}' vault server
```

Volumes

* `/vault/logs`
    * to use for writing persistent audit logs. By default nothing is written here; the file audit backend must be enabled with a path under this directory.
* `/vault/file`
    * to use for writing persistent storage data when using thefile data storage plugin.
    * By default nothing is written here (a dev server uses an in-memory data store); the file data storage backend must be enabled in Vault's configuration before the container is started.
* `/vault/config `
    * the server will load any HCL or JSON configuration files placed here by binding a volume or by composing a new image and adding files
    * or pass json by env `VAULT_LOCAL_CONFIG`.


## Tips

### API

```
$ cat payload.json
{
  "options": {
      "version": "2"
  }
}

$ curl --header "X-Vault-Token: ..." \
       --request POST \
       --data @payload.json \
       http://127.0.0.1:8200/v1/sys/mounts/secret/tune
```

## Reference
* [Vault by HashiCorp](https://www.vaultproject.io/?_ga=2.80492631.1373947065.1521111241-174552816.1502194891)
* [Vault を使ってチーム内のセンシティブな情報を安全に管理する - Qiita](https://qiita.com/munisystem/items/5fe1eead92b946bc5946)
* [Static Secrets \- Guides \- Vault by HashiCorp](https://www.vaultproject.io/guides/secret-mgmt/static-secrets.html)
