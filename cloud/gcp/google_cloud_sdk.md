---
title: Google Cloud SDK
---

## Google Cloud SDK


OSX

```
brew cask install google-cloud-sdk
```

defaultでインストールされるcomponentは以下。

* bq
    * BigQueryのCUI
* gsutil
    * Google Cloud StorageのCUI
* gcloud
    * authentification
    * SDKの設定
    * 

使用可能なcomponentの一覧は以下で見ることができる。

```
gcloud components list
```

installとupdateは

```
gcloud components install COMPONENT_ID
gcloud components update
```

でできる。

プロジェクトの設定は

```
gcloud config set project PROJECT_ID
```

でできる。


## Authentification
Google Cloud SDKをGoogle Cloud PlatformでOAuth2で認証をする。

```
gclodu auth login
```

自動でBrowseのページが開く。

### Service Account
service accountを有効にする。

```
gcloud auth activate-service-account account@hoge.gserviceaccount.com --key-file KEY_FILE
```

* `KEY_FILE`
    * service account作成時にDLできるkey file

## bq
BigQuery用のCLI

### subcommands

* cancel
    * jobをcancelする
* cp
    * tableのcopy
    * `bq cp from to`
* extract
    * tableをGoogle Cloud Storageにコピーする
    * `bq extract table url`
* head
    * rowを表示する
    * `bq head -n 10 table`
* help
    * helpを表示
* init
    * .bigqueryrcファイルの作成とAuthenticate
* insert
    * rowを挿入する
    * json format
    * {"col_name1": val1, "col_name2": val2}
* load
    * sourceから指定したtableにloadする
    * datasetは存在してないとだめ
    * tableに新規にloadするときはschema必須
    * `bq load destination_table souce [<schema>]`
        * destination_tableが存在していれば追記
        * sourceはURIかlocalのファイルpath
        * schemaはtableが存在しない場合にそのschemaを指定する。
            * JSONかtext形式のschema
* ls
    * collectionに含まれるobjectを表示
    * `bq ls`
* mk
    * dataset, table, viewをつくる
    * `bq mk new_dataset.new_table.`
* mkdef
    * GCSのURIにschema定義を紐付ける
    * `bq mkdef uris schema`
* partition
    * tableを分割する
    * `bq partition source_table destination_table`
    * destination_tableは<source_table><YYYYmmdd>で名前がきまる
    * tableは日付で分割される
    * 分割された日付がdestination_tableの日付
* query
    * queryを実行する
    * `bq query "select count(*) from publicdata:samples.shakespeare"`
* rm
    * dataset、tableを削除する
    * `bq rm dataset`
    * `bq rm dataset.table`
* shell
    * interactive settionの開始
* show
    * objectに対する情報
    * `bq show dataset`
    * `bq show dataset.table`
    * `bq show dataset.view`
* update
    * dataset, table, viewのupdate
    * meta dataの追加など
    * `bq update --description "Dataset description" existing_dataset`
* version
    * versionを表示
* wait
    * jobの終了をまつ
    * `bq wait`
        * current jobが終わるまでまつ
    * `bq wait job_id`
        * `job_id`をずっとまつ
    * `bq wait job_id 100`
        * 100秒まつ
    * `bq wait job_id 0`
        * jobが終了しているか調べる
        * 終了していなければすぐ終了
    * `bq wait --fail_on_error job_id`
        * Succeeds if job succeeds.
    * `bq wait --fail_on_error job_id 100`
        * Succeeds if job succeeds in 100 sec.


### schema
BiguQueryのschemaの書き方

* [Preparing Data for Loading  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/preparing-data-for-loading)

既存のtableのschemaは以下で取得できる。

```
bq --format=prettyjson show db_name.table_name > table.json
```


```json
[
    {
        "name": "filed_name",
        "type": "type"
    },
    {
        "name": "filed_name",
        "type": "type"
    }
]
```

使用可能な型

* [Data Types  |  BigQuery Documentation  |  Google Cloud Platform](https://cloud.google.com/bigquery/data-types)


### load

```
bq load --source_format=NEWLINE_DELIMITED_JSON [DATASET].[TABLE_NAME] [PATH_TO_SOURCE] [SCHEMA]
```

```
bq load dataset.new_table gs://path/to/file schema.json
```


### query

## gsutil

* acl
	* Get, set, or change bucket and/or object ACLs
* acls            Working With Access Control Lists
* anon            Accessing Public Data Without Credentials
* apis            Cloud Storage APIs
* cat
	* Concatenate object content to stdout
* compose         Concatenate a sequence of objects into a new composite object.
* config          Obtain credentials and create configuration file
* cors            Get or set a CORS JSON document for one or more buckets
* cp
	* localのファイルも指定できる
	* `-m`
		* parallel
	* `gsutil cp [OPTION]... src_url dst_url`
* crc32c          CRC32C and Installing crcmod
* creds           Credential Types Supporting Various Use Cases
* csek            Supplying Your Own Encryption Keys
* defacl          Get, set, or change default ACL on buckets
* defstorageclass Get or set the default storage class on buckets
* dev             Contributing Code to gsutil
* du              Display object size usage
* encoding        Filename encoding and interoperability problems
* hash            Calculate file hashes
* help            Get help about commands and topics
* iam             Get, set, or change bucket and/or object IAM permissions.
* label           Get, set, or change the label configuration of a bucket.
* lifecycle       Get or set lifecycle configuration for a bucket
* logging         Configure or retrieve logging on buckets
* ls              List providers, buckets, or objects
* mb              Make buckets
* metadata        Working With Object Metadata
* mv              Move/rename objects and/or subdirectories
* naming          Object and Bucket Naming
* notification    Configure object change notification
* options         Top-Level Command-Line Options
* perfdiag        Run performance diagnostic
* prod            Scripting Production Transfers
* projects        Working With Projects
* rb              Remove buckets
* retries         Retry Handling Strategy
* rewrite         Rewrite objects
* rm              Remove objects
* rsync           Synchronize content of two buckets/directories
* security        Security and Privacy Considerations
* setmeta         Set metadata on already uploaded objects
* signurl         Create a signed url
* stat            Display object status
* subdirs         How Subdirectories Work
* support         Google Cloud Storage Support
* test            Run gsutil tests
* throttling      Throttling gsutil
* update          Update to the latest gsutil release
* version         Print version info about gsutil
* versioning      Enable or suspend versioning for one or more buckets
* versions        Object Versioning and Concurrency Control
* web             Set a main page and/or error page for one or more buckets
* wildcards       Wildcard Names


## Reference
* [ハンズオン : Google Cloud SDK 基本と認証 - Qiita](http://qiita.com/yuko/items/1c4ee5b081c5b6a3ac8a)
* [Google BigQuery テーブルスキーマ変更したいです。 - Qiita](http://qiita.com/KAKKA/items/c13d97fac89bf29033e3)
* [BigQueryのbqコマンドを全部試してみたので解説する - apps-gcp](http://www.apps-gcp.com/bq-command/)

