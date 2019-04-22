---
title: usermod
---

## usermod


## CLI

```
usermod [options] LOGIN
```

* `-c, --comment COMMENT`
    * new value of the GECOS field
* `-d, --home HOME_DIR`
    * new home directory for the user account
* -e, --expiredate EXPIRE_DATE
    * set account expiration date to EXPIRE_DATE
* -f, --inactive INACTIVE
    * set password inactive after expiration to INACTIVE
* -g, --gid GROUP
    * force use GROUP as new primary group
* -G, --groups GROUPS
    * new list of supplementary GROUPS
* -a, --append
    * append the user to the supplemental GROUPS mentioned by the -G option without removing him/her from other groups
* -l, --login NEW_LOGIN
    * new value of the login name
* -L, --lock
    * lock the user account
* -m, --move-home
    * move contents of the home directory to the new location (use only with -d)
* -o, --non-unique
    * allow using duplicate (non-unique) UID
* -p, --password PASSWORD
    * use encrypted password for the new password
* -R, --root CHROOT_DIR
    * directory to chroot into
* -s, --shell SHELL
    * new login shell for the user account
* -u, --uid UID
    * new UID for the user account
* -U, --unlock
    * unlock the user account
* -v, --add-subuids FIRST-LAST
    * add range of subordinate uids
* -V, --del-subuids FIRST-LAST
    * remove range of subordinate uids
* -w, --add-subgids FIRST-LAST
    * add range of subordinate gids
* -W, --del-subgids FIRST-LAST
    * remove range of subordinate gids
* -Z, --selinux-user SEUSER
    * new SELinux user mapping for the user account

## Usage
Add user to existing group

```
usermod --apend -g <gorup> <user-name>
```

## Configuration

## Reference
