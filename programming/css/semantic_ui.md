---
title: Semantic UI
---

## Semantic UI


## Install

```
npm install semantic-ui --save
cd semantic/
gulp build
```

gulpをglobalにinstallしてない場合は`gulp build`のかわりに`package.json`に以下のように記載する。

```json
  "scripts": {
    "build_semantic_ui": "cd semantic; gulp build;cd ..;cp -r semantic/dist/* promodoro/semantic/"
  }
```

## Reference
* [Semantic UI](https://semantic-ui.com/)

