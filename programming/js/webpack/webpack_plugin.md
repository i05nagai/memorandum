---
title: Webpack Plugin
---

## Webpack Plugin
Plugins also serve the purpose of doing anything else that a loader cannot do.
A webpack plugin is a JavaScript object that has an apply method.

#### HtmlWebpackPlugin
* [HtmlWebpackPlugin](https://webpack.js.org/plugins/html-webpack-plugin/)
    * The plugin will generate an HTML5 file for you that includes all your webpack bundles in the body using script tags.

```
npm install --save-dev html-webpack-plugin
```

#### DefinePlugin
* [DefinePlugin](https://webpack.js.org/plugins/define-plugin/)
    * 変数を定義する

#### EnivornmentPlugin
* [EnvironmentPlugin](https://webpack.js.org/plugins/environment-plugin/)
    * 環境変数を定義する
    * `process.env.ENVIRONMENT_NAME` の形で変数が参照できるようになる


#### UglifyJsPlugin
* [UglifyjsWebpackPlugin](https://webpack.js.org/plugins/uglifyjs-webpack-plugin/)

Minify (Compress) JavaScript code

```
  // plugin configuratoin
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        // console.log（）などのconsole.*系の記述を取り除いて出力する
        drop_console: true
      },
    }),
  ],
```

## Reference

