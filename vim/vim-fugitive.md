# vim-fugitive
gitのplugin

## shortcut
| gitコマンド            | vim-fugitive      | 備考                                                                        |
|------------------------|-------------------|-----------------------------------------------------------------------------|
| git status             | :Gstatus          | 各ファイルの行を選択した状態で、[-]でadd/resetしたり[D]でdiff取ったりできる |
| git add                | :Gwrite           | ファイルをaddできるが、行指定のaddはできないっぽい                          |
| git checkout FILE_NAME | :Gread            | 修正がよくわかんなくなった時でもパパッとHEADの状態に元通り！                |
| git commit             | :Gcommit          | コミット。言わずもがな。                                                    |
| git blame              | :Gblame           | ファイルの各行がどのコミットのものか調べる                                  |
| git diff               | :Gdiff [revision] |                                                                             |
| git log                | :Glog             |                                                                             |
| git mv                 | :Gmove            |                                                                             |
| git rm                 | :Gremove          |                                                                             |
