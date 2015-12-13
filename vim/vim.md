# vim

## netrw
* ファイル作成
    * %


## vimfilerでファイルのbookmark
uniteが必須。
1. vimfilerで適当なディレクトリを開く
2. bookmarkに追加したディレクトリにカーソルを置き、`a`を押しアクションを起動後、`bookmark`を選択
3. `Please input bookmark file name`と聞かれる。カーソルに選択しているディレクトリがデフォルトのinput file/directoryになるので、EnterでOK
4. `Please input bookmark entry name`と聞かれる。bookmarkの別名を聞かれているので、わかりやすい名前をつける。
5. `:Unite bookmark`でbookmarkの一覧が表示できる。
    * bookmarkの削除は、`d`で行える。
	* bookmarkを開く場合は、`Enter`でUnite上でディレクトリが開かれる。
	* `t`や`e`でファイルを開いたりできる。

## コマンドモードで貼り付け
`:vimfiler `を入力中に、`<Ctr-R>"`で貼り付けできる。

## vimでコードのformatを整える
Normalモードで`=`を押すと、カーソル行以下のフォーマットを整える。
Visual Modeで選択している場合は、選択範囲内を整える。

## バッファを閉じる
`:bd`

