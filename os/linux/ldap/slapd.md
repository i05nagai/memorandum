---
title: slapd
---

## slapd


```
apt-get install -y slapd
```

```
$ debconf-show slapd
  slapd/internal/generated_adminpw: (password omitted)
  slapd/password1: (password omitted)
  slapd/password2: (password omitted)
  slapd/internal/adminpw: (password omitted)
  slapd/password_mismatch:
  slapd/move_old_database: true
  slapd/no_configuration: false
  slapd/backend: MDB
  slapd/upgrade_slapcat_failure:
  slapd/dump_database: when needed
  shared/organization: nodomain
  slapd/domain: nodomain
  slapd/purge_database: false
  slapd/unsafe_selfwrite_acl:
  slapd/invalid_config: true
  slapd/dump_database_destdir: /var/backups/slapd-VERSION
  slapd/ppolicy_schema_needs_update: abort installation
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


## Backends
- [OpenLDAP Software 2\.4 Administrator's Guide: Backends](https://www.openldap.org/doc/admin24/backends.html)

- `hdb`
    - The hdb backend to slapd(8) is a backend for a normal slapd database.
    - It uses the Oracle Berkeley DB (BDB) package to store data.
- `mdb`
- `bdb`
    - hdb is a variant of the original bdb backend which was first written for use with BDB
- `ldif`


## Configuration

## Reference
