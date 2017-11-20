---
title: nvidia-docker
---

## nvidia-docker


## Install

### Xenial

```
# Add the package repositories
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/ubuntu16.04/amd64/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update

# Install nvidia-docker2 and reload the Docker daemon configuration
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd

# Test nvidia-smi with the latest official CUDA image
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```

nvidia-dcoker2は`docker-ce`の` 17.09.0~ce-0~ubuntu`に依存している。
普通にいれると`17.10`が入るので、以下のコマンドで自分でいれる。

```
sudo apt-get install docker-ce=17.09.0~ce-0~ubuntu
```



## Reference
* [GitHub - NVIDIA/nvidia-docker: Build and run Docker containers leveraging NVIDIA GPUs](https://github.com/NVIDIA/nvidia-docker)

