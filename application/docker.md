---
title: Docker
---

## Docker

## Install
For OSX,

```
brew cask install docker
```

インストール後に`/Applications/Docker.app`を起動すれば、daemonが起動する。
起動後にnetworkへのアクセスの権限を要求してくるので、OSXの管理者で承認する。

For Amazon Linux

```
yum install docker
```

daemonの起動

```
sudo service docker start
sudo chkconfig docker on
```


## Commands

### docker images
* [docker images | Docker Documentation](https://docs.docker.com/engine/reference/commandline/images/#filtering)

imageの一覧を表示する

* `--filter`
    * imageのfiltering
    * `key=value`で指定
    * `dangling=true`
        * `<none>`のcontainerを表示
* `--quiet`
    * container IDだけ表示


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

### docker exec
container上でcommandを実行。

```
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

```
docker run --name ubuntu_bash --rm -i -t ubuntu bash
```

```
docker exec -d ubuntu_bash touch /tmp/execWorks
```

* `--detach, -d`
    * backgroundで実行

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
    * [dockerのENTRYPOINTとCMDの書き方と使い分け、さらに併用 - Qiita](http://qiita.com/hnakamur/items/afddaa3dbe48ad2b8b5c)
    * docker imageを実行ファイルとして実行する時の振る舞いを記載

書式は以下の2種類

* ENTRYPOINT ["executable", "param1", "param2"]
    * exec form/json array format
    * 推奨される形式
* ENTRYPOINT command param1 param2
    * shell form
    * `/bin/sh -c`経由で実行される
    * CMDやrunの引数を上書きする

docker runの`<iamge>`の後に引数は、exec formの`ENTRYPOINT`にそのまま渡される。
`ENTRYPOINT`が記載されていない場合は、引数のcommandがそのまま実行される。


CMDとの併用は以下のようにする。
併用時はJSON array formatである必要がある。

```dockerfile
ENTRYPOINT ["/usr/bin/rethinkdb"]
CMD ["--help"]
```

```
docker run image/name
```

で実行すると

```
/usr/bin/rethinkdb --help
```

が実行される。


* CMD
    * CMDはdocker imageのデフォルトのコマンドを定義する
    * `docker run`のときに、引数を渡すとCMDの内容は上書きされる

書式は以下の3種類

* CMD ["executable","param1","param2"] (シェルを介さずに実行。この形式を推奨)
* CMD ["param1","param2"] (ENTRYPOINTのデフォルト引数として利用する場合)
* CMD command param1 param2 (シェルを介して実行)




* RUN
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
* [Docker container will automatically stop after "docker run -d" - Stack Overflow](https://stackoverflow.com/questions/30209776/docker-container-will-automatically-stop-after-docker-run-d)

### expose ans publish
* [Difference between "expose" and "publish" in docker - Stack Overflow](https://stackoverflow.com/questions/22111060/difference-between-expose-and-publish-in-docker)

exposeとpublishのちがい

* exposeはdocker container同士の通信には使える
* exposeかつpublishでdocker外からaccess可能

### No space left on device error
* [No space left on device error - Docker for Mac - Docker Forums](https://forums.docker.com/t/no-space-left-on-device-error/10894/44)

以下でdocker imageやcontainerなどを全て削除できる。
これで改善する可能性がある。

```
docker system prune -a
```

```
ls -lah ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/Docker.qcow2
```

### Data Volume container
データ格納用のコンテナ。
`mysql_data` containerの`/var/lib/mysql`いかがData volumeになる。
このdata volumeは`--volume-from` commandでほかのcontainerから参照できる。

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

## Multi state build
* [Use multi-stage builds | Docker Documentation](https://docs.docker.com/engine/userguide/eng-image/multistage-build/)


### docker without sudo
* [Post-installation steps for Linux | Docker Documentation](https://docs.docker.com/engine/installation/linux/linux-postinstall/#manage-docker-as-a-non-root-user)

Linux環境で、sudoが要求される場合がある。
dockerを使うuserを`docker` groupに追加すれば、良い。
`docker` groupが作成されていなければ、作成する。

```
sudo groupadd docker
```

```
sudo usermod -aG docker $USER
```

logoutして再度loginする。
以下のコマンドが実行できれば良い。

```
docker images
```

### Volume
* [Docker glossary | Docker Documentation](https://docs.docker.com/glossary/?term=volume)
* [Manage data in Docker | Docker Documentation](https://docs.docker.com/engine/admin/volumes/)
* [Top 5 Docker Logging Methods to Fit Your Container Deployment Strategy](https://www.loggly.com/blog/top-5-docker-logging-methods-to-fit-your-container-deployment-strategy/)
* [How To Share Data between Docker Containers | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-share-data-between-docker-containers)

docker内のdataはcontainerのremoveにあわせて削除される。
volumeはcontainerのlifecycleとは、異なる領域を作成し、container間でのvolumeの共有とdataの保持を行う。
以下の3種類のvolumeがある。

* host volume
    * hostのfilesystemをcontainerからaccessできるようにしたもの
* named volume
    * 
* anonymous volume

Mountの種類

* Volume
    * `docker volume create`で明示的に作成する
    * hostのdirectoryで中身が管理される
    * volumeは複数のcontainerに同時にmountできる
    * mountしているcontainerがなくても削除されない
    * 使用していないvolumeの削除は`docker volume prune`
    * `named`と`unnamed`があるが、違いは最初のMount時に明示的に名前を与えたかどうか
    * volume driverをsupportしているので、remoteやcloudも指定可能
* Bind mounts
    * bind mountはperformanceが良い
    * host machineのfileやdirectory
* tmpfs mounts
    * diskではなくmemoryに保存されるので、消えることがある
    * swarmはsensitiveな情報

Bind mountsとVolumeはどちらも`-v`でmountできる。
tmpfs mountsは`--tmpfs`を使用できるが、Docker 17.06以降では、全て`--mount`を使うことが推奨されている。

**Good use case for volumes**

* 複数のcontainerでのdataのshare
* remoteやcloudにdataを保存したいとき
* back upが欲しいとき、volumeのdirectory`/var/lib/docker/volumes/<volume-name>`をcopyする

**Good use case for bind mounts**

* source codeやbuild artifactsを取得するとき、
* 

**Good use cases for tmpfs mounts**


```
docker volume create my-vol
```

```
docker volume ls
```

```
docker volume inspect my-vol
```

```
docker run -d \
  -it \
  --name devtest \
  --mount source=myvol2,target=/app \
  nginx:latest
```


Containerの実行時にDataVolumeを作成すると、containerのimageのpathのファイルがdata volumeにcopyされる。
この場合、`/var`内のfileが`DataVolume3`にcopyされる。

```
docker run -ti --rm -v DataVolume3:/var ubuntu
```


### As Daemon
`tail -f /dev/null`で良い。

```
docker run -d -it --rm \
    image-name \
    tail -f /dev/null
```

### VOLUME command in Dockerfile

image1

```
FROM ubuntu:17.10

COPY /opt/hoge
VOLUME ["/image1-volume"]
```

image2

```
FROM ubuntu:17.10

COPY /opt/hoge
```

以下のようにimage1のcontainerを立ち上げておく。

```
docker run \
    -it \
    --rm \
    --name image1-container \
    image1:latest \
    /bin/bash
```

以下のcommandを実行すると、`image1-container`の`/image1-volume`を`image2-container`が参照することができる。

```
docker run \
    -it \
    --rm \
    --volumes-from image1-container \
    --name image2-container \
    image1:latest \
    /bin/bash
```

このとき、`image1-container`を立ち上げた時に、data volumeが作らており、mountされている。
`docker inspect image1-contianer`の`Mount`の場所を見るとdata volumeが`/image1-volume`にmountされていることが分かる。
なので、VOLUME commandは、`docker run`の前にdata volumeを作って、`docker run`時にmountするのと同じ。

## Reference
* [Dockerfile Best Practices](http://crosbymichael.com/dockerfile-best-practices.html)
* [Python’s super() considered super! | Deep Thoughts by Raymond Hettinger](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)
* [Container Performance Analysis at DockerCon 2017](http://www.brendangregg.com/blog/2017-05-15/container-performance-analysis-dockercon-2017.html)
* [4.8 Creating and Using Data Volume Containers](https://docs.oracle.com/cd/E37670_01/E75728/html/section_ffp_yt4_gp.html)
