---
title: netcat
---

## netcat
nc command.

```
apt-get install netcat
```

## CLI
portがlistenしていれば、`0`を返す。
probeに使える。

```
nc -z localhost 22
```

* -c shell commands
    * as `-e`; use /bin/sh to exec [dangerous!!]
* -e filename
    * program to exec after connect [dangerous!!]
* -b
    * allow broadcasts
* -g gateway
    * source-routing hop point[s], up to 8
* -G num
    * source-routing pointer: 4, 8, 12, ...
* -h
    * help
* -i secs
    * delay interval for lines sent, ports scanned
* -k
    * set keepalive option on socket
* -l
    * listen mode, for inbound connects
* -n
    * numeric-only IP addresses, no DNS
* -o file
    * hex dump of traffic
* -p port
    * local port number
* -r
    * randomize local and remote ports
* -q secs
    * quit after EOF on stdin and delay of secs
* -s addr
    * local source address
* -T tos
    * set Type Of Service
* -t
    * answer TELNET negotiation
* -u
    * UDP mode
* -v
    * verbose [use twice to be more verbose]
* -w secs
    * timeout for connects and final net reads
* -C
    * Send CRLF as line-ending
* -z
    * zero-I/O mode [used for scanning]

## Usage

Listen on port 5000

```
nc -l -p 5000
```


```
# check listening or not
netstat -tulpen 
```


## Reference
* https://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf
