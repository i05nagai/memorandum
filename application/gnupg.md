---
title: GnuPG
---

## GnuPG
作成した自分の秘密鍵はなくすとどうしようもないので、何らかの方法でbackupする必要がある。
秘密鍵の出力は、出力用のコマンドがある。
また出力した秘密鍵のgpgへの登録も同様のコマンドがある。

## CLi


## Usage
Show the list of registered private key

```
gpg --list-secret-keys
```

Show the list of registered public key

```
gpg --list-keys
```

binary形式で相手に渡す公開鍵の作成(export)

* `-o <filename>`
    * output file name
* `key_user_id`
    * user id that you used when you create the key

```
gpg -o ./my.pub --export key_user_id
```

binary形式で秘密鍵の作成(export)

* `-o <filename>`
    * output filename
* `key_user_id`
    * 鍵作成じに指定したuser id

```
gpg -o my.pri --export-secret-key key_user_id
```

受け取った公開鍵/秘密鍵のimport

```
gpg --import my.pub 
gpg --import my.pri
```

importした鍵の信用。
実行すると、対話モードとなるので、`trust`コマンドを実行する

```
gpg --edit-key key_user_id
gpg> trust
```

```
gpg [-o ファイル名] [-r 鍵ユーザID] 暗号化ファイル
```

Configure default key

```
gpg --default-key <user-id>
```

import my key in another host.
You need to trust the imported key.

```
$ gpg --import /path/to/private.key
$ gpg --edit-key <KEY-ID>
...
...
# run trust command
# and choose trust ultimately
gpg> trust
...
...
Please decide how far you trust this user to correctly verify other users' keys
(by looking at passports, checking fingerprints from different sources, etc.)

  1 = I don't know or won't say
  2 = I do NOT trust
  3 = I trust marginally
  4 = I trust fully
  5 = I trust ultimately
  m = back to the main menu

Your decision? 5

gpg> quit
```


## Reference
* [gpgでのファイルの暗号化基礎 - akihiro_obの日記](http://d.hatena.ne.jp/akihiro_ob/20120131/1328031230)
* [gnupg](http://www.math.s.chiba-u.ac.jp/~matsu/gpg/)
* [GnuPG で遊ぶ - 暗号化してみる | そんなこと覚えてない](http://blog.eiel.info/blog/2013/07/31/gpg/)
* [GnuPrivacyGuardHowto - Community Help Wiki](https://help.ubuntu.com/community/GnuPrivacyGuardHowto)
* [GnuPGのコマンド](http://www.nina.jp/server/windows/gpg/commands.html)
* [GPG Cheat Sheet](http://irtfweb.ifa.hawaii.edu/~lockhart/gpg/)
* [14\. 別のホストPCでGnuk Tokenを使う設定 — Gnuk handbook 1\.1 documentation](http://no-passwd.net/fst-01-gnuk-handbook/using-gnuk-token-with-another-computer.html)
