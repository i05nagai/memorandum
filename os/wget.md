---
title: wget
---

## wget

```
wget -c
```

* `-c`, `--continue`
    * resume donwloading
* `-P <prefix>`
    * `--directory-prefix=prefix`
    * prefix of downloaded file
    * path to directory of downloading file
    * filename in URL is used as the filename of downloading file

```
cat urls.txt | xargs -n 1 -P 6 wget -c -P ~/klarna-data/data/
```

## Reference
* [GNU Wget 1\.18 Manual](https://www.gnu.org/software/wget/manual/wget.html)
