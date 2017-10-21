---
title: Webpack
---

## Webpack

## Configuration
* [Core Concepts](https://webpack.js.org/concepts/)

`webpack.conf.js`について。


entry



```
const config = {
  entry: './path/to/my/entry/file.js'
};
const config = {
  entry: {
    main: './path/to/my/entry/file.js'
  }
};
```

## plugins

### DefinePlugin
* [DefinePlugin](https://webpack.js.org/plugins/define-plugin/)
    * 変数を定義する

###  EnivornmentPlugin
* [EnvironmentPlugin](https://webpack.js.org/plugins/environment-plugin/)
    * 環境変数を定義する
    * process.env.ENVIRONMENT_NAMEの形で変数が参照できるようになる

### file-loader
* [webpack-contrib/file-loader: file loader for webpack](https://github.com/webpack-contrib/file-loader)

```javascript
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpg|gif)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
            }
          }
        ]
      }
    ]
  }
}
```

* `name`
    * pack後の出力ファイル名
    * `name: '[path][name].[ext]'`
* `publicPath`
    * 読み込み時のbase path
* `outputPath`
    * pack時の出力ファイルのpath

## Tips

### global variable with webpack
* [javascript - Define global variable with webpack - Stack Overflow](https://stackoverflow.com/questions/37656592/define-global-variable-with-webpack)


## Reference
