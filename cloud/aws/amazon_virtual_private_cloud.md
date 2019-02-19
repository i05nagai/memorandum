---
title: Amazon Virtual Private Cloud
---

## Amazon Virtual Private Cloud

## Route table
* https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#Route_Replacing_Main_Table

Route table basiscs: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#RouteTables

* VPC has an implict router
    * default route table
* VPC automatically comes with a main route table that you can modify
    * main route table
* You can create additional custom route tables for your VPC.
* Each subnet must be associated with a route table
    * the subnet is implicitly associated with the main route table
* You cannot delete the main route table, but you can replace the main route table with a custom table that you've created
    * main table is default route table for the subnets
* There is a limit on the number of route tables you can create per VPC,

Main Route Tables



Custom Route Tables



```
aws ec2 describe-route-tables --filters "Name=tag:Name,Values=*name*"
```

## Security groups
* https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html

* you can assign up to five security groups to the instance
* Security groups act at the instance level, not the subnet level
*  If you don't specify a particular group at launch time, the instance is automatically assigned to the default security group for the VPC
* You can specify allow rules, but not deny rules.
* Instances associated with a security group can't talk to each other unless you add rules allowing it 
    * exception: the default security group has these rules by default

#### Default security group

* inbound
    * source
        * The security group ID (sg-xxxxxxxx)
    * protocol
        * all
    * port range
        * all
    * comment
            * Allow inbound traffic from instances assigned to the same security group.
* outbound
    * destination
        * 0.0.0.0/0
    * Protocol
        * all
    * Port Range
        * all
    * Comments
        * Allow all outbound IPv4 traffic.

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

