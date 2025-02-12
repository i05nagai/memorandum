---
title: libnss-wrapper
---

## libnss-wrapper
Name Server Switch Wrapper.

libnss-wrapper is a library that allows applications to use arbitrary passwd and group files in environments where they would not normally be available, such as in containers or chroot environments.


Applications
- Containerized Applications
    - Many applications require users and groups from /etc/passwd and /etc/group. However, in containerized environments, these files might not exist or might be read-only. libnss-wrapper allows applications to use alternative files for user and group information.


Under the hood

- Interposes NSS Calls: The library intercepts calls to functions like getpwnam(), getpwuid(), getgrnam(), etc., and redirects them to user-defined files.

## Install

```
sudo apt-get install libnss-wrapper
sudo yum install libnss_wrapper
sudo zypper install libnss_wrapper
```


## Configuraition
- NSS_WRAPPER_PASSWD: Path to the alternative passwd file.
- NSS_WRAPPER_GROUP: Path to the alternative group file.

## Reference
- https://packages.debian.org/sid/libnss-wrapper
