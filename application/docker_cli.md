---
title: Docker CLI
---

## Docker CLI
docker clinet.


## docker build
buildのterminalのlogは`/root/build.log`に記録される。
標準error出力に出力すれば、docker-buildの画面にも表示される。
pythonのloggingなどは、stderrに出力するので、python scriptの経過を表示したい場合は、loggingで良い。

```
docker build -t <image>:<tag> /path/to/Dockerfile
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

## docker hisotry
imageの各layerの容量などを表示する。

```
docker history <image-name>
```

## Reference
