# powershell

## 初期設定

## スクリプト実行
### セキュリティポリシー
デフォルトではpowershellは実行できない。
powershellから次を実行する。
```ps1
Set-ExecutionPolicy RemoteSigned
```

### 実行
cmdからは以下のコマンドで`file.ps1`を実行。
拡張子は`ps1`でないといけない。
```cmd
PowerShell -File file.ps1
```

### セキュリティなし実行
powershellの場合は以下で`runme.ps1`をセキュリティポリシーなしで実行できる。
```ps1
GC .runme.ps1 | iex
```
cmdからは次でOK
```ps1
PowerShell.exe -ExecutionPolicy UnRestricted -File .runme.ps1
```

## 基本構文

### if

### for
```ps
foreach(一時変数 in 配列、コレクション){
}
```

## tips

### ファイル一覧
```ps1
foreach($file in ls -name) {
	$file
}
```

###参考
[1](http://qiita.com/opengl-8080/items/bb0f5e4f1c7ce045cc57)
[powershell](http://winscript.jp/powershell/202)
[PowerShell from Japan!! Blog](http://blog.powershell-from.jp/)
