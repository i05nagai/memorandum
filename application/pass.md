
## Install

for mac,

```
brew install pass
echo "source /usr/local/etc/bash_completion.d/password-store" >> ~/.bashrc
```

## Usage

```
pass init gpgkey
```

* `gpgkey`にはGnuPGの公開鍵を指定

```
pass insert EC/amazon.co.jp/filename
```

```
pass insert -m EC/amazon.co.jp/filenma2
```

複数行のデータを入力する場合は`-m`とする。

```
pass show -c EC/amazon.co.jp/filename
```

filenameに保存されている値を表示する。
`-c`がない場合は標準出力に表示、ある場合はクリップボードにコピーされる。

```
pass git init
```

一度pass git initすれば、passwordの追加、削除時に自動でcommitされる。
また、diffも平文でのdiffをとるように `.gitattribute`に必要な設定が記録される。
但し、`git push`をするには`git remote add`などの設定は別途必要。

## Introducing pass
* `gpg`で暗号化
* `~/.password-store`に保存される
* `git`で変更が管理される
* 全ての操作でgitのcommitが作られる
* password storeを同期する場合は、`pass git push`と`pass git pull`をする

## Setting it up

```
zx2c4@laptop ~ $ pass init "ZX2C4 Password Storage Key"
mkdir: created directory ‘/home/zx2c4/.password-store’
Password store initialized for ZX2C4 Password Storage Key.
```

* `ZX2C4 Password Storage Key`はGPG keyのID
* password storeをgit repositoryとして初期化

```
zx2c4@laptop ~ $ pass git init
Initialized empty Git repository in /home/zx2c4/.password-store/.git/
zx2c4@laptop ~ $ pass git remote add origin kexec.com:pass-store
```



## Data Organization

### Usernames, Passwords, PINs, Websites, Metadata, etcetera
* passはplainなtext fileと同じようにpassword以外の保存にも使える
* 例えば、passowrdと秘密の質問のようなものも一緒に保存できる
* 複数行の情報を保存する場合は`--multiline`か`-m`を`insert`コマンドのoptionとして指定する
* `Amazon/bookreader`の場合は以下のような

```
Yw|ZSNH!}z"6{ym9pI
URL: *.amazon.com/*
Username: AmazonianChicken@example.com
Secret Question 1: What is your childhood best friend's most bizarre superhero fantasy? Oh god, Amazon, it's too awful to say...
Phone Support PIN #: 84719
```

* 別の方法としてfolderを利用する方法もある
    * `Amazon/bookreader/password`にpassword
    * `Amazon/bookreader/secretquestion1`に秘密の質問
    * `Amazon/bookreader/sensitivecode`

## Reference
* [Pass: The Standard Unix Password Manager](https://www.passwordstore.org/)
