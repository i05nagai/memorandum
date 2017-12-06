---
title: Google Cloud Identity and Access Management
---

## Google Cloud Identity and Access Management
Google Cloud IAM.

## Concepts
* [Overview  |  Cloud Identity and Access Management Documentation  |  Google Cloud Platform](https://cloud.google.com/iam/docs/overview)

Role/Identity/Permissionの関係は以下のofficialの図がわかりやすい。

<div style="text-align: center">
    <img src="https://cloud.google.com/iam/img/iam-overview-basics.png">
</div>

* IAM
    * (Policy)/Role/Permission/Identites/Service accountなどを提供するserviceの総称
* Permissions(権限)
    * permission名は`<service>.<resource>.<verb>`
        * 例えば、`pubsub.subscriptions.consume`
    * 基本的に、permissionと各serviceのREST APIが対応しており、REST APIで可能な操作の権限を許可/不許可する
    * Permissionは直接Identityには付与できず、PermissionはRoleを通してIdentityに付与される
* Roles(役割)
    * permissionsの集まり
    * IDに対してRoleを付与できる
    * Roleは大きく3種類ある
        1. Primitive roles
            * Projectで予め定義されているRoleで、粗い権限、以下の3つ
            * `Viewer`
                * 読み取り専用の権限
            * `Editor`
                * `Viewer`の権限 + 状態を変更するアクションに必要な権限。
            * `Owner`
                * `Editor`の権限 + projectのAccess managementの権限 + projectのbillingの設定の権限
        2. Predefined role
            * Primitive rolesより細かく、resourceやserviceの用途などに合わせて作られたrole
            * serviceごとに提供されている
        3. Custom roles
            * userが自分で定義するrole
            * Beta test中で対応していないserviceもある
* Identities
    * ID, アカウント
    * GCPでアカウントとして扱われるのは大きく以下の5つ
        * google account(gmailのaccount)
            * 基本的に人間が使う
        * google service account
            * service用のアカウント
            * service accountについては以下の記事が比較的わかりやすい
            * [GCP Service Accountを理解する - Qiita](https://qiita.com/t-yotsu/items/5d3d36847fbc71b72b76)
        * google group
            * Google accountsとService accountsの集まり
            * Groupに属すuserに対して一括してRole/Policyの付与ができる
        * G Suite domain
        * Cloud Identity domain

Identitiesに対して、個別にRoleを付与するのは、現実的ではないので、Policyという機能がある。

Policy/Organization/Folder/Projectの関係は以下のofficialの図がわかりやすい。

<div style="text-align: center">
    <img src="https://cloud.google.com/iam/img/iam-overview-policy.png">
</div>

* Organization
    * 会社の組織など
* Folder
    * 1つのOrganizationに属す
* Project
    * 1つのFolderに属す
* Policy
    * Roles + Identites
    * RoleとIdentitiesの対応の集まり
    * Policyは継承される、つまりOrganizationに付与したPolicyはOrganizationのFolder, Folderに属すProjectに継承される


## Service Accounts
* [GCP Service Accountを理解する - Qiita](https://qiita.com/t-yotsu/items/5d3d36847fbc71b72b76)

Service AccountsはIdentiteisの一つだが、Google accountのように特定の個人に結びつかない。
Service accountsに対して、Google accountと同じようにroleを付与することができる。

Service accountの種類

* GCP-managed keys
    * Google APIs service account
        * `[PROJECT_NUMBER]@cloudservices.gserviceaccount.com`
    * このキーはAppEngineやComputeEngineなどのサービスで使用されるキーであり、ダウンロードはできない。Googleが鍵を管理し、自動的にそれらを毎日ローテーションする
* User-managed keys
    * `[PROJECT-NUMBER]-compute@developer.gserviceaccount.com`
    * このキーはユーザが作成、ダウンロードが可能で、ユーザが管理する

## List of roles
`IAM & admin` -> `Roles`で利用可能なroleの一覧を見ることができる。

以下がdefaultで利用可能なroleの一覧。
Beta版のものを含むので、頻繁に変わる可能性がある。

| Name                                    | Used in                |
+=========================================|========================+
| App Engine Admin                        | App Engine             |
| App Engine Code Viewer                  | App Engine             |
| App Engine Deployer                     | App Engine             |
| App Engine Service Admin                | App Engine             |
| App Engine Viewer                       | App Engine             |
| BigQuery Admin                          | BigQuery               |
| BigQuery Data Editor                    | BigQuery               |
| BigQuery Data Owner                     | BigQuery               |
| BigQuery Data Viewer                    | BigQuery               |
| BigQuery Job User                       | BigQuery               |
| BigQuery User                           | BigQuery               |
| Browser                                 | Project                |
| Cloud Dataflow Service Agent            | Service Management     |
| Cloud Datastore Import Export Admin     | Datastore              |
| Cloud Datastore Index Admin             | Datastore              |
| Cloud Datastore Owner                   | Datastore              |
| Cloud Datastore User                    | Datastore              |
| Cloud Datastore Viewer                  | Datastore              |
| Cloud Debugger Agent                    | Cloud Debugger         |
| Cloud Debugger User                     | Cloud Debugger         |
| Cloud KMS Admin                         | Cloud KMS              |
| Cloud KMS CryptoKey Decrypter           | Cloud KMS              |
| Cloud KMS CryptoKey Encrypter           | Cloud KMS              |
| Cloud KMS CryptoKey Encrypter/Decrypter | Cloud KMS              |
| Cloud Scheduler Admin                   | Cloud Scheduler        |
| Cloud Scheduler Viewer                  | Cloud Scheduler        |
| Cloud Security Scanner Editor           | Cloud Security Scanner |
| Cloud Security Scanner Runner           | Cloud Security Scanner |
| Cloud Security Scanner Viewer           | Cloud Security Scanner |
| Cloud SQL Admin                         | Cloud SQL              |
| Cloud SQL Client                        | Cloud SQL              |
| Cloud SQL Editor                        | Cloud SQL              |
| Cloud SQL Viewer                        | Cloud SQL              |
| Cloud Tasks Admin                       | Cloud Tasks            |
| Cloud Tasks Queue Admin                 | Cloud Tasks            |
| Cloud Tasks Task Deleter                | Cloud Tasks            |
| Cloud Tasks Viewer                      | Cloud Tasks            |
| Cloud Trace Admin                       | Cloud Trace            |
| Cloud Trace Agent                       | Cloud Trace            |
| Cloud Trace User                        | Cloud Trace            |
| Compute Admin                           | Compute Engine         |
| Compute Image User                      | Compute Engine         |
| Compute Instance Admin (beta)           | Compute Engine         |
| Compute Instance Admin (v1)             | Compute Engine         |
| Compute Load Balancer Admin             | Compute Engine         |
| Compute Network Admin                   | Compute Engine         |
| Compute Network User                    | Compute Engine         |
| Compute Network Viewer                  | Compute Engine         |
| Compute OS Admin Login (beta)           | Compute Engine         |
| Compute OS Login (beta)                 | Compute Engine         |
| Compute Security Admin                  | Compute Engine         |
| Compute Storage Admin                   | Compute Engine         |
| Compute Viewer                          | Compute Engine         |
| Container Engine Service Agent          | Service Management     |
| Conversation API Client                 | Other                  |
| Dataflow Admin                          | Dataflow               |
| Dataflow Developer                      | Dataflow               |
| Dataflow Viewer                         | Dataflow               |
| Dataflow Worker                         | Dataflow               |
| Dataproc Editor                         | Dataproc               |
| Dataproc Service Agent                  | Service Management     |
| Dataproc Viewer                         | Dataproc               |
| Dataproc Worker                         | Dataproc               |
| Deployment Manager Editor               | Deployment Manager     |
| Deployment Manager Type Editor          | Deployment Manager     |
| Deployment Manager Type Viewer          | Deployment Manager     |
| Deployment Manager Viewer               | Deployment Manager     |
| Editor                                  | Project                |
| Error Reporting Admin                   | Error Reporting        |
| Error Reporting User                    | Error Reporting        |
| Error Reporting Viewer                  | Error Reporting        |
| Errors Writer                           | Error Reporting        |
| IAP-Secured Web App User                | Cloud IAP              |
| Kubernetes Engine Admin                 | Kubernetes Engine      |
| Kubernetes Engine Cluster Admin         | Kubernetes Engine      |
| Kubernetes Engine Developer             | Kubernetes Engine      |
| Kubernetes Engine Viewer                | Kubernetes Engine      |
| Logging Admin                           | Logging                |
| Logs Configuration Writer               | Logging                |
| Logs Viewer                             | Logging                |
| Logs Writer                             | Logging                |
| Monitoring Admin                        | Monitoring             |
| Monitoring Editor                       | Monitoring             |
| Monitoring Metric Writer                | Monitoring             |
| Monitoring Viewer                       | Monitoring             |
| Organization Administrator              | Resource Manager       |
| Organization Policy Viewer              | Organization Policy    |
| Owner                                   | Project                |
| Private Logs Viewer                     | Logging                |
| Project Billing Manager                 | Billing                |
| Project Deleter                         | Resource Manager       |
| Project IAM Admin                       | Resource Manager       |
| Project Lien Modifier                   | Resource Manager       |
| Pub/Sub Admin                           | Pub/Sub                |
| Pub/Sub Editor                          | Pub/Sub                |
| Pub/Sub Publisher                       | Pub/Sub                |
| Pub/Sub Subscriber                      | Pub/Sub                |
| Pub/Sub Viewer                          | Pub/Sub                |
| Quota Administrator                     | Service Management     |
| Quota Viewer                            | Service Management     |
| Reserve Partner Admin                   | Reserve Partner        |
| Reserve Partner Reader                  | Reserve Partner        |
| Role Administrator                      | Roles                  |
| Role Viewer                             | Roles                  |
| Security Reviewer                       | IAM                    |
| Service Account Actor                   | Project                |
| Service Account Admin                   | Service Accounts       |
| Service Account Key Admin               | Service Accounts       |
| Service Account Token Creator           | Service Accounts       |
| Service Account User                    | Service Accounts       |
| Service Management Administrator        | Service Management     |
| Storage Admin                           | Storage                |
| Storage Object Admin                    | Storage                |
| Storage Object Creator                  | Storage                |
| Storage Object Viewer                   | Storage                |
| Viewer                                  | Project                |

EditorとAdminがあるように見えるが、Adminがある場合はEditorがなく、Editorがある場合はAdminがない場合が多いので、基本的に同じ意味で使われている。
`Monitoring Admin`と`Monitoring Editor`があるが、どちらも同じpermissionを持っているので、違いはない。
例外的に、`Pub/Sub Editor`と`Pub/Sub Admin`の場合は、`Pub/Sub Admin`の方が多くの権限を持っている。

Roleについている`Owner`, `Admin`などの権限の強さはだいたい以下の順で、上に行くほど多くの権限を持っている場合が多い。

1. Owner
2. Administorator ≒ Admin > Editor
3. Viewer ≒ Reader ≒ Browser

`Used in`は使われるGCPのserviceを指していることが多いので、必要なroleの目星をつけるのに役立つ。
`Used in`の項目が、GCPのserviceと対応していないものとして、以下のような項目がある。

* project
    * projct全体に対するRole
* IAM
    * `security reviewer`Roleしか存在しないが、`Security Reviewer`は全serviceの参照権限を持ち、編集権限は持たない
* Roles
    * IAMのRoleの作成や閲覧に関するRole
* Service Accounts
    * Serivce accountの作成と閲覧/編集のRole

## Use cases

### BigQueryでTableの閲覧とQueryの実行権限が欲しい
以下のRoleを付与する。

* `BigQuery User`

### BigQueryでTable/datasetの作成と削除の権限が欲しい
以下のRoleを付与する。

* `BigQuery DataOwner`

### IAMのRoleの一覧を見たい
以下のRoleを付与する。

* `Role viewer`

### IAMのRoleの作成/編集/閲覧
以下のRoleを付与する。

* `Role Viewer`
    * 閲覧のみ
* `Role Administrator`
    * 閲覧/編集/作成

### service accountの作成/編集/閲覧
以下のRoleを全て付与すれば、Service accoutとKeyの作成はできるが、Service AccountにRoleは付与できない。
Service AccoiuntへのRoleの付与は、`Project Editor`のRoleであればできた。

* `Project IAM Admin`
    * resourcemanager.projects.get
    * resourcemanager.projects.getIamPolicy
    * resourcemanager.projects.setIamPolicy
* `Service Account Actor`
    * iam.serviceAccounts.actAs
    * iam.serviceAccounts.get
    * iam.serviceAccounts.getAccessToken
    * iam.serviceAccounts.list
    * iam.serviceAccounts.signBlob
    * iam.serviceAccounts.signJwt
    * resourcemanager.projects.get
* `Service Account Admin`
    * iam.serviceAccounts.create
    * iam.serviceAccounts.delete
    * iam.serviceAccounts.get
    * iam.serviceAccounts.getIamPolicy
    * iam.serviceAccounts.list
    * iam.serviceAccounts.setIamPolicy
    * iam.serviceAccounts.update
    * resourcemanager.projects.get
    * resourcemanager.projects.list
* `Service Account Key Admin`
    * iam.serviceAccountKeys.create
    * iam.serviceAccountKeys.delete
    * iam.serviceAccountKeys.get
    * iam.serviceAccountKeys.list
    * iam.serviceAccounts.get
    * iam.serviceAccounts.list
    * resourcemanager.projects.get
    * resourcemanager.projects.list
* `Service Account Token Creator`
    * iam.serviceAccounts.get
    * iam.serviceAccounts.getAccessToken
    * iam.serviceAccounts.list
    * iam.serviceAccounts.signBlob
    * iam.serviceAccounts.signJwt
    * resourcemanager.projects.get
    * resourcemanager.projects.list
* `Service Account User`
    * iam.serviceAccounts.actAs
    * iam.serviceAccounts.get
    * iam.serviceAccounts.list
    * resourcemanager.projects.get
    * resourcemanager.projects.list


### Billing accountに対するRole
今の所、Billing accountに関するRoleはIAMの画面からは付与できない。
Billing accountは、複数のprojectに結びつくので、特定のprojectのIAMの画面から変更できないようになっている。
Billing accountのRoleが必要な場合は、Billing accountのお支払(Billing)画面から、付与できる。

<div style="text-align: center">
    <img src="image/gcp_billing_account_role_01.png">
</div>

<div style="text-align: center">
    <img src="image/gcp_billing_account_role_02.png">
</div>

Dialogが出ている場合は、`Go to Billint account`にする。

<div style="text-align: center">
    <img src="image/gcp_billing_account_role_03.png">
</div>

## Best Prctice

### Service Accounts
service accountの作成時は、以下を確認する。

* サービス アカウントでアクセス可能なリソース
* サービス アカウントに必要な権限
* サービス アカウントの ID を持つコードが実行される場所（Google Cloud Platform またはオンプレミスのどちらか）


<div style="text-align: center">
    <img src="https://cloud.google.com/iam/img/sa-flowchart.png?hl=ja">
</div>

* Service accountは`display name`を設定する
* サービス アカウントに最小限の権限を付与する
* サービス アカウント キーの管理
* service accountの命名規則を決める

## Reference
* [Using Resource Hierarchy for Access Control  |  Cloud Identity and Access Management Documentation  |  Google Cloud Platform](https://cloud.google.com/iam/docs/resource-hierarchy-access-control)
