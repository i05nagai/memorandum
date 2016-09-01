# mathjax

## 設定

```js
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ], //inline
      displayMath: [ ['$$','$$'], ["\\[","\\]"] ] //display style
    }
  });
```

下記のようにすると、
```js
<script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML&delayStartupUntil=configured" type="text/javascript"></script>
```

下記が呼ばれるまで、Mathjaxが起動しない。
```js
    MathJax.Hub.Configured();
```

### 数式番号

* [MathJax TeX and LaTeX Support — MathJax 2.6 documentation](http://docs.mathjax.org/en/latest/tex.html)
* [The TeX input processor — MathJax 2.6 documentation](http://docs.mathjax.org/en/latest/options/TeX.html)

```js
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  TeX: { equationNumbers: { 
      autoNumber: "AMS",
      formatNumber: function (n) {
        return n;
      }
  } }
      
});
</script>
```

上記設定で、`\begin{equation}` ` \end{equation}`で囲んだものに数式番号がつく。
数式の参照は

```
$$
\begin{equation}
    a + b = c
    \label{eq:sample}
\end{equation}
$$

数式\eqref{eq:sample}は世界最強
```

#### 番号のreset
ページロードなしで、動的にmathjaxを描画していると同じ式に同じlabel番号を貼ることになる。
その為、生成されるDOMに同じidが付与され、エラーが起こる。
動的にpreviewなどを生成してる場合は下記を追加すると、再描画するようになる。
```
MathJax.Hub.Queue(
  ["resetEquationNumbers",MathJax.InputJax.TeX],
  ["PreProcess",MathJax.Hub],
  ["Reprocess",MathJax.Hub]
);
```

## markdown
markdownと連携する場合。
* markdown -> mathjax
  * markdownの方で、mathjaxの囲み文字(`$`, `$$`)などの中の`_`をescapeする必要がある。
* mathjax -> markdown
  * mathjaxの方で、`\`\``や`\`\`\``に囲まれた`$$`や`$`をescapeする必要がある。
  * こちらの方が頻度が低い。


## API
* [The MathJax API — MathJax 1.1 documentation](http://docs.mathjax.org/en/latest/api/)
* [MathJax Example Page](http://cdn.mathjax.org/mathjax/latest/test/examples.html)
