---
title: iptables
---

## iptables
Linux kernel 2.4から標準でinstallされているfirewall.
packet filtering type firewall.

* Chain
    * chainは1つ以上のrule/chainをもつ
* rules
    * ruleは処理の実行単位
    * target, prot, source, destinationとoptionでどのような処理をするかを記述する

## Install
For ubuntu,

```
sudo apt-get install iptables
```

## CLI
listで見るときは、`-v`, `-n`をつける。

Commands

```
iptables -[LS] [chain [rulenum]] [options]
iptables -[FZ] [chain] [options]
iptables -[NX] chain
iptables -E old-chain-name new-chain-name
iptables -P chain target [options]
iptables -h (print this help information)
```

Options

* `--ipv6 -6`
    * Error (line is ignored by iptables-restore)
* `--protocol -p proto`
    protocol: by number or name, eg. `tcp`
* `--source -s address[/mask][...]`
    * source specification
* `--destination -d address[/mask][...]`
    * destination specification
* `--in-interface -i input name[+]`
    * network interface name ([+] for wildcard)
* `--jump -j target`
    * target for rule (may load target extension)
* `--goto      -g chain`
    * jump to chain with no return
* `--match -m match`
    *  extended match (may load extension)
* `--numeric, -n numeric`
    * output of addresses and ports
* `--out-interface -o output name[+]`
    * network interface name ([+] for wildcard)
* `--table	-t table`
    * table to manipulate (default: `filter`)
* `--verbose -v`
* `--wait -w`
    * wait for the xtables lock
* `--line-numbers`
    * print line numbers when listing
* `--exact -x`
    * expand numbers (display exact values)
* `--fragment -f`
    * match second or further fragments only
* `--modprobe=<command>`
    * try to insert modules using this command
* `--set-counters PKTS BYTES`
    * set the counter during insert/append

COMMANDS

* `--replace -R`
    * Replace rule rulenum (1 = first) in chain
    * `--replace -R chain rulenum`
    * `iptables -R chain rulenum rule-specification [options]`
* `--append, -A`
* `--check, -C`
    * check for the existence of a rule
* `--policy, -P`
    * `--policy  -P chain target`
    *  Change policy on chain to target
* `--delete, -D`
    * `iptables -D chain rulenum [options]`
    * Delete matching rule from chain
    * `iptables -[ACD] chain rule-specification [options]`
    * `--delete  -D chain rulenum`
        * Delete rule rulenum (1 = first) from chain
* `--insert, -I`
    * Insert in chain as rulenum (default 1=first)
    * `--insert  -I chain [rulenum]`
    * `iptables -I chain [rulenum] rule-specification [options]`
* `--list -L`
    * List the rules in a chain or all chains
    * `--list    -L [chain [rulenum]]`
* `--list-rules, -S`
    * Print the rules in a chain or all chains
    * `--list-rules -S [chain [rulenum]]`
* `--flush -F`
    * Delete all rules in  chain or all chains
    * `--flush   -F [chain]`
* `--zero, -Z`
    * Zero counters in chain or all chains
    * `--zero    -Z [chain [rulenum]]`
* `--new, -N`
    * `--new     -N chain`
    * Create a new user-defined chain
* `--delete-chain, -X [chain]`
    * Delete a user-defined chain
* `--rename-chain`
* `-E old-chain new-chain`
    * Change chain name, (moving any references)

```
iptables [-t tables] command [match] [target/jump]
```

tcp接続の受信データを破棄するというルールを追加する

```
iptables --append INPUT --protocol tcp --jump DROP
```

tableの種類

* filter
    * packetの通過や遮断の制御
    * よく使う
    * tableを指定しない場合はこのtbaleに追加される

filterにport 80のpacketを破棄するruleを追加。

```
iptables -t filter -p tcp --dport 80 -j -DROP
```

* nat
    * NATの設定

```
iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -j MASQUERADE
```

eth0のport80のTCP packetをlocalの172.31.0.1:80へfowardingする。

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to 172.31.0.1:80
```

* mangle
    * Type of Serviceの値を書き換える
    * TOSはpacket 処理の優先度付を行う

port 80のTOSを高Throughputのものにする。

```
iptables -t mangle -A PREROUTING -p tcp --dport 80 -j TOS --set-tos Maximize-Throughput
```

* raw
    * 追跡を除外するように特定のpacketにmarkをつける
    * 特定の通信をfirewallで処理せずにforwarding/routingする
    * 例えば、通信が1秒間に数千といった高負荷の場合、原因のpacketのい別serverで処理させたい
        * 原因のpacketがDNSへの問い合わせのとき、`53`の通信にNOTRACK markをつける

```
iptables -t raw -I PREROUTING -p udp --dport 53 -j NOTRACK
iptables -t raw -I OUTPUT -p udp --dport 53 -j NOTRACK
```

## Rules
* [IptablesHowTo - Community Help Wiki](https://help.ubuntu.com/community/IptablesHowTo)
* [Man page of IPTABLES](http://ipset.netfilter.org/iptables.man.html)
* Chain
    * INPUT
    * OUTPUT
    * POSTROUTING
* TARGET
    * ACCEPT
        * let packet through
    * DROP
        * drop the packet
    * QUEUE
        * pass the packet to userspace
    * RETURN
        * stop traversing this chain
        * 一つ前のchainの呼び出し元から再開
    * MASQUERADE
        * [Masquerading Made Simple HOWTO](https://www.tldp.org/HOWTO/html_single/Masquerading-Simple-HOWTO/)
        * [MASQUERADE target](https://www.frozentux.net/iptables-tutorial/chunkyhtml/x4422.html)
        * `--to-ports` outgoing packetのsourceになる
    * SNAT
        * [SNAT target](https://www.frozentux.net/iptables-tutorial/chunkyhtml/x4679.html)
        * Source Network Adress Translation

```
sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination
ACCEPT     all  --  anywhere             anywhere            state RELATED,ESTABLISHED
ACCEPT     tcp  --  anywhere             anywhere            tcp dpt:ssh
```


## Configuration
`/etc/sysconfig/iptables`にある。

```
*filter
 # filter settings
COMMIT
```

```
*nat
 # nat settings
COMMIT
```

```
*mangle
 # mangle setting
COMMIT
```

```
*raw
 #ここにraw関係の記述
COMMIT
```

## NAT
* [NAT with Linux and iptables - Tutorial (Introduction)](https://www.karlrupp.net/en/computer/nat_tutorial)
* [HowTos/Network/IPTables - CentOS Wiki](https://wiki.centos.org/HowTos/Network/IPTables)
* `prot`
    * protocol
* `target`
    * ACCEPT
* `opt`
* `source`
* `destination`


```
iptables -t nat -L -n -v
```

```
# iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination
ACCEPT     all  --  anywhere             anywhere            state RELATED,ESTABLISHED 
ACCEPT     icmp --  anywhere             anywhere
ACCEPT     all  --  anywhere             anywhere
ACCEPT     tcp  --  anywhere             anywhere            state NEW tcp dpt:ssh 
REJECT     all  --  anywhere             anywhere            reject-with icmp-host-prohibited 

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination
REJECT     all  --  anywhere             anywhere            reject-with icmp-host-prohibited 

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```


## Reference
* [コピペから脱出！iptablesの仕組みを理解して環境に合わせた設定をしよう | OXY NOTES](http://oxynotes.com/?p=6361)
* [netfilterを利用したDSP監視](https://www.slideshare.net/kazuhitoohkawa/netfilter
