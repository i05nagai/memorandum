---
title: architecture
---

## architecture

## Book
- Patterns of Enterprise Application Architecture
- Clean code
- clean architecture-

## CDN

## Servers

## Cache
Cache can exist at any level of architecture.
In web servers, there

- Application server cache
- Contet Delivery Network (CDN)


Cache invalidation

- Write-though cache
    - data is written into cache and the corresponding database simultaneously
    - pros
        - higher consitency
    - cons
        - higher latency
- Write-around cache
    - data is written directly into database
    - pros
    - cons
        - higher cache miss rate
- Write-back cache
    - data is written to cache. Write to the database is done after the cahce under some conditions
    - pros
        - low latency. high-thoughput for write intencive operations
    - cons
        - the risk of data loss


Algorithms

- Least Recently Used cache
- First In First Out cache
- Last In First Out cache
- Most Recently Used cache
- Least Frequently Used cache
- Random Replacement

Where to cache

- CDN
- 

## Queue

## Load Balancer
LB can be used to improve availability and responsiveness.
Typically, it's placed

- between the user and the web server (e.g. Nginx)
- between web serers and applications severs/cache servers
- between application layers and database


LB should forward traffic to health backends.
Health check functionality has to be implemented.


Algorithms

- Least connection
    - The traffic is directed to the server with the fewest active connections
- Least Response time
    - The traffic is directed to the server with the fewest active connections and the lowest average response time
- Least bandwidth
    - The traffic is directed to the server with the lowest bandwidth (Mbps)
- Round robin
    - The method cycles though a list of all servers and directs a new request to the next server
    - useful when there is not many persistent connections
- Weighted round robin
    - each server assigned a weight. Higher weight receives more connections than ones with lower weights
- IP Hash
    - calculate the hash of ip and direct the request based on it

## Data partitionng

- Horizontal partitioning
    - store different rows in different tables
    - the key to split rows have to be chosen carefully to distribute traffic equally
- Vertical partitioning
    - Put data with different features into different tables
    - e.g. a table for users info, a table for posts
- directory based partitioning
    - 

Criteria

- Key or Hash-based partitionng
- List partitoining
- round robin partitiong
- composite partitiong

Problems

- joins and denormaliation
- referential integrity

## Reference

