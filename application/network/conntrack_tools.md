---
title: conntrack-tools
---

## conntrack-tools

```
apt-get install conntrack
```


## CLI
* [Ubuntu Manpage: conntrack - command line interface for netfilter connection tracking](http://manpages.ubuntu.com/manpages/trusty/man8/conntrack.8.html)

```
conntrack -L
```

You can natively filter the output without using grep

```
 conntrack -L -p tcp --dport 34856
```

Output as XML

```
conntrack -L -o xml
```

* `-L`, `--dump`
    * コネクションの表示
* `-F`, `--flush`
    * ーブルをFlush
* `--event`, `-E`
    * eventを表示
* `-C`, `--count`
    * エントリー数表示
* -S, `--stats`
    * 統計


## Reference
* [The conntrack-tools user manual](http://conntrack-tools.netfilter.org/manual.html)
* [conntrackコマンドの使い方 - Qiita](https://qiita.com/hana_shin/items/a3b02729d96ef09ffc35)
