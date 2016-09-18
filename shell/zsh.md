# zsh

## completion
`~/.zshrc`に以下を追加する。

```zsh
fpath=(~/.zsh/completion/folder $fpath)
```
 
`~/.zsh/completion/folder`においてあるzshの補完用ファイルが読み込まれる。
`/usr/share/zsh`以下にzshの設定ファイルがあり、デフォルトの補完ファイルもこの中に存在する。

### zhs-completions

#### reference
* [zsh-users/zsh-completions: Additional completion definitions for Zsh.](https://github.com/zsh-users/zsh-completions)
* [まだ oh-my-zsh で消耗してるの？ - Qiita](http://qiita.com/b4b4r07/items/875235f6122a6d779306)
