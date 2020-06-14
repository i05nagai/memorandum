---
title: poetry
---

## poetry

## Install

```
pip install poetry
```

```
POETRY_HOME=/path/to/install get-poetry.py --version 0.7.0
```

## CLI

```
poetry [-h] [-q] [-v [<...>]] [-V] [--ansi] [--no-ansi] [-n] <command> [<arg1>] ... [<argN>]
```

GLOBAL OPTIONS

-h (--help)            Display this help message
-q (--quiet)           Do not output any message
-v (--verbose)         Increase the verbosity of messages: "-v" for normal output, "-vv" for more verbose output and "-vvv" for debug
-V (--version)         Display this application version
--ansi                 Force ANSI output
--no-ansi              Disable ANSI output
-n (--no-interaction)  Do not ask any interactive question

AVAILABLE COMMANDS

about                  Shows information about Poetry.
add                    Adds a new dependency to pyproject.toml.
cache                  Interact with Poetry's cache
check                  Checks the validity of the pyproject.toml file.
config                 Manages configuration settings.
debug                  Debug various elements of Poetry.
env                    Interact with Poetry's project environments.
export                 Exports the lock file to alternative formats.
help                   Display the manual of a command
lock                   Locks the project dependencies.
remove                 Removes a package from the project dependencies.
run                    Runs a command in the appropriate environment.
search                 Searches for packages on remote repositories.
self                   Interact with Poetry directly.
shell                  Spawns a shell within the virtual environment.
update                 Update the dependencies as according to the pyproject.toml file.


```
```


new                    Creates a new Python project at <path>.

```
```

init                   Creates a basic pyproject.toml file in the current directory.

```

```

`show` command creates virtualenv in your local computer if it doesn't exist.

```
poetry show <package>
```

* --no-dev               Do not list the development dependencies.
* -t (--tree)            List the dependencies as a tree.
* -l (--latest)          Show the latest version.
* -o (--outdated)        Show the latest version but only for packages that are outdated.
* -a (--all)             Show all packages (even those not compatible with current system).


install                Installs the project dependencies.

install packages to virtualenv for the project.
The install command reads the `poetry.lock` file from the current directory, processes it, and downloads and installs all the libraries and dependencies outlined in that file. If the file does not exist it will look for `pyproject.toml` and do the same.
Even if `poetry.lock` exist, `pyproject.toml` also needs to exists.

```
poetry instasll
```

* --no-dev               Do not install the development dependencies.
* --no-root              Do not install the root package (the current project).
* --dry-run              Output the operations but do not execute anything (implicitly enables --verbose).
* -E (--extras)          Extra sets of dependencies to install. (multiple values allowed)


build                  Builds a package, as a tarball and a wheel by default.

```
poetry build
```

* -f (--format)          Limit the format to either sdist or wheel.


The publish command builds and uploads the package to a remote repository.
Publish will fail if `build` is not executed before.

```
poetry publish
```

* -r (--repository)      The repository to publish the package to.
* -u (--username)        The username to access the repository.
* -p (--password)        The password to access the repository.
* --cert                 Certificate authority to access the repository.
* --client-cert          Client certificate to access the repository.
* --build                Build the package before publishing.


`config` manages `poetry.yaml`.

```
poetry config [<key>] [<value1>] ... [<valueN>]
```

* --list                 List configuration settings.
* --unset                Unset configuration setting.
* --local                Set/Get from the project's local configuration.


version                Shows the version of the project or bumps it when a valid bump rule is provided.
The version command shows the current version of the project or bumps the version of the project and writes the new version back to pyproject.toml if a valid bump rule is provided.

The new version should ideally be a valid semver string or a valid bump rule: patch, minor, major, prepatch, preminor, premajor, prerelease.

```
# show current project version
poetry versoin
# bump current project version
poetry versoin <version-name>
```

## Usage

```
poetry config --local repositories.staging https://foo.bar/simple/
poetry config --unset repositories.foo
```

## Configuration
There are project configuraton file `pyproject.toml` and poetry configuration file `poetry.yaml`.


## Reference
