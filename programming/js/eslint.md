---
title: ESLint
---

## ESLint
lint tool for Javascript.
ECMAScript 2015(ES6)

## Install

```
npm install --save-dev eslint
```

以下を実行すると対話形式で、`.eslint`の初期設定を作成してくれる。

```
npx eslint --init
```

`package.json`に以下を記載する。

```json
{
    "scripts": {
        "lint": "eslint path/to/js"
    }
}
```

```
npm run lint
```

runコマンドに引数は渡せない。

## Usage

## Configuration
Multiple filenames are supported. `.eslintrc.js`.

```
{
    "root": true,
    "extends": [
        "eslint:recommended",
        "plugin:@typescript-eslint/recommended"
    ],
    "parser": "@typescript-eslint/parser",
    "parserOptions": { "project": ["./tsconfig.json"] },
    "plugins": [
        "@typescript-eslint"
    ],
    "rules": {
        "@typescript-eslint/strict-boolean-expressions": [
            2,
            {
                "allowString" : false,
                "allowNumber" : false
            }
        ]
    },
    "ignorePatterns": ["src/**/*.test.ts", "src/frontend/generated/*"]
}
```

- `root: true`
    - eslint merges configuration files in parent direcotries up to home directory or root directory.
    - if true is specified, stop 

global変数を指定する。
keyは変数名で、値はglobal変数が書き換え可能かどうかで、書き換え不可ならfalseにする。

```json
  "globals": {
    "$": false,
    "jQuery": false
  }
```

ES6の構文を静的検証する場合は`env`に以下を記載する。

```json
    "env": {
        "es6": true
    },
```

browserのglobal変数とbrwoser用のいくつかのruleが適用される。

```json
    "env": {
        "browser": true
    },
```

## Rules

* object-shorthand
    * [object-shorthand - Rules - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/rules/object-shorthand)
* no-unused-vars
    * [no-unused-vars - Rules - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/rules/no-unused-vars)
    * エラーを特定の変数だけ無効にする場合は、コメントで`/* exported variableName */`


```json
{
    "rules": {
        "no-unused-vars": ["error", { "vars": "all", "args": "after-used", "ignoreRestSiblings": false }]
    }
}
```

* `vars`
    * `all`
        * global変数も全てcheck
    * `local`
        * global変数はcheckの対象としない
* `args`
* `varsIgnorePattern`
    * 無視する変数名のpatternを記載

* prefer-template
    * [prefer-template - Rules - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/rules/prefer-template)


* no-restricted-syntax
    * [no-restricted-syntax - Rules - ESLint - Pluggable JavaScript linter](http://eslint.org/docs/rules/no-restricted-syntax)
    * 表記を統一させる目的などのために、構文を制限している
    * `for in `, `for of`など制限されている

* no-prototype-builtins
    * `hasOwnProperty`などのmeta情報取得の禁止


```
// ✔ GOOD
Object.hasOwnProperty.call(obj, "prop")
// ✘ BAD
obj.hasOwnProperty("prop")
```

* no-underscore-dangle
    * 変数の最初に`_`をつけるな

```
/*eslint no-underscore-dangle: ["error", { "allow": ["foo_", "_bar"] }]*/
```


## With gulp
* [GitHub - adametry/gulp-eslint: A Gulp plugin for identifying and reporting on patterns found in ECMAScript/JavaScript code.](https://github.com/adametry/gulp-eslint)

```
npm install --save-dev gulp-eslint
```

eslintのpluginを使う場合は合わせてインストールする。

```
npm install --save-dev eslint-config-airbnb-base
```

`.eslintrc`に設定を記載しておく。

```json
{
    "extends": "airbnb-base"
}
```

```javascript
const gulp = require('gulp');
const gulpEslint = require('gulp-eslint');

gulp.task('lint', () => {
    // ESLint ignores files with "node_modules" paths.
    // So, it's best to have gulp ignore the directory as well.
    // Also, Be sure to return the stream from the task;
    // Otherwise, the task may end before the stream has finished.
    return gulp.src(['**/*.js','!node_modules/**'])
        // eslint() attaches the lint output to the "eslint" property
        // of the file object so it can be used by other modules.
        .pipe(gulpEslint())
        // eslint.format() outputs the lint results to the console.
        // Alternatively use eslint.formatEach() (see Docs).
        .pipe(gulpEslint.format())
        // To have the process exit with an error code (1) on
        // lint error, return the stream and pipe to failAfterError last.
        .pipe(gulpEslint.failAfterError());
});
```

## Rules
airbnb-base

```
# install dependency if you use npm 5+
npx install-peerdeps --dev eslint-config-airbnb
# then
npm install --save-dev eslint-config-airbnb
```

`.eslintrc`に設定を記載しておく。

```json
{
    "extends": "airbnb-base"
}
```

airbnb

baseとの違いは、React, JSXなどのfrontend用のruleも読み込まれる。
Server sideで使う場合は不要な場合が多いので、その場合はbaseを使う。

```
npm install --save-dev eslint-config-airbnb
```

`.eslintrc`に設定を記載しておく。

```json
{
    "extends": "airbnb"
}
```

#### Error: window is not defined
Specify environemnt in `.eslintrc`.
[Configuring ESLint \- ESLint \- Pluggable JavaScript linter](https://eslint.org/docs/user-guide/configuring.html#specifying-environments)


## Plugins

#### import
- [import\-js/eslint\-plugin\-import: ESLint plugin with rules that help validate proper imports\.](https://github.com/import-js/eslint-plugin-import#resolvers)



## Reference
* [ESLint 最初の一歩 - Qiita](http://qiita.com/mysticatea/items/f523dab04a25f617c87d)
* [ESLint をグローバルにインストールせずに使う - Qiita](http://qiita.com/mysticatea/items/6bd56ff691d3a1577321)
* [ESLint v4.0.0 released - ESLint - Pluggable JavaScript linter](http://eslint.org/blog/2017/06/eslint-v4.0.0-released)
- [Find and fix problems in your JavaScript code \- ESLint \- Pluggable JavaScript Linter](https://eslint.org/)
