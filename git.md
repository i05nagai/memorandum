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

