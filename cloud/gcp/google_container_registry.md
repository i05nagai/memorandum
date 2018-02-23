---
title: Google Container Registry
---

## Google Container Registry

docker imageの名前は以下のようにする。

```
[HOSTNAME]/[PROJECT-ID]/[IMAGE]
```

* `HOSTNAME`
    * [Pushing and Pulling Images  |  Container Registry  |  Google Cloud Platform](https://cloud.google.com/container-registry/docs/pushing-and-pulling)
    * gcr.io
        * without a prefix hosts your images in the United States, but this behavior may change in a future release
    * us.gcr.io
        * hosts your images in the United States
    * eu.gcr.io
        * hosts your images in the European Union
    * asia.gcr.io
        * hosts your images in Asia
* `PROJECT-ID`
    * project id of gcp
* `image`
    * image name

## CLI
push image

```
gcloud docker -- push gcr.io/my-project/quickstart-image
```

pull image

```
gcloud docker -- pull [HOSTNAME]/[PROJECT-ID]/[IMAGE]
```

delete image in registry

```
gcloud container images delete [HOSTNAME]/[PROJECT-ID]/[IMAGE]
```

*Managing image*

[Managing Images  |  Container Registry  |  Google Cloud Platform](https://cloud.google.com/container-registry/docs/managing)

Listing image in registry

```
gcloud container images list --repository=[HOSTNAME]/[PROJECT-ID]
```

List image of tags

```
gcloud container images list-tags [HOSTNAME]/[PROJECT-ID]/[IMAGE]
```

Tagging image in registry

```
gcloud container images add-tag [HOSTNAME]/[PROJECT-ID]/[IMAGE]:latest [HOSTNAME]/[PROJECT-ID]/[IMAGE]:[TAG]
```

Untag

```
gcloud container images untag [HOSTNAME]/[PROJECT-ID]/[IMAGE]:[TAG]
```

dockerでLogin

```
# with auth token
docker login -u oauth2accesstoken -p "$(gcloud auth application-default print-access-token)" https://gcr.io
# with json key
docker login -u _json_key -p "$(cat keyfile.json)" https://gcr.io
```

## Access control
* [Configuring Access Control  |  Container Registry  |  Google Cloud Platform](https://cloud.google.com/container-registry/docs/access-control)

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

