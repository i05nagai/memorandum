---
title: Redis
---

## Redis
in memory KVS.

## Install

```
sudo apt-get install redis-tools
```

## DataType
* string
* hash
* set
* sorted set
* lists


## Configuration
`redis.conf`をする。
versionごとのconfigurationのsampleがある。

[Redis configuration – Redis](https://redis.io/topics/config)


## CLI
以下で指定したhostのredisにcommandを送る。

* https://www.cheatography.com/tasjaevan/cheat-sheets/redis/

```
redis-cli -h hostname -p port_num command
```

* `-n <db>`
    * specify database number

以下でinteractive modeになる。

```
redis-cli -h hostname -p port_num
```

```
help @[category]
```

* `KEYS pattern`
    * `keys *`
        * 保存されているkey一覧
* `TYPE keys`


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

## in Docker
* [library/redis - Docker Hub](https://hub.docker.com/_/redis/)

Dockerの中でredis CLIが使える。

```
redis-cli -h redis -p 6379
```

redisの設定を変更する。
docker run時に`/usr/local/etc/redis/redis.conf`をvolumeとしてつけるか、Dockerfileを作って以下のようにする。

```
FROM redis
COPY redis.conf /usr/local/etc/redis/redis.conf
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
```


## redis-server

```
./redis-server [/path/to/redis.conf] [options]
```

- `-v`
    - version
- `-h`
    - help
- `--test-memory <megabytes>`
- `--port <port>`
- `--slaveof 127.0.0.1 8888`
- `--log-level verbose`
- `--sentinel`

Examples:
       ./redis-server (run the server with default conf)
       ./redis-server /etc/redis/6379.conf
       ./redis-server --port 7777
       ./redis-server --port 7777 --slaveof 127.0.0.1 8888
       ./redis-server /etc/myredis.conf --loglevel verbose

Sentinel mode:
       ./redis-server /etc/sentinel.conf --sentinel


## Lock
- [11\.2\.1 Why locks in Lua? \| Redis](https://redis.com/ebook/part-3-next-steps/chapter-11-scripting-redis-with-lua/11-2-rewriting-locks-and-semaphores-with-lua/11-2-1-why-locks-in-lua/)

## Lua script


## Reference
* [Command reference – Redis](https://redis.io/commands)
