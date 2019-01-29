---
title: newuser
---

## newuser


## CLI

```
useradd [options] LOGIN
useradd -D
useradd -D [options]
```

* `-b, --base-dir BASE_DIR`
    * base directory for the home directory of the new account
* -c, --comment COMMENT
    * GECOS field of the new account
* -d, --home-dir HOME_DIR
    * home directory of the new account
* `-D, --defaults`
    * print or change default useradd configuration
* -e, --expiredate EXPIRE_DATE
    * expiration date of the new account
* -f, --inactive INACTIVE
    * password inactivity period of the new account
* `-g, --gid GROUP`
    * name or ID of the primary group of the new account
* -G, --groups GROUPS
    * list of supplementary groups of the new account
* -h, --help
    * display this help message and exit
* `-k, --skel SKEL_DIR`
    * use this alternative skeleton directory
* -K, --key KEY=VALUE
    * override /etc/login.defs defaults
* -l, --no-log-init
    * do not add the user to the lastlog and faillog databases
* `-m, --create-home`
    * create the user's home directory
* -M, --no-create-home
    * do not create the user's home directory
* -N, --no-user-group
    * do not create a group with the same name as the user
* -o, --non-unique
    * allow to create users with duplicate (non-unique) UID
* -p, --password PASSWORD
    * encrypted password of the new account
* -r, --system
    * create a system account
* -R, --root CHROOT_DIR
    * directory to chroot into
* `-s, --shell SHELL`
    * login shell of the new account
* `-u, --uid UID`
    * user ID of the new account
* -U, --user-group
    * create a group with the same name as the user
* -Z, --selinux-user SEUSER
    * use a specific SEUSER for the SELinux user mapping
* --extrausers
    * Use the extra users database

## Usage

Show default user options.

```
$ useradd -D
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/sh
SKEL=/etc/skel
CREATE_MAIL_SPOOL=no
```

Create new user with home directory and bash as a login shell

```
useradd --create-home --shell /bin/bash newusername
```

Create new user with home directory and bash as a login shell

```
useradd --uid <uid> --gid <gid> newusername
```

## Reference

