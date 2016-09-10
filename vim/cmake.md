# cmake.vim

## Installs
NeoBundleが使える。
以下でOK。

```vim
NeoBundleLazy 'jalcine/cmake.vim', {
    \ "autoload": {
    \	"filetypes": ["cmake"],
    \ },
    \ "build": {
    \	"mac": "rake",
    \	"unix": "rake",
    \ }}
```

デフォルトだと`CmakeList.txt`がcmakeのファイルと認識されないので以下を`vimrc`の適当な場所に追加しておく。
```vim
augroup CmakeSettings
    autocmd!
    autocmd BufNewFile,BufRead CmakeList.txt set filetype=cmake
augroup END
```

