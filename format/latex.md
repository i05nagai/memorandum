---
title: LaTeX
---

## LaTeX

## Tips

### Font T1/cmr/m/n/10=ecrm1000 at 10.0pt not loadable: Metric (TFM) file not fou

`tlmgr search --file ecrm1000.tfm --global`

```
! Font T1/cmr/m/n/10=ecrm1000 at 10.0pt not loadable: Metric (TFM) file not fou
nd.
<to be read again>
                   relax
                   l.105 \fontencoding\encodingdefault\selectfont

                   pandoc: Error producing PDF
```

下記で必要なパッケージをインストール。

`tlmgr install ec`

* [Error in TeX Live – Font ... not loadable: Metric (TFM) file not found - TeX - LaTeX Stack Exchange](http://tex.stackexchange.com/questions/75166/error-in-tex-live-font-not-loadable-metric-tfm-file-not-found)


### Cannot determine type of tlpdb from /root/texmf!

```
Cannot determine type of tlpdb from /root/texmf!
cannot setup TLPDB in /root/texmf at /usr/bin/tlmgr line 5713.
The command '/bin/sh -c tlmgr install ec' returned a non-zero code: 2
```

### Commutative diagrams
* [LaTeX で可換図式を描くパッケージ各種 \| 雑記帳](https://blog.miz-ar.info/2017/06/commutative-diagrams-in-latex/)
* https://www.jmilne.org/not/Mamscd.pdf

Available in Mathjax too. But diagonal arrow is not supported.

* `@>>>`
    * 右向き矢印（キーボードに > キーがない人のために、代替記法として @))) が用意されている）
* `@<<<`
    * 左向き矢印（キーボードに > キーがない人のために、代替記法として @((( が用意されている）
* `@AAA`
    * 上向き矢印
* `@VVV`
    * 下向き矢印
* `@=`
    * 等号（横）
* `@|`, `@\vert`
    * 等号（縦）
* `@.`
    * 矢印を出力しない

$$
\begin{CD}
    A @>{f}>> B
    \\
    @V{g}VV    @VVV
    \\
    C   @>>>  D
\end{CD}
$$

pd-diagram

$$
\begin{diagram}
    \node{A} \arrow{e,t}{f} \arrow{s,l}{g} \node{B} \arrow{s} \\
    \node{C} \arrow{e} \node{D}
\end{diagram}
$$

### Rightarrow implies
* [\Rightarrow vs. \implies, and "does not imply" symbol - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/47063/rightarrow-vs-implies-and-does-not-imply-symbol)

* Is it better to use \Rightarrow or \implies to symbolize logical implications? Why?
    * Use `\implies`



## Reference
* [oda_tex.dvi](https://www.math.tohoku.ac.jp/tmj/oda_tex.pdf)
* [List of LaTeX mathematical symbols - OeisWiki](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)
