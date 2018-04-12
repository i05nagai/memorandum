---
title: Spinnaker
---

## Spinnaker
Spinnakerの構成要素

* deck
    * web UI
* echo
    * 通知サービスのメッセージングを制御
* rosco
    * vmのイメージを作成
* front50
    * パイプライン、通知およびアプリケーションのデータストア
* clouddriver
    * プラットフォームの統合
    * プラットフォームの認証情報を管理
* rush
    * 汎用スクリプトエンジン、スクリプトの管理
* orca
    * ワークフローのオーケストレーションを提・供
    * pipelineとtaskの制御                  ・
* gate
    * 単一のエンドポイントとして異なるサブシステムのゲートウェイサーバとして動作
* igor
    * jenkins、stash、およびGitHubへのインタフェース(ci連携)



`/opt/spinnaker` にfileがinstallされる。


* Server group
    * cluster/instance group
* Artifact
    * 
    * GCS
    * GitHUb
    * HTTP

## Pipeline

Pipeline expression

* [Pipeline Expressions Guide - Spinnaker](https://www.spinnaker.io/guides/user/pipeline-expressions/)


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
## Kubernetes
[lwander/spin-kub-demo: Spinnaker code to prod demo for Kubernetes](https://github.com/lwander/spin-kub-demo)

## Reference
* [spinnaker/spinnaker: Spinnaker is an open source, multi-cloud continuous delivery platform for releasing software changes with high velocity and confidence.](https://github.com/spinnaker/spinnaker)
* [Can I push that? Building safer, low-risk deployments with Spinnaker](https://blog.spinnaker.io/can-i-push-that-building-safer-low-risk-deployments-with-spinnaker-a27290847ac4)
