---
title: Docker CLI
---

## Docker CLI
docker clinet.


## docker build
* [docker build | Docker Documentation](https://docs.docker.com/engine/reference/commandline/build/#tarball-contexts)

buildのterminalのlogは`/root/build.log`に記録される。
標準error出力に出力すれば、docker-buildの画面にも表示される。
pythonのloggingなどは、stderrに出力するので、python scriptの経過を表示したい場合は、loggingで良い。

```
docker build -t <image>:<tag> /path/to/Dockerfile
```

dockerfileは1 commandごとにhistoryが作成される。
historyはgitのcommit logと同じなので、imageの容量増加の要因となる。
`--squash`をつけると過去のhistoryをsquashできる。

```
docker build -t <image>:latest /path/to/Dockerfile
docker build --squash -t <image>:latest-postsquash /path/to/Dockerfile
```

2回目のsquashつきのbuildはcacheがあるので、一瞬で終わる。
最初に作ったもののhistoryはsquashされない。
release時にだけsquashをつけるようにしても良い。

* `--cache-from <registory-image-uri>`
    * cacheのimageとして利用する
    * remote repositoryを指定しても自動でPullはしてくれないので、一度pullしてからcahce-fromに指定する
    * [Docker "--cache-from" flag not working - CircleCI 2.0 / 2.0 Support - CircleCI Community Discussion](https://discuss.circleci.com/t/docker-cache-from-flag-not-working/11525)
    * multi state buildの場合最初のlayerのcacheはきかない
        * [--cache-from and Multi Stage: Pre-Stages are not cached · Issue #34715 · moby/moby](https://github.com/moby/moby/issues/34715)


## docker hisotry
imageの各layerの容量などを表示する。

```
docker history <image-name>
```

## docker system
get disk udage of docker.

```
$ docker system df
TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE
Images              29                  9                   3.349 GB            1.507 GB (45%)
Containers          20                  18                  18.64 MB            74.39 kB (0%)
Local Volumes       1                   1                   69.65 MB            0 B (0%)
```

## docker images
* [docker images | Docker Documentation](https://docs.docker.com/engine/reference/commandline/images/#filtering)

imageの一覧を表示する

* `--filter`
    * imageのfiltering
    * `key=value`で指定
    * `dangling=true`
        * `<none>`のcontainerを表示
* `--quiet`
    * container IDだけ表示


## docker run
* [Docker run リファレンス — Docker-docs-ja 1.13.RC ドキュメント](http://docs.docker.jp/engine/reference/run.html)
* [docker run | Docker Documentation](https://docs.docker.com/engine/reference/commandline/run/)

複数コマンドを使いたい場合は bashを使う。

```
docker run <image> /bin/bash -c "cd /path/to/somewhere; python a.py"
```

* `-v=[<host_directory:container_directory>]`
    * `-v \`pwd\`:\`pwd\``
        * で現在のディレクトリが使える。
* `--workdir`
* `--env "var_name=value"`
    * 複数の場合は複数個つける
* `--cap-add=`
    * add linux capability
    * Runtime privilege and Linux capabilities
* `--cap-drop=`
    * drop linux capability
    * Runtime privilege and Linux capabilities
* `--privileged=false`
    * Runtime privilege and Linux capabilities
* `--device=[]`
    * `--device=/dev/snd:/dev/snd:w`
        * `/path/to/dev:[wmr]`
            * `w`: read and write
            * `r`: read
            * `m`: mknod
    * Allows you to run devices inside the container without the --privileged flag.
    * If you want to limit access to a specific device or devices you can use the --device flag. It allows you to specify one or more devices that will be accessible within the container.

[List of capablility](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities)

* `IPC_LOCK`
    * Lock memory (mlock(2), mlockall(2), mmap(2), shmctl(2)).



## docker exec
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

## docker tag
* [docker tag | Docker Documentation](https://docs.docker.com/engine/reference/commandline/tag/#extended-description)

tagの最大長は128char

## docker ps

Get a container ID by image name

```
docker ps --filter ancestor=<image> --format "{{.ID}}" | tr -d "\s"
```

Get a container ID by container name

```
docker ps --filter name=<container name> --format "{{.ID}}" | tr -d "\s"
```

## Reference
