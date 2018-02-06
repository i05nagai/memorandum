---
title: Docker CLI
---

## Docker CLI
docker clinet.


## docker build

```
docker buidl -t <image>:<tag> /path/to/Dockerfile
```

dockerfileは1 commandごとにhistoryが作成される。
historyはgitのcommit logと同じなので、imageの容量増加の要因となる。
`--squash`をつけると過去のhistoryをsquashできる。

```
docker build -t <image>:latest /path/to/Dockerfile
docker build --squash -t <image>:latest-postsquash /path/to/Dockerfile
```

2回目のsquashつきのbuildはcacheがあるので、一瞬で終わる。
最初に作ったもののhistoryはsquashされない。
release時にだけsquashをつけるようにしても良い。

## Reference
