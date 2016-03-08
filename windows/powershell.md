# powershell

## 初期設定
起動時に下記の`profile.ps1`が読み込まれる。
ExecutionPolicyの設定が必要。
```
%windir%\system32\WindowsPowerShell\v1.0\profile.ps1
%windir%\system32\WindowsPowerShell\v1.0\Microsoft.PowerShell_profile.ps1
%USERPROFILE%\Documents\WindowsPowerShell\profile.ps1
%USERPROFILE%\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

ExecutionPolicyなしで同等のことをする場合は、powershellのショートカットを次のようにする。
```ps1
C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe -NoExit -ExecutionPolicy UnRestricted -File C:\Users\admin\Documents\WindowsPowerShell\01_setup.ps1
```
これで、起動時に`01_setup.ps1`に書かれている内容が読み込まれる。


## alias
- 組み込みAliasの取得
-- `get-alias` or `gal`
- コマンド->alias
-- `gal -Definition set-alais`
- aliasの設定
-- `set-alias -name list -value get-children`

### 引数つきのalias
関数を作ってaliasを設定する。
```ps1
function __cdh {cd $home}
sal cdh __cdh
```

## プロンプト変更
`profile.ps1`で`prompt`関数を上書きする。
サンプル。
```ps1
function Prompt
{
    $promptString = "PS " + $(Get-Location) + ">"
   
    # Custom color for Windows console
    if ( $Host.Name -eq "ConsoleHost" )
    {
        Write-Host ("[") -nonewline -foregroundcolor DarkGray
        Write-Host ($env:username) -nonewline -foregroundcolor DarkCyan
        Write-Host ("@") -nonewline -foregroundcolor DarkGray
        Write-Host (hostname) -NoNewline -ForegroundColor DarkGreen
        Write-Host (" ") -nonewline -foregroundcolor DarkGray
        write-host (shorten-path (pwd).Path) -nonewline -foregroundcolor DarkYellow
        Write-Host ("]") -nonewline -foregroundcolor DarkGray
        Write-Host ("#") -nonewline -foregroundcolor DarkMagenta
 
    }
    # Default color for the rest
    else
    {
        Write-Host $promptString -NoNewline
    }
   
    return " "
}
function shorten-path([string] $path) {
   $loc = $path.Replace($HOME, '~')
   # remove prefix for UNC paths
   $loc = $loc -replace '^[^:]+::', ''
   # make path shorter like tabs in Vim,
   # handle paths starting with \\ and . correctly
   return ($loc -replace '\\(\.?)([^\\])[^\\]*(?=\\)','\$1$2')
}
```
### 参考
[good](http://shirokichi2.blog.so-net.ne.jp/2014-03-15)

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

## 環境変数
- `$home`
-- home directory

## Modules
### monokai
color scheme的なもの。
レジストリをいじる

###参考
[1](http://qiita.com/opengl-8080/items/bb0f5e4f1c7ce045cc57)
[powershell](http://winscript.jp/powershell/202)
[PowerShell from Japan!! Blog](http://blog.powershell-from.jp/)

