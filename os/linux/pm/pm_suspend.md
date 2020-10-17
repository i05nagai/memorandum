---
title: pm-suspend
---

## pm-suspend


## CLI

## Usage

## Configuration
- /etc/pm/config.d
    - The files in this directory are evaluated in C sort order. These files can be provided by individual packages outside of pm-utils. If a global configuration variable is set, the value set to will be appended to the previous value. If any other variable is set, it will be ignored. The syntax is simply: VAR_NAME = value. See the CONFIGURATION VARIABLES section for valid variables defined by pm-utils. External packages can define others, see their respective documentation for more information.
- /etc/pm/sleep.d, /usr/lib/pm-utils/sleep.d
    - Programs in these directories (we call them hooks) are combined and executed in C sort order before suspend and hibernate with as argument 'suspend' or 'hibernate'. Afterwards they are called in reverse order with argument 'resume' and 'thaw' respectively. If both directories contain a similar named file, the one in /etc/pm/sleep.d will get preference. It is possible to disable a hook in the distribution directory by putting a non-executable file in /etc/pm/sleep.d, or by adding it to the HOOK_BLACKLIST configuration variable.
- /var/log/pm-suspend.log
    - The log file shows what was done on the last suspend/hibernate and resume/thaw.

## Reference
- [pm\-suspend\(8\): Suspend/Hibernate your computer \- Linux man page](https://linux.die.net/man/8/pm-suspend)
