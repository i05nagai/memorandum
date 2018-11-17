---
title: Cloud Dataflow
---

## Cloud Dataflow

## Deploying a pipeline
[Deploying a Pipeline  \|  Cloud Dataflow Documentation  \|  Google Cloud](https://cloud.google.com/dataflow/service/dataflow-service-desc)


* Execute apache beam code
* Construct execution graph
* the execution graph is translated into JSON
* JSON execution graph is transmitted to Cloud Dataflow
* Cloud Dataflow Validate JSON execution graph


* The Cloud Dataflow service gurantee
    * every element in your input PCollection is processed by a DoFn instance excactly once
* The Cloud Dataflow service does not gurantee
    * how many times a DoFn will be invoked
    * how the distributed elements are grouped
    * the exact number of DoFn instances that will be created over the course of a pipeline



* `--worker_machine_type`
* persistent disk
    * limited to
        * 15 persistent disks per worker instance
    * by default
        * 250 GB in batch mode
        * 400 GB in streaming mode
* location
    * by default
        * `us-central1-f` zone of the `us-central1` region
    * `--region`, `--zone`


Streaming Engine

* benefits
    * a reduction in comsumed CPU, memory, and Persistent Disk,
    * more rsponsive autoscaling
    * improved supportability, since you don't need to redeploy your pipeline


* Apache beam
    * construct pipeline
* pipeline runner
    * reads JSON execution graph and executes it


## Python SDK
* [SDK and Worker Dependencies  \|  Cloud Dataflow Documentation  \|  Google Cloud](https://cloud.google.com/dataflow/docs/concepts/sdk-worker-dependencies#sdk-for-python)



## Pricing

Pricing in lowa

* WorkerはGCE baseだが、GCEの料金はかからない
* Batch
    * worker defaults
        * 1 vCPU, 3.75GB memory, 250GB Persistent Disk.
* Streaming
    * worker defaults
        * 4 vCPU, 15GB memory, 420GB Pesistent Disk.

| Worker Type | vCPU(per Hour) | Mem(per GB per Hour) | Local PD (per GB per Hour) | Local SSD (per GB per Hour) | Dataflow Shuffle (per GB per Hour) |
+=============|================|======================|============================|=============================|====================================+
| Batch       | 0.056USD       | 0.003557USD          | 0.000054USD                | 0.000298USD                 | 0.0216USD                          |
| Streaming   | 0.069USD       | 0.003557USD          | 0.000054USD                | 0.000298USD                 | N/A                                |

**Example**

1hour, 1worker, no shuffle, Batch

1 * 0.56 + 3.75 * 0.003557 + 250 * 0.000054 = 0.58683875 USD

1hour 1worker, shuffle, Batch

0.58683875 + 0.0216 = 0.60843875 USD

## Reference
* [Google Cloud Dataflow で Google BigQuery へストリーミング ETL するの巻 - おくみん公式ブログ](http://blog.okumin.com/entry/2017/08/20/201901)
