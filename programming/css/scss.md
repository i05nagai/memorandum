---
title: SCSS
---

## SCSS
SASSのsyntaxの1つ。
CSSに似た記法でかける。


```css
.article .title {
  font-size: 15px;
  font-size: 1.5rem;
}
```

```scss
@mixin rem($size) {
  font-size: $size + px;
  font-size: $size / 10 * 1rem;
}

.article {
  .title {
    @include rem(15);
  }
}
```

## Syntax

`$`をつけると変数を宣言できる。

```scss
// my_module.scss
$message-color: blue !default;
```

最後に`!default`をつけるとdefault値を定義できる。
`default`値はimpportした場合に意味をimport元で変数を上書きできる。

```scss
$message-color: black;
@import 'my-module';
```

## Reference
* [SCSS vs SASS どっちが便利か違いを比較。おまいら SASS 使えよ！ - オリジナルゲーム.com](http://original-game.com/scss-vs-sass/)
* [Advanced SCSS, or, 16 cool things you may not have known your stylesheets could do · GitHub](https://gist.github.com/jareware/4738651)
* [File: SASS_REFERENCE — Sass Documentation](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#syntax)
