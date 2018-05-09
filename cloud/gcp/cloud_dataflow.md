---
title: Cloud Dataflow
---

## Cloud Dataflow

## Pricing

lowaのPricing

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

1時間 1worker shuffleなし Batch

1 * 0.56 + 3.75 * 0.003557 + 250 * 0.000054 = 0.58683875 USD

1時間 1worker shuffleあり Batch

0.58683875 + 0.0216 = 0.60843875 USD


## Reference
* [Google Cloud Dataflow で Google BigQuery へストリーミング ETL するの巻 - おくみん公式ブログ](http://blog.okumin.com/entry/2017/08/20/201901)
