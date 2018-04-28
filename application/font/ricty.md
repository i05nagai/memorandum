---
title: Ricty
---

## Ricty


For OSX

```
brew tap sanemat/font
brew cask install xquartz
brew install autoconf
brew install automake
brew install pkg-config
brew install ricty --with-powerline
cp -f /usr/local/Cellar/ricty/3.2.4/share/fonts/Ricty*.ttf ~/Library/Fonts/
fc-cache -vf
```

For Ubuntu 16.04

```
sudo apt-get install fontforge fonts-inconsolata
wget http://www.rs.tus.ac.jp/yyusa/ricty/ricty_generator.sh
```

```
#!/bin/sh

sudo apt-get install fontforge

mkdir -p ~/.local/share/fonts

TMPDIR=$(mktemp -d /tmp/ricty-XXXXX)
cd $TMPDIR

# miku
wget http://iij.dl.sourceforge.jp/mix-mplus-ipa/59022/migu-1m-20130617.zip
unzip migu-1m-*.zip
cp migu-1m-*/*.ttf .

# incosolat
wget https://github.com/google/fonts/raw/master/ofl/inconsolata/Inconsolata-Regular.ttf
wget https://github.com/google/fonts/raw/master/ofl/inconsolata/Inconsolata-Bold.ttf

# ricty
wget http://www.rs.tus.ac.jp/yyusa/ricty/ricty_generator.sh
bash ricty_generator.sh Inconsolata-{Regular,Bold}.ttf migu-1m-{regular,bold}.ttf

cp *.ttf ~/.local/share/fonts/

rm -rf $TMPDIR

fc-cache -f -v
fc-list | grep Ricty
```

## Reference
