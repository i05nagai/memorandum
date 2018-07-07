---
title: base64
---

## base64

## BSD

```
Usage:  base64 [-hvD] [-b num] [-i in_file] [-o out_file]
  -D, --decode   decodes input
  -b, --break    break encoded string into num character lines
  -i, --input    input file (default: "-" for stdin)
  -o, --output   output file (default: "-" for stdout)
```

## GNU

```
  -d, --decode          decode data
  -i, --ignore-garbage  when decoding, ignore non-alphabet characters
  -w, --wrap=COLS       wrap encoded lines after COLS character (default 76).
```

GNU base64は出力を折り返して表示する。
折り返しなしにする場合は、以下でBSDと同じ出力になる。
`--wrap`でもできるが、BSDと互換性がなくなる。
GNU trの`-d`はどちらにもある。

```
echo 'aaa' | base64 | tr -d '\n'
```

* `--wrap 72`
    * default 72 charで折り返し
    * 0で折り返しなし
* `--decode`

```
echo 'aaa' | base64 --wrap=0
```

## Reference
