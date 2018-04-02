---
title: dns-sd
---

## dns-sd
dsn service discovery.
nslookupはcurlなどが使うMacOSのDNSスタックを使わない。
dns-sdを使う。

## Usage

Get address information for hostname

```
dns-sd -G v4 example.com
dns-sd -G <v4/v6/v4v6> <name>
```

Enumerate recommended registration domains

```
dns-sd -E
```

Enumerate recommended browsing domains

```
dns-sd -F
dns-sd -R <Name> <Type> <Domain> <Port> [<TXT>...]             (Register a service)
dns-sd -B        <Type> <Domain>                     (Browse for service instances)
dns-sd -L <Name> <Type> <Domain>                       (Resolve a service instance)
dns-sd -Q <name> <rrtype> <rrclass>             (Generic query for any record type)
dns-sd -Z        <Type> <Domain>               (Output results in Zone File format)
dns-sd -H                                   (Print usage for complete command list)
dns-sd -V                (Get version of currently running daemon / system service)
```

## Reference
* [DNS Service Discovery (DNS-SD)](http://www.dns-sd.org/)
