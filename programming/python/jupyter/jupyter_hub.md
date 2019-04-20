---
title: Jupyter Hub
---

## Jupyter Hub


## CLI

```
jupyterhub <subcommand> <option>
```

Subcommands

* `token`
    * Generate an API token for a user
* `upgrade-db`
    * Upgrade your JupyterHub state database to the current version.

Arguments that take values are actually convenience aliases to full
Configurables, whose aliases are listed on the help line. For more information
on full configurables, see '--help-all'.

* `--debug`
    * set log level to logging.DEBUG (maximize logging output)
* `--generate-config`
    generate default config file
* `--no-db`
    disable persisting state database to disk
* `--upgrade-db`
    * Automatically upgrade the database if needed on startup.
    * Only safe if the database has been backed up.
    * Only SQLite database files will be backed up automatically.
* `--no-ssl`
   * [DEPRECATED in 0.7
* `--base-url=<URLPrefix> (JupyterHub.base_url)`
    * Default: `/`
    * The base URL of the entire application.
    * deprecated: 0.9
    * Use JupyterHub.bind_url
* `-y <Bool> (JupyterHub.answer_yes)`
    * Default: `False`
    * Answer yes to any questions (e.g. confirm overwrite)
* `--ssl-key=<Unicode>` (JupyterHub.ssl_key)
    * Default: ''
    * Path to SSL key file for the public facing interface of the proxy
    * When setting this, you should also set ssl_cert
* `--ssl-cert=<Unicode> (JupyterHub.ssl_cert)`
    * Default: ''
    * Path to SSL certificate file for the public facing interface of the proxy
    * When setting this, you should also set ssl_key
* `--url=<Unicode> (JupyterHub.bind_url)`
    * Default: 'http://:8000'
    * The public facing URL of the whole JupyterHub application.
    * This is the address on which the proxy will bind. Sets protocol, ip, base_url
* `--ip=<Unicode> (JupyterHub.ip)`
    * Default: ''
    The public facing ip of the whole JupyterHub application (specifically
    referred to as the proxy).
    This is the address on which the proxy will listen. The default is to listen
    on all interfaces. This is the only address through which JupyterHub should
    be accessed by users.
    * deprecated: 0.9
    * Use JupyterHub.bind_url
* `--port=<Int> (JupyterHub.port)`
    * Default: 8000
    The public facing port of the proxy.
    This is the port on which the proxy will listen. This is the only port
    through which JupyterHub should be accessed by users.
    .. deprecated: 0.9
        Use JupyterHub.bind_url
* `--pid-file=<Unicode> (JupyterHub.pid_file)`
    Default: ''
    File to write PID Useful for daemonizing JupyterHub.
* `--log-file=<Unicode> (JupyterHub.extra_log_file)`
    * Default: ''
    * DEPRECATED: use output redirection instead, e.g.
    * `jupyterhub &>> /var/log/jupyterhub.log`
* `--log-level=<Enum> (Application.log_level)`
    Default: 30
    Choices: (0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')
    Set the log level by value or name.
* `-f <Unicode> (JupyterHub.config_file)`
    * Default: 'jupyterhub_config.py'
    * The config file to load
* `--config=<Unicode> (JupyterHub.config_file)`
    Default: 'jupyterhub_config.py'
    The config file to load
* `--db=<Unicode> (JupyterHub.db_url)`
    Default: 'sqlite:///jupyterhub.sqlite'
    url for the database. e.g. `sqlite:///jupyterhub.sqlite`


## Usage

```
jupyterhub --help-all
```


generate default config file:

```
jupyterhub --generate-config -f /etc/jupyterhub/jupyterhub_config.py
```

spawn the server on 10.0.1.2:443 with https:

```
jupyterhub \
    --ip 10.0.1.2 \
    --port 443 \
    --ssl-key my_ssl.key \
    --ssl-cert my_ssl.cert
```

## Configuration

## Reference

