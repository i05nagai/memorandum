---
title: tr
---

## tr

replace 

```
tr '\n' ' '
```

delete newline

```
tr -d '\n'
```

delete nelines and convert double quote to single quote

```
cat /path/to/file | tr '\n' ' ' | sed 's/"/\x27/g'
```

## Reference
