---
title: Flask
---

## Flask

## Static files
以下のような感じでおく。

* static
* templates
* app.py

program中でstati fileのurlが必要な場合は以下のcodeで取得できる。

```python
url_for('static', filename='style.css')
```

template内でも利用できる。

```html
<a href="{{ url_for('static', filename='hoge.css')"></a>
```

## Externally visible server
* [Quickstart — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application)

自分のPC以外やdocker containerの外かららアクセスするようにしたい場合は、`host=0.0.0.0`で起動する。

```
app.run(host='0.0.0.0', port=500)
```

## With wsgi and apache222




## Reference
* [Welcome to Flask — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/)
