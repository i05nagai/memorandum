---
title: Google Cloud Compute Engine
---

## Google Cloud Compute Engine

## SSH key
https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys

* Compute Engine automatically creates and manages SSH keys for you when you connect to instances using SSH from the Browser or the gcloud comand-line tool
* If you are an advanced user who needs to manage SSH keys manually, manage instance access using OS Login.

```
gcloud compute --project "project-name" ssh --zone "us-east1-b" "instance-name" --ssh-flag="-v"
```

this generats private key in `~/.ssh/google_compute_engine` and public key in `~/.ssh/google_compute_engine.pub`.

## Adding storage

```
sudo mkdir -p /mnt/disks/[MNT_DIR]
sudo mount -o discard,defaults /dev/[DEVICE_ID] /mnt/disks/[MNT_DIR]
sudo chmod a+w /mnt/disks/[MNT_DIR]
echo UUID=`sudo blkid -s UUID -o value /dev/sdb` /mnt/disks/disk-1 ext4 discard,defaults,nofail 0 2 | sudo tee -a /etc/fstab
```

## Preemptible VM Instaces
* [Preemptible VM Instances  |  Compute Engine Documentation  |  Google Cloud](https://cloud.google.com/compute/docs/instances/preemptible?hl=en_US&_ga=2.13732919.-1205531873.1513079066#preemptible_with_instance_groups)

* system eventでいつでも停止される
* system eventによる停止の確率は通常低いが、day to day, zone to zoneで違う
* 24 hoursで停止
* resourceに限りがあるので、常に利用可能なわけではない
* live migrate, maintenance eventでのautomatically restartはない
* Google Compute Engine SLAで保証されてない

Preemption process

1.`ACPI G2 Soft Off` signalが送信される
    * [Advanced Configuration and Power Interface - Wikipedia](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states)
    * [Creating and Starting a Preemptible VM Instance  |  Compute Engine Documentation  |  Google Cloud](https://cloud.google.com/compute/docs/instances/create-start-preemptible-instance#handle_preemption)
2. 30sec停止しない場合は、` ACPI G3 Mechanical Off` signalがOSに送られる
    * [Advanced Configuration and Power Interface - Wikipedia](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states)
3. TERMINATED stateに移行する

## Quotas
* [Regions and Zones  |  Compute Engine Documentation  |  Google Cloud](https://cloud.google.com/compute/docs/regions-zones/#quotas)
* [Resource Quotas  |  Compute Engine Documentation  |  Google Cloud](https://cloud.google.com/compute/quotas)


* region, globalごとの使えるCPUやmemoryの数に制限がある。
* GCPのQuotasのpageで確認可能。
* Quotasは変更可能だが、 `Owner, Editor, and Quota Administrator`のRoleがついている必要がある。
    * permissionとしては、 `serviceusage.quotas.update`

## Reference
