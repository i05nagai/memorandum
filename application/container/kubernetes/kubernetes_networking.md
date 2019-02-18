---
title: Kubernetes Networking
---

## Kubernetes Networking

* cluster IP
    * The service’s cluster IP 10.3.241.152 is in an IP address range that is separate from the pod network
    * from the network that the nodes themselves are on
* Node IP
* NodePort
    * node ip + port -> pods + target port
* LoadBalancer
     * On cloud providers which support external load balancers, setting the type field to LoadBalancer will provision a load balancer for your Service


## GKE
When docker works on each node, each container belongs to either a network, host or none.
For instance, kube-proxy and fluentd Pod belongs to host network.


## Reference
* https://medium.com/google-cloud/understanding-kubernetes-networking-ingress-1bc341c84078
