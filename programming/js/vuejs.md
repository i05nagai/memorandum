---
title: Vue.js
---

## Vue.js

## API

* `Vue.exnted`
* `Vue.directive`
* `Vue.use(plugin)`

## directive

* `v-on`
* `v-bind:something=""`
    * 省略記法は`:something=""`
* `v-model`
* `v-for="item in items"`

## vuex

```javascript
import Vuex from 'vuex';
imoprt Vue from 'vue';

Vue.use(Vuex);

const store = Vuex.Store({
    state: {
    },
    mutations: {
    },
});

new Vue({
  components,
  store,
});
```


## vue-cli
Install

```
npm install --save-dev vue-cli
```

```
vue init <template-name> [project-name]
```

* template-name
    * template名
    * vue listでtemplateの一覧を確認できる
* project-name
    * 自分のproject銘

* vue list
* vue build

使えるtemplateは以下。

```
★  browserify - A full-featured Browserify + vueify setup with hot-reload, linting & unit testing.
★  browserify-simple - A simple Browserify + vueify setup for quick prototyping.
★  pwa - PWA template for vue-cli based on the webpack template
★  simple - The simplest possible Vue setup in a single HTML file
★  webpack - A full-featured Webpack + vue-loader setup with hot reload, linting, testing & css extraction.
★  webpack-simple - A simple Webpack + vue-loader setup for quick prototyping.
```

## Reference
* [はじめに - Vue.js](https://jp.vuejs.org/v2/guide/)
