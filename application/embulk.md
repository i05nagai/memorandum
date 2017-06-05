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
liquid tagの中を以下のようにかく。

```liquid
{{ "{% include 'path/to/inc' " }}%}
```

大事なのは、

* file名の接頭辞は`_`
* 拡張子は`.yml.liquid`
* includeするときは、接頭辞と拡張子は省略
* include字のpathはquotationで囲む
* includeするファイルは、includeしているファイルと同じか下の階層でないとだめ
    * pathに`..` は使えない

## Plugins

### csv formatter plugin
* delimiter
    * defaultは`,`
* quote
    * defaultは`"`
* escape
    * defaultはquoteと一緒

### local executor plugin

pluginごとの設定に加えて、  

* [Configuration — Embulk 0.8 documentation](http://www.embulk.org/docs/built-in.html)
    * configに最大

```yaml
exec:
  max_threads: 8         # run at most 8 tasks concurrently
  min_output_tasks: 1    # disable page scattering
```

### guess executor

```yaml
exec:
  guess_plugins: ['csv_all_strings']
  exclude_guess_plugins: ['csv']
```

### embulk-input-gcs
* service-accountではadminが必要

* [GitHub - embulk/embulk-input-gcs: Embulk plugin that loads records from Google Cloud Storage](https://github.com/embulk/embulk-input-gcs)

```
embulk gem install embulk-input-gcs
```

### embulk-input-mysql
* [embulk-input-jdbc/embulk-input-mysql at master · embulk/embulk-input-jdbc](https://github.com/embulk/embulk-input-jdbc/tree/master/embulk-input-mysql)

```
embulk gem install embulk-input-mysql
```

* parser
    * 必須
    * columns:
        * 必須
        * 列の定義を与える
* auth_method
    * defaultだとprivate_key
    * json_keyも選べる
    * json_keyはservice-accountでDLできるjsonファイルなどが指定できる


columnsには以下が指定できる。

```yaml
columns:
    - {name: id, type: long}
    - {name: account, type: long}
    - {name: time, type: timestamp, format: '%Y-%m-%d %H:%M:%S'}
    - {name: purchase, type: timestamp, format: '%Y%m%d'}
    - {name: comment, type: string}
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
    * ファイルの拡張子
* delete_from_local_when_job_end
    * trueだと、ジョブの終了後に生成されたlocal fileを削除する
* source_format
    * `CSV` or `NEWLINE_DELIMITED_JSON`
    * 読み込みのファイル形式
    * 内部的には一度、ファイルに出力してファイルからimportしている
    * formatterはduprecatedになったので、指定しても無意味
* field_delimiter
    * CSVのdelimiter
* encoding
    * 転送元ファイルのencoding
* allow_quoted_newlines
    * defaultでfalse
    * 文字列内に改行を含む場合は必要
* send_timeout_sec
    * requestの待ち時間
    * timeout_secはdeprecatedになった
* read_timeout_sec
    * responceの待ち時間
    * timeout_secはdeprecatedになった
* auto_create_table
    * trueでテーブルを自動で作る
* schema_file
    * tableのschemaへのpath
* column_options
    * 列の定義(schema)
    * `{name: date, type: STRING, timestamp_format: %Y-%m-%d, timezone: "Asia/Tokyo"}`
* project
    * 出力先のproject名
    * 必須
* dataset
    * 出力先のdataset名
    * 必須
* table
    * 必須
    * 出力先のtable名

```yaml
out:
  dataset:
```

### embulk-input-s3
* bucket
    * S3のbucket名
* path_prefix
    * bucket名からのpath
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
または、`{{ "{% include 'path/to/inc' " }}%}`とpathをquotationで囲む。

```
Error: org.embulk.config.ConfigException: com.fasterxml.jackson.databind.JsonMappingException: Setting null to a task field is not allowed. Use Optional<T> (com.google.common.base.Optional) to represent null.
```

### RaiseException + path prefix
path_prefixで指定したファイル名と一緒にこのエラーがでている場合は、 `path_prefix`のpathが存在しているかチェックする。

```
Error: org.jruby.exceptions.RaiseException: (Errno::ENOENT) /path/to/intermediate_file.1013.5932.csv
```

### Error
csvの改行系のエラーの場合が多い。

* allow_quoted_newlines: true

```
Error: org.jruby.exceptions.RaiseException: (Error) failed during waiting a Load job, get_job(retty-dpi, embulk_load_job_), errors:[{:reason=>"invalid", :message=>"Too many errors encountered."}, {:reason=>"invalid", :location=>"mediaupload-snapshot", :message=>"CSV table references column position .., but line starting at position:.... contains only .. columns."}]
```

configに以下を指定すると、複数threadで動作しなくなるので、error messageとして、error positionが出る場合はエラーの場所を追いやすい。

```yaml
exec:
  max_threads: 1
  min_output_tasks: 1
```

## Reference
* [embulk/embulk-output-bigquery: Embulk output plugin to load/insert data into Google BigQuery](https://github.com/embulk/embulk-output-bigquery#mode)
* [Embulk YAMLメモ(Hishidama's Embulk YAML Memo)](http://www.ne.jp/asahi/hishidama/home/tech/embulk/yaml.html)
