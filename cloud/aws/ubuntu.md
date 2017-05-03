# ubuntu


## 接続
```shell
ssh -i /path/to/pem ubuntu@hostname
```
## アカウント
デフォルトでは`ubuntu`がユーザとして使える。
パスワードの設定は、
```shell
sudo passwd ubuntu
```
でできる。

## nginx

```shell
cd /tmp/ && wget http://nginx.org/keys/nginx_signing.key
sudo apt-keys add nginx_signing.key
sudo apt-get update
```
