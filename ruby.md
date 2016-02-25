# ruby

## WindowsでRuby処理系の切り替え
windows以外だとrvmが一般的だが、windowsの場合は下記が候補となる。
* pik
    * gemとしてインストール
    * 更新停止
* [uru](https://bitbucket.org/jonforums/uru)
    * executionファイル。multi-platform
    * まだ開発中

uruについて解説
### インストール(without Chocolately)
1. bitbucket上で開発されている。下記よりDLする。
    * [uru download](https://bitbucket.org/jonforums/uru/wiki/Downloads)
    * Windowsの場合は、`uru-0.8.1-windows-x86`をDL。64bitもx86でOK。
2. DLしたら適当なディレクトリに解凍する。 ここでは`C:\hoge`とする。 
3. 解凍したディレクトリにパスを通す。
    * ここでは`C:\hoge`
4. コマンドプロンプトで`C:\hoge`を開き、下記を実行
```
uru_rt admin install
```

### インストール(with Chocolately)
Chocoでパッケージは配布されていないが、下記手順でChocoを使ってインストール可能。
[Install](https://bitbucket.org/jonforums/uru/wiki/Chocolatey)
1. [uru.0.8.1.nupkg](https://bitbucket.org/jonforums/uru/downloads)をDL。
2. 適当なディレクトリに配置し、管理者権限つきでコマンドプロンプトかpowershellを起動。
3. `choco install uru.X.Y.Z.nupkg`を実行。`X.Y.Z`はversion番号。
4. 登録完了。

### 既に存在している処理系を追加
uruを導入する時点ですでにruby処理系がインストールされている場合は次の手順で追加できる。
```
uru_rt admin add system
```
複数ruby処理系が既にインストールしてある場合は`system`として認識されるrubyは適当にきまるようなので、明示的にパスを指定して追加も可能。
```
uru_rt admin add \path\to\ruby
```

### コマンド
* 現在利用している処理系や利用可能な処理系の一覧
```
uru ls
```
    * 出力
```
    904         : jruby 9.0.4.0 (2.2.2) 2015-11-12 b9fb7aa Java HotSpot(TM) 64-Bit...
 => system      : ruby 2.2.3p173 (2015-08-18 revision 51636) [x64-mingw32]
```

* 処理系切り替え
```
> ruby --version
> uru 904
---> now using jruby 9.0.4 tagged as `904`
> ruby --version
```
    * cmdの環境変数を読み込み直さないとrubyコマンドの呼び出し先は変わらない。

ruby実行
```
uru ruby test.rb
```

### Chocolatelyでrubyをいれた場合
Chocolatelyでrubyをいれた場合は、rubyのパスが通されているので手動でChocolatelyが通したrubyのパスを除く。

### 参考
[uruコマンド一覧](https://bitbucket.org/jonforums/uru/wiki/Examples)


## tips

### ファイル読み込み1
```ruby
File.open("filename") do |file|
    #1行ずつ
    file.each_line do |line|

    end
    #1度によみこみ
    file.read.split('\n').each |line|

    end
    #1文字ずつ
    file.each_char |char|

    end
end
```

### ファイル読み込み4
ファイルロック+読みこみ
```ruby
File.open("filename") do |file|
    file.flock(File::LOCK_EX)
    file.each_line |line|

    end
end
```

### ファイル読み込み1
```ruby

```

### n進数へ変換
```ruby
a = 255
n = 3
p a.to_s(n) #n進数
```

### n進数から数値へ変換

```ruby
a = '1011011'
p ("0b" + a).oct 
```

## 配列

### 逆からeach
reverse_each


