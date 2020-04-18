---
title: poetry
---

## poetry

```
pip install poetry
```

## CLI

```
poetry [-h] [-q] [-v [<...>]] [-V] [--ansi] [--no-ansi] [-n] <command> [<arg1>] ... [<argN>]
```

GLOBAL OPTIONS

-q (--quiet)           Do not output any message
-v (--verbose)         Increase the verbosity of messages: "-v" for normal output, "-vv" for more
                     verbose output and "-vvv" for debug
-V (--version)         Display this application version
--ansi                 Force ANSI output
--no-ansi              Disable ANSI output
-n (--no-interaction)  Do not ask any interactive question

about                  Shows information about Poetry.
add                    Adds a new dependency to pyproject.toml.
build                  Builds a package, as a tarball and a wheel by default.
cache                  Interact with Poetry's cache
check                  Checks the validity of the pyproject.toml file.
config                 Manages configuration settings.
debug                  Debug various elements of Poetry.
env                    Interact with Poetry's project environments.
export                 Exports the lock file to alternative formats.
help                   Display the manual of a command
init                   Creates a basic pyproject.toml file in the current directory.
install                Installs the project dependencies.
lock                   Locks the project dependencies.
new                    Creates a new Python project at <path>.
publish                Publishes a package to a remote repository.
remove                 Removes a package from the project dependencies.
run                    Runs a command in the appropriate environment.
search                 Searches for packages on remote repositories.
self                   Interact with Poetry directly.
shell                  Spawns a shell within the virtual environment.
show                   Shows information about packages.
update                 Update the dependencies as according to the pyproject.toml file.
version                Shows the version of the project or bumps it when a valid bump rule is
                         provided.

## Reference
- [Basic Usage \| Documentation \| Poetry \- Python dependency management and packaging made easy\.](https://python-poetry.org/docs/basic-usage/)
