---
title: osx
---

## osx

## OS X で Shift+Space で入力ソースを切り替える方法
* [OS X で Shift+Space で入力ソースを切り替える方法 | Carpe Diem](https://www.sssg.org/blogs/naoya/archives/2579)
* [Defaults & symbolichotkeys in Mac OS X - krypted.com](http://krypted.com/mac-os-x/defaults-symbolichotkeys/)

xcodeが必要。

```
open ~/Library/Preferences/com.apple.symbolichotkeys.plist
```

```
# you can find list of keycode
vim /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/Headers/Events.h
```

1. 61 > value > parameters > item 2 の値を 1572864 を Shift のキーコードである 131072 に変更
    * default opt+ctrl+space
    * 32
    * 49
    * 786432
2. 60 > value > parameters > item 2 の値を 1048576 を Option-Shift キーの値である 655360 に変更
    * default ctrl+space
    * 32
    * 49
    * 262144
3. 保存して再起動する

System Preferences->Keyboard->Shortcutsの一覧がこのファイルに記録されている。
直にshort cut keyを書き換えることで、強引にショートカットとしてShiftを割り当てている。


## Writing Extern HDD

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


### Install

1. fuse for osxをインストール

```zsh
sudo port install osxfuse
```

2. NTFSドライバをインストール

```zsh
sudo port install ntfs-3g
```

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

## Socks
* [ssh経由のSOCKSプロキシを通じてMac上のGoogle Chromeでブラウジング](http://blog.wktk.co.jp/ja/entry/2014/03/11/ssh-socks-proxy-mac-chrome)

## Tips

#### mds_worker 
* [What is mds\_stores process? \- Apple Community](https://discussions.apple.com/thread/5595772)
    * Meta Data Server
    * mds_worker
    * mds_stores
* [mds – what MDS process is and why it uses CPU on the Mac](http://osxdaily.com/2010/08/05/mds-mac/)

Disable spotlights.

#### Disabling spotlights
[MacOS Sierra: Enable/Disable Spotlight Indexing](https://www.technipages.com/macos-sierra-enable-disable-spotlight)

disable

```
From the Apple menu, choose “Restart…” > “Restart“.
Simultaneously press and hold the “Command” and “R” buttons. This will start you in Recovery Mode.
Select “Utilities” > “Terminal“.
Type one of the following, then press “Enter“:
Disable System Integrity Protection: csrutil disable
Enable System Integrity Protection: csrutil enable
```

```
# Enable Indexing
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist
# Disable Indexing
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist
```

#### Share iPad screen
* [How to Draw & Display your iPad LIVE in a video chat — Catherine Madden](http://catherinemaddenrelay.com/blog/2017/12/20/ipadtutorial)
* [Good Ways to Mirror iPad to Mac](https://airmore.com/share-ipad-screen-on-mac.html)
* [Tip: Record your iPad's screen on your Mac with QuickTime Player](https://appleinsider.com/articles/18/03/26/tip-record-your-ipads-screen-on-your-mac-with-quicktime-player)


* Connect iPad with a cable
* Open QuickTime
* File -> New Moview Recording
* Change Camera to `iPad`

#### Decompress zip file compressed in Windows without garbling text

* Use 7z
    * it does not work

```
brew install p7zip
```

* Use python script
    * [rekka/unzip\-jp: Unzip zip archives from Japanese systems on non\-Japanese ones](https://github.com/rekka/unzip-jp)
    * it works

#### What to do before you sell
* [What to do before you sell, give away, or trade in your Mac \- Apple Support](https://support.apple.com/en-us/HT201065)
* [Erase process failed \- couldn't open devi… \- Apple Community](https://discussions.apple.com/thread/7739562)

* Sign out
    * iTunes
    * iCloud
    * iMessage
* Remove bluetooth paired devices
* Erase disk
    * [How to erase a disk for Mac \- Apple Support](https://support.apple.com/en-us/HT208496#why)
    * unmount all volumes belongs to the disk before easing the disk
* Reinstall OSX

#### Stop iTunes from opening when you conenct your iPhone
[Stop iTunes from opening when you connect your iPhone \- CNET](https://www.cnet.com/how-to/stop-itunes-from-opening-when-you-connect-your-iphone/)

* Preferences -> Devices

## Reference
* [Macのデスクトップ切り替え時のエフェクトを減らして、切り替えを多少すばやくする - Qiita](http://qiita.com/ikedakenno/items/58daf8a961f1813b3c1b)
* [macOSでディスプレイ1枚で作業する技術 - Qiita](http://qiita.com/saboyutaka/items/d6cfd2a2b60f1a374d60)
