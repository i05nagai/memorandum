---
title: Flask CLI
---

## Flask CLI

You need to 

```
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
```



## CLI

```
flask run
```

Environment vairables

* `FLASK_APP=hello.py`
* `FLASK_ENV=development`
    * by default flask run `production` mode

* `-h, --host TEXT`
    * The interface to bind to.
* `-p, --port INTEGER`
    * The port to bind to.
* `--cert PATH`
    * Specify a certificate file to use HTTPS.
* `--key FILE`
    * The key file to use when specifying a certificate.
* `--reload / --no-reload`
    * Enable or disable the reloader.
    * By default the reloader is active if debug is enabled.
* `--debugger / --no-debugger`
    * Enable or disable the debugger.
    * By default the debugger is active if debug is enabled.
* `--eager-loading / --lazy-loader`
    * Enable or disable eager loading.
    * By default eager loading is enabled if the reloader is disabled.
* `--with-threads / --without-threads`
    * Enable or disable multithreading.

```
flask
```

## Usage

Run `src/app.py` with `development` mdoe

```
FLASK_APP=src/app.py FLASK_ENV=development flask run
```

## Configuration

## Reference
