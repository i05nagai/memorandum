---
title: debconf-set-selections
---

## debconf-set-selections
Insert new values into the debconf database.

## CLI

```
 debconf-set-selections [-vcu] [file]
```

* `-v, --verbose`
    * verbose output
* `-c, --checkonly`
    * only check the input file format
* -u, --unseen
    * do not set the 'seen' flag when preseeding values

## Usage
See what configurations are available.

```
debconf-show <packagename>
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

Configure package

```
# <packagename> <configuration> <type> <value>
$ cat <<EOF | debconf-set-selections
slapd slapd/internal/generated_adminpw password ${LDAP_ADMIN_PASSWORD}
slapd slapd/internal/adminpw password ${LDAP_ADMIN_PASSWORD}
slapd slapd/password2 password ${LDAP_ADMIN_PASSWORD}
slapd slapd/password1 password ${LDAP_ADMIN_PASSWORD}
slapd slapd/dump_database_destdir string /var/backups/slapd-VERSION
slapd slapd/domain string ${LDAP_DOMAIN}
slapd shared/organization string ${LDAP_ORGANISATION}
slapd slapd/backend string ${LDAP_BACKEND^^}
slapd slapd/purge_database boolean true
slapd slapd/move_old_database boolean true
slapd slapd/allow_ldap_v2 boolean false
slapd slapd/no_configuration boolean false
slapd slapd/dump_database select when needed
EOF
```

```
export DEBIAN_FRONTEND=noninteractive
cat /root/debconf-slapd.conf | debconf-set-selections
apt install ldap-utils slapd -y
```

## Configuration

## Reference
- [Ubuntu Manpage: debconf\-set\-selections \- insert new values into the debconf database](http://manpages.ubuntu.com/manpages/xenial/man1/debconf-set-selections.1.html)
- [shell script \- Automating Slapd Install \- Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/362547/automating-slapd-install)
