---
title: Virtual Private Cloud
---

## Virtual Private Cloud


## Firewall
* [Firewall Rules Overview  |  VPC  |  Google Cloud Platform](https://cloud.google.com/vpc/docs/firewalls)


```
gcloud compute firewall-rules create [NAME] \
    [--network [NETWORK]; default=”default”] \
    [--allow ([PROTOCOL][:PORT[-PORT]],[PROTOCOL[:PORT[-PORT]],...]] | all ) \
    [--action (deny | allow )] \
    [--rules ([PROTOCOL][:PORT[-PORT]],[PROTOCOL[:PORT[-PORT]],...]] | all ) \
    [--direction (ingress|egress|in|out); default=”ingress”] \
    [--priority [PRIORITY];default=1000] \
    [--destination-ranges [CIDR-RANGE][,CIDR-RANGE...]] \
    [--source-ranges [CIDR-RANGE][,CIDR-RANGE…]] \
    [--source-tags [TAG][,TAG,...]] \
    [--target-tags [TAG][,TAG,...]] \
    [--source-service-accounts=[EMAIL] \
    [--target-service-accounts=[EMAIL]
```

* `--target-tags`
    * A list of instance tags. The rule in question is assigned to any instances in the network with any of the tags and does not apply to instances without one. You cannot specify both tags and service accounts in a rule.


```
gcloud compute firewall-rules create deny-subnet1-webserver-access \
    --network my-network \
    --action deny \
    --direction ingress \
    --rules tcp \
    --source-ranges 0.0.0.0/0 \
    --priority 1000 \
    --target-tags webserver
```

```
gcloud compute firewall-rules create vm1-allow-ingress-tcp-port80-from-subnet1 \
    --network my-network \
    --action allow \
    --direction ingress \
    --rules tcp:80 \
    --source-ranges 10.240.10.0/24 \
    --priority 50 \
    --target-tags webserver
```

## Virtual Private Cloud Cloud Network
* [Virtual Private Cloud (VPC) Network Overview  |  VPC  |  Google Cloud Platform](https://cloud.google.com/vpc/docs/vpc)

* subnetとsubnetworkは同じ意味で使われている
* VPC network
    * subnetworks
        * subnetworkはsingle region

Mode

* auto mode
    * 新しいregionができた時、自動でsubnetworkが作られる
    * `10.128.0.0/9`の中でregionごとにsubnetmaskが決まっている
* custom mode
    * 自分で全部定義する

Reserved IP

| Reserved Address           | Description                                                   | Example                   |
|----------------------------|---------------------------------------------------------------|---------------------------|
| Network                    | First address in the primary IP range for the subnet          | 10.1.2.0 in 10.1.2.0/24   |
| Default Gateway            | Second address in the primary IP range for the subnet         | 10.1.2.1 in 10.1.2.0/24   |
| Second-to-last Reservation | Second-to-last address in the primary IP range for the subnet | 10.1.2.254 in 10.1.2.0/24 |
| Broadcast                  | Last address in the primary IP range for the subnet           | 10.1.2.255 in 10.1.2.0/24 |

## Routes
VMIをでた後以下の順序でrouteを決定する。

1. より詳細なroutingがあればそちらを選ぶ、例えば
    * `destinationIP`
        * `10.240.1.1`
    * `routing`
        * `10.240.1.0/24`へのrouting
        * `10.240.0.0/16`へのrouting
    * 選ばれるroute
        * `10.240.1.0/24`
2. 同じprefix lengthで複数のrouteがある場合は、priorityが最も小さいものを選ぶ
3. ?
4. forward先が見つからないときは、packetをdropしてICMP destination/network unreachable errorを返す

GCPはnext hopを決める時distnanceを考えない。
Routingがあっても、firewallが空いていなければpacketは到達しない。


## firewall

* default and implied rules
    * 全てのVPCがもつfirewall
    * 削除できない
    * `implied allow egress rule`
        * 全てのinstanceがdefaultでinternetにaccessできる
        * priority `65535`
        * egress
        * destination `0.0.0.0`
    * `implied deny ingress rul`
        * 全てのinstanceへのaccessを無効
        * priority `65535`
        * ingress
        * source `0.0.0.0`
* additional rules
    * `default`のVPCが持つrule
* target
    * All instances in the network
    * Specific instances by target tag
    * Specific instances by service account



## Shared VPC
Connect to another GCP project.

host projectの以下の権限が必要。

```
compute.subnetworks.getIamPolicy for host project host-procjet-id
resourcemanager.projects.getIamPolicy for host project host-procjet-id
```


## VPN aws-gcp
Connect to another cloud pvodier.

* (1) GCPのVPNでcloud routerを作る
* (2) AWSの`Customer gateway`を作る
    * 1のIPを指定する
* (3) AWSの`Virtual Private Gateway`がなければ作る
* (4) AWSの`VPN connection`作る
* (5) VPNのConfigurationをDLする
* (6) GCPのVPNを作成する

AWSのVPN connectionを作ると以下の設定fileがDLできる。

* `Download Configuration`
* 以下にしてDL
    * Vendor: `Generic`
    * Platform: `Generic`
    * Sowftware: `Vendor Agnostic`

```
Outside IP Addresses:
  - Customer Gateway 		        : outside.customer.gateway.ip
  - Virtual Private Gateway	        : outside.private.gateway.ip
		
Inside IP Addresses
  - Customer Gateway         		: inside.customer.gateway.ip/30
  - Virtual Private Gateway             : inside.private.gateway.ip/30


BGP Configuration Options:
  - Customer Gateway ASN	          : customer.gateway.asn
  - Virtual Private  Gateway ASN          : private.gateway.asn
  - Neighbor IP Address     		  : neighbor.ip
  - Neighbor Hold Time       : ...
```

neighbor.ip = inside.private.gateway.ip


* forwarding rules
    * ip address
        * statci.ip attached to router
* vpn-tunnle-interface
    * ip range
        * inside.customer.gateway.ip/30
* vpn-tunnel 
    * (remote_peer_gateway) peer_ip
        * outside.private.gateway.ip
* Google cloud gateway
    * ip address
        * outside.customer.gateway.ip
* bgp
    * peer_ip_address
        * Neighbor IP Address
        * 

## legacy networks
https://cloud.google.com/vpc/docs/legacy
In a legacy network, instance IP addresses are not grouped by region or zone

* legacy network is not recommended for production
    * https://cloud.google.com/vpc/docs/vpc

## Alias IP ranges
https://cloud.google.com/vpc/docs/alias-ip




## Reference
