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

## Options

`-D`と`-L`のportfowarding

* [SSH Port ForwardingでLAN内のサーバにリモートアクセスする - ももいろテクノロジー](http://inaz2.hatenablog.com/entry/2013/04/30/221348)

* `-D`
    * port forwarding するときに使う
* `-L`
    * port forwarding するときに使う

```
ssh -fNL 8080:kmc.gr.jp:80 hogehoge@forward.kuins.kyoto-u.ac.jp
```

## config
* [~/.ssh/configについて - Qiita](http://qiita.com/passol78/items/2ad123e39efeb1a5286b)
* [`Include`キーワードで`ssh_config`を分割できるようになった件 - Qiita](http://qiita.com/masa0x80/items/ecb692ad93f7d06a07b0)

```
# サーバーへ定期的(今回は60秒毎)に生きている報告をする(全体的に記述を有効にする場合は先頭辺りに書いておくといい)
ServerAliveInterval 60

# 個別に有効にしたい場合は、個別の設定に行を開けないで追記しておくといい
Host 任意の接続名(hoge)
    HostName ホスト名(IP/host)
    User ユーザー名(user_name)
    Port ポート番号(22)
    IdentityFile 鍵へのPATH(例えば~/.ssh/hoge.key)
    ServerAliveInterval 60
    # ssh -L 1111:proxy.domain:2222 user_name@where.is.myhost
    LocalForward    1111    proxy.domain:2222
    ForwardAgent    yes
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
    ServerAliveInterval 300
    TCPKeepAlive yes
```

```
ssh hoge
```

* `ForwardAgent yes`
    * [ssh-agentの基本 - Qiita](http://qiita.com/yudoufu/items/82f752807893c63f06db)
    * `-A` optionと同じ

* [楽しいトンネルの掘り方(オプション: -L, -R, -f, -N -g) — 京大マイコンクラブ (KMC)](https://www.kmc.gr.jp/advent-calendar/ssh/2013/12/09/tunnel2.html)

* `-f`
    * sshでloging後にバックグラウンドへ
* `-N`
    * 何もしない



