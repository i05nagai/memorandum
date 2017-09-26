---
title: calibre
---

## Calibre

## Install
for OSX

```
brew cask install calibre
```

## From kindle to pdf

* [How to Convert a Kindle Ebook to PDF | Digital Trends](http://www.digitaltrends.com/mobile/how-to-convert-kindle-to-pdf/)
* [Dealing with Kindle for PC/Mac 1.19 and KFX in calibre - MobileRead Forums](https://www.mobileread.com/forums/showthread.php?t=283371)


```
chmod -x /Applications/Kindle.app/Contents/MacOS/renderer-test
```

kindle本は,Kindle->Preferenceで登録されているdirectoryに保存されている。
defaultでは、`/Library/Application Supports/Kindle/My Kindle Content/`
これでkindleからpdfに変換ができるようになるが、DRMがついているものについては変換できない。
多くの本にはDRMがついているので、変換はきたいしない方が良い。


## Reference
* [calibre - Download for OS X](https://calibre-ebook.com/download_osx)
