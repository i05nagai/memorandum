---
title: Docker
---

## Docker

## Install
For OSX,

```
brew cask install docker
```

```
sudo port install docker
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

For Ubuntu,

Officialのguideに従っても、`docker-ce`をInstallできない場合がある。
その場合は、Ubuntuが提供している`docker.io`をinstallする。

```
apt-get install docker.io
```

もしくはsnapcraftでinstallする

```
sudo snap install docker
```

```
sudo apt-get install \
  apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
sudo apt-get update
sudo apt-get install docker-ce
```

docker daemonのrunは

```
sudo systemctl enable docker
```

## settings
`~/.docker/config.json`に設定をかく。

### detach key
下記で`ctrl-\ `にdetach keyを変更可能。

```json
{
    "detachKeys": "ctrl-\\"
}
```


### error

#### docker: Cannot connect to the Docker daemon. Is the docker daemon running on this host?.

```
docker-machine start default  # 立ち上げ
```

## docker imagesの名前変更
* [Dockerイメージの名前を変更する - Qiita](http://qiita.com/hirocueki/items/4f077795ac8d94c6ad8f)

## Tips
* [Dockerfile ベストプラクティス (仮) - Qoosky](https://www.qoosky.io/techs/f38c112ca9)
* [Docker container will automatically stop after "docker run -d" - Stack Overflow](https://stackoverflow.com/questions/30209776/docker-container-will-automatically-stop-after-docker-run-d)

### docker command in docker build
docker build時にdocker commmandを使う。
`docker build`のoptionに`--network`が指定できるので、dindのImageをdockerのnetworkにつなげてnetworkを通してdockerを使う。
例えば以下のようにする。

```sh
if [ -z `docker volume ls --filter name=docker --quiet` ]; then
    docker volume create docker
fi
if [ -z `docker network ls --filter name=docker_network --quiet` ]; then
    docker network create docker_network
fi
docker run \
    --rm -it \
    --privileged \
    --name docker \
    --network docker_network \
    --volume docker:/var/lib/docker \
    -d \
    docker:dind
docker build --network docker_network -t <image>:<tag> .
docker kill docker
docker volume rm docker
```

dockerfileは以下のようにする。

```Dockerfile

RUN \
    DOCKER_HOST=tcp://docker:2375 docker images
```

### completion
* [コマンドライン補完 — Docker-docs-ja 1.12.RC ドキュメント](http://docs.docker.jp/compose/completion.html)

zsh

```shell
curl -L https://raw.githubusercontent.com/docker/compose/$(docker-compose version --short)/contrib/completion/zsh/_docker-compose > ~/.zsh/completion/_docker-compose
```

### expose and publish
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
* [Docker の Data Volume まわりを整理する - Qiita](http://qiita.com/lciel/items/e21a4ede3bac7fb3ec5a)


| オプション                      | 意味                                                                          |
|---------------------------------|-------------------------------------------------------------------------------|
| -v `<host_path>:<container_path>` | ホストの `<host_path>` を `<container_path>` にマウントしてコンテナを起動         |
| -v `<container_path>`             | Data Volume を作成して `<container_path>` にマウントしてコンテナを起動          |
| --volumes-from `<container>`      | `<container>` で指定したコンテナの Data Volume を全部マウントしてコンテナを起動 |

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

### Multi state build
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

#### On Mac
* https://docs.docker.com/desktop/mac/

On OSX, you need to expose dirs to mount host dirs explictly.
Otherwise, docker returns the following error.

```
docker: Error response from daemon: Mounts denied:
The path /path/to/dir is not shared from the host and is not known to Docker.
You can configure shared paths from Docker -> Preferences... -> Resources -> File Sharing.
See https://docs.docker.com/docker-for-mac for more info.
```

This is also applicable when you mount a dir in a container mounted on host.
In the bewow example, `/home/foobar/A` must be exposed in File Sharing.

* container A
    * run from host
    * volume: `/Users/foobar/A:/home/foobar/A`
* container B
    * run from container A
    * volume: `/home/foobar/A:/home/foobar/B`




### As Daemon
`tail -f /dev/null`で良い。

```
docker run -d -it --rm \
    image-name \
    tail -f /dev/null
```

### Docker in docker
* [library/docker - Docker Hub](https://hub.docker.com/_/docker/)

`privileged` が必要。


### Docker config
* `$HOME/.docker/config.json`
    * docker loginするとcredentialが書き込まれる
    * credentialsは`username:password`の形式をbase64でencodeしたもの
    * GCRの場合は、`_json_key`でloginした場合も`oauth2accesstoken`とtokenが記録される
* `$HOME/.dockercfg`
* [Advanced Authentication Methods  |  Container Registry  |  Google Cloud Platform](https://cloud.google.com/container-registry/docs/advanced-authentication)

Login to GCP

```
docker login -u oauth2accesstoken -p "$(gcloud auth application-default print-access-token)" https://gcr.io
```

### Content digest
* [HTTP API V2 | Docker Documentation](https://docs.docker.com/registry/spec/api/#content-digests)

* `digest`
    * digetstの構成は `algorithm ":" hex`
    * e.g. `sha256:6c3c624b58dbbcd3c0dd82b4c53f04194d1247c6eebdaab7c610cf7d66709b3b`
* `algorithm`
    * `/[A-Fa-f0-9_+.-]+/`
* `hex`
    * `/[A-Fa-f0-9]+/`

* DIGEST HEADER
    * docker daemonのresponseは全て1`Docker-Content-Digest` HEADERを含んでいる


## pseudo tty
- [Containers, pseudo TTYs, and backward compatibility \[LWN\.net\]](https://lwn.net/Articles/688809/)


## Layer
* [Explaining Docker Image IDs](https://windsock.io/explaining-docker-image-ids/)
* [Odd Bits - Unpacking Docker images with Undocker](http://blog.oddbit.com/2015/02/13/unpacking-docker-images/)
* [Digging into Docker layers – Jessica G – Medium](https://medium.com/@jessgreb01/digging-into-docker-layers-c22f948ed612)


## Tips

#### unexepected EOF
When you pull docker images, you get this error.

- https://www.jfrog.com/jira/browse/RTFACT-16398 
- https://forums.docker.com/t/unexpected-eof-when-pulling-base-image/66182



## Reference
* [Dockerfile Best Practices](http://crosbymichael.com/dockerfile-best-practices.html)
* [Python’s super() considered super! | Deep Thoughts by Raymond Hettinger](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)
* [Container Performance Analysis at DockerCon 2017](http://www.brendangregg.com/blog/2017-05-15/container-performance-analysis-dockercon-2017.html)
* [4.8 Creating and Using Data Volume Containers](https://docs.oracle.com/cd/E37670_01/E75728/html/section_ffp_yt4_gp.html)
