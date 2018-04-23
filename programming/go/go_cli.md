---
title: go CLI
---

## go CLI

## clean
* `-i`
    * delete installed archive/binary
* `-n`
    * cleanのdry-run

## Tips


go getでgetしたものを削除

```
go get github.com/prasmussen/gdrive
```

の場合以下で削除のdry-run.
`-n`を抜けば実行する。

```
go clean -i -n github.com/prasmussen/gdrive
```

## Reference
* [Removing packages installed with go get - Stack Overflow](https://stackoverflow.com/questions/13792254/removing-packages-installed-with-go-get)
