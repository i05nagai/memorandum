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
