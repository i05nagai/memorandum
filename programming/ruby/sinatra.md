---
title: sinatra
---

## sinatra


## content_type
* [Method: Sinatra::Helpers#content_type — Documentation for sinatra/sinatra (master)](http://www.rubydoc.info/github/sinatra/sinatra/Sinatra%2FHelpers%3Acontent_type)

## Resposen json data
`content_type :json`が必要。
`charset: 'utf-8'`は必要であればつける。

```ruby
require 'json'

get '/' do
  content_type :json, charset: 'utf-8'
  val = params['val']
  { data: val }.to_json
end
```

## restful API
* [How To Create a Ruby API with Sinatra](https://x-team.com/blog/how-to-create-a-ruby-api-with-sinatra/)


## Tips

### Cross site origin
* [html - Sinatra access-control-allow-origin for sinatra public folder - Stack Overflow](https://stackoverflow.com/questions/7109971/sinatra-access-control-allow-origin-for-sinatra-public-folder)

以下の形式で許可するsiteを選ぶ

```ruby
before do
    response['Access-Control-Allow-Origin'] = 'http://whatever.org'
end
```

## Reference
* [Sinatraがデフォルトでは外部から繋がらなくなってたよ - Qiita](https://qiita.com/u1_fukui/items/b86b21f6ed39f4c10d5d)
