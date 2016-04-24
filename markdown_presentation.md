# markdown presentation
Markdownでプレゼンテーションを行うソフトと使い方

## Remark.js
[github](https://github.com/gnab/remark)

jsをurlで読み込めるので、ネットにつながる環境ならすごく便利。
以下の`index.html`を作り、同じディレクトリに`contents.md`を配置する。
`index.html`をブラウザで開けばOK。

`index.html`
```html
<DOCTYPE html>
<html>
<head><title>Presentation</title></head>
<body>
  <script src="http://gnab.github.io/remark/downloads/remark-latest.min.js" type="text/javascript"></script>
  <script type="text/javascript">
    var slideshow = remark.create({
      sourceUrl: "contents.md",
      highlightStyle: 'default',
      highlightLanguage: 'sh'
    });
  </script>
</body>
</html>
```

`contents.md`
```md
# slied 1 
- 1ページ目
---
# slide 2
- 2ページ目

```

### キー操作
* `j` 次のスライド
* `k` 前のスライド
* `c` スライドのclone
    * スライドを clone すると、元のスライドでページ移動した際、clone 先のスライドも同期して移動する。
* `f` フルスクリーン
* `p` プレゼンモード
* `h` ヘルプの表示

### gh-pagesに公開
1. githubにレポジトリを作る。
2. `gh-pages`という名前でブランチを切る。
3. `https://username.github.io/repository_name`にアクセスするとレポジトリトップの`index.html`のファイルが表示される。
    * uploadしたデータが反映されるまで10分ほどかかるみたいなので気長にまつ。

個人的には、スライドごとにレポジトリを作る気分にあんまりならないので、下記のように1つのレポジトリをまとめている。
特に工夫はないが、レポジトリのトップの`contents.md`はレポジトリ内のスライドへのリンクテーブルになっている個人的に便利。
1. githubにレポジトリを作る。
2. レポジトリのトップに、`index.html`と`contetns.md`を置く。`contents.md`はサブディレクトリへのリンク。
```md

```
3. レポジトリにスライドごとにディレクトリを作り、各ディレクトリに`index.html`と`contents.md`を作る。


### mathjaxを使う
`index.html`にmathjaxを読み込む設定を書く。
`contents.md`では、普通にmarkdown中にmathjaxを書けばOK。
具体的には、`$$`で数式を囲む。
mathjaxのURLに`delayStartupUntil=configured`オプションを含めると、markdownで問題になる`_`のエスケープなどが不要になるので便利。

`index.html`
```html
<DOCTYPE html>
<html>
<head><title>Presentation</title></head>
<body>
  <script src="http://gnab.github.io/remark/downloads/remark-latest.min.js" type="text/javascript"></script>
  <script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML&delayStartupUntil=configured" type="text/javascript"></script>
  <script type="text/javascript">
    var slideshow = remark.create({
      sourceUrl: "contents.md"
    });

    // Setup MathJax
    MathJax.Hub.Config({
      tex2jax: {
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre']
      }
    });
    MathJax.Hub.Queue(function() {
      $(MathJax.Hub.getAllJax()).map(function(index, elem) {
        return(elem.SourceElement());
      }).parent().addClass('has-jax');
    });
    MathJax.Hub.Configured();
  </script>
</body>
</html>
```

```md
# slide 1 
- 1ページ目
---

# slide 2
- 2ページ目

$$
x = a_{1} + b^{2}
$$
## フーリエ変換
$$
  F(u) = \int\_{-\infty}^{\infty} f(x)\mathrm{e}^{-j2\pi ux}dx
$$

## 2次元のフーリエ変換
$$
  F(u,v) = \int\_{-\infty}^{\infty} \int\_{-\infty}^{\infty} f(x,y)\mathrm{e}^{-j2\pi (ux + vy )}dxdy
$$
```

### 参考
[markdown + remark.js + gh-pages でプレゼン資料を公開する](http://qiita.com/harasou/items/1fa3cca6ac1ef175c876)

## Reveal.js
[github](https://github.com/hakimel/reveal.js/)

### 参考
[mathjaxを使う](http://qiita.com/hilohiro/items/147536f84a537d485d11)


