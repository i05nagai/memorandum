---
title: Embulk Plugin
---

## Embulk Plugin


### csv formatter plugin
configで設定するのは、主に以下。

* delimiter
    * defaultは`,`
* quote
    * defaultは`"`
* escape
    * defaultはquoteと一緒

### local executor plugin
thread数とか決める。

```yaml
exec:
  max_threads: 8         # run at most 8 tasks concurrently
  min_output_tasks: 1    # disable page scattering
```

### guess executor
CSVの区切り文字とかguessしてくれる。

```yaml
exec:
  guess_plugins: ['csv_all_strings']
  exclude_guess_plugins: ['csv']
```

* guess_plugins
    * guessで使用するplugin
* exclude_guess_plugins
    * guessに使用させないplugin

csv_all_strings pluginは、CSVのすべてのcolumnをstringとして判定する。
上の例では、csv guess pluginを使わないようにして、全てstringとして判定させている。

### embulk-input-gcs
GCSからのデータの転送ができる。
Installは以下でできる。

### file

```
out:
  type: file
  path_prefix: /path/to/output/sample_
  file_ext: csv
  formatter:
    type: csv
```

### stdout

```
out:
  type: stdout
```

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
GCSからのデータの転送ができる。
Installは以下でできる。
* service-accountではadminが必要

* [GitHub - embulk/embulk-input-gcs: Embulk plugin that loads records from Google Cloud Storage](https://github.com/embulk/embulk-input-gcs)

```
embulk gem install embulk-input-gcs
```
* service-accountではadminが必要
* [GitHub - embulk/embulk-input-gcs: Embulk plugin that loads records from Google Cloud Storage](https://github.com/embulk/embulk-input-gcs)


### embulk-input-mysql
MySQLからのデータの転送ができる。
Installは以下でできる。

```
embulk gem install embulk-input-mysql
```

* [embulk-input-jdbc/embulk-input-mysql at master · embulk/embulk-input-jdbc](https://github.com/embulk/embulk-input-jdbc/tree/master/embulk-input-mysql)
* parser
    * 必須
    * columns:
        * 必須
        * 列の定義を与える
* auth_method
    * defaultだとprivate_key
    * json_keyも選べる
    * json_keyはservice-accountでDLできるjsonファイルなどが指定できる
* incremental
    * 差分転送するか
    * defalut false
* incremental_columns
    * [embulk-input-jdbc/embulk-input-mysql at master · embulk/embulk-input-jdbc](https://github.com/embulk/embulk-input-jdbc/tree/master/embulk-input-mysql#incremental-loading)
    * default primary keys
    * 差分転送に利用するcolumn name
    * [Embulk 0.8.3で導入された-cオプションはLiquidを使った設定ファイルとの連携に便利 - Qiita](http://qiita.com/hiroysato/items/3552366ddf7d29bf7829)
    * 指定したKeyを元に以下のようなqueryが実行され、差分だけ転送される
        * `incremental_columns: [updated_at, id]`の場合
    * column nameで指定するcolumnの組は、indexがないとfull table scanになる
        * `CREATE INDEX embulk_incremental_loading_index ON table (updated_at, id);`のようなindexが必要
    * 推奨される方法は、`AUTOINCREMENTAL`のcolumnでprimary keyのものを使う
        * `incremental_columns: []`だと自動で見つけるようになっている

```
SELECT * FROM (
  ...original query is here...
)
ORDER BY updated_at, id
```

columnsには以下が指定できる。

```yaml
columns:
    - {name: id, type: long}
    - {name: account, type: long}
    - {name: time, type: timestamp, format: '%Y-%m-%d %H:%M:%S'}
    - {name: purchase, type: timestamp, format: '%Y%m%d'}
    - {name: comment, type: string}
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
BigQueryへのデータの転送ができる。
Installは以下でできる。

```
embulk gem install embulk-output-bigquery
```

* [GitHub - embulk/embulk-output-bigquery: Embulk output plugin to load/insert data into Google BigQuery](https://github.com/embulk/embulk-output-bigquery)
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
S3からのデータの転送ができる。

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

## Reference
