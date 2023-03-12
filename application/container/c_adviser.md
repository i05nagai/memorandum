---
title: cAdviser
---

## cAdviser
Analyzes resource usage and performance characteristics of running containers.
It's integrated in Kubelet.

## Quickstart

```
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:latest
```

Access via `http://localhost:8080`

## metrics
- working set memory
    - The amount of working set memory, this includes recently accessed memory,dirty memory, and kernel memory. Working set is `<= "usage"`.
- container_memory
    - The amount of anonymous and swap cache memory (includes transparent hugepages).

## Monitoring
https://github.com/google/cadvisor/blob/master/docs/storage/prometheus.md

## Reference
* [google/cadvisor: Analyzes resource usage and performance characteristics of running containers.](https://github.com/google/cadvisor)
