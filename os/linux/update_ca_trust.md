---
title: update-ca-trust
---

## update-ca-trust

## Install

```
yum install ca-certificates
```


## CLI

```
update-ca-trust <subcommand>
```

- subcommads
    - extract
    - check
    - enable
    - disable
    - force-enable
    - force-disable

## Usage

To add a certificate in the simple PEM or DER file formats to the list of CAs trusted on the system
In Centos, place certificate in `/etc/pki/ca-trust/source/anchors/`

```
# Update 
update-ca-trust extract
```

If your certificate is in the extended BEGIN TRUSTED file format (which may contain distrust/blacklist trust flags, or trust flags for usages other than TLS) then
Add it `/etc/pki/ca-trust/source/`

```
update-ca-trust extract
```

## Configuration

- `/usr/share/pki/ca-trust-source/`
    - CA certificates and trust settings in the PEM file format
    - lower priority
- `/etc/pki/ca-trust/source/`
    - CA certificates and trust settings in the PEM file format
    - higher priority


## Reference
- [Adding trusted root certificates to the server](https://manuals.gfi.com/en/kerio/connect/content/server-configuration/ssl-certificates/adding-trusted-root-certificates-to-the-server-1605.html)
- [update\-ca\-trust command man page \- ca\-certificates](https://www.mankier.com/8/update-ca-trust)
- [How do you add a certificate authority \(CA\) to Ubuntu? \- Super User](https://superuser.com/questions/437330/how-do-you-add-a-certificate-authority-ca-to-ubuntu)
