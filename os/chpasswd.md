---
title: chpasswd
---

## chpasswd
Change passwords.


## CLI

```
chpasswd
```

* `-c, --crypt-method METHOD`
    * the crypt method (one of NONE DES MD5 SHA256 SHA512)
* `-e, --encrypted`
    * supplied passwords are encrypted
* `-m, --md5`
    * encrypt the clear text password using the MD5 algorithm
* `-R, --root CHROOT_DIR`
    * directory to chroot into
* `-s, --sha-rounds`
    * number of SHA rounds for the SHA*

## Usage

```
echo 'root:<password>' | chpasswd
```

## Configuration

## Reference
