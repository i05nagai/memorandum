# osx

## OS X で Shift+Space で入力ソースを切り替える方法
* [OS X で Shift+Space で入力ソースを切り替える方法 | Carpe Diem](https://www.sssg.org/blogs/naoya/archives/2579)
* [Defaults & symbolichotkeys in Mac OS X - krypted.com](http://krypted.com/mac-os-x/defaults-symbolichotkeys/)

xcodeが必要。

```
open ~/Library/Preferences/com.apple.symbolichotkeys.plist
```

1. 61 > value > parameters > item 2 の値を 1572864 を Shift のキーコードである 131072 に変更します
2. 60 > value > parameters > item 2 の値を 1048576 を Option-Shift キーの値である 655360 に変更します
3. 保存して再起動する

System Preferences->Keyboard->Shortcutsの一覧がこのファイルに記録されている。
直にshort cut keyを書き換えることで、強引にショートカットとしてShiftを割り当てている。


## 外付けドライブへの書き込み
### 事前設定
`/sbin`のMountを書き換えるので、事前にrootユーザをONにする。
1. Apple メニューから「システム環境設定」を選択します。
2. 「表示」メニューから「ユーザとグループ」を選択します。
3. 鍵アイコンをクリックし、管理者アカウントで認証します。
4. 「ログインオプション」をクリックします。
5. 右下の「編集」または「接続」ボタンをクリックします。
6. 「ディレクトリユーティリティを開く」ボタンをクリックします。
7. 「ディレクトリユーティリティ」ウインドウの鍵アイコンをクリックします。
8. 管理者アカウント名とパスワードを入力し、「OK」をクリックします。
9. 「編集」メニューから「ルートユーザを有効にする」を選択します。
10. 利用するルートパスワードをパスワードフィールドとその確認用フィールドに入力し、「OK」をクリックします。

ログインする場合
1. すでにログインしている状態の場合は、Apple メニューから「ログアウト」を選択します。
2. 画像付きのユーザ名のリストを使ってログインしている場合は、「その他」をクリックします。
3. 「名前」フィールドに「root」と入力します。
4. 「パスワード」フィールドに、ルートユーザアカウントの設定時に定義したパスワードを入力します。


### インストール

1. fuse for osxをインストール
```zsh
sudo port install osxfuse
```
2. NTFSドライバをインストール
```zsh
sudo port install ntfs-3g
```
3. 


## update

### zsh

```shell
# check the zsh info
brew info zsh

# install zsh
brew install --without-etcdir zsh

# add shell path
sudo vim /etc/shells

# add the following line into the very end of the file(/etc/shells)
/usr/local/bin/zsh

# change default shell
chsh -s /usr/local/bin/zsh
```
