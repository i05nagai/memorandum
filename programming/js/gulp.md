---
title: gulp
---

## gulp
JS性のtask runner。

```
npm install --save-dev gulp
```

`gulpfile.js`にtask記載する。

## Usage

```javascript
"use strict;"

var gulp = require('gulp');

gulp.task('hello', function() {
  console.log('Hello gulp!');
});

gulp.task('default', ['hello']);
```



## API
* `gulp.src(globs[, opitons])`
    * pipe可能な`globs`にマッチするファイル群を返す


* `gulp.dest(path[, options])`
    * 

```javascript
gulp.src('./client/templates/*.jade')
  .pipe(jade())
  .pipe(gulp.dest('./build/templates'))
  .pipe(minify())
  .pipe(gulp.dest('./build/minified_templates'));
```

* `gulp.task(name [, deps] [, fn])`
    * taskを定義する
    * nameはtask名
    * depsは配列で、依存しているtaskを記述する
        * このtaskの実行前に実行されるtaskのいちらん
    * fn
        * taskの処理
    * `deps`も`fn`どちらか一方、あるいは両方省略可能

* `gulp.watch(glob [, opts], tasks)`
    * fileの監視をする
    * fileに変更があったときに、EventEmitterを`chagne`eventを返す
    * `glob`は監視するファイルをString, Arrayで指定する
    * `opts`は`geze`に渡されるopiton
    * `tasks`ファイルに変更があったときに実行するtask群

```javascript
var watcher = gulp.watch('js/**/*.js', ['uglify','reload']);
watcher.on('change', function(event) {
  console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
});
```

* `gulp.watch(glob [, opts, cb])`
    * fileの監視をする
    * fileに変更があったときに、EventEmitterを`chagne`eventを返す
    * `glob`は監視するファイルをString, Arrayで指定する
    * `opts`は`geze`に渡されるopiton
    * 変更があったときのcallback

```javascript
gulp.watch('js/**/*.js', function(event) {
  console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
});
```

## Plugins
Incremental buildsのためにofficialに推奨されているpluginもある。

* gulp-changed
    * only pass through changed files
    * 変更されたファイルを検知する
* gulp-cached
    * in-memory file cache, not for operation on sets of files
    * メモリにファイルをキャッシュする
* gulp-remember
    * pairs nicely with gulp-cached
* gulp-newer
    * pass through newer source files only, supports many:1 source:dest


* gulp-rename

```
npm install --save-dev gulp-rename
```

```javascript
var gulp = require("gulp");  
var rename = require("gulp-rename");  

gulp.task("build", function() {  
  gulp.src('./hoge.js')
    .pipe(rename({
      extname: '.min.js'
    }))
    .pipe(gulp.dest('./'))
    ;
});
```


* gulp-git
    * gitのコマンドが使える
* gulp-postcss
    * gulpでpostcssを使う


## Reference
* [現場で使えるgulp入門 - gulpとは何か | CodeGrid](https://app.codegrid.net/entry/gulp-1)
* [GitHub - gulpjs/gulp: The streaming build system](https://github.com/gulpjs/gulp)
* [gulp/docs/recipes at master · gulpjs/gulp · GitHub](https://github.com/gulpjs/gulp/tree/master/docs/recipes#recipes)
* [gulp の gulp-rename モジュールを使って出力するファイルに .min をつける方法 | phiary](http://phiary.me/gulp-rename-min/)
* [PostCSSをSCSS記法に近づける+便利にするためのプラグイン11選 | be-into](http://be-into.com/blog/web/11-plugins-to-make-postcss-closer-to-scss/)
