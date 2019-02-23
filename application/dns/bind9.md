---
title: BIND 9
---

## BIND 9

```
apt-get -y install bind9 bind9utils
```

## CLI
Run nameserver.
nameserverのerrorは`syslog` daemonに送られるので、`syslog` daemonがが起動していることを確認する。
syslogのdaemon facilityにlogが出力される。

```
named
```

name daemonのreload

```
ndc reload
```

`rndc.conf`の雛形作成

```
rndc-confgen > /etc/rndc.conf
```

```
rndc [-b address] [-c config] [-s server] [-p port] [-k key-file ] [-y key] [-V] command
```

* server
    * nameserver

## Configuration

`/etc/bind/named.conf`


### options

```
options { 
        directory "/var/lib/named"; 
        forwarders { 10.0.0.1; };
        notify no;
};
```

* `directory`
    * path to zone file
    * defautl `/var/lib/named`
* `forwarders { ip }`
    * DSN requsestが解決できない場合にfowardする先
    * 基本的にはproviderのname sever
* `foward first`
    * root name severでDNS requestを解決する前に転送する
* `listen-on port 53 { 127.0.0.1; ip-address; }`
    * 
* `allow-transfer ! *;;`
    * zone 転送を許可しない
* `notify no;`
    * 他のDNSにzone dataを変更したとき、name severが再起動した時伝えない

### logging

```
logging {
        category default { null; };
};
```

### zone

```
zone "my-domain.de" in {
      type master;
      file "my-domain.zone";
      notify no;
};
```

* `type [slave|master|hint]`
* `file my-domain.zone`
    * zone dataが格納されてるfile
* `masters { server-ip-address; };`
    * 

## zone file
以下の順番で記載する。

* SOA records
    * authority for this zone
* NS records
    * list a nameserver for this zone
* Other records
    * data about hosts

```
$TTL 2D
world.cosmos. IN SOA      gateway  root.world.cosmos. (
            2003072441  ; serial
            1D          ; refresh
            2H          ; retry
            1W          ; expiry
            2D )        ; minimum

            IN NS       gateway
            IN MX       10 sun

gateway     IN A        192.168.0.1
            IN A        192.168.1.1
sun         IN A        192.168.0.2
moon        IN A        192.168.0.3
earth       IN A        192.168.1.2
mars        IN A        192.168.1.3
www         IN CNAME    moon
```

* `$TTL 2D`
    * defaultの寿命
* SOA records
    * start of authority record
    * `world.cosmos.`
        * domain nameがprimary nameserverと同じ場合は、`@`で良い
    * `gateway`
        * primary nameserver
        * 末尾に`.`がついてないので、`gateway.world.cosmos.`となる
    * `root.world.cosmos`
        * name serverの管理者のmail address
        * `root@world.cosmos`
            * `@`は特別な意味をもつので、`.`を使う
    * `2003072441  ; serial`
        * 他のname serverに更新を知らせる場合に使うID
        * 慣習的に`YYYYMMDDNN`の形式が使われる
            * `NN`は実行番号で、同じ日付に更新する際にcountを増やす
    * `1D          ; refresh`
        * refresh rate
        * secondary name serverがzone serial numberを確認する時間間隔
    * `2H          ; retry`
        * retry
        * errorが起きたときにsecondary name severがprimary name serverに再度通知する時間
    * `1W          ; expiry`
        * secondary name serverがprimary serverに再通知できなかった場合にcacheしたdataを廃棄するまでの時間
    * `2D )        ; minimum`
        * negative cache TTL
        * DNS queryが解決できないという他のserverからの結果を保持しておく
* NS records
    * NameServer records
    * `IN NS       gateway`
        * domainの担当するnameserver
        * `gateway.world.cosmos.`
        * `notify no`にしないとzonefileの変更時にここで指定したnameserverに通知される
* MX records
    * `IN MX       10 sun`
    * `10`はpreference value
        * 小さいものが選ばれる
    * `sun.world.cosmos.`
