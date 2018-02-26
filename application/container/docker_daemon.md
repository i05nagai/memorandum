---
title: Docker Daemon
---

## Docker Daemon

* 2375をunencryptに使う
* 2376をencrypyptに使う
* `--tlsverify`

```
sudo dockerd -H unix:///var/run/docker.sock -H tcp://192.168.59.106 -H tcp://10.10.10.2
```

## docker in docker


```
docker run \
    --rm
```

## Reference
* [dockerd | Docker Documentation](https://docs.docker.com/engine/reference/commandline/dockerd/)
