---
title: Terraform Resource
---

## Terraform Resource
Providerが提供しているResourceの設定について記載

## AWS Provider
* [Provider: AWS - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/index.html)

Resource

* `aws_instance`
    * `ami`
    * `availability_zone`
    * `disable_api_termination`
        * trueだとEC2 Instance Termination Protectionをenableにする
        * trueだとprotectionをつける
    * `instance_type`
    * `key_name`
    * `vpc_security_group_ids`
    * `subnet_id`
    * `associate_public_ip_address`
        * trueだとPublic IPに関連付ける
    * `tags`
    * `volume_tags`
    * `root_block_device`
    * `ebs_block_device`
    * `tags`
        * tagつける
    * `volume_tags`
        * volumeにtagをつける
* `aws_db_instance`
    * `identifier`
    * `allocated_storage`
        * storageの容量をGBで指定
    * `storage_type`
    * `engine`
    * `engine_version`
    * `name`
        * DB名、省略するとDBを作らない
    * `password`
        * master DB userのpassword
        * logとstate fileに記録される可能性がある
    * `username`
        * master DB userのusername
    * `skip_final_snapshot`
        * RDS terminate時にDBのsnapshotを保存するかを指定
        * defaultはfalse
        * falseの場合は`final_snapshot_identifier`を指定する必要がある
    * `final_snapshot_identifier`
        * `final_snapshot`時のsnapshotの名前
    * `tags`
        * tagを記載
    * `copy_tags_to_snapshot`
        * snapshotにtagをcopy
        * `final_snapshot_identifier`を指定している必要がある
* `aws_eip`
    * [AWS: aws_eip - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/r/eip.html)
    * Elastic IPを作成する
    * `vpc`
        * EIPがVPCの中ならtrue
    * `instance`
        * EIPを割り当てるEC2 instance ID

```
$ terraform import aws_eip.bar eipalloc-00a10e96
```

* `aws_eip_association`
    * [AWS: aws_eip_association - Terraform by HashiCorp](https://www.terraform.io/docs/providers/aws/r/eip_association.html)
    * 取得したElasticp IPをEC2 instanceと割り当てるときに使う
    * `aws_eip` resourceと一緒に使うことが多い
    * `instance_id`
    * `allocation_id`

## Google Cloud Provider
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


    * `description`
        * clusterの説明
    * `logging_service`
        * noneか`logging.googleapis.com`
        * defaultは`logging.googleapis.com`
    * `maintenance_policy `

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



## Terraform
* `backend`
    * remote stateのbackend
    * `gcp`
        * `bucket`
            * bucket名
        * `credentials`
        * `prefix`
            * remote stateの保存先
            * `<prefix>/<name>.tfstate`のfileが作られる
        * `path`
        * `project`
        * `region`
        * `encryption_key`
            * stateのencryptionのための32 byte base64 encoded key

## Reference
