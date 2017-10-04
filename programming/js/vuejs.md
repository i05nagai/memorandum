---
title: Vue.js
---

## Vue.js

## API

* `Vue.exnted`
* `Vue.directive`
* `Vue.use(plugin)`

## directive

* `v-on:something`
    * 省略記法は`@something=""`
* `v-bind:attribute=""`
    * [Vue.js](https://vuejs.org/v2/api/#v-bind)
    * 省略記法は`:attribute=""`
    * attributeにの値を評価する時にjavascript式として評価する
    * vueのjavascriptの変数などが利用できる
* `v-bind:class`
    * 省略記法は`:class=""`
    * `v-bind:class`と`class`attributeは上書きではなく追加

以下のように書くと、`class`をisActiveがtrueのとき、activeを適用し、hasErrorがtrueのときtext-dangerを適用する。

```
<div class="static"
     v-bind:class="{ active: isActive, 'text-danger': hasError }">
</div>
```

* `v-model`
* `v-for="item in items"`
    * [List Rendering — Vue.js](https://vuejs.org/v2/guide/list.html)
    * with component
        * [List Rendering — Vue.js](https://vuejs.org/v2/guide/list.html#v-for-with-a-Component)
    * itemが動的に変更される可能性がある場合
        * iterateする要素に更新があった時にVueはviewを再描画する必要がある
        * viewの更新時のlistのreorderingなどに備えて一意なKeyを指定する必要がある

```
<div v-for="item in items" :key="item.id">
  <!-- content -->
</div>
```

## Tips

### did you register the component correctly? For recursive components, make sure to provide the "name" option.
* [Components — Vue.js](https://vuejs.org/v2/guide/components.html)

## vue devtools
* [Vue.js Devtoolsの導入方法と機能まとめ。Vue.jsを用いた開発を効率化させよう！ - Qiita](https://qiita.com/hashimoto-1202/items/c81f5d4c271eef16d957)


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

## Single file component

```
<template>
  <div>This will be pre-compiled</div>
</template>
<script src="./my-component.js"></script>
<style src="./my-component.css"></style>
```


## Template
* [7 Ways To Define A Component Template in VueJS – Vue.js Developers – Medium](https://medium.com/js-dojo/7-ways-to-define-a-component-template-in-vuejs-c04e0c72900d)

## Component



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
