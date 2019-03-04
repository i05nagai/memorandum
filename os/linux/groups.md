---
title: groups
---

## groups
`/etc/group` is the list of existing groups.

## CLI


## Usage
Show a group which the user belogns to

```
groups <USERNAME>
```

Show the users in the group

```
getent group <GROUPNAME>
getent group <groupname> | awk -F: '{print $4}'
```

## Reference
* [Users and groups \- ArchWiki](https://wiki.archlinux.org/index.php/users_and_groups)
* [Guidelines for Using User Names, User IDs, and Group IDs \(System Administration Guide: Basic Administration\)](https://docs.oracle.com/cd/E19120-01/open.solaris/819-2379/userconcept-30/index.html)
* [UNIX Groups \(System Administration Guide: Basic Administration\)](https://docs.oracle.com/cd/E19120-01/open.solaris/819-2379/userconcept-35906/index.html)
