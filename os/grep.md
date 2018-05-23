---
title: grep
---

## grep

## Tips

### Recursively grep
`-r`がsupportされているものとされていないものがある。
OSXはされている。

されている場合は以下でOK。

```
grep -r PATTERN target_directory
```

また不要なディレクトリを除外する場合は

```
grep -r pattern --exclude-dir exclude_dir target_directory
```

`--exclude-dir`は複数指定できる。
逆に指定したディレクトリだけ検索したい場合は、

```
grep -r pattern --include-dir include_dir target_directory
```

`--include-dir`は複数指定できる。

されていない場合は、`find`と組み合わせる

```
find . | grep "pattern"
```

### 不要なディレクトリを除外

```
find path/to/dir -not -path ".git/*" | grep pattern
```



## Reference
* [grep / 文字列を検索する - Qiita](http://qiita.com/shunsakai/items/9187afbd58ffe3925f90)
