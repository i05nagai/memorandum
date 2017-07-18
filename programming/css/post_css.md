---
title: PostCSS
---

## PostCSS
CSSの変換のためのFramework。

入力として、CSS形式のファイルをうけとり、PostCSS形式のASTを構成して、CSSを出力とする。

1. CSS形式のファイルをうけとる
2. 1をparseする
3. 2からPostCSS形式のASTを構成する
4. ASTから新しいCSSを出力する

2, 4にpluginを適用して、CSSの入力構文を拡張、CSSに変換するpluginを作成できる。
既存のCSSのmeta言語をPostCSSの枠組みで利用することも可能である。

## Install

```
npm install --save-dev postcss-cli
```



## With gulp

```javascript
gulp.task('css', function () {
    var postcss    = require('gulp-postcss');
    var sourcemaps = require('gulp-sourcemaps');

    return gulp.src('src/**/*.css')
        .pipe(sourcemaps.init())
        .pipe(postcss([ require('precss'), require('autoprefixer') ]))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('build/'));
});
```

## Plugins
* postcss-reporter
    * [GitHub - postcss/postcss-reporter: Log PostCSS messages in the console](https://github.com/postcss/postcss-reporter)


```javascript
gulp.task('css', function() {
  return gulp.src('./src/*.css')
    .pipe(postcss([
      bemLinter(),
      customProperties(),
      calc(),
      rejectAllColors(),
      reporter(myOptions) // <------ ding
    ]))
    .pipe(gulp.dest('./dist'));
});
```

## Tips

### SCSS to CSS with gulp
* [GitHub - postcss/postcss-scss: SCSS parser for PostCSS.](https://github.com/postcss/postcss-scss)

```
npm install --save-dev gulp-postcss
npm install --save-dev postcss-scss
```

```javascript
"use strict;"
var gulp = require('gulp');
gulp.task('buildcss', ["lintcss"], function() {
  const gulpPostcss = require('gulp-postcss');
  const gulpRename = require('gulp-rename');
  const postcssScss = require('postcss-scss');
  const autoprefixer = require('autoprefixer');
  return gulp.src('/path/to/scss')
    .pipe(
      gulpPostcss([
          autoprefixer()
      ]), {
        syntax: postcssScss
      }
    )
    .pipe(
      gulpRename({
        extname: '.css'
      })
    )
    .pipe(gulp.dest('./path/to/css/'));
});
```

### With autoprefixer

```
npm install --save-dev gulp-postcss
npm install --save-dev autoprefixer
```

以下が変換後に変更されていれば動いている。

```css
a {
    display: flex;
}
```

```javascript
"use strict;"
var gulp = require('gulp');
gulp.task('buildcss', ["lintcss"], function() {
  const gulpPostcss = require('gulp-postcss');
  const autoprefixer = require('autoprefixer');
  return gulp.src('/path/to/scss')
    .pipe(
      gulpPostcss([
          autoprefixer()
      ])
    )
    .pipe(
    )
    .pipe(gulp.dest('./path/to/css/'));
});
```

## Reference
* [PostCSS まとめ - Qiita](http://qiita.com/morishitter/items/4a04eb144abf49f41d7d)
* [GitHub - postcss/postcss: Transforming styles with JS plugins](https://github.com/postcss/postcss)
