---
title: Scrapy
---

## Scrapy

```
scrapy startproject sample_project
```

`sample_project/sample_project/settings.py`の`DOWNLOAD_DELAY`に平均DL間隔を秒で指定する。
defaultは0なので、comment outされた行をcommetinしておく。

```
├── sample_project
│   ├── __init__.py
│   ├── __pycache__
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
└── scrapy.cfg
```

* `items.py`

設定をもとに以下のcommandでspiderを作成できる。

```
scrapy genspider spider_name domain
```

途中から再開できるようにしてcrawl開始

```
crapy crawl somespider --set JOBDIR=crawl1
```


## Spider
* [Spiders — Scrapy 1.4.0 documentation](https://doc.scrapy.org/en/latest/topics/spiders.html)

## Request/Response
* [Requests and Responses — Scrapy 1.4.0 documentation](https://doc.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Response)
* [Requests and Responses — Scrapy 1.4.0 documentation](https://doc.scrapy.org/en/latest/topics/request-response.html#formrequest-objects)

* FormRequest
    * 必要な情報をformに入力しrequestを出す
    * loginや検索に使える

* `response.body`
* `response.meta`
    * 



## Item Pipeline
* [Item Pipeline — Scrapy 1.4.0 documentation](https://doc.scrapy.org/en/latest/topics/item-pipeline.html)


## Item
* [Items — Scrapy 1.4.0 documentation](https://doc.scrapy.org/en/latest/topics/items.html)



## CLI

```
scrapy genspider spider_name domain
```

* `--list`, `-l`
    * spider作成時に利用可能なtemplate
* `--template=TEMPLATE_NAME`, `-t TEMPLATE_NAME`
    * templateを指定できる

```
scrapy shell file/url
```


## Tips

### 実行時に引数わたす
spiderのinitに以下のように引数を定義する。
`start_urls`などはinit内で定義してあれば良い。

```
class SomeSpider(scrapy.Spider):
    name = 'some'
    allowed_domains = ['some.domain']

    def __init__(self, some_key='default_val'):
        super().__init__()
        self.start_urls = [
            'some_url',
        ]
```

crawl実行時に`-a`でkeywordと値を渡す。

```
scrapy crawl spider_name -a some_key=n00021265
```

### Download files
以下をsettings.pyに記載する。

```python
ITEM_PIPELINES = {
    'scrapy.pipelines.files.FilesPipeline': 1
}
FILES_STORE = '/path/to/valid/dir'
FILES_URLS_FIELD = 'field_name_for_your_files_urls'
FILES_RESULT_FIELD = 'field_name_for_your_processed_files'
```

```
<FILES_STORE>/full/3afec3b4765f8f0a07b78f98c07b83f013567a0a.jpg
```

* `files`
    * list of dict
* `file_urls`
    * list of urls

### robots.txt
* ROBOTSTXT_OBEY=False

## Reference
