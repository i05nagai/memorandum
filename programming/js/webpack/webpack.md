---
title: Webpack
---

## Webpack

## Configuration
* [Core Concepts](https://webpack.js.org/concepts/)
* https://stackoverflow.com/questions/59407534/can-i-use-as-es-modules-for-webpack-config

If you use `webpack.conf.mjs`, it interpret as ES module.
If you use `webpack.conf.cjs`, it interpret as CommonJS module.


Entry

* An entry point indicates which module webpack should use to begin building out its internal dependency graph
* by default `./src/index.js`

```javascript
const config = {
  entry: './path/to/my/entry/file.js'
};
const config = {
  entry: {
    main: './path/to/my/entry/file.js'
  }
};
```

Output

* The output property tells webpack where to emit the bundles it creates and how to name these files
* By default `./dist/main.js`

```javascript
const path = require('path');
module.exports = {
  entry: './path/to/my/entry/file.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'my-first-webpack.bundle.js'
  }
};
```

Loaders

* Out of the box, webpack only understands JavaScript and JSON files
* Loaders allow webpack to process other types of files and convert them into valid modules that can be consumed by your application and added to the dependency graph.
* two properties
    * `test`
        * filename
    * `use`
        * what loader

```
const path = require('path');

module.exports = {
  output: {
    filename: 'my-first-webpack.bundle.js'
  },
  module: {
    rules: [
      { test: /\.txt$/, use: 'raw-loader' }
    ]
  }
};
```

Plugins


Mode

* you can enable webpack's built-in optimizations that correspond to each environment
    * `development`
    * `production`
        * by default
    * `none`


## Plugin

#### html-webpack-plugin
https://webpack.js.org/plugins/html-webpack-plugin/

Create an index html as a entrypoint.

## Tips

### global variable with webpack
* [javascript - Define global variable with webpack - Stack Overflow](https://stackoverflow.com/questions/37656592/define-global-variable-with-webpack)

## Reference
* [webpack 3 入門 - Qiita](https://qiita.com/soarflat/items/28bf799f7e0335b68186)
* [pinglinh/simple\_webpack\_boilerplate: 🕸📦Ever wondered how you could set up a React project from scratch? This is the repo for you\! I have also written up a blog tutorial to follow along\.](https://github.com/pinglinh/simple_webpack_boilerplate)
