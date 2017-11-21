---
title: Docker CE
---

## Docker CE
Docker Community Edition.

## Install

### Ubuntu
* xenial 16.04 or higher

```
sudo apt-get remove docker docker-engine docker.io
```

```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo apt-get update
sudo apt-get install docker-ce
```

もしくはInstall用のscriptがある

```
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## Reference
