## docker

## Install
For OSX,

```
brew cask install docker
```

インストール後に`/Applications/Docker.app`を起動すれば、daemonが起動する。
起動後にnetworkへのアクセスの権限を要求してくるので、OSXの管理者で承認する。


## settings
`~/.docker/config.json`に設定をかく。

### detach key
下記で`ctrl-\ `にdetach keyを変更可能。

```json
{
    "detachKeys": "ctrl-\\"
}
```

## docker run

### multiple commands
複数コマンドを使いたい場合は bashを使う。

```
docker run <image> /bin/bash -c "cd /path/to/somewhere; python a.py"
```

## completion

### zsh

```shell
curl -L https://raw.githubusercontent.com/docker/compose/$(docker-compose version --short)/contrib/completion/zsh/_docker-compose > ~/.zsh/completion/_docker-compose
```

### reference
* [コマンドライン補完 — Docker-docs-ja 1.12.RC ドキュメント](http://docs.docker.jp/compose/completion.html)

## mac

```shell
sudo port install docker
```

```
brew cask install docker
```

### error

#### docker: Cannot connect to the Docker daemon. Is the docker daemon running on this host?.

```
docker-machine start default  # 立ち上げ
```

## reference
* [Dockerfile のベストプラクティス — Docker-docs-ja 1.9.0b ドキュメント](http://docs.docker.jp/engine/articles/dockerfile_best-practice.html)

## docker imagesの名前変更

* [Dockerイメージの名前を変更する - Qiita](http://qiita.com/hirocueki/items/4f077795ac8d94c6ad8f)
* [Docker の Data Volume まわりを整理する - Qiita](http://qiita.com/lciel/items/e21a4ede3bac7fb3ec5a)


| オプション                      | 意味                                                                          |
|---------------------------------|-------------------------------------------------------------------------------| | -v `<host_path>:<container_path>` | ホストの `<host_path>` を `<container_path>` にマウントしてコンテナを起動         |
| -v `<container_path>`             | Data Volume を作成して `<container_path>` にマウントしてコンテナを起動          |
| --volumes-from `<container>`      | `<container>` で指定したコンテナの Data Volume を全部マウントしてコンテナを起動 |

```
FROM ubuntu:16.10
```

このDockerfileのmainterを記載。

```
MAINTAINER name "mail@mail"
```

image作成のために、実行するcommand。
`RUN yum install package`とか`RUN apt-get install`とかをよく使う。

```
RUN command
```

json配列で指定。

```
VOLUME ["/data"]
```

* `FROM ubuntu:16.10`
* `MAINTAINER name "mail@mail"`
* `RUN command`


* `ENV variable value`
* `ENV variable=value`

```Dockerfile
# 複数行かけない
ENV variable value
# 複数行かける
ENV variable1=value1 \
    variable2=value2
```

複数行かける場合は、valeu2の中でvariable1を使うことはできない。
その場合はENVを分ける必要がある。

* `EXPOSE <port> [<port>...] `
    * portをListenすることをコンテナに伝える
    * hostからアクセスするには、更にコンテナの起動時に`-p`でポートを公開する
* ADD
* COPY
* ENTRYPOINT
* RUN
* CMD
* `VOLUME ["/path/to"< ""...>]`
    * 指定したpathを外部からマウント可能にする
* USER
* WORKDIR
    * Dockerfileのコマンド実行時のcurrent directoryを指定
* ARG
* ONBUILD

## Commands/CLI

### docker run
* [Docker run リファレンス — Docker-docs-ja 1.13.RC ドキュメント](http://docs.docker.jp/engine/reference/run.html)
* [docker run | Docker Documentation](https://docs.docker.com/engine/reference/commandline/run/)

* `-v=[<host_directory:container_directory>]`
    * `-v \`pwd\`:\`pwd\``
        * で現在のディレクトリが使える。
* `--workdir`
* `--env "var_name=value"`
    * 複数の場合は複数個つける？

## Tips
* [Dockerfile ベストプラクティス (仮) - Qoosky](https://www.qoosky.io/techs/f38c112ca9)


### Data Volume container
データ格納用のコンテナ。


```Dockerfile
# 永続化のためのデータ領域を作成
docker run -v /var/lib/mysql --name mysql_data busybox
```

* `-v`
    * volumeのmount先
* `--name`
    * runしたcontainerの名前
* `busybox`
    * container imageの名前

このcontainerにmountして起動する場合は、

```Dockerfile
docker run --volumes-from mysql_data --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql
```

* `--volumes-from`
    * container imageの名前
* `-e`
    * 起動したcontainerの環境変数を設定
    * mysqlの公式imageの場合は、mysqlの設定を外からの環境変数で制御する
* `-d`
    * dockerをbackgroundで起動
* `-p`
    * port

### push to docker hub
最初に、docker hubでアカウントを作る。
`username`はdockerhubのアカウントのusernameにする。

```
docker login
docker built -t username/image_name .
docker push username/image_name
```
