---
title: twine
---

## twine
Upload distributions to PyPI.

## Install
```
pip install twine
```

## CLI

```
twine upload <dist>
```
* `dist`
    * The distribution files to upload to the repository
                        (package index). Usually dist/* . May additionally
                        contain a .asc file to include an existing signature
                        with the file upload.

optional arguments:

* `-r REPOSITORY, --repository REPOSITORY`
    * The repository (package index) to upload the package to.
    * Should be a section in the config file
        * (default: pypi).
        * (Can also be set via TWINE_REPOSITORY environment variable.)
* `--repository-url REPOSITORY_URL`
    * The repository (package index) URL to upload the package to.
    * This overrides --repository.
    * (Can also be set via TWINE_REPOSITORY_URL environment variable.)
* `-s, --sign`
    * Sign files to upload using GPG.
* `--sign-with SIGN_WITH`
    * GPG program used to sign uploads (default: gpg).
* `-i IDENTITY, --identity IDENTITY`
    * GPG identity used to sign files.
* `-u USERNAME, --username USERNAME`
    * The username to authenticate to the repository (package index) as.
    * (Can also be set via TWINE_USERNAME environment variable.)
* `-p PASSWORD, --password PASSWORD`
    * The password to authenticate to the repository (package index) with.
    * (Can also be set via TWINE_PASSWORD environment variable.)
* `-c COMMENT, --comment COMMENT`
    * The comment to include with the distribution file.
* `--config-file CONFIG_FILE`
    * The .pypirc config file to use.
* `--skip-existing`
    * Continue uploading files if one already exists.
    * (Only valid when uploading to PyPI. Other implementations may not support this.)
* `--cert path`
    * Path to alternate CA bundle (can also be set via TWINE_CERT environment variable).
* `--client-cert path`
    * Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.

```
twine register [-h] -r REPOSITORY [--repository-url REPOSITORY_URL]
                      [-u USERNAME] [-p PASSWORD] [-c COMMENT]
                      [--config-file CONFIG_FILE] [--cert path]
                      [--client-cert path]
                      package
```

positional arguments:

* package
    * File from which we read the package metadata.

optional arguments:

* `-r REPOSITORY, --repository REPOSITORY`
    * The repository (package index) to register the package to.
    * Should be a section in the config file.
    * (Can also be set via TWINE_REPOSITORY environment variable.)
    * Initial package registration no longer necessary on pypi.org
* `--repository-url REPOSITORY_URL`
    * The repository (package index) URL to register the package to.
    * This overrides --repository.
    * (Can also be set via TWINE_REPOSITORY_URL environment variable.)
* `-u USERNAME, --username USERNAME`
    * The username to authenticate to the repository (package index) as.
    * (Can also be set via TWINE_USERNAME environment variable.)
* `-p PASSWORD, --password PASSWORD`
    * The password to authenticate to the repository (package index) with.
    * (Can also be set via TWINE_PASSWORD environment variable.)
* `-c COMMENT, --comment COMMENT`
    * The comment to include with the distribution file.
* `--config-file CONFIG_FILE`
    * The .pypirc config file to use.
* `--cert path`
    * Path to alternate CA bundle (can also be set via TWINE_CERT environment variable).
* `--client-cert path`
    * Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.

## Usage
Upload to PyPI.

```
python setup.py sdist bdist_wheel
twine upload dist/*
```

## Reference
* [Tool recommendations — Python Packaging User Guide](https://packaging.python.org/guides/tool-recommendations/)
* [twine · PyPI](https://pypi.org/project/twine/)

