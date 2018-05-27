---
title: Vim Vimscript
---

## Vim Vimscript

```vim
:echo expand("%")
"# => カレントファイルの名前を出力

:echo expand("%:p")
"# => カレントファイルのフルパスを出力

:echo expand("%:r")
"# => カレントファイルの名前、拡張子抜きを出力

:echo expand("%:e")
"# => カレントファイルの拡張子を出力
```

## Reference
