---
title: iptables
---

## iptables
Linux kernel 2.4から標準でinstallされているfirewall.
packet filtering type firewall.

## Install
For ubuntu,

```
sudo apt-get install iptables
```

## CLI

```
iptables -[ACD] chain rule-specification [options]
       iptables -I chain [rulenum] rule-specification [options]
       iptables -R chain rulenum rule-specification [options]
       iptables -D chain rulenum [options]
       iptables -[LS] [chain [rulenum]] [options]
       iptables -[FZ] [chain] [options]
       iptables -[NX] chain
       iptables -E old-chain-name new-chain-name
       iptables -P chain target [options]
       iptables -h (print this help information)
```

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


## Reference
* [コピペから脱出！iptablesの仕組みを理解して環境に合わせた設定をしよう | OXY NOTES](http://oxynotes.com/?p=6361)
