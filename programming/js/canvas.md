---
title: Canvas
---

## Canvas


### Uncaught DOMException: Failed to execute 'toDataURL' on 'HTMLCanvasElement': Tainted canvases may not be exported.


以下はOK。

```
ctx.filter = "brightness(2.05) contrast(1.05) saturate(1.10) url('index.html#filter-sharpen')";
```

はtaintedになる。

```
ctx.filter = "brightness(2.05) contrast(1.05) saturate(1.10) url('#filter-sharpen')";
```

別fileに切り出している場合もOK

```
ctx.filter = "brightness(2.05) contrast(1.05) saturate(1.10) url('filter.svg#filter-sharpen')";
```

## Reference
* [Applying SVG effects to HTML content - SVG | MDN](https://developer.mozilla.org/en-US/docs/Web/SVG/Applying_SVG_effects_to_HTML_content)
