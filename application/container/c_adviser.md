---
title: cAdviser
---

## cAdviser
Analyzes resource usage and performance characteristics of running containers.
Kubeletに組み込まれている。

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

`http://localhost:8080`で動く。

## Monitoring
https://github.com/google/cadvisor/blob/master/docs/storage/prometheus.md

## Reference
* [google/cadvisor: Analyzes resource usage and performance characteristics of running containers.](https://github.com/google/cadvisor)
