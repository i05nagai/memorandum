# windows

## console
ConEmuがよさそう。
Chocolatelyがあれば次でOK.
```
choco install conemu
```

## Windowsでパッケージ管理
Chocolatelyは、Windowsのパッケージマネージャー。
Linuxのapt-getとかmacのmacportsとかhomebrewの類のもの。
[Chocolately](https://chocolatey.org/)

### インストール
インストールは既定のディレクトリのデータの展開とパスを通すだけ。
レジストリ等は汚さないので、コントロールパネルからアンインストールなどもできない。（する意味がいない）

1. cmdかpowershellを管理者として実行で起動する。
2. 以下を実行すると、`C:\ProgramData\chocolatey\`にインストールされる。
    * cmdの場合
```bat
 @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
```
    * powershellの場合
```bat
iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
```

### 機能
オプションはUnix系のオプション指定`/h`ではなく`-h`などで指定可能。
* インストール
```
choco install git
```
* アンインストール
```
choco uninstall git
```
* 検索
```
choco search git
```
* localのパッケージ一覧
```
clist -l
```
* help
```
choco -h
```

### メモ
```
choco install 7zip.install 
choco install ruby
choco install jruby
```


## pdfのテキスト抽出
Xpdfで抽出できる。
[link](http://www.foolaBs.com/xpdf/download.html "link")
解凍するとbinフォルダに変換用のexeが入っているので目的に合わせて変換する。 
ただソースコードなどは綺麗にとれない。

## IME

### Ctrl+Spaceで半角全角切り替え
IME->プロパティ->全般タブ->編集操作のキー設定の変更
* IMEのオン/オフ
    * 半角全角
* 既定の検索
    * 既定の検索プロバイダで検索
* 選択して検索
    * 検索プロバイダを指定して検索

## フォント

### Ricty
https://github.com/yascentur/Ricty

Windwosでは下記のように生成

1.以下をDL
    * Ricty
        * https://github.com/yascentur/Ricty
    * unofficial fontfrge
        * http://www.geocities.jp/meir000/fontforge/index.html
        * `fontforge-cygwin_2015_01_21.zip`をDL
    * Inconsolata
        * https://www.google.com/fonts#UsePlace:use/Collection:Inconsolata
        * 右のDLからダウンロード。
    * Migu_1M
        * http://mix-mplus-ipa.osdn.jp/migu/
        * `migu-1m-20150712.zip`をDL
2. 作業用のtempディレクトリを適当に作成し以下を配置。

| 解凍フォルダ                    | 移動対象ファイル、フォルダ                               |
|---------------------------------|--------------------------------------------------------  |
| Rictyフォント生成生成スクリプト | `ricty_generator.sh,ricty_discord_patch.pe,miscフォルダ` |
| unofficial fontforge            | fontforge.bat,`_image.7z`,`7zr.exe`                      |
| Inconsolata                     | Inconsolata.otf                                          |
| Migu 1M                         | migu-1m-regular.ttf,migu-1m-bold.ttf                     |

3. `fontforge.bat`の下記を修正

変更前
```bat
xwin-close.exe -wait
fontforge.exe -nosplash %file0% %1 %2 %3 %4 %5 %6 %7
xwin-close.exe -close
```
変更後
```bat
xwin-close.exe -wait
sh ricty_generator.sh auto
sh misc/os2version_reviser.sh Ricty-*.tty RictyDiscord-*.ttf
xwin-close.exe -close
```

4. cmdから`fontforge.bat`を実行すると以下が作成されるので、インストール。
    * Ricty-Regular.ttf
    * Ricty-Bold.ttf
    * RictyDiscord-Regular.ttf
    * RictyDiscord-Bold.ttf
