## ag

## Install

### mac

```
brew install ag
```

or

```
brew install the_silver_searcher
```

どちらも一緒。
zshであればtabでoptionの補完がきく。

## usage
hoge を文字列として含むファイルをカレントディレクトリから再帰的に調べる。

```shell
ag hoge
```

| オプション | 意味                               |
|------------|------------------------------------|
| -a         | 無視リストも対象                   |
| -u         | 隠しファイルおよび無視リストも対象 |
| -g         | ファイル名で検索                   |
| -G         | 検索対象の指定 [ag -G *.css]       |
| -l         | 一致したファイル名のみ             |
| -L         | 一致していないファイル名のみ       |
| -v         | 不一致検索                         |
| -Q         | 正規表現を無視                     |
| -z         | 圧縮ファイルも対象                 |

対応している言語を表示

```
ag --list-file-types
```


| FILE TYPE | suffix                                  |
|-----------|-----------------------------------------|
| --cc      | .c .h .xs                               |
| --cpp     | .cpp .cc .C .cxx .m .hpp .hh .h .H .hxx |
| --html    | .htm .html .shtml .xhtml                |
| --java    | .java .properties                       |
| --js      | .js .jsx                                |
| --perl    | .pl .pm .pm6 .pod .t                    |
| --php     | .php .phpt .php3 .php4 .php5 .phtml     |
| --python  | .py                                     |
| --ruby    | .rb .rhtml .rjs .rxml .erb .rake .spec  |
| --shell   | .sh .bash .csh .tcsh .ksh .zsh          |
| --xml     | .xml .dtd .xsl .xslt .ent               |
| --yaml    | .yaml .yml                              |


## Reference
* [The Silver Searcher のススメ - Qiita](http://qiita.com/thermes/items/e1e0c94e2875df96921c)

