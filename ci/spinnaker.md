---
title: Spinnaker
---

## Spinnaker
Components of Spinnaker

* deck
    * Spinnaker’s UI.
    * Consists of a set of static HTML, JavaScript, and CSS files.
    * Generally served from an Apache server, but there is nothing special about Apache that makes Deck work. Replace with your favorite HTTP(S) server if you’d like.
* echo
    * messaging
    * 通知サービスのメッセージングを制御
* rosco
    * vmのイメージを作成
* front50
    * datastore for pipeline, notification and appliaction
* clouddriver
    * プラットフォームの統合
    * プラットフォームの認証情報を管理
* rush
    * 汎用スクリプトエンジン、スクリプトの管理
* orca
    * providing orchestration of workflow
    * Managing pipelines and tasks
* gate
    * Spinnaker’s API Gateway.
    * All traffic (including traffic generated from Deck) flows through Gate.
    * It is the point at which authentication is confirmed and one point (of several) where authorization is enforced.
* igor
    * jenkins、stash、およびGitHubへのインタフェース(ci連携)
* IdentityProvider
    * This is your organization’s OAuth 2.0, SAML 2.0, or LDAP service. X.509 client certificates can be used in addition to any of these services, or used standalone.




`/opt/spinnaker` にfileがinstallされる。


* Server group
    * cluster/instance group
* Artifact
    * 
    * GCS
    * GitHUb
    * HTTP

## Install

Install on Kubernetest cluster with Helm chart

* [charts/stable/spinnaker at master · helm/charts](https://github.com/helm/charts/tree/master/stable/spinnaker)

```
heml install --name <release-name> stable/spinnaker
```

## Pipeline

Pipeline expression

* [Pipeline Expressions Guide - Spinnaker](https://www.spinnaker.io/guides/user/pipeline-expressions/)

### Triggering Pipelines

#### From GCS
* [Receiving artifacts from GCS \- Spinnaker](https://www.spinnaker.io/guides/user/pipeline/triggers/gcs/)


#### From github
* https://www.spinnaker.io/setup/triggers/github/

* Under your GitHub repository, navigate to Settings > Webhooks > Add Webhook


#### Managing Pipelines


## Stage
Stageの種類

* Bake
    * imageのbuild
    * packerによる
* Check preconditions
* Clone Server Group
* Deploy
* Deploy Server Group
* Destroy Server Group
* Disable Server group
* Disable Cluster 
* Enable Server Group
* Find image from cluster
* Find image from tags
* group
    * a group of stage
* manual judgement
* pipeline
    * run a pipeline
* resize server group
* scale down cluster
* scrip
    * run a script
* shrink cluster
* tag image
* wait
* webhook

## Strategy
* Custom
    * 
* Highlander
    * destroy all previsou server group as soon as new server group passes health check
* None
    * 何もしない
* Red/Black
    * disbale all previsou server grup as soon as new server group passes health check

## GCP
GCPで使う場合は、 Cloud lancher にSpinnakerが登録してある。
* [GoogleCloudPlatform/spinnaker-deploymentmanager](https://github.com/GoogleCloudPlatform/spinnaker-deploymentmanager)
* [Running Spinnaker on Compute Engine  |  Solutions  |  Google Cloud](https://cloud.google.com/solutions/spinnaker-on-compute-engine)
* [Continuous Delivery Pipelines with Spinnaker and Kubernetes Engine  |  Solutions  |  Google Cloud](https://cloud.google.com/solutions/continuous-delivery-spinnaker-kubernetes-engine)
* [viglesiasce/continuous-delivery-spinnaker-gke: Tutorial for deploying, configuring and running Spinnaker on GKE for continuous delivery](https://github.com/viglesiasce/continuous-delivery-spinnaker-gke)

* [GKE のアプリデプロイは Spinnaker に任せて！](https://www.slideshare.net/HammoudiSamir/gke-spinnaker)


## Parametrize
* [Pipeline Expressions Guide - Spinnaker](https://www.spinnaker.io/guides/user/pipeline-expressions/)

## Kubernetes
* [lwander/spin-kub-demo: Spinnaker code to prod demo for Kubernetes](https://github.com/lwander/spin-kub-demo)
* [Parameterize Kubernetes Manifests - Spinnaker](https://www.spinnaker.io/guides/user/kubernetes-v2/parameterize-manifests/)
* `?:`

With manifests

以下のようなに`namespace`というparameterを定義して、manifest内で参照できる
条件

```
metadata:
  namespace: '${ parameters.namespace }'
```

https://www.spinnaker.io/setup/install/providers/kubernetes-v2/#adding-an-account

Spinnaker Kubernetes Providers installes the two components along with spinnaker.

* `kubeconfig`
    * The kubeconfig allows Spinnaker to authenticate against your cluster and to have read/write access to any resources you expect it to manage.
    * `kubectl config`
* `kubectl`
    * Spinnaker relies on kubectl to manage all API access

## Best practices
* [Best Practices for the Kubernetes Provider V2 - Spinnaker](https://www.spinnaker.io/guides/user/kubernetes-v2/best-practices/)

For Kubernetes

* docker imageのtagはdocker digestを使う
* clusterの変更状況を把握するため、spinnakerがaudit logを出力するようにするよう推奨
    * [Spinnaker/Echo + Google Cloud Functions + Stackdriver Logging == Spinnaker Audit Log](https://blog.spinnaker.io/spinnaker-echo-google-cloud-functions-stackdriver-logging-spinnaker-audit-log-81139f084db9)
* config mapとsecretのversionningをする
    * You want to slowly roll out a configuration change
        * configmapが更新されるとconfig mapを参照している全てのpodsが更新される
        * 更新はdeploymentのrolling updateを設定していても全てのpodsが対象となる
        * configmapをversioningしていれば、新しくdeploymentするものについてはconfigmapのversionを変更したものをdeployするようにすれば良い
    * You need to roll back a broken configuration changT
        * configmapをversioningしていない場合は、deplooymentやstatefulsetsなどにconfigmapの変更は表示されない
        * configmapをrollbackkする場合は、古い設定のconfigmapの値に roll forwardする必要がある
            * configmapを参照している全てのpodsが、必要なくともroll forwardされる
* Ad-hoc edit featureは極力使わない


## Reference
* [spinnaker/spinnaker: Spinnaker is an open source, multi-cloud continuous delivery platform for releasing software changes with high velocity and confidence.](https://github.com/spinnaker/spinnaker)
* [Can I push that? Building safer, low-risk deployments with Spinnaker](https://blog.spinnaker.io/can-i-push-that-building-safer-low-risk-deployments-with-spinnaker-a27290847ac4)
* [Multi-Cloud Continuous Delivery with Spinnaker report now available.](https://medium.com/netflix-techblog/multi-cloud-continuous-delivery-with-spinnaker-report-now-available-6040ba83b765)
