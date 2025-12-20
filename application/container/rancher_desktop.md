---
title: Rancher Desktop
---

## Rancher Desktop


## Recreate VM
https://github.com/rancher-sandbox/rancher-desktop/issues/1521

Stop Rancvher Desktop.

Run

```
rm -rf ~/Library/Application\ Support/rancher-desktop/lima/0
```

## Configuraiton

On OSX,

```
~/Library/Application\ Support/rancher-desktop/lima/_config/override.yaml
```

## amd64 build for golang
https://github.com/rancher-sandbox/rancher-desktop/issues/8606

```
fatal error: lfstack.push
```

```
docker run --privileged --rm tonistiigi/binfmt:qemu-v7.0.0 --uninstall amd64
docker run --privileged --rm tonistiigi/binfmt:qemu-v7.0.0 --install amd64
```



## Reference
- https://github.com/rancher-sandbox/rancher-desktop/issues/1521
