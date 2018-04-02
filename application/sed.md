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
* [sed, a stream editor: Command-Line Options](https://www.gnu.org/software/sed/manual/html_node/Command_002dLine-Options.html#Command_002dLine-Options)

```
sed SCRIPT INPUTFILE...
```

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

sedのcommandの形式

```
[addr]X[options]
```

`X`はsignle-letter sed command.
`[addr]`は`[addr]`にmatchしたlineにのみ処理を適用する。
30,35行目のdelete

```
sed '30,35d' input.txt > output.txt
```


ファイルの中身を置換

```
sed -i -e "s/REPLACER/REPLACEE/g" /path/to/file
```

### regular expression
* [Regular Expressions - sed, a stream editor](https://www.gnu.org/software/sed/manual/html_node/Regular-Expressions.html)
* [sed, a stream editor: BRE vs ERE](https://www.gnu.org/software/sed/manual/html_node/BRE-vs-ERE.html#BRE-vs-ERE)

Basic Regular Expression (BRE)と Extended Regular Expression (ERE)がある。
`-E`でEREが使える。

* `\(regexp\)`

### Commands
* [sed, a stream editor: Other Commands](https://www.gnu.org/software/sed/manual/html_node/Other-Commands.html#Other-Commands)
* [sed, a stream editor: sed commands list](https://www.gnu.org/software/sed/manual/html_node/sed-commands-list.html#sed-commands-list)
* [sed, a stream editor: Multiple commands syntax](https://www.gnu.org/software/sed/manual/html_node/Multiple-commands-syntax.html#Multiple-commands-syntax)

`sed 's//'`などの`s`はcommand

* `s///[we] (substitute with e or w flags)`

## Reference
* [sed コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/sed.html)
