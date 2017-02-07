
## config
vim-quickrunのデフォルトの設定が参考になる。

* [vim-quickrun/quickrun.vim at 637aa0f9eab485874eb3606be35586735855d880 · thinca/vim-quickrun](https://github.com/thinca/vim-quickrun/blob/637aa0f9eab485874eb3606be35586735855d880/autoload/quickrun.vim)

以下でconfigのhelpが見られる

```vim
:help b:quickrun_config
```

defaultの設定を以下に記載する。

```vim
 \   "_" : {
"bufferへの出力がからの時はbufferを閉じる
 \       "hook/close_buffer/enable_empty_data" : 1,
"失敗した時閉じる。失敗した時はquickfixでみるので
 \       "hook/close_buffer/enable_failure" : 1,
"成功しても閉じる。成功してたらどうでも良い
 \       "hook/close_buffer/enable_success" : 1,
 \       "hook/close_quickfix/enable_exit" : 1,
 \       "hook/close_quickfix/enable_success" : 1,
 \       "hook/close_unite_quickfix/enable_hook_loaded" : 1,
 \       "hook/time/enable" : 1,
 \       "hook/unite_quickfix/enable_failure" : 1,
 \       "outputter" : "multi:buffer:quickfix",
 \       "outputter/buffer/split" : "rightbelow",
 \       "runner" : "vimproc",
 \       "runner/vimproc/updatetime" : 40,
 \   },
```

## Reference
* [quickrun.vim について語る - C++でゲームプログラミング](http://d.hatena.ne.jp/osyo-manga/20130311/1363012363)
* [shabadou.vim を使って quickrun.vim をカスタマイズしよう - C++でゲームプログラミング](http://d.hatena.ne.jp/osyo-manga/20120919/1348054752)
* [quickrun.vim で make する - C++でゲームプログラミング](http://d.hatena.ne.jp/osyo-manga/20130316/1363403701)
