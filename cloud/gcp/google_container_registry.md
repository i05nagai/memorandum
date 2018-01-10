---
title: Google Container Registry
---

## Google Container Registry


## Pricing
* [Pricing  |  Container Registry  |  Google Cloud Platform](https://cloud.google.com/container-registry/pricing)

最初にimageをpushするとCloud Storageにbucketが作られそこにimageが保存される。
DefaultではMulti-Regionalで作られる。

* ImageのGCSの利用料
    * Multi-Regionalで、0.026USD/GB
* imageのpush/pullのnetwrok利用料
    * GCSのnetwork利用料と同じ
    * [Cloud Storage Pricing  |  Cloud Storage Documentation  |  Google Cloud Platform](https://cloud.google.com/storage/pricing#network-pricing)
    * 最初の1TB で0.12USD/GB

## Reference

