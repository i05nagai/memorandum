## sed

* `-n`
    * replaceしたする行を出力しない
* `-e`
    * 

シェル変数を使う場合は、シェル変数の部分のみ引用符を外す。

```
sed -e 's/hoge/a'"$var"'/g'
```

## Reference
* [sed コマンド | コマンドの使い方(Linux) | hydroculのメモ](https://hydrocul.github.io/wiki/commands/sed.html)
