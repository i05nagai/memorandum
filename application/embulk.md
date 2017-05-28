---
title: Embulk
---

## Embulk

## Install

```sh
curl --create-dirs -o ~/.embulk/bin/embulk -L "https://dl.embulk.org/embulk-latest.jar"
chmod +x ~/.embulk/bin/embulk
echo 'export PATH="$HOME/.embulk/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

For OSX

```sh
brew install embulk
```


## Plugins

### embulk-input-gcs
* [GitHub - embulk/embulk-input-gcs: Embulk plugin that loads records from Google Cloud Storage](https://github.com/embulk/embulk-input-gcs)

```
embulk gem install embulk-input-gcs
```

### embulk-output-bigquery
* [GitHub - embulk/embulk-output-bigquery: Embulk output plugin to load/insert data into Google BigQuery](https://github.com/embulk/embulk-output-bigquery)

```
embulk gem install embulk-output-bigquery
```

* path_prefix
    * 内部的に使うtemp fileのpathのprefix
    * 絶対パスで指定しないならカレントディレクトリからの相対パス
* file_ext
    * 
* delete_from_local_when_job_end
    * trueだと、ジョブの終了後に生成されたlocal fileを削除する
* source_format
    * 読み込みのファイル形式
    * 内部的には一度、ファイルに出力してファイルからimportしている

### embulk-input-s3
* bucket
    * S3のbucket名
* path_prefix
* endpoint
* auth_method
    * 認証方法
    * basic
        * access_key_id
            * AWS access key id
        * secret_key_id
            * AWS secret access key id
    * env
    * instance
    * profile
    * properties
    * anonymous
    * session
    * default


## Reference
* [embulk/embulk-output-bigquery: Embulk output plugin to load/insert data into Google BigQuery](https://github.com/embulk/embulk-output-bigquery#mode)

