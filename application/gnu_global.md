# Gnu Global
etagsやctagsのような

## feature
pygmentsを使うと対応言語を増やせる。

* supports C, C++, Yacc, Java, PHP4 and assembly.
* works the same way across diverse environments like follows:
    * Shell command line
    * Bash shell
    * Vi editor (Nvi, Elvis, vim)
    * Less viewer
    * Emacs editor (Emacs, Mule, Xemacs)
    * Web browser
    * Doxygen documentation system 
* finds locations of specified symbol quickly.
* locates not only definitions but also references.
* allows duplicate tags.
* locates paths which matches to the specified pattern.
* hierarchical searches by default.
* searches not only in a source project but also in library projects.
* generates completion list for completing input method.
* supports various output formats.
* allows customizing of a set of candidate files to be tagged.
* understands POSIX 1003.2 regular expression.
* supports idutils as an external search engine.
* tag files are independent of machine architecture.
* supports incremental updating of tag files.
* plug-in parser is available to treat new language.
* supports customizing using ‘gtags.conf’.
* generates a hypertext of source code.
* compact format to save disk space.
* supports client/server environment (TRAMP ready).
* ignores binary files, dot files and specified files.
* includes cscope-compatible program (gtags-cscope).
* includes grep-like command (-g command).
* supports grep-like symbol highlighting. 


## Install
### Mac
pygments optionをつけておけば、defaultのparserで対応していない言語まで対応可能。

```shell
brew install global --with-pygments
```

## Usage

```
gtags -v
```

### with pygments

```
gtags --globallabel=pygments
```


## vim
globalのインストール先に、vim scriptがインストールされるので、vim上でも同様に使える。
* `/path/to/global/share/gtags/gtags.vim`

| :Gtags 関数名        | 関数名 → ソースコード（定義） |
|----------------------|-------------------------------|
| :Gtags -r 関数名     | 関数名 → ソースコード（参照） |
| :Gtags -f ファイル名 | ソースコード → 関数一覧       |
| :Gtags -g 検索文字列 | ソースコードの grep           |

## Reference
* [ソースコードを快適に読むための GNU GLOBAL 入門 (前編) - まちゅダイアリー(2009-03-07)](http://www.machu.jp/diary/20090307.html#p01)
* [GNU GLOBAL source code tag system](https://www.gnu.org/software/global/manual/global.html)
