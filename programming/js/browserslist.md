---
title: Browserslist
---

## Browserslist

The config to share target browsers and Node.js versions between different front-end tools. It is used in:

* Autoprefixer
* Babel
* postcss-preset-env
* eslint-plugin-compat
* stylelint-no-unsupported-browser-features
* postcss-normalize

## Configuration
[browserslist/browserslist: 🦔 Share target browsers between different front\-end tools, like Autoprefixer, Stylelint and babel\-preset\-env](https://github.com/browserslist/browserslist#queries)

* `browserslist` key in `package.json` file in current or parent directories.
    * We recommend this way.
* Tool options. For example browsers option in Autoprefixer.
* BROWSERSLIST environment variable.
* browserslist config file in current or parent directories.
* .browserslistrc config file in current or parent directories.
* If the above methods did not produce a valid result Browserslist will use defaults: > 0.5%, last 2 versions, Firefox ESR, not dead.

## Reference
* [browserslist/browserslist: 🦔 Share target browsers between different front\-end tools, like Autoprefixer, Stylelint and babel\-preset\-env](https://github.com/browserslist/browserslist)
