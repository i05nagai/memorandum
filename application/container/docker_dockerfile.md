---
title: Docker Dockerfile
---

## Docker Dockerfile
* [Dockerfile のベストプラクティス — Docker-docs-ja 1.9.0b ドキュメント](http://docs.docker.jp/engine/articles/dockerfile_best-practice.html)

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
なので、VOLUME commandは、`docker run`の前にdata volumeを作って、`docker run`時にmountするのと同じだが、docker build時に存在したfileがdata volumeにcopyされる。

## Reference
