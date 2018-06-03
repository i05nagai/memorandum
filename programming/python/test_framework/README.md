## unit testing framework
pytest が良い。

| テストツール      | 特徴                                                                                                 | カバレッジ |
|-------------------|------------------------------------------------------------------------------------------------------|------------|
| unittest          | Python標準パッケージに含まれている単体テストライブラリ                                               | ×          |
| Django + unittest | Django の manage.py ユーティリティから、unittest が便利に使うことができる                            | ×          |
| nose              | 多彩なオプションで柔軟なテストができ、カバレッジを取ることもできる。特定のクラスを継承する必要がない | ○          |
| django-nose       | Django の manage.py ユーティリティから、nose を使えるようにしたもの                                  | ○          |

### nose

```
pip install nose
pip install coverage
```

noseの命名規則

* [Finding and running tests — nose 1.3.7 documentation](http://nose.readthedocs.io/en/latest/finding_tests.html)

### reference
* [Python, Django 界隈の単体テスト事情（unittest / nose / django-nose） - akiyoko blog](http://akiyoko.hatenablog.jp/entry/2015/01/01/212712)
* [Python nose でユニットテストを書いてみた / 桃缶食べたい。](http://blog.chocolapod.net/momokan/entry/80)
