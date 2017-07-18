---
title: stylelint
---

## stylelint
lintのruleの数が多く、customizeしやすい。

```
npm install --save-dev stylelint
```

## Usage
file名を渡す。
`!`を最初に指定すると、一致するファイルを除外する。

```
stylelint "foo/*.css, !**/docker/**"
```

lintの設定ファイルを指定する。
defaultでは`.stylelintrc`ファイルが適用される。

```
stylelint "foo/*.css" --config .mystylelintrc
```

`scss`ファイルをlintする。
`--syntax`としては、`scss`, `less`, `sugarss`が使える。

```
stylelint "foo/**/*.scss" --syntax scss
```

errorを自動で修正する。
fixできなかったerrorはreportで表示される。
実験的な機能なので、極力しようしないようにしたい。

```
stylelint "foo/*.css" --fix
```

```
stylelint --config .stylelintrc --ignore-path .stylelintignore 'src/styles/**/*.css
```


## Configs
`.stylelintrc`ファイルにconfigを記載する。

利用可能なrule一覧は以下。

* [Rules](https://stylelint.io/user-guide/rules/)


## Plugins
* `stylelint-scss`
    * SCSSのlint
    * [GitHub - kristerkari/stylelint-scss: A collection of SCSS specific linting rules for stylelint](https://github.com/kristerkari/stylelint-scss#list-of-rules)

```
npm install --save-dev stylelint-scss
```

```json
{
  "plugins": [
    "stylelint-scss"
  ],
  "rules": {
    "scss/dollar-variable-pattern": "^foo",
    "scss/selector-no-redundant-nesting-selector": true,
    ...
  }
}
```

## Tips

### With gulp
* [GitHub - olegskl/gulp-stylelint: Gulp plugin for running Stylelint results through various reporters.](https://github.com/olegskl/gulp-stylelint)

```
npm install --save-dev gulp-stylelint
```

lintの設定は、`.stylelintrc`に記載する。

```javascript
const gulp = require('gulp');

gulp.task('lint-css', function lintCssTask() {
  const gulpStylelint = require('gulp-stylelint');
  return gulp
    .src('src/**/*.css')
    .pipe(gulpStylelint({
      reporters: [
        {formatter: 'string', console: true}
      ]
    }));
});
```

### With gulp and PostCSS
PostCSSから利用できるが、`gulp-sytlelint`が利用可能な場合はこちらを使った方が良い。

```
npm install --save-dev gulp-postcss
npm install --save-dev postcss-scss
npm install --save-dev sytlelint
```

以下は動かない。

```javascript
var gulp = require('gulp');
var postcss = require("gulp-postcss");
var postcssReporter = require("postcss-reporter");
var postcssScss = require("postcss-scss");
var stylelint = require('stylelint')

// CSS to be processed
var path_to_scss = "file.scss"

gulp.task('lintcss', function() {
  gulp.src(path_to_scss)
  .pipe(
    postcss([
      stylelint()
    ])
  )
  .pipe(gulp.dest('.'));
});
```


## Reference
* [GitHub - stylelint/stylelint: A mighty, modern CSS linter](https://github.com/stylelint/stylelint)
* [stylelint: モダンCSSリンター - Qiita](http://qiita.com/morishitter/items/da3331c03c4a0ba44b8f)
* [User guide](https://stylelint.io/user-guide/)
* [ここがすごいぞ！ stylelint！ - Qiita](http://qiita.com/inuscript/items/ff4f6972c988afbec3a8)
