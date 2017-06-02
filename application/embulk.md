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

## config

### template
liquidテンプレートが使える。
includeで、別ファイルの設定や変数などを読み込むことができる。
includeするファイル名は`_name_of_template.yml.liquid`とすると以下でincludeできる。

```liquid
{% include 'path/to/inc' %}
```

大事なのは、

* file名の接頭辞は`_`
* 拡張子は`.yml.liquid`
* includeするときは、接頭辞と拡張子は省略
* include字のpathはquotationで囲む



## Plugins

### csv formatter plugin
* delimiter
    * defaultは`,`
* quote
    * defaultは`"`
* escape
    * defaultはquoteと一緒

### embulk-input-gcs
* [GitHub - embulk/embulk-input-gcs: Embulk plugin that loads records from Google Cloud Storage](https://github.com/embulk/embulk-input-gcs)

```
embulk gem install embulk-input-gcs
```

### embulk-input-mysql
* [embulk-input-jdbc/embulk-input-mysql at master · embulk/embulk-input-jdbc](https://github.com/embulk/embulk-input-jdbc/tree/master/embulk-input-mysql)

```
embulk gem install embulk-input-mysql
```

### embulk-output-bigquery
* [GitHub - embulk/embulk-output-bigquery: Embulk output plugin to load/insert data into Google BigQuery](https://github.com/embulk/embulk-output-bigquery)

```
embulk gem install embulk-output-bigquery
```

* path_prefix
    * 内部的に使うtemp fileのpathのprefix
    * 絶対パスで指定しないならカレントディレクトリからの相対パス
    * pathに含まれるdirectoryは存在している必要がある
    * `/hoge/fuga`ならhogeディレクトリにfugaという接頭辞のファイルが作られる
* file_ext
    * 
* delete_from_local_when_job_end
    * trueだと、ジョブの終了後に生成されたlocal fileを削除する
* source_format
    * `CSV` or `NEWLINE_DELIMITED_JSON`
    * 読み込みのファイル形式
    * 内部的には一度、ファイルに出力してファイルからimportしている
    * formatterはduprecatedになったので、指定しても無意味
* allow_quoted_newline
    * defaultでfalse
    * 文字列内に改行を含む場合は必要
* send_timeout_sec
    * requestの待ち時間
    * timeout_secはdeprecatedになった
* read_timeout_sec
    * responceの待ち時間
    * timeout_secはdeprecatedになった

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

## Tips

### JsonMappingException
以下のエラーのときは、configで設定が必要な項目に値が設定されてない場合が多い。
または、`{% include 'path/to/inc' %}`とpathをquotationで囲む。

```
Error: org.embulk.config.ConfigException: com.fasterxml.jackson.databind.JsonMappingException: Setting null to a task field is not allowed. Use Optional<T> (com.google.common.base.Optional) to represent null.
```

### RaiseException + path prefix
path_prefixで指定したファイル名と一緒にこのエラーがでている場合は、 `path_prefix`のpathが存在しているかチェックする。

```
Error: org.jruby.exceptions.RaiseException: (Errno::ENOENT) /path/to/intermediate_file.1013.5932.csv
```

## Reference
* [embulk/embulk-output-bigquery: Embulk output plugin to load/insert data into Google BigQuery](https://github.com/embulk/embulk-output-bigquery#mode)

