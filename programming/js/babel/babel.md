---
title: babel
---

## Babel


## Concept

Presets and plugins

[configuration \- Difference between plugins and presets in \.babelrc \- Stack Overflow](https://stackoverflow.com/questions/45943889/difference-between-plugins-and-presets-in-babelrc#:~:text=Presets%20are%20collections%20of%20plugins,plugins%20are%20loaded%20before%20presets.)
Presets are just a collection of plugins.

## Install

```
npm install babel
```

## Configuration
`bable.config.json`

```
{
  "presets": [
    [
      "@babel/preset-env",
      {
        "targets": {
          "edge": "17",
          "firefox": "60",
          "chrome": "67",
          "safari": "11.1"
        },
        "useBuiltIns": "usage",
        "corejs": "3.6.5"
      }
    ]
  ]
}
```

## Reference
* [Babelの手ほどき - Babelとは | CodeGrid](https://app.codegrid.net/entry/babel-1)
* [Babel is on Open Collective](https://opencollective.com/babel)

