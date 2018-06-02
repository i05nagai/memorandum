---
title: nvidia driver
---

## nvidia driver

## Install
* [Install NVIDIA Driver and CUDA on Ubuntu / CentOS / Fedora Linux OS](https://gist.github.com/wangruohui/df039f0dc434d6486f5d4d098aa52d07)

```
sudo add-apt-repository ppa:graphics-drivers
sudo apt-get update
sudo apt-get install nvidia-xxx
```

where `nvidia-xxx` is the latest package whici is availabled in repository.
You need to restart your computer.

## Supported devices
* [NVIDIA DRIVERS Linux 64bit Ubuntu 14\.04](http://www.nvidia.com/download/driverResults.aspx/124091/en-us)
* [NVIDIA DRIVERS Linux x64 \(AMD64/EM64T\) Display Driver](http://www.nvidia.com/Download/driverResults.aspx/106780/en-us)
    * 367
* [NVIDIA DRIVERS Quadro Desktop Driver Release 375 WHQL](http://www.nvidia.com/download/driverResults.aspx/120238/en-us)
    * 375
* [NVIDIA DRIVERS Quadro Desktop Driver Release 384 WHQL](http://www.nvidia.com/download/driverResults.aspx/123335/en-us)
    * 384
* [Download Drivers \| NVIDIA](http://www.nvidia.com/Download/index.aspx?lang=en-us)
    * you can search the driver for the specific graphic board

Older package is a packageはTransional package to higher version so that you just need to install the latest package.

```
apt-cache search nvidia
```



## Reference
* [\[How To\] Install Latest NVIDIA Drivers In Linux](http://www.linuxandubuntu.com/home/how-to-install-latest-nvidia-drivers-in-linux)
