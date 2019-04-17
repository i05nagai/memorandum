---
title: GnuPG
---

## GnuPG
作成した自分の秘密鍵はなくすとどうしようもないので、何らかの方法でbackupする必要がある。
秘密鍵の出力は、出力用のコマンドがある。
また出力した秘密鍵のgpgへの登録も同様のコマンドがある。

## CLI


## Usage

Create gpg key. Recommended way.

```
gpg --full-generate-key

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 0
Key does not expire at all
Is this correct? (y/N) y

Real name: <your-name>
Email address: <your-email>
Comment:
You selected this USER-ID:
    "<your-name> <your-email>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
```

Create gpg key.

```
gpg --default-new-key-algo rsa4096 --gen-key
Real name: <your name>
Email address: <your-email-address>
You selected this USER-ID:
    "<your name> <your-email-address>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit? o
```

Show the list of registered private key

```
gpg --list-secret-keys
```

Show the list of registered public key

```
gpg --list-keys
```

Export public keys as binary format


* `-o <filename>`
    * output file name
* `key_user_id`
    * user id that you used when you create the key

```
gpg -o ./my.pub --export key_user_id
```

Export private keys as binary format

* `-o <filename>`
    * output filename
* `key_user_id`
    * user id specified when you create key

```
gpg -o my.pri --export-secret-key key_user_id
```

Importing received public/private ssh key

```
gpg --import my.pub 
gpg --import my.pri
```

Trust imported keys with interactive mode.
In interactive mode, you can use `trust` command to trust the key.

```
gpg --edit-key key_user_id
gpg> trust
```

```
gpg [-o filename] [-r key-userid] <encrypted-file>
```

Delete imported public keys. If you have corresponding private key, you need to delete private key first.

```
gpg --delete-key <key-user-id>
```

Delete imported private key

```
gpg --delete-secret-key <key-user-id>
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
