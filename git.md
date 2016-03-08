# Git

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


