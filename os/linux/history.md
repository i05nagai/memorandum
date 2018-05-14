---
title: history
---

## history
We use history command frequently in our daily routine jobs to check history of command or to get info about command executed by user.
This may be useful for audit purpose or to find out what command is executed at what date and time.


## Usage
List Last/All Executed Commands in Linux

```
history
```

```
export HISTTIMEFORMAT='%F %T  '
history
```

* `%F`
    * Equivalent to %Y - %m - %d
* `%T`
    * Replaced by the time ( %H : %M : %S )

Filter Commands in History

```
export HISTIGNORE='ls -l:pwd:date:'
history
```

Ignore Duplicate Commands in History

```
export HISTCONTROL=ignoredups
history
```

Unset export Command

```
unset export HISTCONTROL
```

List Specific User’s Executed Commands

```
cat .bash_history
```

Delete or Clear History of Commands

```
history -c
```

## Reference
* [The Power of Linux "History Command" in Bash Shell](https://www.tecmint.com/history-command-examples/)
