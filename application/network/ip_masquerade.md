---
title: IP masquerade
---

## IP masquerade
NATがグローバルとプライベートの IPアドレスの変換を行ったのに対し、IP MasquerdeではUDP/TCPのポート番号の 変換まで行う

* ICMP
    * IP MasqueradeはUDP/TCPのポート番号の変換を行うことを前提にしている。 そのため、ポート番号の概念がないICMPは取り扱えない。
    ただし、ICMP Echo/Echo ReplyだけはIdentifierフィールドをポート番号と 同様に取り扱うことでIP Masqueradeでも扱えるようにしている。 すなわち、pingは通るということである。
* グローバル側からのアクセス
    * グローバル側からアクセスされる場合、最初のパケットは当然 グローバル側からやってくる。グローバルアドレスとプライベートアドレスが 1対1対応のNATであれば、そのような場合でもパケットの配送先が分かるが、 IP Masqueradeの場合は1対1対応ではないため、どのホストにパケットを 送るべきかの判断がつかない。
* rsh系のコマンド(rsh、rlogin、rcpなど)やlprなど
     * rsh系のコマンドで使われるプロトコルやlprで使われる LPRプロトコルでは、クライアント側のポート番号が WELL KNOWNポートの範囲内にあることが要求される。 そのため、ポート番号を変換してしまうIP Masquerade越しには 使えない。

## Reference
* [Linux IP Masquerade HOWTO](https://www.tldp.org/HOWTO/IP-Masquerade-HOWTO/index.html)
* [IP Masquerade, what is?](http://www.rtpro.yamaha.co.jp/RT/docs/nat/ip-masquerade.html)
