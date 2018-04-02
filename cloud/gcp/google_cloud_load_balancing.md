---
title: Google Cloud Load Balancing
---

## Google Cloud Load Balancing


## L7 load balancer
L7 load balancerはHealth checkを使う。
IP Range

```
$ gcloud compute firewall-rules create allow-130-211-0-0-22 \
  --source-ranges 130.211.0.0/22,35.191.0.0/16 \
  --target-tags $TAG \
  --allow tcp:$NODE_PORT
```

現状firewallは適用できない。

* [google cloud platform - Apply firewall rules to an HTTP load balancer - Server Fault](https://serverfault.com/questions/810506/apply-firewall-rules-to-an-http-load-balancer)
* https://issuetracker.google.com/issues/35904903
    * feature request


## Reference
* [Load Balancing  |  Compute Engine Documentation  |  Google Cloud Platform](https://cloud.google.com/compute/docs/load-balancing/)
