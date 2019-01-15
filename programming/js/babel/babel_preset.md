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

