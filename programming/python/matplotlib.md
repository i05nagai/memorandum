# matplotlib

## pyplot

### pyenvで動かす

`matplotlibrc`の38行目の

```
backend : macosx
```

これを

```
backend : Tkagg
```

に変更。
`matplotlibrc`の場所は以下のコマンドでわかる。

```shell
$python -c "import matplotlib;print(matplotlib.matplotlib_fname())"
```

### Reference
* [pyenvとvirtualenvで環境構築した時にmatplotlib.pyplotが使えなかった時の対処法 - Qiita](http://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49)

# Reference
* [matplotlib入門 - りんごがでている](http://bicycle1885.hatenablog.com/entry/2014/02/14/023734)

