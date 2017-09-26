---
title: perf
---

## perf
Pefromance analysis for linux.
macでは使えない。
macでは、`google-perftools`が代替になるかもしれない。

## Install
For Ubuntu

ubuntuのversionごとに`linux-tools-`の接頭辞のついたpackageがある。

```
apt-cahce search 
apt-get install linux-tools-
```

## CLI

perfomanceの計測。
`-o output_filename`を指定しない場合は`perf.data`に出力される。

```
perf record -o otuput_perffile -- execution_file
```

profile結果を見る。
`-i output_perffile`を指定しない場合は、`perf.data`が読み込まれる。

```
perf report -i output_perffile
```

callgraphを出力

```
perf record --call-graph
```

callgraphの結果を閲覧

```
perf report --call-graph -G
```


## Visualize callgraph
* [jrfonseca/gprof2dot: Converts profiling output to a dot graph.](https://github.com/jrfonseca/gprof2dot)

callgrphの可視化は別toolを使う。

```
/path/to/your/executable arg1 arg2
```

## Tips
docker上でperfを使う場合は、dockerはhostのmachineのkernel上で動作する。
perfはkernelごとにinstallするので、hostのkernelと同じperfを入れる必要がある。
docker imageのdistributionによっては、hostのkernelのperfを提供していない場合がある。


## reference
* [perfの使いかた](http://int.main.jp/txt/perf/)
* [perfでプロファイルを実行する - Narrow Escape](https://www.hiroom2.com/2014/08/22/perf%E3%81%A7%E3%83%97%E3%83%AD%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E5%AE%9F%E8%A1%8C%E3%81%99%E3%82%8B/)
