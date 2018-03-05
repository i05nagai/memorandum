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
    * 
* custom mode


## Reference
