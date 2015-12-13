# bat

## 一行で複数コマンド
```cmd
command1 & command2
```
ショートカットにcmdプロンプトを設定するとき、下記のようにコマンドをいくつか実行したショートカットを設定できる。
```
%comspec% /k "cmd1 & cmd2"
```

## ファイル移動
`move from to`

## ないもの
* 配列
* ハッシュ

## 相対パス
bat内の相対パスは、実行場所からの相対パスで、batファイルの場所からではない。
## コマンドプロンプトのホームディレクトリの設定
ショートカットでcmdを起動する場合に、作業フォルダに指定したディレクトリがホームディレクトリになる。

## 管理者として実行
* cmdやbatを実行する場合に、プロパティ->ショートカットタブ->詳細設定->管理者として実行にチェックで管理者として実行可能。
* コマンドを選択して実行する時に、Ctrl+Shift+Enter

## %の扱い
batファイル内で`%`を文字列として渡したい場合は、`%%`とする。
変数に`%%`とつけるのはそのため。

## comment
```bat
rem comment here
```

## 変数の宣言
`=`の前後に空白は入れない。変数に小数は代入できない。
```bat
SET 変数名=[文字列]
SET /A 変数名=[数式]
```

## 文字列
文字列の長さを求めるコマンドはない。
```bat
SET str1=abc
SET str2=de f
SET str2= g hi
rem 結合
SET str1=aaa
SET str2=bbb
SET str3=%str1%%str2%              … aaabbb
```
文字列の切り出し
```bat
:: 切り出し
SET str1=abcd
SET str2=%str1:~0,2%               … ab（1桁目（オフセット0）から2文字）
```

## redirect
`>>`で追記。
```bat
input.bat > output.txt
input.bat >> output.txt
```

## alias
```bat
doskey マクロ名=テキスト


## for文、if文を複数行に書くときの注意
http://tounderlinedk.blogspot.jp/2011/01/if-windowsbatcmd.html

## 文字コードの変換
```bat
chcp charcter_code
```
* character_code
    * 437      IBM437        OEM United States
    * 932      shift_jis     ANSI/OEM Japanese; Japanese (Shift-JIS)
    * 1200     utf-16        Unicode UTF-16, little endian byte order (BMP of ISO 10646); available only to managed applications
    * 20127    us-ascii      US-ASCII (7-bit)
    * 20932    EUC-JP        Japanese (JIS 0208-1990 and 0121-1990)
    * 50220    iso-2022-jp   ISO 2022 Japanese with no halfwidth Katakana; Japanese (JIS)
    * 50222    iso-2022-jp   ISO 2022 Japanese JIS X 0201-1989; Japanese (JIS-Allow 1 byte Kana - SO/SI)
    * 51932    euc-jp        EUC Japanese
    * 65001    utf-8         Unicode (UTF-8)

## シンボリックリンクの作成
cmdで以下のコマンドを実行。
```cmd
mklink link target
mklink path\to\link path\to\target
```
* link:シンボリックリンク名
* リンクが参照するパス
* `/D`でディレクトリへのリンク
* `/H`でハードリンク
* `/J`ディレクトリジャンクション

## ファイル一覧
```bat
@echo off
echo -----------------------フルパス
for %%A in (*.txt) do echo %%~fA
echo -----------------------ドライブ名
for %%A in (*.txt) do echo %%~dA
echo -----------------------親パス
for %%A in (*.txt) do echo %%~pA
echo -----------------------ファイル名
for /F %%A in ('dir /b *.txt') do echo %%A
echo -----------------------ファイル名（拡張子抜き）
for %%A in (*.txt) do echo %%~nA
echo -----------------------拡張子
for %%A in (*.txt) do echo %%~xA
```

## ファイル削除
ディレクトリの削除はできない。
```bat
del (option) [file / directory] 
```

## ディレクトリ削除
```bat
rmdir directory
```
* `/s`
    * ファイルやサブディレクトリも含めて削除する

## for文
```bat
for %variable in (<pattern>) do <command-line>
for /D %variable in (<pattern>) do <command-line>
for /R [[<drive-letter>:]<path>] %variable in (<pattern>) do <command-line>
for /L %variable in (<start>,<step>,<end>) do <command-line>
for /F ["<options>"] %variable in (<pattern>) do <command-line>
```
* %variable
    * 「variable」には1文字の英数字を指定します。この変数は、下記の <command-line> で用いることができ、使用すると列挙中のファイル名に置き換えられます。大文字・小文字が区別されます。

複数行に書くときは`()`で囲む。
```bat
foir %variable in (<pattern>) do (

)
```
閉じるときの`)`は行頭に置く。

## if文
```bat
IF 条件 (
    処理
) ELSE (
    処理
)
```
条件
```bat
IF [NOT] ERRORLEVEL 番号 コマンド
IF [NOT] 文字列1==文字列2 コマンド
IF [NOT] EXIST ファイル名 コマンド
IF 文字列1 比較演算子 文字列2 コマンド
```

比較演算子
* EQU - 等しい
* NEQ - 等しくない
* LSS - より小さい
* LEQ - 以下
* GTR - より大きい
* GEQ - 以上
