---
title: vim-table-mode
---

## vim-table-mode

```
NeoBundle 'dhruvasagar/vim-table-mode'
```

## Usage
`<Leader>tm`か以下のコマンドでtable modeになる。

```
:TableModeToggle
```

この状態で表の一行目を書く。

```
| name | address | phone |
```

2行目で`||`と入力すると

```
| name | address | phone |
|------+---------+-------|
```

となる。
3行目以後は区切りに`|`を入力すれば、列間を適当に調整してくれる。

markdown compatibleにする場合は

```
let g:table_mode_corner='|'
```

restructuredText compatibleにする場合は、

```
let g:table_mode_corner_corner='+'
let g:table_mode_header_fillchar='='
```

既存のtableの整形は`:Tableize`か`<Leader>tt`を使う。


## Reference
* [dhruvasagar/vim-table-mode: VIM Table Mode for instant table creation.](https://github.com/dhruvasagar/vim-table-mode)
