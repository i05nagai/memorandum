---
title: Bind
---

## Bind

## named.conf
`/etc/named.conf`にある。

```
acl "name" {
    ip address/network
};
```

```conf
options { 
     version “unknown”;
     hostname “somehost.some.domain”;
     directory “/var/named/”; 
     dump-file “/var/named/data/cache_dump.db”; 
     statistics-file “/var/named/data/named_stats.txt”; 
     pid-file “/var/run/named/named.pid”;
     //
     listen-on port 53 {
         127.0.0.1;
         192.168.0.2;
     };
    auth-nxdomain yes;;
     // Zone transfer specifications
     notify no;
    max-transfer-time-in 60;
    transfer-format many-answers; 
    transfers-in 10; 
    transfers-per-ns 2;
    //
    allow-transfer { none; };
    allow-query-cache { internalnet; localhost; };
    allow-query { internalnet; localhost; };
    // 
    recursion yes;
    allow-recursion { localnets; localhost; internalnet; };
};
```

* `version`
    * versionは知られないように`UNKOWN`, `GUESS`など返す
* `directory`
    * `/var/named`が一般的
* `dump-file`
    * `rndc`でdumpしたときのdump先のfile path
* `pid-file`
    * DNS processのpid
* `listen-on port`
    * DNSにaccess可能なPortとIP addres
* `notify`
    * `yes/no`
    * zone dataに更新があった際に更新を指定されたslave serverに伝えるか
* `max-transfer-time-in`
    * inbound zone transferのtimeout
    * defaultは120 sec
    * secで指定
* `allow-transfer`
    * zone 転送を許可するremote server
* `allow-query-cache`
    * cache dataに対するDNS queryを許可するremote host

## Terms
* `Start Of Authority`
    * domainがzoneで分割されtreeで管理されている
    * SOAではzoneの権限を指定する

## Reference
* [Dockerコンテナ上にdns環境を構築する - Qiita](https://qiita.com/hakaicode/items/478ba39055c101d6197d)
* [強いBIND DNSサーバを構築する　第二回　named.confの基本設定 | ユーロテック情報システム販売株式会社](http://www.eis.co.jp/bind9_src_build_2/)
