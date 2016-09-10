# Git


## 設定
`git config --global`でアカウント共通設定が可能。
* windowsは、`~/.gitconfig`

### alias
下記のようにaliasを設定可能。
```git
git cofing --gloabl alias.st st
```
ただ、一度にaliasを追加する場合やまとめて編集する場合は、`.gitconfig`ファイルを開いて編集した方が楽。
フォーマットは下記の通り。
```
[alias]
	l = log --abbrev-commit --date=iso --graph --pretty=format:'%C(red)%h %C(yellow)%d%C(green)%cd %C(blue)%cn\n%C(reset)%s\n'
```

## windowsでのpushエラー
### 症状
使用しているgitは以下。
```shell
$ git version
git version 2.6.3.windows.1
```

次のコマンドを実行すると、
```shell
git remote add origin https://hogehoge.gihttps://github.com/user_id/hogehoge.git
git push origin master
```
下記のエラーがでる。
```
!!!bash: /dev/tty: No such device or address!!!
!!!error: failed to execute prompt script (exit code 1)!!!
!!!fatal: could not read Username for 'https://github.com': Invalid argument!!!
!!!vimshell: exit 128 "git push origin master"!
```

上記はvimshellでのエラーだが、cmdから直接実行しても同様のエラーがでる。

###対処法?
1. 以下の方法によるが、試してない。
[https://github.com/atom/atom/issues/8984:title]
以下のURLをremote repositoryのURLとして設定する。

```
https://<username>:<password>@github.com/<username>/<repo_name>.git
```
* username:hoge
* password:fuga
* repo_name:hage
の場合
```
git remote add origin https://hoge:fuga@github.com/hage/hage.git
```

2. こちらは、cmd上で動作は確認。vimshell上では未確認。

```
https://hoge@github.com/hage/hage.git
```
とするとパスワードが求められるので、入力する。

## Commit message
一応古典的には下記が原則
1. タイトルの後は1行空けて本文を書く
1. タイトルを50字以内におさめる
1. タイトルの文頭を大文字にする
1. タイトルの文末にピリオドを付けない
1. タイトルは命令形で記述する
1. 本文は1行あたり72字以内におさめる
1. 本文ではどのようにではなく何をとなぜを説明する

```
Summarize changes in around 50 characters or less
 
More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.
 
Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequenses of this
change? Here's the place to explain them.
 
Further paragraphs come after blank lines.
 
 - Bullet points are okay, too
 
 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here
 
If you use an issue tracker, put references to them at the bottom,
like this:
 
Resolves: #123
See also: #456, #789
```

チケット番号を要約に含める場合もある。

### reference
* [Gitのコミットメッセージの書き方 | プログラミング | POSTD](http://postd.cc/how-to-write-a-git-commit-message/)
* [spring-framework/CONTRIBUTING.md at 30bce7fa169df320bbff8e56efe9610449a9d60b · spring-projects/spring-framework](https://github.com/spring-projects/spring-framework/blob/30bce7fa169df320bbff8e56efe9610449a9d60b/CONTRIBUTING.md)
* [tbaggery - A Note About Git Commit Messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)


## windowsでのlocale error
Windowsのgitで`git add -p`をすると以下のエラーがでた。
```
!!!perl: warning: Setting locale failed.!!!
!!!perl: warning: Please check that your locale settings:!!!
!!!	LC_ALL = (unset),!!!
!!!	LANG = "ja"!!!
!!!    are supported and installed on your system.!!!
!!!perl: warning: Falling back to the standard locale ("C").!!!
```
gitは中でperlを呼んでいるが、localeが設定されていないので起こられている。
よってlocaleの設定をしてあげればOK。
Linuxなどの場合は設定方法が色々調べれば出るので、扱わない。
以下ではWindowsでのlocaleの設定方法について述べる。

### 方法1 cmdで設定
cmd上でgitを利用している場合はcmdの環境変数として`LC_ALL`と`LANG`を設定する。
```cmd
set LC_ALL=ja_JP.UTF-8
set LANG=ja_JP.UTF-8
```

### 方法2 環境変数を設定
vimshellなどから使う場合は、環境変数として設定する。
コントロールパネル->システム->詳細タブ->環境変数から以下のように設定する。
* 変数:LC_ALL
* 値:ja_JP.UTF-8
* 変数:LANG
* 値:ja_JP.UTF-8

## patch
gitでpatchを作る場合は以下のようにする。
`--no-prefix`をつけないと、`a/file_name`, `b/file_name`などのファイル名で差分が生成される。

```shell
git diff --no-prefix > diff.patch
```

patchの適用は`patch`コマンドを使う。
```shell
patch -p0 < diff.patch
```

## tips

### Gitの最初のコミットは空コミット
[Gitの最初のコミットは空コミットにしよう](http://qiita.com/NorsteinBekkler/items/b2418cd5e14a52189d19)
最初のコミットは`git rebase -i`できないので、

```shell
# リポジトリ作成
git init
# 最初のコミット
git commit --allow-empty -m "first commit"
```

### reset/checkout
`master`ブランチにいるとする。
`HEAD`は`master`ブランチを指しているとする。

* 最初のコミットのSHA1が`11...`
* 2つ目のコミットのSHA1が`22...`
* `master`は`22...`を指している
* `HEAD`も`22...`を指している

1. `git reset --soft HEAD~`
  * `master`ブランチの指しているコミットが一つ前(`11....`)に戻る
2. `git reset HEAD~` or `git reset --mixed HEAD~`
  * オプションを省略すると`--mixed`がつく
  * この場合は1に加えて、indexに一つ前のコミット(`11....`)をコピーする。
3. `git reset --hard HEAD~`の場合
  * 2に加えて、作業ディレクトリも一つ前のコミット(`11....`)をコピーする。


## hooks

