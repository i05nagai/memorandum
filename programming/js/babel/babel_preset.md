---
title: babel preset
---

## babel preset


#### react
* [@babel/preset\-react · Babel](https://babeljs.io/docs/en/babel-preset-react)
    * Do not use `babel-preset-react`

```
npm install --save-dev @babel/preset-react
```

```javascript
{
  "presets": ["@babel/preset-react"]
}
```

#### env
preset-env is a smart preset that allows you to use the latest JavaScript without needing to micromanage which syntax transforms (and optionally, browser polyfills) are needed by your target environment(s).

* [@babel/preset\-env · Babel](https://babeljs.io/docs/en/babel-preset-env)
    * Do not use `babel-preset-es2015`

```
npm install --save-dev @babel/preset-env
```

## Configuration

```javascript
{
  "presets": [
    [
      "@babel/preset-env",
      {
        "useBuiltIns": "entry"
      }
    ]
  ]
}
```

## Reference

