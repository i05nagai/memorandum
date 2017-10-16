---
title: element ui
---

## element ui

## Quickstart
* [Component | Element](http://element.eleme.io/#/en-US/component/quickstart)
    * webpack.config.jsのloaderの設定は揃える
    * `.babelrc`の`preset`は従わなくても良い
    * On Demandの場合は`npm install babel-plugin-component -D`
    * htmlでcssやjsのloadは不要
        * webpack側で処理される



## el-select
* [Edit fiddle - JSFiddle](http://jsfiddle.net/vcgftLvn/21/)


default valueは上の例を参考にする。
`<el-select v-model="hoge">`で`hoge`にdefault valueを代入しておけば良い。

o
## 

```
      {
        test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
        loader: 'file-loader',
        options: {
          publicPath: 'static/dist/'
        }
      },
```

## Reference
* [Element - A Desktop UI Toolkit for Web](http://element.eleme.io/#/en-US)
