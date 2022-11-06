---
title: Nuxt.js
---

## Nuxt.js

Project templateが容易されている。
vue-cliを使えば以下でinstallできる。

```
npm install vue-cli
./node_modules/.bin/vue init nuxt-community/starter-template <project-name>
```

その後project directoryに移動して、

```
npm install
```

他に利用可能なtemplate

* `nuxt-community/express-template`

## Preprocessor
SASSを使う

```
npm install --save-dev node-sass sass-loader style-loader
```

`nuxt.config.js`に以下を記載する。

```javascript
module.exports = {
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, ctx) {
      if (ctx.dev && ctx.isClient) {
        config.module.rules.push(
          {
            test: /\.scss$/,
            loaders: [
              'style-loader',
              'css-loader?-url&minimize&sourceMap',
              'sass-loader'
            ],
            exclude: /(node_modules)/
          }
        )
      }
    }
  }
}
```

## Asset
* [アセット - Nuxt.js](https://ja.nuxtjs.org/guide/assets)



## Directory structure
* assets
    * compileしないfile
    * SASS, LESS, javascriptなど
* components
    * Vue.js components
* layouts
    * application layouts
* middleware
    * page/group of pageのrender前に実行するmiddleware
* pages
    * application view and route.
    * このfolderの`.vue` fileを全て読んで、routesを作成する
* plugin
    * root Vue.js applicationのinstance化の前に実行するjavascript plugin
* static
    * `/static/robots.txt`は`/robots.txt`にmapされる
    * 静的なfile
* store
    * Vuex store files
* nuxt.config.js

## Reference
* [GitHub - nuxt/nuxt.js: Versatile Vue.js Framework](https://github.com/nuxt/nuxt.js)

