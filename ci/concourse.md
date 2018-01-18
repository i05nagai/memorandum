---
title: Concourse
---

## Concourse
OSSのCI/CD Tool。 Post Jenkinsとして作られた。
`Wercker`のように、Pipelineを作って各stepはcontainer内で実行する。
stepの生成物を、他のstepに受け渡すことができ、stepの挙動を環境変数を指定して挙動を変更できる。

officialのCIの画面
https://ci.concourse.ci/

## Concepts
* pipeliens
    * `.travis.yml`や`.circle.yml`にあたる
    * resources/resource_types/jobs/groups/の関係性を記述したもの
    * resources
        * gitのrepositoryやgithubのPRなどがresourceとして参照できる
        * githubのrepositoryをresourceとして`get`できる
        * slackのwebhookに対して`put`で通知できるなど
    * resource_types
        * [Resource Types](http://concourse.ci/resource-types.html)
        * resourceの設定
    * jobs
        * pipelineで実行する処理がjob
        * jobは複数のtaskから成る
* tasks
    * container内で実行される単一のscript
    * pipelineでJobとして利用できる
    * 他のtaskの生成物などをinputとして受け取ることができ、
    * `0` exitでsuccess
    * job/CLIから実行できる

1. pipelineで全体の流れを記述しする
2. stepをtaskとしてtask fileに分ける
    * 再利用できる

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


### task
* [Tasks](https://concourse.ci/running-tasks.html#platform)
* taskは純粋な関数で、`inputs`を入力に`outputs`を出力する
* taskは一度設定すれば、Jobで再利用できる


```yaml
---
platform: linux

# taskの動作するcontainer
image_resource:
  type: docker-image
  source:
    repository: golang
    tag: '1.6'

# 環境変数として利用できる
params:
  SOME_PARAM: some-default-value

# getで指定したものか、 outputsで出力されたものが指定できる
# pathを省略するとnameのfolderに配置される
inputs:
- name: some-input
- name: some-input-with-custom-path
  path: some/custom/path

# outputとして、指定したディレクトリに出力したものは、他のtaskのinputとして利用できる
outputs:
- name: some-output

run:
  path: sh
  args:
  - -exc
  - |
    whoami
    env
    go version
    find .
    touch some-output/my-built-artifact
```

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

teamを作る
teamの認証は、

* Authなし
* Basic Auth
* Genric OAuth
* Github Auth
* Gitlab Auth
* UAA Auth
* BitBucket Cloud Auth
* BitBucket Server Auth

```
fly --target target_name set-team -n team_name \
    --basic-auth-username=... \
    --basic-auth-password=...
```

pipeplineを登録
登録したpipelieneはdefaultではpauseになっている。

```
fly --target target_name set-pipeline -p pipeline_name \
    --var "private-repo=$(cat /path/to/ssh/key)"
```

unpause pipeliene

```
fly -t target_name unpause-pipeline -p pipeline_name
```

## Resources
* git
    * disable_ci_skip
        * defaultでは`[skip ci]`, `[ci skip]`があるとresourceはこの更新を無視する

* [Implementing a Resource](http://concourse.ci/implementing-resources.html#resource-metadata)


## Tips

### Error
* [Concourse Pipeline has failed to fetch digest: 401 Unauthorized](http://www.starkandwayne.com/blog/concourse-pipeline-has-failed-to-fetch-digest-401-unauthorized/)

以下のようなerrorがでたら、`resource`のimage名が間違っていないか調べる。

```
resource script '/opt/resource/check []' failed: exit status 1

stderr:  
failed to fetch digest: 401 Unauthorized  
```

## Reference
* [Hello, world!](https://concourse.ci/hello-world.html)
* [Downloads](https://concourse.ci/downloads.html)
