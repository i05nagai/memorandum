---
title: systemctl
---

## systemctl


## CLI

Query or send control commands to the systemd manager.

* --system         Connect to system manager
* --user           Connect to user service manager
* -H --host=[USER@]HOST
    * Operate on remote host
* -M --machine=CONTAINER
                      Operate on local container
* -t --type=TYPE      List units of a particular type
* --state=STATE    List units with particular LOAD or SUB or ACTIVE state
* -p --property=NAME  Show only properties by this name
* -a --all            Show all properties/all units currently in memory,
                      including dead/empty ones. To list all units installed on
                      the system, use the 'list-unit-files' command instead.
* --failed         Same as --state=failed
* -l --full           Don't ellipsize unit names on output
* -r --recursive      Show unit list of host and local containers
     --reverse        Show reverse dependencies with 'list-dependencies'
     --job-mode=MODE  Specify how to deal with already queued jobs, when
                      queueing a new job
     --show-types     When showing sockets, explicitly show their type
     --value          When showing properties, only print the value
  -i --ignore-inhibitors
                      When shutting down or sleeping, ignore inhibitors
     --kill-who=WHO   Who to send signal to
  -s --signal=SIGNAL  Which signal to send
     --now            Start or stop unit in addition to enabling or disabling it
     --dry-run        Only print what would be done
* -q --quiet          Suppress output
     --wait           For (re)start, wait until service stopped again
     --no-block       Do not wait until operation finished
     --no-wall        Don't send wall message before halt/power-off/reboot
     --no-reload      Don't reload daemon after en-/dis-abling unit files
     --no-legend      Do not print a legend (column headers and hints)
     --no-pager       Do not pipe output into a pager
     --no-ask-password
                      Do not ask for system passwords
     --global         Enable/disable/mask unit files globally
     --runtime        Enable/disable/mask unit files temporarily until next
                      reboot
                unit is required or wanted

  -f --force          When enabling unit files, override existing symlinks
                      When shutting down, execute action immediately
     --root=PATH      Enable/disable/mask unit files in the specified root
                      directory
  -n --lines=INTEGER  Number of journal entries to show
  -o --output=STRING  Change journal output mode (short, short-precise,
                             short-iso, short-iso-precise, short-full,
                             short-monotonic, short-unix,
                             verbose, export, json, json-pretty, json-sse, cat)
--firmware-setup Tell the firmware to show the setup menu on next boot
--plain          Print unit dependencies as a list instead of a tree


Unit File Commands:

* `list-unit-files [PATTERN...]`
    * List installed unit files
* `enable [NAME...|PATH...]`
    * Enable one or more unit files
* `disable NAME...`
    * Disable one or more unit files
  reenable NAME...                Reenable one or more unit files
  preset NAME...                  Enable/disable one or more unit files
                                  based on preset configuration
  preset-all                      Enable/disable all unit files based on
                                  preset configuration
  is-enabled NAME...              Check whether unit files are enabled
  mask NAME...                    Mask one or more units
  unmask NAME...                  Unmask one or more units
  link PATH...                    Link one or more units files into
                                  the search path
  revert NAME...                  Revert one or more unit files to vendor
                                  version
  add-wants TARGET NAME...        Add 'Wants' dependency for the target
                                  on specified one or more units
  add-requires TARGET NAME...     Add 'Requires' dependency for the target
                                  on specified one or more units
  edit NAME...                    Edit one or more unit files
  get-default                     Get the name of the default target
  set-default NAME                Set the default target

Machine Commands:

  list-machines [PATTERN...]      List local containers and host

Job Commands:

* `list-jobs [PATTERN...]`
    * List jobs
* cancel [JOB...]                 Cancel all, one, or more jobs


Environment Commands:

* show-environment                Dump environment
* set-environment NAME=VALUE...   Set one or more environment variables
* unset-environment NAME...       Unset one or more environment variables
* import-environment [NAME...]    Import all or some environment variables

Manager Lifecycle Commands:
  daemon-reload                   Reload systemd manager configuration
  daemon-reexec                   Reexecute systemd manager

System Commands:
  is-system-running               Check whether system is fully running
  default                         Enter system default mode
  rescue                          Enter system rescue mode
  emergency                       Enter system emergency mode
  halt                            Shut down and halt the system
  poweroff                        Shut down and power-off the system
  reboot [ARG]                    Shut down and reboot the system
  kexec                           Shut down and reboot the system with kexec
  exit [EXIT_CODE]                Request user instance or container exit
  switch-root ROOT [INIT]         Change to a different root file system
  suspend                         Suspend the system
  hibernate                       Hibernate the system
  hybrid-sleep                    Hibernate and suspend the system
  suspend-then-hibernate          Suspend the system, wake after a period of
                                  time and put it into hibernate

## Usage

## Reference
