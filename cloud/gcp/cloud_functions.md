---
title: Cloud Functions
---

## Cloud Functions
Beta

* Node.js
    * v6.11.5
* docker image
    * gcr.io/google-appengine/nodejs
    * https://github.com/GoogleCloudPlatform/nodejs-docker

## Source code
* Inline editor
    * Web UI in GCP
* Zip upload
* Zip from GCS
* Cloud Source repository
    * 以下を指定できる
        * repository
        * branch/tag
        * branch name
        * path to source code
        * function name in the source code

## Events
Cloud functionsの起動event

* HTTP—invoke functions directly via HTTP requests
* Cloud Storage
* Cloud Pub/Sub
* Firebase (DB, Storage, Analytics, Auth)


cloud functionsのevent parameter

* data
    * eventに関するdata
    * 起動eventごとに異なる
* context
    * The context object for the event
* context.eventId
    * A unique ID for the event.
* context.timestamp
    * The date/time this event was created.
* context.eventType
    * The type of the event.
* context.resource
    * The resource that emitted the event.


## Pub/Sub


## Pricing
料金は、Innvocations, Network, Comute timeについて課金される。

* Innvocations
    * Innvocationsの方法によらず料金は一定
        * HTTP request, background functions, call API
    * 最初の2 million requestは無料
    * その後のrequestは0.4 doller /million
* Network

| Type                                            | Price/GB |
|-------------------------------------------------|----------|
| Outbound Data (Egress)                          | 0.12 USD |
| Outbound Data per month                         | 5GB Free |
| Inbound Data (Ingress)                          | Free     |
| Outbound Data to Google APIs in the same region | Free     |


* Compute Time
    * 100msごとにかかる
    * 100ms以下の時間は四捨五入
    * GB-second
        * 1 GB-second は1GBのmemoryを1秒利用
    * GHz-second
        * 1 GHz-second は1GHzのCPUを1秒利用
    * Cloud functionsで利用されるinstance typeは以下の5種類だが、利用料金はGB-second, GHz-secondの料金から決められている
        * 例えば、512MB, 800MHzの場合は
        * 0.0000100 USD * 0.8 + 0.0000025 USD * 0.5 = 9.250000000000001e-06

1GB-second, 1GHz-second単位の金額は以下のようになる。

| Unit       | Price      |
|------------|------------|
| GB-Second  | 0.0000025 USD |
| GHz-Second | 0.0000100 USD |


| Memory   | CPU1      | Price/100ms     | Price/100ms |
| -------- | --------- | --------------  | ---------   |
| 128MB    | 200MHz    | 0.000000231 USD | 2.31 e-06 USD  |
| 256MB    | 400MHz    | 0.000000463 USD | 4.63 e-06 USD  |
| 512MB    | 800MHz    | 0.000000925 USD | 9.25 e-06 USD  |
| 1024MB   | 1.4 GHz   | 0.000001650 USD | 1.65 e-05 USD  |
| 2048MB   | 2.4 GHz   | 0.000002900 USD | 2.90 e-05 USD  |


* Free tier
    * 2 million invocations per month
    * 400,000 GB-seconds, 200,000 GHz-seconds of compute time per month
    * 5GB of Internet egress traffic per month


## Accessing to other GCP service
Nodejs用のGCP用のAPI libraryを利用する。

* [googleapis/nodejs-bigquery: Node.js client for Google Cloud BigQuery: A fast, economical and fully-managed enterprise data warehouse for large-scale data analytics.](https://github.com/googleapis/nodejs-bigquery#samples)

## Tips and Tricks
* Write idempotent functions
* Always call the callback
* Do not start background activities
* Always delete temporary files
* Error reporting
    * `console.error(new Error('message'))`でStackderiverにerror通知できる
    * uncautght exceptionはだめ


Performance

* Minimize dependencies
* Use global variables to reuse objects in future invocations
    * cloud functionがexecution environmentをrecycleする場合がある
    * その場合は、global scopeの変数は再計算されないのでcacheとして使える
* Do lazy initialization of global variables
    * 


## Monitoring Cloud Functions
* [Monitoring Cloud Functions  |  Cloud Functions Documentation  |  Google Cloud](https://cloud.google.com/functions/docs/monitoring/)


Writing logs

* `console.log()`
    * info level log
* `console.info(new Error('message'));`
    * info level logなので、stackdriver error reportingには通知されない
* `console.error()`
    * error level log
* internal system message
    * debug level log
* `throw 1;`
    * stackdriver error reporingに通知されない
* `console.error(new Error('message'));`
    * stackdriver error reporingに通知
* `callback('message');`
    * HTTP status codeの500を返す場合もstackdriver error reporingに通知されない

Viewing logs

Stackdriver loggingからでも見られる。

```
gcloud beta functions logs read
gcloud beta functions logs read <FUNCTION_NAME> --execution-id d3w-fPZQp9KC-0
```

## Testing and CI/CD
* [Testing and CI/CD  |  Cloud Functions Documentation  |  Google Cloud](https://cloud.google.com/functions/docs/bestpractices/testing)
    * testの一般論と、cloud functionでどうsystem testsまでするかが書いてある

Unit tests

* GCP componentsはSinon.JSのようなmockを使う
* test frameworkはAVAがreferされている

integration tests

* cloud functio emulator
    * localでPub/SubやGCSのnotificationをmockしてくれる
    * alpha feature


## Local emulator
* [Cloud Functions Local Emulator  |  Cloud Functions Documentation  |  Google Cloud](https://cloud.google.com/functions/docs/emulator)

## Reference
* [Google Cloud Functions Documentation  |  Cloud Functions  |  Google Cloud Platform](https://cloud.google.com/functions/docs/)
* [GCP: 今月のGCP課金額をslackに自動的に書き込む | エクスチュア株式会社ブログ](http://ex-ture.com/blog/2017/11/06/gcp-billing-to-slack/)

