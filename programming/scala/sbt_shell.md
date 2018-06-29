---
title: sbt shell
---

## sbt shell


## CLI
Compiles and runs all tests.

```
test
```

Runs the main class for the project in the same virtual machine as sbt.

```
run <argment>
```

Compiles the main sources (in src/main/scala and src/main/java directories).

```
compile
```

Displays basic information about sbt and the build.

```
about
```

Lists the tasks defined for the current project.

```
tasks
```

Lists the settings defined for the current project.

```
settings
```

(Re)loads the current project or changes to plugins project or returns from it.

```
reload
```

Creates a new sbt build.

```
new
```

Lists the names of available projects or temporarily adds/removes extra builds to the session.

```
projects
```

Displays the current project or changes to the provided `project`.

```
project    
```

Lists the tasks defined for the current project.

```
tasks
```

Evaluates a Setting and applies it to the current project.

```
set [every] <setting>
```

Manipulates session settings.  For details, run 'help session'.

```
session
```

Prints the value for 'key', the defining scope, delegates, related definitions, and dependencies.

```
inspect [tree|uses|definitions|actual] <key>
```

Sets the logging level to 'log-level'.  Valid levels: debug, info, warn, error

```
<log-level>
```

Lists currently available plugins.Lists currently available plugins.

```
plugins
```

Displays output from a previous command or the output from a specific task.Displays output from a previous command or the output from a specific task.

```
last
```

Shows lines from the last output for 'key' that match 'pattern'.

```
last-grep
```

Executes tasks and displays the equivalent command lines.

```
export <tasks>+
```

Displays the result of evaluating the setting or task associated with 'key'.

```
show <key>
```

Executes all of the specified tasks concurrently.

```
all <task>+
```

Displays a list of completions for the given argument string (run 'completions <string>').

```
completions
```

Runs the provided semicolon-separated commands.

```
; <command> (; <command>)*
```

Schedules a command to run before other commands on startup.

```
early(<command>)
```

Executes the specified command whenever source files change.Executes the specified command whenever source files change.

```
~ <command>
```

* `!`
    * show history command help
* `!!`
    * Execute the previous command again.
* `!:`
    * Show all previous commands.
* `+`
* `++`
* `+-`
* `<`
* `^`
* `^^`
* alias
* append
* apply
* client
* eval
* iflast
* onFailure
* reboot
* shell
* startServer


## Configuration

## Reference
