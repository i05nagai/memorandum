---
title: MathJax
---

## mathjax

## Supportex latex packages
* [MathJax TeX and LaTeX Support — MathJax 2\.7 documentation](http://docs.mathjax.org/en/latest/tex.html)

AMScd

```
TeX: {
  extensions: ["AMScd.js"]
}
```

`\require{AMScd}`をpageに記載する。

### Define new commands
You can use `Macros` parameters or `\def` command.

```javascript
Macros: {
    braket: ['{\\langle #1 \\rangle}', 1],
   Abs: ['\\left\\lvert #2 \\right\\rvert_{\\text{#1}}', 2, ""]
}},
```

### nulldelimiterspace
https://github.com/mathjax/MathJax-docs/wiki/TeX-Macro-with-number

In mathjax, `\nulldelimiterspace` is 0pt, so just leave out `\kern-\nulldelimiterspace`.


#### Macros
* [MathJax/sample\-macros\.html at master · mathjax/MathJax](https://github.com/mathjax/MathJax/blob/master/test/sample-macros.html)
* [Configuring MathJax — MathJax 3\.2 documentation](http://docs.mathjax.org/en/v3.2-latest/options/index.html)


## configuration
- [Configuring and Loading MathJax — MathJax 3\.2 documentation](http://docs.mathjax.org/en/v3.2-latest/web/configuration.html#using-a-local-file-for-configuration)

## Tips

#### Upgrade from v2 to v3
- [Painful Upgrade to MathJax 3 \| Chris Yeh](https://chrisyeh96.github.io/2020/03/29/mathjax3.html)

## Reference
* [MathJax basic tutorial and quick reference - Mathematics Meta Stack Exchange](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)
* [MathJax で利用可能な TeX コマンド（非公式）](http://memopad.bitter.jp/web/mathjax/TeXSyntax.html)
* [TeX Commands available in MathJax](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm)
