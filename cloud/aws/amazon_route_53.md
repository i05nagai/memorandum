---
title: Amazon Route 53
---

## Amazon Route 53

* Standard Queries
    * first 1 Billion queries / month
        * 0.400USD per million queries
    * over 1 Billion queries / month
        * 0.200USD per million queries
* Hosted zone
    * for the first 25 hosted zones
        * 0.50 USD per hosted zone / month 
    * for additional hosted zones
        * 0.10 USD per hosted zone / month 
* Traffic flow
    * 50.00 USD per policy record / month
* Geo DNS and Geoproximity Queries
    * first 1 Billion queries / month
        * 0.700 USD per million queries
    * over 1 Billion queries / month
        * 0.350 USD per million queries
            o

* The typical TTL setting for the NS record is 172800 seconds, or two days.

* Private hosted zone
    * amazon VPC
* Public hosted zone
    * internet

Private zoneとPublic zoneがoverlapしているとき、

* 以下のいずれかにqueryのdomaiがmatchする場合はprivate zoneのDNS
    * 完全一致
    * queryの親domainがprivate
* matchしないものは全てpublic DNS resolverでかいけつ
* private zoneのDNSで一致するrecordがない場合は、public DNSへforwardingされずに `NXDOMAIN` recordがかえる

## Public host zone

* defaultで4つのNS serverが各host zoneに割り当てられる


## Reference
* [What Is Amazon Route 53? - Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
* [DNSとかネームサーバとかRoute53とかAレコードとかCNAMEとかがわからない人のためのまとめ - ふじいけ技術メモ](http://fujiike.hateblo.jp/entry/2015/09/14/191934)
* [AWS再入門2018 Amazon Route 53（DNS）編 ｜ Developers.IO](https://dev.classmethod.jp/cloud/aws/2018-aws-re-entering-route53/)
* [Managed Cloud DNS - Domain Name System - Amazon Route 53 | AWS](https://aws.amazon.com/route53/)
