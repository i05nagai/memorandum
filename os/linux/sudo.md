---
title: sudo
---

## sudo

## CLI

login shellで実行

```
sudo -i command
```

userのlogin shellで実行する。

```
sudo -i -u USER command
```

userの`$HOME`を参照

```
sudo -i -u user echo \$HOME
```

## Reference
* [bash - sudo as another user with their environment - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/176997/sudo-as-another-user-with-their-environment)
