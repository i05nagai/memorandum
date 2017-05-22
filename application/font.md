## Font

## Ricty

To OSX

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
