---
title: Google Cloud Container Builder
---

## Google Cloud Container Builder
docker imageで、Buildを実行する。
docker imageのbuildも可能。


## Image
* [GoogleCloudPlatform/cloud-builders: Supported builder images for Google Cloud Container Builder](https://github.com/GoogleCloudPlatform/cloud-builders)
    * officialで提供されているbuild用のdocker image.
    * `gcr.io/cloud-builders/<name>`で利用可能

* bazel
    * runs the bazel tool
* docker
    * runs the docker tool
* gcloud
    * runs the gcloud tool
* git
    * runs the git tool
* go
    * runs the go tool
* gradle
    * runs the gradle tool
* gsutil
    * runs the gsutil tool
* kubectl
    * runs the kubectl tool
* mvn
    * runs the maven tool
* npm
    * runs the npm tool
* wget
    * runs the wget tool
* yarn
    * runs the yarn tool

## Automating build
* [Automating Builds using Build Triggers  |  Cloud Container Builder  |  Google Cloud](https://cloud.google.com/container-builder/docs/running-builds/automate-builds)

* You need source code in `Cloud Source Repository`, `GitHub`, or `Bitbucket`
* build triggerの設定は、 Container Reigstryのpageから行う
* Trigger type
    * 特定のbranchのcommit, 
    * 特定のtagのcommit,
    * 
* GitHub, Bitbucketを使うときは、projectにowener level permissionが必要
* `[ci skip]`, `[skip ci]`でtriggerをskipできる

## Configuration
* [Build Configuration Overview  |  Cloud Container Builder  |  Google Cloud](https://cloud.google.com/container-builder/docs/build-config)

YAML/JSONでかく。
全体のformatは以下のようになる。

```yaml
steps:
- name: string
  args: list
  env: list
  dir: string
  id: string
  waitFor: string
  entrypoint: string
  secretEnv: string
  volumes: object(Volume)
  timeout: string (Duration format)
- name: string
  ...
- name: string
  ...
timeout: string (Duration format)
logsBucket: string
options:
 sourceProvenanceHash: enum(HashType)
 machineType: enum(MachineType)
 diskSizeGb: string (int64 format)
 substitutionOption: enum(SubstitutionOption)
 logStreamingOption: enum(LogStreamingOption)
substitutions: map (key: string, value: string)
tags: string
secrets: object(Secret)
images: [string, string, ...]
```

Buld steps
stespの例

* name
    * imageの名前
* args
    * imageのargments
* env
    * list of `key=value`
* dir
    * working directory
    * by default `/workspace`
    * buildの生成物は 他のstepでも`/workspace` に保持され続ける
    * relative pathを指定したら、`/workspace/<dir>`がworking directoryになる
        * e.g. `'examples/hello_world'`
    * absolute pathを指定したら、`<dir>`がworking directoryになるが、buildの生成物は他のstepで参照できない
        * e.g. `'/examples/hello_world'`
* timeout: 500s
* id
    * build stepにidをふれる
    * `waitFor`でidを指定するxo
* waitFor
    * 指定がない場合はそれ以前の全てのbuild stepの成功をまつ
* entrypoint
    * docker runのentrypoint
* secretEnv
    * Cloud KMS crypto keyでencryptedされたenv var
    * [Using Encrypted Resources  |  Cloud Container Builder  |  Google Cloud](https://cloud.google.com/container-builder/docs/securing-builds/use-encrypted-secrets-credentials#using_the_encrypted_variable_in_build_requests)
* volume
    * build step間でfileを保持しつづけるdocker container
    * defaultで`workspace` volumeが`/workspace`にmountされている
* logsBucket: 'gs://my-bucket'
    * GCSのbucket
    * 指定しない場合はdefaultのbucketが利用される
* options
    * [REST Resource: projects.builds  |  Cloud Container Builder  |  Google Cloud](https://cloud.google.com/container-builder/docs/api/reference/rest/v1/projects.builds#Build.BuildOptions)
    * buildのoption
    * machine_typeのdefaultは1 cpu
    * substitution_option
        * [Substituting Variable Values  |  Cloud Container Builder  |  Google Cloud](https://cloud.google.com/container-builder/docs/configuring-builds/substitute-variable-values)
* images
    * containerにBuilderにpushするimageの名前
    * build stepsで作成したbuild imageの名前を指定する
* secrets

```yaml
steps:
- name: gcr.io/cloud-builders/git
  args: ['clone', 'https://github.com/GoogleCloudPlatform/cloud-builders']
  env: ['PROJECT_ROOT=hello']
  volumes:
  - name: 'vol1'
    path: '/persistent_volume'
options:
  sourceProvenanceHash: ['SHA256']
  machineType: 'N1_HIGHCPU_8'
  diskSizeGB: 200
  logStreamingOption: STREAM_ON
  substitution_option: 'ALLOW_LOOSE'
- name: gcr.io/cloud-builders/docker
  args: ['build', '-t', 'gcr.io/my-project-id/myimage', '.']
```


```
steps:
- name: 'ubuntu'
  args: ['echo', 'hello ${_SUB_VALUE}']
substitutions:
    _SUB_VALUE: world
options:
    substitution_option: 'ALLOW_LOOSE'
```

## Usage

docker imageのBuild

```yaml
- name: gcr.io/cloud-builders/docker
  args: ['build', '-t', 'gcr.io/my-project-id/myimage', '.']
```

source codeのclone

```yaml
- name: gcr.io/cloud-builders/git
  args: ['clone', 'https://github.com/GoogleCloudPlatform/cloud-builders']
```

## Environment variables
* [Substituting Variable Values  |  Cloud Container Builder  |  Google Cloud](https://cloud.google.com/container-builder/docs/configuring-builds/substitute-variable-values)
    * substitution optionsが使える

* `$PROJECT_ID`
    * build.ProjectId
* `$BUILD_ID`
    * build.BuildId
* `$COMMIT_SHA`
    * build.SourceProvenance.ResolvedRepoSource.Revision.CommitSha
* `$SHORT_SHA`
    * The first seven characters of COMMIT_SHA
* `$REPO_NAME`
    * build.Source.RepoSource.RepoName (only available for triggered builds)
* `$BRANCH_NAME`
    * build.Source.RepoSource.Revision.BranchName (only available for triggered builds)
* `$TAG_NAME`
    * build.Source.RepoSource.Revision.TagName (only available for triggered builds)
* `$REVISION_ID`
    * build.SourceProvenance.ResolvedRepoSource.Revision.CommitSha (only available for triggered builds)

## Tips

### Speeding up builds
* [Speeding up your Builds  |  Cloud Container Builder  |  Google Cloud](https://cloud.google.com/container-builder/docs/speeding-up-builds#using_custom_virtual_machine_sizes)

### Accessing private GitHub repository
* [Accessing Private GitHub Repositories  |  Cloud Container Builder Documentation  |  Google Cloud](https://cloud.google.com/container-builder/docs/access-private-github-repos)



## Reference
* [Google Cloud Container Builder Documentation  |  Cloud Container Builder  |  Google Cloud](https://cloud.google.com/container-builder/docs/?hl=en_US&_ga=2.110153093.-1205531873.1513079066)
