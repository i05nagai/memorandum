---
title: Google Chrome
---

## Google Chrome

## Install

For ubuntu,

https://askubuntu.com/questions/510056/how-to-install-google-chrome

```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update
sudo apt-get install -y google-chrome-stable
```

## Shortcut keys

For OSX

* 戻る
    * `cmd+[`
* 進む
    * `cmd+]`

## Socks
* [ssh経由のSOCKSプロキシを通じてMac上のGoogle Chromeでブラウジング](http://blog.wktk.co.jp/ja/entry/2014/03/11/ssh-socks-proxy-mac-chrome)

## Developer tools

## Addon
* [Chromeをvimライクに使えるようにするvimium - Qiita](https://qiita.com/satoshi03/items/9fdfcd0e46e095ec68c1)
* [Vimium - the hacker's browser](http://vimium.github.io/)


## Headless mode
* [ヘッドレス Chrome ことはじめ  |  Web  |  Google Developers](https://developers.google.com/web/updates/2017/04/headless-chrome?hl=ja)
* [Using headless Chrome as an automated screenshot tool](https://medium.com/@dschnr/using-headless-chrome-as-an-automated-screenshot-tool-4b07dffba79a)

```
/path/to/chrome \
  --headless \
  --disable-gpu \
  --remote-debugging-port=9222 \
  https://www.chromestatus.com
```

Dump DOM

```
chrome --headless --disable-gpu --dump-dom https://www.chromestatus.com/
```

Print PDF

```
chrome --headless --disable-gpu --print-to-pdf https://www.chromestatus.com/
```

Take a screenshot.
画像はcurrent directoryに保存される

```
# Nexus 5X
chrome --headless --disable-gpu --screenshot --window-size=412,732 https://www.chromestatus.com/
```

## CLI
* [List of Chromium Command Line Switches « Peter Beverloo](https://peter.sh/experiments/chromium-command-line-switches/)
    * list of opitons

* `--allow-file-access-from-files`

## Release channel
* https://www.chromium.org/getting-involved/dev-channel

* stable
* beta
    * minimal riskで新しい機能を試せる
* dev channel
* canary
    * buildごとに作成されたrelease

```
rew tap caskroom/versions
brew cask install google-chrome-canary
```

## Configuration

* `chrome://flags/#overscroll-history-navigation `
    * overscrollでforward/back

## devtools

#### remote debugging
- https://developer.chrome.com/blog/devtools-mobile/



## Tips

### google account require login each time in ubuntu
* [linux \- Chrome doesn't remember browser sessions after restart \- Super User](https://superuser.com/questions/1130862/chrome-doesnt-remember-browser-sessions-after-restart)

google accountに毎回loginを要求される。

* `Online account` -> `Google account`を追加
* Google ChromeのSettingsからbackgroundで動く設定をdisableにする
    * settingsからsearchでbackgroundといれれば出る


Solution
To fix this issue you need to unlock your keyring before launching chrome.

* Disconnect your Google account; go to chrome://settings click Disconnect your Google Account... check the box to clear local Chrome data, sign out and then close Chrome.
* Launch seahorse by typing seahorse into the terminal or open it from Menu>Passwords and Keys.
* In Default keyring delete Chrome Safe Storage and any accounts.google.com enteries.
* Unlock the Default Keyring and Login by right clicking and clicking Unlock
* Launch Chrome, go to chrome://settings and click Sign in to Chrome
* Hopefully this fixes your problem, I recently installed Linux Mint and this worked for me, I don't fully understand why but it seems Chrome does not wait for the keyring to unlock and this results in chrome not being signed in.

Reproduce This Issue
Steps to reproduce this issue:

Install Linux (mint or otherwise) with cinnamon (on a VM or otherwise)
Install Chrome and sign in
Reboot
Ensure Keyrings are locked - go to Passwords and Keys and lock all Keyrings
Open chrome - you will be prompted to unlock the Keyring and sign in will fail

## Reference
* [Chrome keyboard shortcuts - Google Chrome Help](https://support.google.com/chrome/answer/157179?hl=en)
