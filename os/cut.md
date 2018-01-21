---
title: cut
---

## cut


## GNU cut

```
cut -b list [-n] [file ...]
cut -c list [file ...]
cut -f list [-d delim] [-s] [file ...]
```

* `-d`
    * delimiter
    * defaultはtab
* `-n`
    * multibyte characgerをsplitしない
* `-b`
* `-f`
    * delimiterでsplit後の指定したfiledだけ表示
* `-c`

```
cut -d : -f 1,7 /etc/passwd
who | cut -c 1-16,26-38
```

## Reference
