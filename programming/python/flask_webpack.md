---
title: Flask-webpack
---

## Flask-webpack


## Settingso
* WEBPACK_MANIFEST_PATH: default None
    * webpackが生成するmanifest.jsonが必要
    * Required: You may consider using ./build/manifest.json, it's up to you.
* WEBPACK_ASSETS_URL: default publicPath from the webpack.config.js file
    * Optional: Use this asset url instead of the publicPath. 
    * You would set this to your full domain name or CDN in production.

## Reference
* [nickjj/flask-webpack: A Flask extension to manage assets with Webpack.](https://github.com/nickjj/flask-webpack)
