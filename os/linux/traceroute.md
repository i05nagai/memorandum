---
title: traceroute
---

## traceroute

```
traceroute [OPTION...] HOST
```

* `-f, --first-hop=NUM`
    * set initial hop distance, i.e., time-to-live
* `-g, --gateways=GATES`
    * list of gateways for loose source routing
* `-I, --icmp`
    * use ICMP ECHO as probe
* `-m, --max-hop=NUM`
    * set maximal hop count (default: 64)
* `-M, --type=METHOD`
    * use METHOD (icmp or udp) for traceroute
    * operations, defaulting to udp
* `-p, --port=PORT`
    * use destination PORT port (default: 33434)
* `-q, --tries=NUM`
    * send NUM probe packets per hop (default: 3)
* `--resolve-hostnames`
    * resolve hostnames
* `-t, --tos=NUM`
    * set type of service (TOS) to NUM
* `-w, --wait=NUM`
    * wait NUM seconds for response (default: 3)

## Reference
* [traceroute(8) - Linux man page](https://linux.die.net/man/8/traceroute)
* [経路調査ツール【traceroute/tracert 】の仕組み、使い方 〜WindowsとLinuxでの違い、利用プロトコル、経路途中のIPが表示されない、アスタリスクの意味〜 | SEの道標](http://milestone-of-se.nesuke.com/nw-basic/ip/traceroute/)
