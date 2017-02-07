## python module


## from hoge import *の意味

```
from fibo import *
```

上の操作は、アンダースコア (_) で開始する名前以外の全ての名前を import します。
モジュールやパッケージから * を import するのはだめ。
というのは、この操作を行うとしばしば可読性に乏しいコードになるからです。

## モジュール検索のパス
`sys.path`のパスを検索する。
`sys.path`は以下で構成される。

* スクリプトのあるディレクトリ (あるいはカレントディレクトリ)。
* 環境変数`PYTHONPATH`に記載のパス
* installerごとに設定されるパス

## Pythonファイルのコンパイル
拡張子が`*.pyc`のプログラムがコンパイル後のPythonプログラム。

* `*.pyc`には`*.py`ファイルの修正時刻が記録されており、実行時の`*.py`の修正時刻と一致しなければ`*.pyc`ファイルは無視される
* `*.pyc`は自動で作られる
* 無事コンパイルされるとコンパイルが成功したバージョンを`*.pyc`として書き出すが、失敗してもエラーにはならない
* 書き出しが途中で失敗した場合は、`*.pyc`は無視される
* `*.pyc`の内容はプラットフォーム(OSなど）に依存しない

### 起動時間短縮のTips
* Python実行時に`-O`をつけると最適化されたバイトコードが`*.pyo`ファイルに生成される
    * 最適化は2.7では`assert`分と`SET_LINNO`命令を削除するだけ
    * 最適化される場合は、`*.pyc`ファイルは無視される
* `-OO`をつけると、`-O`の最適化に加え`__doc__`文字列を削除する
    * プログラムが`__doc__`に依存していると正しく動作しなくなる
* **`*.pyo`や`.pyc`はファイルの読みこみが早くなるだけで、動作速度はかわらない**
* `compilleall`コマンドは、`.pyc`ファイル（`-O`があるときは、`.pyo`）
    * `python -m compileall <path>`で`<path>`以下の`*.py`ファイルをコンパイルする
    * [32.11. compileall — Python ライブラリをバイトコンパイル — Python 2.7.x ドキュメント](http://docs.python.jp/2/library/compileall.html)
* `python script.py`では`.pyc`ファイルなどは作られない
    * スクリプトをmoduleにして、importすると`pyc`が生成されるので起動時間が短縮できる

## 6.2. 標準モジュール
* 標準モジュールの一部はOSに依存している為、windowsにしかないモジュールなどもある
* `sys`は全てのPythonインタープリタに存在する

## 6.3 dir()関数
* `dir(some_module)`は`some_module`モジュールに定義されている名前を列挙
* 引数なし`dir()`の場合は組み込み関数や変数以外の現在定義されている全ての名前を列挙
* 組み込み関数や変数を表示する場合は`dir(__builtin__)`

## 6.4 パッケージ

## Pacaging and Distributing Projects
* [Packaging and Distributing Projects — Python Packaging User Guide documentation](https://packaging.python.org/distributing/)
* [GitHub - pypa/sampleproject: A sample project that exists for PyPUG's "Tutorial on Packaging and Distributing Projects"](https://github.com/pypa/sampleproject)
* [Building and Distributing Packages with Setuptools — Setuptools documentation](http://setuptools.readthedocs.io/en/latest/setuptools.html)
* [How To Add Custom Build Steps and Commands To setup.py - Season of Code](https://seasonofcode.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy.html)
* [Python: セットアップスクリプト (setup.py) に自作のコマンドを追加する - CUBE SUGAR CONTAINER](http://blog.amedama.jp/entry/2015/09/17/224627)

## Reference
* [6. モジュール — Python 2.7.x ドキュメント](http://docs.python.jp/2/tutorial/modules.html)
* [Packaging and Distributing Projects — Python Packaging User Guide documentation](https://packaging.python.org/distributing/)
