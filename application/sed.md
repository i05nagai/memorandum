---
title: sed
---

## sed

* `-n`
    * replaceしたする行を出力しない
* `-e`

シェル変数を使う場合は、シェル変数の部分のみ引用符を外す。

```
sed -e 's/hoge/a'"$var"'/g'
```

## GNU sed

* -n, --quiet, --silent
    * suppress automatic printing of pattern space
* -e script, --expression=script
    * add the script to the commands to be executed
* -f script-file, --file=script-file
    * add the contents of script-file to the commands to be executed
* --follow-symlinks
    * follow symlinks when processing in place
* -i[SUFFIX], --in-place[=SUFFIX]
    * edit files in place (makes backup if SUFFIX supplied)
*  -l N, --line-length=N
    * specify the desired line-wrap length for the l command
* --posix
    * disable all GNU extensions.
* -r, --regexp-extended
    * use extended regular expressions in the script.
* -s, --separate
    * consider files as separate rather than as a single continuous long stream.
* -u, --unbuffered
    * load minimal amounts of data from the input files and flush the output buffers more often
* -z, --null-data
    * separate lines by NUL characters

ファイルの中身を置換

```
sed -i -e "s/REPLACER/REPLACEE/g" /path/to/file
```

## Reference
* [sed コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/sed.html)
