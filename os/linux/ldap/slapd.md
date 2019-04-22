---
title: slapd
---

## slapd


```
apt-get install -y slapd
```

## CLI


## Usage

```
slapd
```

* -4
    * IPv4 only
* -6
    * IPv6 only
* `-T {acl|add|auth|cat|dn|index|passwd|test}`
    * Run in Tool mode
* -c cookie
    * Sync cookie of consumer
* `-d level`
    * Debug level
* -f filename
    * Configuration file
* -F dir
    * Configuration directory
* `-g group`
    * Group (id or name) to run as
* `-h URLs`
    * e.g. `-h "ldap://$HOSTNAME ldaps://$HOSTNAME ldapi:///"`
    * List of URLs to serve
* -l facility
    * Syslog facility (default: LOCAL4)
* -n serverName
    * Service name
* -o <opt>[=val]
    * generic means to specify options; supported options:
    slp[={on|off|(attrs)}] enable/disable SLP using (attrs)
* -r directory
    * Sandbox directory to chroot to
* -s level
    * Syslog level
* `-u user`
    * User (id or name) to run as
* -V
    * print version info (-VV exit afterwards, -VVV print info about static overlays and backends)

## Configuration

## Reference

