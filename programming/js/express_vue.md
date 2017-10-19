---
title: express-vue
---

## express-vue

```
npm install --save express-vue
```

`app.js`に以下を記載する。

```JavaScript
var expressVue = require('express-vue');

var app = express();
const vueOptions = {
    rootPath: path.join(__dirname, '../example/views'),
    layout: {
        start: '<div id="app">',
        end: '</div>'
    }
};
const expressVueMiddleware = expressVue.init(vueOptions);
app.use(expressVueMiddleware);
```

Routingのファイルに以下を記載すると `views/main.vue`を描画できる。

```JavaScript
router.get('/main', (req, res, next) => {
    const data = {
        otherData: 'Something Else'
    };
    const vueOptions = {
        head: {
            title: 'Page Title',
            meta: [
                { property:'og:title', content: 'Page Title'},
                { name:'twitter:title', content: 'Page Title'},
            ]
        }
    }
    res.renderVue('main', data, vueOptions);
});
```

## Reference
* [GitHub - express-vue/express-vue: Vue rendering engine for Express.js. Use .Vue files as templates using streams](https://github.com/express-vue/express-vue)
