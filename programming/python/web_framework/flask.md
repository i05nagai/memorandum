---
title: Flask
---

## Flask

## Quickstart
* [Quickstart — Flask 1\.0\.2 documentation](http://flask.pocoo.org/docs/1.0/quickstart/)

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
`<a href="{{ url_for('static', filename='hoge.css') }}"></a>`

## Externally visible server
* [Quickstart — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application)

自分のPC以外やdocker containerの外かららアクセスするようにしたい場合は、`--host=0.0.0.0`で起動する。

```
flask run --host=0.0.0.0
```

## With wsgi and apache222

## Get query

```
# http://example.com/path?body=hoge&attrs[]=fuga&attrs[]=hage
# get parameter
body = request.args.get('body')
# get list
attrs = request.args.getlist('attrs[]')
```

#### Directory structure
* [Organizing your project — Explore Flask 1\.0 documentation](http://exploreflask.com/en/latest/organizing.html)

* `run.py`
    * This is the file that is invoked to start up a development server.
    * It gets a copy of the app from your package and runs it. This won’t be used in production, but it will see a lot of mileage in development.
* `requirements.txt`
    * This file lists all of the Python packages that your app depends on. You may have separate files for production and development dependencies.
* `config.py`
    This file contains most of the configuration variables that your app needs.
* `/instance/config.py`
    * This file contains configuration variables that shouldn’t be in version control.
    * This includes things like API keys and database URIs containing passwords. This also contains variables that are specific to this particular instance of your application. For example, you might have DEBUG = False in config.py, but set DEBUG = True in instance/config.py on your local machine for development. Since this file will be read in after config.py, it will override it and set DEBUG = True.
* `/yourapp/`
    * This is the package that contains your application.
* `/yourapp/__init__.py`
    * This file initializes your application and brings together all of the various components.
* `/yourapp/views.py`
    * This is where the routes are defined. It may be split into a package of its own (yourapp/views/) with related views grouped together into modules.
* `/yourapp/models.py`
    * This is where you define the models of your application. This may be split into several modules in the same way as views.py.
* `/yourapp/static/`
    * This directory contains the public CSS, JavaScript, images and other files that you want to make public via your app. It is accessible from yourapp.com/static/ by default.
* `/yourapp/templates/`
    * This is where you’ll put the Jinja2 templates for your app.

#### Flask with React
* [realpython/ultimate\-flask\-front\-end: blog post](https://github.com/realpython/ultimate-flask-front-end)

#### Production server
* http://flask.pocoo.org/docs/1.0/tutorial/deploy/
    * https://docs.pylonsproject.org/projects/waitress/en/stable/
* http://flask.pocoo.org/docs/1.0/deploying/wsgi-standalone/


```
gunicorn -w 4 -b 127.0.0.1 5000 <filename>:<flask-app-var-name>
```

#### Monitoring
Monitoring with DataDog

https://www.datadoghq.com/blog/monitoring-flask-apps-with-datadog/

## Reference
* [Welcome to Flask — Flask Documentation (0.12)](http://flask.pocoo.org/docs/0.12/)
