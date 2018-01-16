---
title: Concourse
---

## Concourse
OSSのCI/CD Tool.
Post Jenkinsとして作られた。

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
* groups


## CLI
* [concourse/fly: Concourse CLI for interacting with the ATC API](https://github.com/concourse/fly)
* [Downloads](https://concourse.ci/downloads.html)

fly commandを使う。
Downloadからbinaryをdowloadする。
pathの通っている場所に配置する。



## Reference
* [Hello, world!](https://concourse.ci/hello-world.html)
* [Downloads](https://concourse.ci/downloads.html)
