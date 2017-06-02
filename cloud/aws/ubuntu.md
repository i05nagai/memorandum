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

## Add new account

* [AWSにubuntu 14.04インストールして初期設定したメモ。 - shuto_log.aep](http://shutosg.hatenadiary.com/entry/2016/04/16/144647)
* [AWS EC2 インスタンスにユーザー追加する方法 - ハトネコエ Web がくしゅうちょう](http://nekonenene.hatenablog.com/entry/2016/08/22/043437)
    * CentOS
* [Linux インスタンスでのユーザーアカウントの管理 - Amazon Elastic Compute Cloud](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/managing-users.html)
    * [Amazon EC2にSudoユーザーを追加する。 - Qiita](http://qiita.com/syou007/items/f3feaa6688ce70900642)
    * AMI

```sh
sudo adduser my_user
```
