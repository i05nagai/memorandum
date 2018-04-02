---
title: Amazon Virtual Private Cloud
---

## Amazon Virtual Private Cloud

## VPN connections
* [AWS Managed VPN Connections - Amazon Virtual Private Cloud](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)


* Virtual Private Gateway
    * AWS側のVPN peer
    * defaultでASNは64512
* Customer Gateway
    * 接続先のVPN peer
    * AWS側でCustomer Gateway Resourceを作る必要がある
    * Internet-routable IP address (static) of the customer gateway's external interface.
        * static IPを指定
        * NATを使っている場合はNATのdeviceのpublic ip addressを指定して、UDP4500をportであける
    * The type of routing
        * static/dynamic.
    * Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the customer gateway.
* Inside tunnel CIDR

## Reference

