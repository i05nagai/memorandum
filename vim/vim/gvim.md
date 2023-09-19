---
title: gvim
---

# gvim

##インストール(Win7)
VimShellやVimfilerでunixコマンドを使用するので、cygwinかMSYSをインストールする必要がある。
cygwinは重いので、MSYSのインストールをする。

### MSYSのインストール(32bit)
1. `http://sourceforge.net/projects/mingw/files/`より、`mingw-get-setup.exe`をダウンロード。
2. 実行すると、インストールするパッケージの選択画面になる。
3. `MSYS Basic System`と適当にgccコンパイラ(64bitの場合は、64bitのgccコンパイラを入れるので不要？）を選択し、他はお好むでインストールする。
4. MSYSのインストール先のbinフォルダにPATHを通す。
    * インストール先が`C:\MinGW`なら、`C:\MinGW\msys\1.0\bin`

### MSYSのインストール(64bit)
MSYS32bitのインストールに加えて64bitのMinGW64をインストールする。
`vimproc`の`make-mingw64.mak`では、MinGW64のgccを呼ぶようになっているので、下記を設定を記述し、NeoBundleInstallでOK
```vim
		NeoBundle 'Shougo/vimproc', {
		  \ 'build' : {
			\ 'windows' : 'make -f make_mingw64.mak',
			\ 'cygwin' : 'make -f make_cygwin.mak',
			\ 'mac' : 'make -f make_mac.mak',
			\ 'unix' : 'make -f make_unix.mak',
		  \ },
		\ }
```
1. 下記より64bitインストーラ`mingw-w64-install.exe`をDLする。
    `http://sourceforge.net/projects/mingw-w64/`
2. 起動するとarchitectureの選択がでるので、適当に選択肢、`C:\MinGW64`にインストールする。（どこでも良いが）
    * versionは最新
    * cpu architectureは`x86_64`を選択
    * threadはposix
    * exceptionは`SEF`を選択。win64だと早いらしい。
    * build versionは適当に1を選択。
3. インストールが完了したら、`C:\MinGW64\mingw64\bin`にパスを通す。このとき、MSYSのものより先にパスを通す。

## VimShellのインストール

##NeoBundleのインストール
Gitはインストール済みの前提。
    mkdir %userprofile%\.vim\bundle
    cd %userprofile%\.vim\bundle
    git clone git://github.com/Shougo/neobundle.vim


## option

##カラースキーマについて
とりあえずデフォルトのカラースキーマからよさげなものを選ぶ。
http://nanasi.jp/colorscheme/default_install.html

おすすめは`colorscheme desert`

### wombat
追加でいれるなら以下が良い。
http://www.vim.org/scripts/script.php?script_id=1778

1. 上記サイトから`wombat.vim`をDL
2. `vim73-kaoriya-win64\vim73\colors`に配置。
3. vimrcに`colorscheme wombat`

##gvimrcとvimrcの場所
以下のコマンドでいずれかで確認できる。
windowsの場合は、`%userprofile%`に結びついてるのかも。
windowsの場合、シンボリックリンクを作れば読み込んでくれる。（ショートカットはだめ）
```vimrc
:echo $HOME
:echo $VIM
```


## フォント
vimrcに以下を記載すれば設定可能。
Rictyフォントがおすすめ。
```vim
"半角文字の設定
set guifont=Ricty\ Discord:h12
"全角文字の設定
set guifontwide=Ricty\ Discord:h12
```

