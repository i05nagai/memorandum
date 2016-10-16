# open-ssh

## keyを作る

```shell
sh-keygen -t rsa

```

## server
ログインしたいuserを`ssh-user`とする。
* loginするuserのhome directoryの下(`~/.ssh/`)に設定ファイルを。
* `~/.ssh/authorized_keys`にログインするユーザの公開鍵をいれる
    * `cat id_rsa.pub >> ~/.ssh/authorized_keys`
    * file permissionは`chmod 600 authorized_keys`
    * userとgroupはログインするユーザ(`ssh-user`)のもの
        * `chown ssh-user:ssh-user authorized_keys`

## client
* sshでの接続時のPassは、キー作成時のpass phraseでlogin userのpasswordではない。
* sshでアクセスする時、pass phraseを設定してないのにpassが求められるとき
    * identity fileが読み込めてない

## debug
client側のdebugは`-v`
server側のdebugは`-d`
