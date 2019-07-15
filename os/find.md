---
title: find
---

## find
findコマンドの使い方

## Usage

```
find [option] [path...] [expression]
find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
```

### Expression
よく使うもの。

expressionは`-and`, `-or`, `-not`で条件づけることができる。

ファイル名の条件

```
-name pattern
```

ファイルのタイプで検索。

* `type_str`
    * `d`
        * ディレクトリ
    * `f`
        * ファイル
    * `l`
        * symbolic link

```
-type type_str
```

階層の制限

```
-mindepth 1
-maxdepth 2
```

```
-path "pattern"
```

## Tips

### patternを含むpathを除外

```
findd path/to/dir -not -path "*/pattern/*"
```

#### Exclude some directories

```
find /path/to/search \
  -type d \( -path '*/.git' -o -path '*/somedir' \) -prune -o \
  -type f
```

## Reference
* [Linuxコマンド集 - 【 find 】 ファイルやディレクトリを検索する：ITpro](http://itpro.nikkeibp.co.jp/article/COLUMN/20060227/230777/)
