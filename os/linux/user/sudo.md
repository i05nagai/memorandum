---
title: sudo
---

## sudo
password required by `sudo` command can be set with `passwd <username>` command.
Empty password is not allowed.

## CLI

Run command with login shell

```
sudo -i command
```

Run command as a specific user with user's login shell

```
sudo -i -u USER command
```

Show user's environment variable

```
sudo -i -u user echo \$HOME
```


Show configuration for current user

```
sudo -ll 
```

Show configuration for specifc user

```
sudo -lU user
```

## Configuration

- `Defaults env_reset`
- `root    ALL=(ALL) ALL`
    - lets root do everything on any machine as any user
- `%admin ALL=(ALL) AL`
    - lets anybody in the admin group run anything as any user.

```
# any user can be USER_NAME
USER_NAME   ALL=(ALL) ALL
# anyuser can be UER_NAME only on HOST_NAME machine
USER_NAME   HOST_NAME=(ALL) ALL
# to disable asking for password for user `USERNAME`
Defaults:USER_NAME      !authenticate
# If you are annoyed by sudo's defaults that require you to enter your password every time you open a new terminal, disable tty_tickets
Defaults !tty_tickets

# ask root passwrod instead of user password
Defaults targetpw
#  restrict to specifc group
Defaults:%wheel targetpw
```

## Reference
- [Sudoers \- Community Help Wiki](https://help.ubuntu.com/community/Sudoers)
- [Sudo \- ArchWiki](https://wiki.archlinux.org/index.php/sudo)
* [bash - sudo as another user with their environment - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/176997/sudo-as-another-user-with-their-environment)
