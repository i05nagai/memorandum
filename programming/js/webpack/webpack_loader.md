---
title: Webpack Loader
---

## Webpack Loader
Loaders are transformations that are applied on the source code of a module.

## Syntax
There are multiple sytanx to write loader in configuration file.
To use multiple loader, you have `use`

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

#### file-loader
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

#### babel-loader
* [babel\-loader](https://webpack.js.org/loaders/babel-loader/)
* [Setting up React for ES6 with Webpack and Babel \- Twilio](https://www.twilio.com/blog/2015/08/setting-up-react-for-es6-with-webpack-and-babel-2.html)
* Compile ES2015(ES6) to ES5 compatible

```
# For babel-loader 8.x
npm install -D babel-loader @babel/core @babel/preset-env webpack
# 
npm install babel-loader babel-core babel-preset-env --save-dev
```

ruleにloaderの適用ruleを記載していく。

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
    {
      // loader target files
      test: /\.js$/,
      // exclude pattern
      exclude: /node_modules/,
      // specify babel-loader
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

#### eslint-loader
* [webpack\-contrib/eslint\-loader: eslint loader \(for webpack\)](https://github.com/webpack-contrib/eslint-loader)
* [React Code Style with ESLint \+ Babel \+ Webpack \- RWieruch](https://www.robinwieruch.de/react-eslint-webpack-babel/)
* [Linting React Using ESLint with Create React App ← Alligator\.io](https://alligator.io/react/linting-react/)
    * lint for React
* Lint for JavaScript code

```
npm install --save-dev eslint eslint-loader
# for react
npm install --save-dev eslint-plugin-react
# to use after babel-loader
npm install --save-dev babel-eslint
```

Create `.eslintrc`

```javascript
{
  parser: "babel-eslint",
  "plugins": [
    "react"
  ],
  "extends": ["airbnb-base"]
}
```

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
    {
      test: /\.js$/,
      exclude: /node_modules/,
      use: [{
        loader: 'babel-loader',
        options: {
          presets: ['env']
        }
      }, {
        loader: 'eslint-loader',
      }]
      ],
    }
    ],
  },
};
```

#### sytle-loader
* [style\-loader](https://webpack.js.org/loaders/style-loader/)
* dds CSS to the DOM by injecting a `<style>` tag

```
npm install style-loader --save-dev
```

```
{
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          { loader: "style-loader" },
          { loader: "css-loader" }
        ]
      }
    ]
  }
}
```

#### css-loader
* [webpack\-contrib/css\-loader: CSS Loader](https://github.com/webpack-contrib/css-loader)

## Tips

#### React
[Setting up React for ES6 with Webpack and Babel \- Twilio](https://www.twilio.com/blog/2015/08/setting-up-react-for-es6-with-webpack-and-babel-2.html)


```
npm install --save-dev babel-preset-react
```



## Reference
