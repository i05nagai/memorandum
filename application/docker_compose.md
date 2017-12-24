## Docker Compose

## API
version

### services
以下のような構成になる。
`service_name1`は、自分でサービスの名前を定義する。

```yaml
services:
    service_name1:
        build:
    service_name2:
```

buildと並列に使えるオプションは以下。

* dependes_on
    * `docker-compose up`のときに、依存関係の順番に従って起動する
    * `docker-compose up service_name`で依存しているものを起動してくれる
    * version3ではk`condition`をつけることができない

```yaml
version: '2'
services:
  web:
    build: .
    depends_on:
      - db:
      - redis
  redis:
    image: redis
  db:
    image: postgres
```

* env_files
    * 環境変数が定義されたファイルを読み込み
    * ファイルは`NAME=value`の形式で、`#`で始まる行は無視される

```yaml
services:
  web:
    env_file:
      - ./common.env
      - ./apps/web.env
      - /opt/secrets.env
```

* environment
    * 環境変数を定義する
    * 以下の2つの形式で定義できる

```yaml
environment:
  RACK_ENV: development
  SHOW: 'true'
  SESSION_SECRET:
environment:
  - RACK_ENV=development
  - SHOW=true
  - SESSION_SECRET
```

* expose
    * コンテナのhostには公開されない
    * service間で公開用のポート番号を指定

```yaml
services:
  web:
    expose:
     - "3000"
     - "8000"
```

* external_links
    * docker-composeの外にある、コンテナとリンクする

```yaml
services:
  web:
    external_links:
     - redis_1
     - project_db_1:mysql
     - project_db_1:postgresql
```

* image
    * コンテナイメージ

```yaml
services:
  web:
    image:
      redis
```

* network_mode
    * `docker run`の`--net`で指定するものと同じ
    * `bridge`
    * `host`
    * `none`
    * `service:[service name]`
    * `container:[container name/id]`

* ports
    * ホスト側とコンテナ側の両方のポートを指定
    * 文字列として指定するのが推奨

```
ports:
 - "3000"
 - "3000-3005"
 - "8000:8000"
 - "9090-9091:8080-8081"
 - "49100:22"
 - "127.0.0.1:8001:8001"
 - "127.0.0.1:5000-5010:5000-5010"
```

* entrypoint
    * defaultで実行されるcommand
* command
    * entrypointの引数になる
    * defaultのコマンドの上書き
* hostname
    * docker runのオプションと同じ
* volumes
    * `host_path:container_path`でhostのvolumeをcontainerのvolumeとしてマウントする
    * `host_path:container_path:rw`でアクセス権限も付与できる

```yaml
volumes:
  # パスを指定したら、Engine はボリュームを作成
  - /var/lib/mysql
  # 絶対パスを指定しての割り当て
  - /opt/data:/var/lib/mysql
  # ホスト上のパスを指定する時、Compose ファイルからのパスを指定
  - ./cache:/tmp/cache
  # ユーザの相対パスを使用
  - ~/configs:/etc/configs/:ro
  # 名前付きボリューム（Named volume）
  - datavolume:/var/lib/mysql
```

* healthcheck
    * test
        * listの場合は最初は`NONE`, `CMD`, `CMD-SHELL`の何れか
        * `CMD-SHELL`はtestの引数を文字列で渡すのと同じ

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 1m30s
  timeout: 10s
  retries: 3
```

* configs
    * serviceごとのconfig fileをcontianerにどのように配置するかを設定できる

## CLI
* up
    * build, create, start and attach
* `docker-compose run web bash`
    * bashはコマンド


### compose file
compose file内で実行環境の環境変数が使える。

```
web:
  image: "webapp:${TAG}"
```

* `env_file`
    * compose-fileからの相対pathでenvironment variableを指定できる
    * [Declare default environment variables in file | Docker Documentation](https://docs.docker.com/compose/env-file/)
```yaml
env_file: .env

env_file:
  - ./common.env
  - ./apps/web.env
  - /opt/secrets.env
```

env_fileの中身は次のようになる。

```
# Set Rails/Rack environment
RACK_ENV=development
```

### Control startup
* [Control startup order in Compose | Docker Documentation](https://docs.docker.com/compose/startup-order/)

imageの起動の順序やserviceの起動を待つ方法
shell scriptを各しかない。

* [vishnubob/wait-for-it: Pure bash script to test and wait on the availability of a TCP host and port](https://github.com/vishnubob/wait-for-it)

```yaml
version: "3"
services:
  web:
    build: .
    ports:
      - "80:8000"
    depends_on:
      - "db"
    command: ["./wait-for-it.sh", "db:5432", "--", "python", "app.py"]
  db:
    image: postgres
```

### could not change group /var/run/docker.sock to docker: group docker not found
docker-composeでhostの`/var/run/docker.sock`を`docker:dind`imageにmountすると上記のmessageがでる。

```
RUN addgroup -g 2999 docker
```

## Reference
* [Docker Compose — Docker-docs-ja 1.13.RC ドキュメント](http://docs.docker.jp/compose/toc.html)
* [docker-composeを使うと複数コンテナの管理が便利に - Qiita](http://qiita.com/y_hokkey/items/d51e69c6ff4015e85fce)
* [Compose ファイル・リファレンス — Docker-docs-ja 1.13.RC ドキュメント](http://docs.docker.jp/compose/compose-file.html)
