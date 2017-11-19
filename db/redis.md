---
title: Redis
---

## Redis
in memory KVS.


## Pipeline
* [Using pipelining to speedup Redis queries – Redis](https://redis.io/topics/pipelining)

いくつかのRequestをまとめる。
Round Time Tripを減らすことができる。
Requestは一つにまとめて送られるが、server側はResponseをqueueするので、commandの数だけqueueを消費する可能性がある。
問題になる場合は、client側で適当な数にまとめる処理が必要。
Serverへの負荷という意味では小さいが、commandの送信はSocket I/Oの点ではcostになっている。


## Memory Optimization
* 32bit instance
    * 32bitで使う場合は、pointerのsizeは小さくなるが、4GBまでしかmemoryが使えない
* bit and byte level operation
    * GETRANGE, SETRANGE, GETBIT, SETBIT
* Use hashes when possible
    * hashは小さくなるようにencodeされるので、最初はhashとして表現できるかを考えるべき
* Using hashes to abstract a very memory efficient plain key-value store on top of Redis
    * 

## Redis Modules

## An introduction to Redis data types and abstractions
Redisがsupportしているdata structureは以下。

* Bineary-safe string
* Lists
    * 基本的にlinked list
* Sets
* Sorted sets
* Hashes
    * map
* Bit arrays
* HyperLogLogs
    * 集合のcardinalityを推定するのに使われる確率的なdata structure
    * 一般にはkeyのcardinalityに応じたmemory sizeが必要だが、 12KBのconstantなmemory sizeを使ってkeyの一意性の計算をする

* Redis Keys
    * binary safeなのでどんなByte列もKeyとして使える
    * JPEG fileの中身もOK
    * 長過ぎるKeyも短すぎるKeyもだめ
    * 512MBが最大size
* Redis Strings

## Configuration
`redis.conf`に設定を記載する。
formatは以下となる。

```
keyword argument1 argument2 ... argumentN
```

command lineで設定を渡すこともできる。

## on Docker
* [library/redis - Docker Hub](https://hub.docker.com/_/redis/)

Dockerの中でredis CLIが使える。

```
redis-cli -h redis -p 6379
```

## Reference
* [Command reference – Redis](https://redis.io/commands)
