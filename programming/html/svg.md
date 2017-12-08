---
title: SVG
---

## SVG

## Filter
* [<filter> - SVG | MDN](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter)

```html
<!-- Learn about this code on MDN: https://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter -->
<svg
 xmlns="http://www.w3.org/2000/svg"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <filter id="blurMe">
  <feGaussianBlur in="SourceGraphic" stdDeviation="5"/>
 </filter>
</svg>

<svg>
 <circle cx="60"  cy="60" r="50" fill="green" />
 <circle cx="170" cy="60" r="50" fill="green"
          filter="url(#blurMe)" />
</svg>
```
* `<feBlend>`
    * `in`
        * source image
    * `in2`
        * blending image
    * `mode`
        * `normal | multiply | screen | darken | lighten`
* `<feColorMatrix>`
* `<feComponentTransfer>`
    * RGBAのchannelごとのmappingをする
        * `<feFuncA>`
        * `<feFuncR>`
        * `<feFuncG>`
        * `<feFuncB>`
    * `type`
        * [Filter Effects – SVG 1.1 (Second Edition)](https://www.w3.org/TR/SVG11/filters.html#feComponentTransferTypeAttribute)
        * `identity | table | discrete | linear | gamma`
    * `tableValues, slope, intercept, amplitude, exponent, offset`
* `<feComposite>`
* `<feConvolveMatrix>`
    * `<feConvolveMatrix>`はconvolutionを計算するfilterで、指定可能なparameterは以下に記載されている。
    * [feConvolveMatrix - SVG | MDN](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feConvolveMatrix)
        * `divisor`
          * default値はKernel matrixの要素和
          * divisorと明るさ(intensity)が対応する
        * `bias`
          * alpha channelをRGBに加えるかどうか
          * defaultは0で、biasなし
        * `preserveAlpha`
          * alpha channelもconvlutionで計算するかどうか
          * falseの場合は convolutionを計算
          * trueの場合は、sourceのalpha channelを引き継ぐ
          * defaultはfalseで、convlutionあり
        * `targetX`
            * convolutionのcolumnのoffset
            * default値は`floor(orderX/2)`でkernel matrixの中心
        * `targetY`
            * convolutionのrowのoffset
            * default値は`floor(orderY/2)`でkernel matrixの中心
        * `order="orderX orderY"`
          * kernel matrixのsize
          * `orderX`
            * col
            * 整数値で1以上で指定
          * `orderY`
            * row
            * 整数値で1以上で指定


$$
\begin{eqnarray}
  A^{\prime}(i, j)
  & := &
    \left(
      \sum_{i^{\prime}=0}^{\mathrm{orderY}-1}
        \sum_{j^{\prime}=0}^{\mathrm{orderX}-1}
          A(i - \mathrm{taregetX} + i^{\prime}, j - \mathrm{targetY} + j^{\prime})
          K(\mathrm{orderX} - i^{\prime} - 1, \mathrm{orderY}  - j^{\prime} - 1)
    \right) / \mathrm{divisor}
  \nonumber
  \\
  & & +
    \mathrm{bias}
    \times
    \alpha(i, j)
\end{eqnarray}
$$


* `<feDiffuseLighting>`
* `<feDisplacementMap>`
* `<feFlood>`
* `<feGaussianBlur>`
    * `in`
        * `SourceGraphic | SourceAlpha | BackgroundImage | BackgroundAlpha | FillPaint | StrokePaint | <filter-primitive-reference>`
    * `stdDeviation`
    * `edgeMode`
        * `duplicate | wrap | none`
* `<feImage>`
* `<feMerge>`
* `<feMorphology>`
* `<feOffset>`
* `<feSpecularLighting>`
* `<feTile>`
* `<feTurbulence>`

## Reference
