---
title: Terraform Resource Google
---

## Terraform Resource Google
Google Cloud Provider


* `google_container_cluster`
    * [Google: google_container_cluster - Terraform by HashiCorp](https://www.terraform.io/docs/providers/google/r/container_cluster.html)
    * `name`
        * name of cluster
    * `zone`
        * initial_node_countが作られるzone
    * `initial_node_count`
        * masterを除くnodeの数
        * `node_pool`ないときは必須
    * `additional_zones`
        * 指定すると追加したzoneにもinitial_node_count分GCE instanceが作成される
    * `addons_config`
        * `horizontal_pod_autoscaling`
            * defaultは`disabled = true`
        * `http_load_balancing`
            * defaultは`disabled = true`
        * `kubernetes_dashboard`
            * defaultは`disabled = true`
    * `description`
        * clusterの説明
    * `logging_service`
        * noneか`logging.googleapis.com`
        * defaultは`logging.googleapis.com`
    * `maintenance_policy `

```
addons_config {
  http_load_balancing {
    disabled = true
  }
  horizontal_pod_autoscaling {
    disabled = true
  }
}
```

```
maintenance_policy {
  daily_maintenance_window {
    start_time = "03:00"
  }
}
```

* `master_auth`
    * kubernetes masterへの認証情報
    * `username=?`
    * `password=?`
* `network`
    * clusterが接続する`self_link`
* `network_policy`
* `node_config`
* `node_pool`
    * `google_container_node_pool`を指定
    * [REST Resource: projects.locations.clusters.nodePools  |  Kubernetes Engine  |  Google Cloud Platform](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools#NodePool)


```
resource "google_container_node_pool" "np" {
  name               = "my-node-pool"
  zone               = "us-central1-a"
  cluster            = "${google_container_cluster.primary.name}"
  initial_node_count = 3
}
```

* `google_container_node_pool`
    * `name`
        * defaultはterraformが生成するunique id
    * `zone`
    * `cluster`
        * `google_container_cluster`のnameを指定
    * `initial_node_count`
    * `autoscaling`
        * `min_node_count`
        * `max_node_count`
    * `management`
        * `auto_repair`
        * `auto_upgrade`
    * `name_prefix`
        * node poolの名前のprefix
    * `node_config`
    * `node_count`
        * number of node per instance group
    * `project`
        * defaultはprovider-configured project

```
resource "google_bigquery_dataset" "default" {
  dataset_id                  = "foo"
  friendly_name               = "test"
  description                 = "This is a test description"
  location                    = "EU"
  default_table_expiration_ms = 3600000

  labels {
    env = "default"
  }
}
```

* `google_bigquery_dataset`
    * `dataset_id`
    * `friendly_name`
    * `description`
        * description of dataset
    * `location`
        * default value is US
        * EU or US
    * `default_table_expiration_ms`
        * tableが削除される時間
        * minimum value が`3600000` msで1hour


```
resource "google_compute_disk" "default" {
  name  = "test-disk"
  type  = "pd-ssd"
  zone  = "us-central1-a"
  image = "debian-8-jessie-v20170523"
  labels {
    environment = "dev"
  }
}
```

* google_compute_disk
    * [Storage Options  |  Compute Engine Documentation  |  Google Cloud Platform](https://cloud.google.com/compute/docs/disks/)
    * type
        * pd-standard
        * pd-ssd
* google_storage_bucket_object
    * GCSにfile uploadできる
    * [Google: google_storage_bucket_object - Terraform by HashiCorp](https://www.terraform.io/docs/providers/google/r/storage_bucket_object.html)

* google_sql_database_instance
    * second generation/first generationがあるがsecondだけ使っていればOK
    * `replica_configuration`
        * `connect_retry_interval`
            * default 60
            * seconds
        * `dump_file_path`
            * e.g. `gs://bucket/filename`
            * Path to a SQL file in GCS from which slave instances are created.
        * `master_heartbeat_period`
            * ms
        * `password`
        * `username`
        * `verify_server_certificate`
    * `settings`
        * `tier`
        * `activation_policy`
        * `crash_safe_replication `
        * `disk_autoresize`
        * `disk_size`
            * default 10GB
            * GB unit
            * Size of a running instance cannot be reduced but can be increased.
        * `disk_type `
            * default PD_SSD
            * PD_HDD, PD_SSD
        * `pricing_plan`
            * PER_USE, PACKAGE
        * `replication_type `
            * ASYNCHRONOUS
            * SYNCHRONOUS
    * `settings.database_flags[]`
        * `name`
            * name of flags
        * `value`
            * value of flags
    * `settings.maintenance_window `
        * UTC time
        * 1 hour maintenance window to update instance if needed.
        * `day`
            * 1-7
            * 1: monday, 7:sunday
            * day of week
        * `hour`
            * 00-23
        * `udpate_track`
            * canary, stable
    * `settings.location_preference`
        * `follow_gae_application`
        * `zone`
            * preferred compute engine zone
    * `settings.ip_configuration.authorized_networks[]`
        * `expiration_time `
            * whitelists expiration time
        * `name`
            * name of this whitelist
        * `value`
            * CIDR for IPv4 or IPv6 address
    * `settings.backup_configuration`
        * `binary_log_enabled`
            * True/False
        * `enabled`
            * True/False
            * backup configuration enabled or not
        * `start_time`
            * HH:MM format time
            * backup configuration start time
    * `settings.database_flags`
    * `settings.ip_configuration`
        * `ipv4_enabled`
            * true/false
            * for second generation this must be true
        * `require_ssl`
            * true -> mysqld default to` REQUIRE X509`
* `google_sql_user` 
    * `name`
        * usernmae
    * `host`
        * 可能なaccess元
        * `%` anyhost
        * documentにsecond generationは指定するなと記載があるが、多分問題ない

`google_kms_key_ring`
KMSのkeyring

`google_kms_crypto_key`
KMSのkeyを作成

`google_kms_crypto_key_iam_binding`
keyに対してIAMを付与

* `crypto_key_id`
* `members`
* `role`

`google_dataproc_cluster`
[Google: google\_dataproc\_cluster \- Terraform by HashiCorp](https://www.terraform.io/docs/providers/google/r/dataproc_cluster.html)

* `name`
* `region`
* `labels`
* `cluster_config`
    * `staging_bucket`
    * `delete_autogen_bucket`
    * `gce_cluster_config`
    * `master_config`
    * `worker_config`
    * `preemptible_worker_config`
    * `software_config`
    * `initialization_action`
* `cluster_config.gce_cluster_config`
    * `zone`
    * `network`
    * `subnetwork`
    * `service_account`
    * `service_account_scopes`
    * `tags`
    * `internal_ip_only`


## Tips

### google_sql_database_instance
[google_sql_database_instance Error 403: The client is not authorized to make this request., notAuthorized · Issue #1069 · terraform-providers/terraform-provider-google](https://github.com/terraform-providers/terraform-provider-google/issues/1069)

以下のように`master_instance_name`があるときは、`master`がいないとだめ。
replicaを作る時にのみ値を設定する。

```
resource "google_sql_database_instance" "replica" {
  name                 = "instance-replica"
  region               = "us-west1"
  project              = "${google_project_service.service.project}"
  master_instance_name = "${google_sql_database_instance.master.name}"

  settings {
    tier = "db-f1-micro"

    availability_type = "ZONAL"
    disk_autoresize = true
    disk_size       = 100
    disk_type       = "PD_SSD"

  }
}
```

## Reference
