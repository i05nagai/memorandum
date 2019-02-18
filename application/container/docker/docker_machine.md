---
title: docker-machine
---

## docker-machine


##

```
docker-machine ls
docker-machine create --driver virtualbox default
docker-machine env default
docker-machine ip default

docker-machine create -d "virtualbox" --virtualbox-disk-size=50000 default

docker-machine stop default
docker-machine start default
```

## Reference
* https://docs.docker.com/machine/get-started/
