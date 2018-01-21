---
title: Google Chrome
---

## Google Chrome

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

## Reference
* [Chrome keyboard shortcuts - Google Chrome Help](https://support.google.com/chrome/answer/157179?hl=en)
