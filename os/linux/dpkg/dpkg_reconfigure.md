---
title: dpkg-reconfigure
---

## dpkg-reconfigure


## CLI

```
dpkg-reconfigure [options] packages
```

* -u,  --unseen-only
    * Show only not yet seen questions.
* --default-priority
    * Use default priority instead of low.
* --force
    * Force reconfiguration of broken packages.
* --no-reload
    * Do not reload templates. (Use with caution.)
* -f,  --frontend
    * Specify debconf frontend to use.
* -p,  --priority
    * Specify minimum priority question to show.
* --terse
    * Enable terse mode.

## Usage

```
dpkg-reconfigure -f noninteractive <package>
```

## Configuration

## Reference
