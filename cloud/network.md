---
title: Network
---

## Network

- CSP
    - Cloud Service Provider
- SDCI providers
    - Software Defined Cloud Infrastructure
- MPLS
    - Multi Protocol Label Switching

## Multicloud benefits
- Every public cloud has slightly different networks. Capacity, topology, and bandwidth availability can all be slightly distinct, making management, administration, and orchestration complex.
- Public clouds are not designed to connect to each other, which makes it more difficult to run applications on multiple clouds.
- Security and compliance risks also must be factored when managing multicloud networks.

- Low latency
- Independence
    - multicloud network technologies empower organizations to more easily mix and match platforms and vendors and avoid being locked in to individual cloud providers.
    - Companies using multicloud network technologies also have the ability to reconfigure their cloud infrastructure as business needs change.
- disaster recovery


## Multicloud

- Public internet connection to CSP
    - VPN tunnel from on-premise to cloud
    - There are many potential pitfalls to running VPN tunnels over the internet to the public cloud – especially scalability and complexity.
    - https://www.megaport.com/blog/the-hidden-cost-of-running-cloud-hosted-sd-wan-for-iaas/
- private cloud ports
    - Using private cloud port services like AWS Direct Connect or Microsoft Azure ExpressRoute can provide better performance and security than public internet connectivity to those clouds.
    - there’s a major limitation of this method for multicloud. The connections are one to one, meaning that you must configure a private connection on your end of the infrastructure in the form of an MPLS circuit, an Ethernet connection, or a digital cross-connect service inside a data center or as provided by a carrier
    - The use case for private cloud ports is really best suited for high-traffic applications that are best hosted with one cloud.
- Private cloud hub
- Private software-defined cloud interconnection


- Using a data center
- Using carrier-managed MPLS
- Using a virtual cloud router


## Vendors
- aviatrix
    - https://networkinterview.com/multi-cloud-network-architecture-aviatrix/
- Alkira
- Prosimo

## Reference
- https://www.megaport.com/blog/multicloud-connectivity-complete-guide/
- https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/
- https://www.megaport.com/blog/how-to-simplify-your-multicloud-management-in-2022/
- https://www.megaport.com/blog/the-hidden-cost-of-running-cloud-hosted-sd-wan-for-iaas/
- https://azure.microsoft.com/en-us/blog/azure-multicloud-networking-native-and-partner-solutions/
    - azure
- https://cloud.google.com/architecture/network-hybrid-multicloud
    - gcp
- https://alexandrahuides.medium.com/multi-cloud-enterprise-network-architectures-natively-bridging-aws-and-azure-at-scale-part-1-3edeb5dea890
- https://networkinterview.com/multi-cloud-network-architecture-aviatrix/
