---
title: CURL
---

## curl


```
curl -v -D
```

HTTPのheaderのdebugで有用なオプション。

* `-v`はverbose。
* `-D`は
* `-C <offset>`
    * `-C -`
        * resume download
        * HTTP server must support bytes ranges
* `-o <path-to-local>`
* `-O`
    * store downloaded content as filename in URL

download

```
curl -0 <URL> > file.html
```

Resume downloading

```

```
