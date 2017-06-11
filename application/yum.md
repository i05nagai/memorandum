## yum

```
man 5 yum.conf
man yum
```



```
sudo yum install package_name
```

いらないパッケージの削除
yum eraseのalias

```
sudo yum remove package_name
```

すでに不要な依存packageを削除

* [Removing packages with dependencies - Ask Fedora: Community Knowledge Base and Support Forum](https://ask.fedoraproject.org/en/question/33785/removing-packages-with-dependencies/)

```
sudo yum autoremove
```

install可能なpackage一覧

```
yum list available
```
