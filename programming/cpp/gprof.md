---
title: gprof
---

## gprof
gccのprofiler。

## Usage
gccで`-pg`optionを使ってbuildする。

```
g++ -pg file.cc
```

できたexecファイルを実行すると、`gmon.out`というファイルがexec fileと同じdirectoryにできる。

```
gprof /path/to/exec /path/to/gmon.out
```

を指定すると、関数ごとのprofile結果が出力される。

## Visualize callgraph
* [jrfonseca/gprof2dot: Converts profiling output to a dot graph.](https://github.com/jrfonseca/gprof2dot)

callgrphの可視化は別toolを使う。

```
/path/to/your/executable arg1 arg2
gprof path/to/your/executable | gprof2dot.py | dot -Tpng -o output.png
```

## Reference
* [gprofを使いこなす - minus9d's diary](http://minus9d.hatenablog.com/entry/20140112/1389502918)
