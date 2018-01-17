---
title: Concourse
---

## Concourse
OSSのCI/CD Tool.
Post Jenkinsとして作られた。

## Concepts
* pipeliens
    * jobsとresourceのconnectionをつけたもの
* tasks
    * 単一のscriptの実行
    * `0` exitでsuccess
    * job/CLIから実行できる
* jobs
* resources

## Configuraring pipelins

```yaml
resources:
- name: concourse
  type: git
  source:
    uri: https://github.com/concourse/concourse.git
    branch: master
```

* resources
    * jobsで使われるobject
    * name
        * required
        * unique name
    * type
        * required
    * source
        * optional
        * resourceの場所、指定の仕方はresource typeごとに異なる
    * check_every
        * optional
        * defaultは1m
        * resourceのnew versionのcheckの間隔
    * tags
        * optional
        * default `[]`
        * tagsを複数つけられる
    * webhook_token
    * optional

```yaml
resource_types:
- name: pull-request
  type: docker-image
  source:
    repository: jtarchie/pr
```

* resource_type
    * name
        * resource type name
    * type
        * resourceのcontainer imageの種類
        * 基本的には`docker-image`
    * source
        * optional
        * resource type のresourceの場所
        * `docker-image`の場合はDocker Registryのrepository
    * privileged
        * optional, boolean
        * default false
    * params
        * resourceをfetchしてくるときの追加のparams
    * tags
* jobs
    * name
    * serial
        * optional
        * default: false
        * 直列に実行する
    * build_logs_to_retain
        * optional, integer
        * 直近のBuildから指定した回数のLogを残す
    * serial_groups: [string]
        * tagsを指定
        * 指定したtagのjobは同時に実行されない
    * plan
        * required
        * Build planを記載

```yaml
name: banana-unit
plan:
- get: banana
  trigger: true
- task: unit
  file: banana/task.yml
```

```yaml
plan:
- aggregate:
  - get: component-a
  - get: component-b
  - get: integration-suite
```

* plan
    * [Build Plans](https://concourse.ci/build-plans.html)
    * 実行stepのlist
    * `banana` resourceをget
    * `banana` resourceが更新されるたびに`task` stepを実行する
    * `get`
        * fetch resource
    * `put`
        * resourceへのpush
    * `task`
        * inlineで定義されたtaskか外部ファイルに定義されたtaskを実行
    * `aggregate`
        * aggregateのtask/stepを並列に実行する
        * resourceの並列取得


* task
    * [Tasks](https://concourse.ci/running-tasks.html#platform)
    * taskは純粋な関数で、`inputs`を入力に`outputs`を出力する
    * taskは一度設定すれば、Jobで再利用できる
* groups


## CLI
* [concourse/fly: Concourse CLI for interacting with the ATC API](https://github.com/concourse/fly)
* [Downloads](https://concourse.ci/downloads.html)

fly commandを使う。
Downloadからbinaryをdowloadする。
pathの通っている場所に配置する。

```
fly --target name login --concourse-url /url/to/concourse --team-name main
```

* `--target`
    * login先のaliasとして記録される
* `--team-name`
    * defaultは`main`
* `--concourse-url`
    * concourseのURL


login先の一覧

```
fly targets
```

Taskの実行

```
fly --target target_name execute --config build.yaml
```

`build.yaml`の中身

```yaml
platform: linux

image_resource:
  type: docker-image
  source: {repository: busybox}

inputs:
- name: flight-school

run:
  path: ./flight-school/ci/test.sh
```


## Reference
* [Hello, world!](https://concourse.ci/hello-world.html)
* [Downloads](https://concourse.ci/downloads.html)
