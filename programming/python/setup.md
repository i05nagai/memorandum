# setup.py
`setup.py`の書き方など。

## setup.py sdist
platformに応じたソースコードの配布物を生成する。
Unixの場合は`.tar.gz`で、Windowsの場合は`.zip`がデフォルト。
`--formats`オプションで生成するファイルは指定可能。

```
python setup.py --formats=gztar,zip 
```

配布するファイルの指定は以下の規則で解釈される。
* `py_modules` と `packages` オプションに指定された Python ソースファイル全て
* `ext_modules` オプションと `libraries` オプションで挙げられている C ソースファイル全て



# Reference

* [4. ソースコード配布物を作成する — Python 2.7.x ドキュメント](http://docs.python.jp/2/distutils/sourcedist.html)
