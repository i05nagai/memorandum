--t-
title: CSS
---

## CSS

* flex-box
    * [A Complete Guide to Flexbox | CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

## Tips

line-heightを指定しないとたてのalignはできない？

## Property

### Filter
* https://www.w3schools.com/cssref/css3_pr_filter.asp

```
filter: none | blur() | brightness() | contrast() | drop-shadow() | grayscale() | hue-rotate() | invert() | opacity() | saturate() | sepia() | url();
```

spaceで区切れば複数のfilterを指定できる。
`url`はSVGのfilterを指定できる。

```html
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <filter id="filter-blur">
  <feGaussianBlur in="SourceGraphic" stdDeviation="5"/>
 </filter>
</svg>
<img src="" style="filter: url('#filter-blur')">
```



## Pseau

## Coding Style guide
* [Guidelines · Primer](http://primercss.io/guidelines/)

## selector

* `#id`
    * id selector
    * `<div id="id">`の特定のidのついたものを指定
* `.class`
    * class selector
    * `<div class="class">`の特定のclassのついたものを指定
* `p`
* `p, h1, h2`

* `selector:pseudo-class`
* `p::pseudo-element`
    * [CSS Pseudo-elements](https://www.w3schools.com/css/css_pseudo_elements.asp)
    * pseudo-element
    * 最初の要素や、最後の要素だけを指定する

## API
* `@media`
    * [CSS3 @media Rule](https://www.w3schools.com/cssref/css3_pr_mediaquery.asp)
    * media query
    * 画面やdeviceのsizeなどの確認ができる
    * 条件にあわせてCSSの設定を変更できる


## Grammer
- [CSS Snapshot 2020](https://www.w3.org/TR/CSS/#css)

## Reference

