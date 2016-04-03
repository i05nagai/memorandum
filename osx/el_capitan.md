# el capitan

## MacportsのUpdate
1. xcodeのupdateをAppSotreから行う。
2.  [https://www.macports.org/install.php](macports dl)からmacportsのパッケージをダウンロードしてインストールする。
3. portのself updateを行う。
```zsh
sudo port selfupdate
```
4. xcodeのtoolsetをupdateする。
```zsh
xcode-select --install
```
5. xcodeのライセンスに同意する。
```zsh
sudo xcodebuild -license
```
6. `sudo port upgrade outdated`を実行する。
    * 前のバージョンを削除する場合は`sudo port -u upgrade outdated`と`-u`をつける。
    * deactiveのものを削除する場合は、install後に`sudo port uninstall inactive`
    * `dyld-headers`をuninstallしろとエラーがでたので、`sudo port uninstall dyld-headers`で削除。

## 文字変換
### ライブ変換
ライブ変換機能がついて、入力中に自動で文字変換してくれるようになったが、邪魔なのでオフにする。
1. `System Preferences`から`Keyboard`を開く
2. `Input Souces`から`Live Conversion`をオフにする。


