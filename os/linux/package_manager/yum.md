---
title: yum
---

## yum

```
man 5 yum.conf
man yum
```

## CLI


## Usage
```
yum install package_name
```

Eraise unused package. This is an alias for `yum-erase`.

```
yum remove package_name
```

Remove the unused packages including its dependencies

* [Removing packages with dependencies - Ask Fedora: Community Knowledge Base and Support Forum](https://ask.fedoraproject.org/en/question/33785/removing-packages-with-dependencies/)

```
sudo yum autoremove
```

Show list of available packages

```
yum list available
```

```
yum list installed
```


Show dependencies of the package

```
yum deplist <package>
```

```
yum repolist
```

Removes all cached package downloads and cached headers that contain information about remote packages. 

```
yum clean all
```

## Reference
- [2\.4 Using Yum from the Command Line](https://docs.oracle.com/cd/E37670_01/E37355/html/ol_creating_yum_repo.html)
