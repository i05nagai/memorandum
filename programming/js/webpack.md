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

## Loader
loaderの設定は書き方が色々ある。
`use`を使うと、複数かける。

```javascript
module: {
  rules: [{
    test: /\.js$/,
    exclude: /node_modules/,
    use: [{
        loader: 'babel-loader',
        options: {
          presets: ['env']
        },
      }, {
        loader: 'jshint-loader'
      }
    ]
  }],
},
```


### babel-loader
* ES2015（ES6）のコードをES5のコードに変換するローダー

```
npm install babel-loader babel-core babel-preset-env --save-dev
```

ruleにloaderの適用ruleを記載していく。

```
module.exports = {
  module: {
    rules: [
    {
      // ローダーの処理対象ファイル
      test: /\.js$/,
      // ローダーの処理対象から外すディレクトリ
      exclude: /node_modules/,
      // 利用するローダー
      use: [{
        loader: 'babel-loader',
        options: {
          presets: ['env']
        }
      }],
    }
    ],
  },
};
```

### eslint-loader
JavaScriptのコードを検証するローダー。

```
npm install eslint eslint-loader --save-dev
```

## Plugin
loaderとは別にpluginも存在する。
bundle時に実行する処理。

### UglifyJsPlugin
JavaScriptを圧縮するプラグイン

```
  // プラグインの設定
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        // console.log（）などのconsole.*系の記述を取り除いて出力する
        drop_console: true
      },
    }),
  ],
```

## Tips

### global variable with webpack
* [javascript - Define global variable with webpack - Stack Overflow](https://stackoverflow.com/questions/37656592/define-global-variable-with-webpack)


## Reference
* [webpack 3 入門 - Qiita](https://qiita.com/soarflat/items/28bf799f7e0335b68186)

