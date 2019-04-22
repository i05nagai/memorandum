---
title: debconf
---

## debconf
Debian package configuration system.

## CLI

```
debconf [options] command [args]
```

* `-o,  --owner=package`
    * Set the package that owns the command.
* -f,  --frontend
    * Specify debconf frontend to use.
* -p,  --priority
    * Specify minimum priority question to show.
* --terse
    * Enable terse mode.

## Forntends
- `readline`
- `dialog`
- `noninteractive`
- `gnome`
- `kde`
- `editor`
- `web`


## Usage

## Configuration

## Reference
- [Ubuntu Manpage: debconf \- Debian package configuration system](http://manpages.ubuntu.com/manpages/xenial/man7/debconf.7.html)
- [The Debconf Programmer's Tutorial](http://www.fifi.org/doc/debconf-doc/tutorial.html)
