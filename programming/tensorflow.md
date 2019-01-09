---
title: Tensorflow
---

## Tensorflow

## Install

### Ubuntu

GPU setup

下記のlinkからplatformを選んでDLする。
`deb(network)`がおすすめ

* [CUDA Toolkit Download | NVIDIA Developer](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu)

dlしたファイルを適当に配置して以下を実行する。

```
# cuda-repo-ubuntu1604_9.0.176-1_amd64.debがcurrent directoryにある
sudo dpkg -i cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```

```
sudo apt-get install linux-headers-$(uname -r)
```

```
sudo apt-get install libcupti-dev
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev libpng-dev
```

With virtualenv

```
sudo apt-get install python3-pip python3-dev python-virtualenv 
```

With pyenv

```
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
pyenv install anaconda3-5.0.1
```

```
# CPU only
pip install --ignore-installed --upgrade \
 https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.0-cp34-cp34m-linux_x86_64.whl
# GPU
pip install --ignore-installed --upgrade \
 https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.0-cp36-cp36m-linux_x86_64.whl
```

```
# python 3.4
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.0-cp34-cp34m-linux_x86_64.whl
# python 3.5
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.0-cp35-cp35m-linux_x86_64.whl
# python 3.6
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.0-cp36-cp36m-linux_x86_64.whl
```


## Nvidia docker

```
docker run --rm -it gcr.io/tensorflow/tensorflow:latest-gpu bash
````

## Tutorials

#### using CIFAR 10
* [Advanced Convolutional Neural Networks  \|  TensorFlow](https://www.tensorflow.org/tutorials/images/deep_cnn)
* [models/tutorials/image/cifar10 at master · tensorflow/models](https://github.com/tensorflow/models/tree/master/tutorials/image/cifar10/)




## Reference
* [Installing TensorFlow  |  TensorFlow](https://www.tensorflow.org/install/)
