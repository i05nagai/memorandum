## vim-alignta
文字列整列用のplugin

## コメントの行末での整列
vimで行末のようなコメントを揃えるときの話。
矩型選択などを利用して揃えるものはあるが、プラグインを使った解説をしているものがなかったのでメモ。

### 準備
`Alignta`を入れる。
`Alingta`は、文章整形用のvim plugin。
同様のツールに`Align`があるが、`Alignta`の方が高機能？
markdownのテーブルの整形などにも使えるので、入れておいて損はない。

#### インストール
NeoBundleの場合は下記でOK。
```vim
NeoBundle 'h1mesuke/vim-alignta'
```

### やり方
下記のコードを例にする。
```c++
int a; // hoge
const int b = 1; // fuga
const double c = 2.0; // hage
```

揃えたい行を全て選択する。
`:`を押して、下記コマンドを入力する。

```vim
:'<,'>Alignta <- //
```

下記のように揃う。

```c++
int a;                // hoge
const int b = 1;      // fuga
const double c = 2.0; // hage
```

#### コマンドの意味

```vim
:'<,'>Alignta <- //
```

* `'<,'>`は選択範囲を表すvimのコマンド。
* `Alignta`はAligntaのコマンド。
* `<-`はAligntaの整形用のオプションで、ソースコード部分は変更しないためにつけている
    * 揃える文字(この場合`//`)の最初で揃える
* `//`は揃える文字の先頭。

### 補足
行末コメントを揃えるのはメンテナンス性が悪いので、googleのcoding guidelineなどでは使用しないように記載されている場合もあるが、Cの場合はマクロを見やすくするために`¥`を行末にいれることがしばしばある。

[python coding guideline](http://works.surgo.jp/translation/pyguide.html#id56)


## Tips

### 特定の行を除きたい

```vim
:'<,'>Alignta v/\/* //
```

* `v/pattern`に無視したい行のパターンを記述する
* 上の例だと`/*`を含む行は無視

### 特定の行だけ整列したい

```vim
:'<,'>Alignta g/\/\/ //
```

* `g/pattern`に無視したい行のパターンを記述する
* 上の例だと`//`を含んでいる行はだけ整列

### エスケープを省略
基本的にパターンは正規表現で記述する。
正規表現で使う文字はエスケープする必要がある。
`-e`をつけると文字をそのまま使うことができる。


```vim
:'<,'>Alignta -e \d
```


### 囲み文字の整列

```
+---------------------+-------------------------+
| Original            | :Alignta = /* */        |
+---------------------+-------------------------+
| a = 1 /* AAAAA */   | a     = 1   /* AAAAA */ |
| bbb = 10 /* BBB */  | bbb   = 10  /* BBB   */ |
| ccccc = 100 /* C */ | ccccc = 100 /* C     */ |
+---------------------+-------------------------+
```

### markdown table
* [Aligntaを使ってMarkdownのテーブルを書く](http://www.minimalab.com/blog/2014/07/13/markdown-alignta/)

