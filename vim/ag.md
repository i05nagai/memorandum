# ag.vim

## Install

```vim
NeoBundle 'rking/ag.vim''
```

## Usage

| コマンド      | 結果                                               |
|---------------|----------------------------------------------------|
| :Ag           | カレントディレクトリを再帰的に検索して quickfix へ |
| :AgAdd        | :Ag同様だが結果を追加                              |
| :AgFromSearch | 前回の検索パターンを使用(/による検索など)          |
| :LAg          | :Ag同様だが、結果を location-list へ               |
| :LAgAdd       | :AgAdd同様だが、結果を location-list へ            |
| :AgFile       | ファイル名の検索                                   |
| :AgHelp       | vimのドキュメントが検索対象                        |

### quickfix

| コマンド | 内容                     |
|----------|--------------------------|
| e        | 開くと同時に終了         |
| o        | 開く                     |
| go       | プレビュー               |
| t        | タブで開く               |
| T        | タブで開く(silently)     |
| h        | 水平分割で開く           |
| H        | 水平分割で開く(silently) |
| v        | 垂直分割で開く           |
| gv       | 垂直分割で開く(silently) |
| q        | 終了                     |

## reference
* [agでvimの検索関連を高速化 - Qiita](http://qiita.com/0829/items/7053b6e3371592e4fbe6)
