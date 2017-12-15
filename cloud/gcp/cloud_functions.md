---
title: Cloud Functions
---

## Cloud Functions

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



## Reference
* [Google Cloud Functions Documentation  |  Cloud Functions  |  Google Cloud Platform](https://cloud.google.com/functions/docs/)
* [GCP: 今月のGCP課金額をslackに自動的に書き込む | エクスチュア株式会社ブログ](http://ex-ture.com/blog/2017/11/06/gcp-billing-to-slack/)

