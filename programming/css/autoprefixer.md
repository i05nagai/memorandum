---
title: Autoprefixer
---

## Autoprefixer
CSSのBrowserごとのprefixを自動で補ってくれる。
Can I Useのデータを元に整形をしている。

## Usage

## With gulp and PostCSS
PostCSSで提供されているので、gulp経由で利用する。

```javascript
gulp.task('autoprefixer', function () {
    var postcss      = require('gulp-postcss');
    var sourcemaps   = require('gulp-sourcemaps');
    var autoprefixer = require('autoprefixer');

    return gulp.src('./src/*.css')
        .pipe(sourcemaps.init())
        .pipe(postcss([ autoprefixer() ]))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./dest'));
});
```


## Reference
* [GitHub - postcss/autoprefixer: Parse CSS and add vendor prefixes to rules by Can I Use](https://github.com/postcss/autoprefixer)
* [Autoprefixerによる、CSS3の管理｜Web Design KOJIKA17](http://kojika17.com/2014/01/autoprefixer.html)


