---
title: Google App Engine
---

## Google App Engine


## Examples
* [googlearchive/appengine-modules-helloworld-python](https://github.com/googlearchive/appengine-modules-helloworld-python)

## app.yaml
* [app.yaml Reference  |  App Engine standard environment for Python  |  Google Cloud Platform](https://cloud.google.com/appengine/docs/standard/python/config/appref)

```yaml
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /
  script: home.app

- url: /index\.html
  script: home.app

- url: /stylesheets
  static_dir: stylesheets

- url: /(.*\.(gif|png|jpg))$
  static_files: static/\1
  upload: static/.*\.(gif|png|jpg)$

- url: /admin/.*
  script: admin.app
  login: admin

- url: /.*
  script: not_found.app
```

* env_variables
* handlers
* includes
    * yamlのincludeができる
* instance_class
    * default F1

```
libraries:
- name: PIL
  version: "1.1.7"
- name: webob
  version: "latest"
```

```
skip_files:
- ^(.*/)?#.*#$
- ^(.*/)?.*~$
- ^(.*/)?.*\.py[co]$
- ^(.*/)?.*/RCS/.*$
- ^(.*/)?\..*$
```

* skip_files
    * App Engineにuploadされないfile
* threadsafe
    * true/false


```yaml
handlers:
# The root URL (/) is handled by the WSGI application named
# "app" in home.py. No other URLs match this pattern.
- url: /
  script: home.app

# The URL /index.html is also handled by the home.py script.
- url: /index\.html
  script: home.app

# A regular expression can map parts of the URL to the
# path of the script.
- url: /browse/(books|videos|tools)
  script: \1.catalog.app

# All other URLs use the WSGI application named in "app"
# in not_found.py.
- url: /.*
  script: not_found.app
```

* handlers
    * `home.app`は`home.py`の`home.app` WSGI applicationを呼び出す
    * extensionがappの場合はWSGI, `.py`の場合はCGI scriptとして実行される
    * 正規表現も使える

```
automatic_scaling:
  min_idle_instances: 5
  max_idle_instances: automatic  # default value
  min_pending_latency: 30ms  # default value
  max_pending_latency: automatic
  max_concurrent_requests: 50
```

* automatic_scaling
    * min_idle_instances
        * default valueはautomatic
    * max_concurrent_requests
        * default 8, maximum 80
    * max_pending_latency


## Cron jobs
* [Scheduling Tasks With Cron for Python  |  App Engine standard environment for Python  |  Google Cloud Platform](https://cloud.google.com/appengine/docs/standard/python/config/cron)
* [cron.yaml Reference  |  App Engine standard environment for Python  |  Google Cloud Platform](https://cloud.google.com/appengine/docs/standard/python/config/cronref)

```yaml
cron:
- description: "daily summary job"
  url: /tasks/summary
  schedule: every 24 hours
- description: "monday morning mailout"
  url: /mail/weekly
  schedule: every monday 09:00
  timezone: Australia/NSW
- description: "new daily summary job"
  url: /tasks/summary
  schedule: every 24 hours
  target: beta
```

* description 
* retry_parameters
    * retryする回数
    * default 0
* schedule
    * format
        * [cron.yaml Reference  |  App Engine standard environment for Python  |  Google Cloud Platform](https://cloud.google.com/appengine/docs/standard/python/config/cronref#schedule_format)
* target
    * service名
* url
    * requestを送るurl
* timezone
    * TZの値が使える
        * [List of tz database time zones - Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
    * default UTC

## Pricing
* [App Engine Pricing  |  App Engine Documentation  |  Google Cloud Platform](https://cloud.google.com/appengine/pricing)

以下の価格は`lowa` regionの価格

* Standard Enviornment
    * Instaceごとに1時間ごとの利用料金がかかる
    * B1: 0.05USD
    * F4_1G: 0.3USD
* Flexible Environment
    * VMのCPU/memory/persistent diskごとに利用料金がかかる
    * vCPU: 0.0526USD/core hour
    * Memory: 0.0071USD/GB hour
    * Persistent disk: 0.041USD/GB monthourh


## Monitoring
* [Google App Engine Cron Job Monitoring – Google Cloud Platform — Community – Medium](https://medium.com/google-cloud/google-app-engine-cron-job-monitoring-bbf5c2ed6ca3)

## CLI

```
gcloud app 
```


## Reference
