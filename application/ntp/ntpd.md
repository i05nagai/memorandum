---
title: ntpd
---

## ntpd


## Ubuntu
* [Time Synchronisation](https://help.ubuntu.com/lts/serverguide/NTP.html)

```
apt install ntp
```

reload ntpd

```
sudo systemctl reload ntp.service
```

## Configuration
`/etc/ntp.conf`に設定がある。

```
# Use servers from the NTP Pool Project. Approved by Ubuntu Technical Board
# on 2011-02-08 (LP: #104525). See http://www.pool.ntp.org/join.html for
# more information.
server 0.ubuntu.pool.ntp.org
server 1.ubuntu.pool.ntp.org
server 2.ubuntu.pool.ntp.org
server 3.ubuntu.pool.ntp.org
```

## Reference
