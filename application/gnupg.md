---
title: GnuPG
---

## GnuPG
作成した自分の秘密鍵はなくすとどうしようもないので、何らかの方法でbackupする必要がある。
秘密鍵の出力は、出力用のコマンドがある。
また出力した秘密鍵のgpgへの登録も同様のコマンドがある。


## Commands
秘密鍵の確認

```
gpg --list-secret-keys
```

公開鍵の確認

```
gpg --list-keys
```

binary形式で相手に渡す公開鍵の作成(export)

* `-o`
    * 出力ファイル名
* `key_user_id`
    * 鍵作成じに指定したuser id

```
gpg -o ./my.pub --export key_user_id
```

binary形式で秘密鍵の作成(export)

* `-o`
    * 出力ファイル名
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


## Reference
* [gpgでのファイルの暗号化基礎 - akihiro_obの日記](http://d.hatena.ne.jp/akihiro_ob/20120131/1328031230)
* [gnupg](http://www.math.s.chiba-u.ac.jp/~matsu/gpg/)
* [GnuPG で遊ぶ - 暗号化してみる | そんなこと覚えてない](http://blog.eiel.info/blog/2013/07/31/gpg/)
* [GnuPrivacyGuardHowto - Community Help Wiki](https://help.ubuntu.com/community/GnuPrivacyGuardHowto)
* [GnuPGのコマンド](http://www.nina.jp/server/windows/gpg/commands.html)