* A records
    * addres/alias records
    * name to address maping
    * `gateway     IN A        192.168.0.1`
        * `gateway.world.cosmos.`を`192.168.0.1`に対応させる
        * 2つ以上のaddressを返すことができる
        * Round robinでqueryに対して交互にadressを返すか
        * address sortingで最も近いaddressを返す
* CNAME records
    * canonical name records
    * CNAME recordsを見つけた場合は、CNAMEの名前に置き換えてqueryの検索を続ける
    * `www         IN CNAME    moon`
* SRV records
    * service: the symbolic name of the desired service.
    * proto: the transport protocol of the desired service; this is usually either TCP or UDP.
    * name: the domain name for which this record is valid, ending in a dot.
    * TTL: standard DNS time to live field.
    * class: standard DNS class field (this is always IN).
    * priority: the priority of the target host, lower value means more preferred.
    * weight: A relative weight for records with the same priority, higher value means more preferred.
    * port: the TCP or UDP port on which the service is to be found.
    * target: the canonical hostname of the machine providing the service, ending in a dot.

```
_service._proto.name. TTL class SRV priority weight port target.
```

example

```
_sip._tcp.example.com. 86400 IN SRV 0 5 5060 sipserver.example.com.
```

```
$TTL 2D
1.168.192.in-addr.arpa. IN SOA gateway.world.cosmos. root.world.cosmos. (
                        2003072441      ; serial
                        1D              ; refresh
                        2H              ; retry
                        1W              ; expiry
                        2D )            ; minimum

                        IN NS           gateway.world.cosmos.

1                       IN PTR          gateway.world.cosmos.
2                       IN PTR          earth.world.cosmos.
3                       IN PTR          mars.world.cosmos.
```

* `db.192.249.249`
    * 192.249.249/24のaddressからnameのmapping
    * filename
* PTR records
    * pointer records
    * address to name mapping
    * `1 IN PTR gateway.world.cosmos.`
        * `192.168.1.1`のmapping


```
$TTL 3h
0.0.127.in-addr.arpa. IN SOA toystory.movie.edu. al.movie.edu. (
    1   ; Serial
    3h  ; refresh
    1h  ; retry
    1w  ; expire
    1h ) ; negative cashing TTL
0.0.127.in-addr.arpa. IN NS toystory.movie.edu.
0.0.127.in-addr.arpa. IN NS wormhole.movie.edu.

1.0.0.127.in-appr.arpa. IN PTR localhost.
```

* `db.ADDR` file
    * loopback network
    * nameserverで必要

## Tools

```
named-checkconf
```

引数を省略すると`/etc/named.conf`の文法をcheckする。

```
name-checkzone zonename filename
```

## resolver
`/etc/resolve.conf`でresolverの設定ができる。

[Man page of RESOLV.CONF](http://linuxjm.osdn.jp/html/LDP_man-pages/man5/resolv.conf.5.html)


```
nameserver ip_address
```

nameerverがloaclで動いていないときは、問い合わせるDNSの設定が必要なので、ここで設定できる。
listされた順に問い合わせをする。
nameserverが設定されていない場合は、localmachineのnameserverに問い合わせる。

```
domain local_domain_name
```

local domain nameはroot domainを省略した場合のdefault domainとして利用される。

```
search domain1 domain2 domain3
```

CLIなどでroot domain `.`を省略した場合に補完するdomainのlist
defaultではlocal domainが使われる。


## Reference
* [BIND 9 Documentation | Internet Systems Consortium](https://www.isc.org/downloads/bind/doc/)
* [Dockerコンテナ上にdns環境を構築する - Qiita](https://qiita.com/hakaicode/items/478ba39055c101d6197d)
* [GitHub - sameersbn/docker-bind: Dockerize BIND DNS server with webmin for DNS administration](https://github.com/sameersbn/docker-bind)
* [第33章 ドメインネームシステム](https://www.suse.com/ja-jp/documentation/sles10/book_sle_reference/data/cha.dns.html)
* [33.4. 設定ファイル/etc/named.conf](https://www.suse.com/ja-jp/documentation/sles10/book_sle_reference/data/sec.dns.named.html)
