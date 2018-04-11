---
title: ElasticSearch
---

## ElasticSearch

## QueryDSL
* [Query DSL | Elasticsearch Reference [6.2] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

Queryはquery contexstとfilterがある。

* query context
    * `"query":`の中のquery
    * どの程度query clauseにmatchするか
    * `_score` のscoreを計算する
* filter context
    * `"filter":`の中のquery
    * documentがquery clauseにmatchするか
    * yes/noのbool
    * `bool`, `must_not_`, 

* `constant_score`
    * 中のqueryにmatchするものはconstant scoreを返す

```json
GET /_search
{
    "query": {
        "constant_score" : {
            "filter" : {
                "term" : { "user" : "kimchy"}
            },
            "boost" : 1.2
        }
    }
}
```

* `bool`
    * bool query
    * `must`
        * matchするもの
        * matchしたもののscoreにいれる
    * `filter`
        * matchするもの
        * socreには換算しない
        * cachingの対象になる
    * `must_not`
        * 一致しないもの
        * socreには換算しない
        * cachingの対象になる
    * `should`
        * `should`にmatchしなくても、`bool`がquery contextの中で、`must` or `filter` clauseがmatchするならば一致にする
        * `bool` queryがfilter contextの中か、`must`, `filter`を持たないなら、`should`の中の1つにmatchする必要がある
            * `minimum_should_match`でmatchすべき`should`の数を指定できる

```json
POST _search
{
  "query": {
    "bool" : {
      "must" : {
        "term" : { "user" : "kimchy" }
      },
      "filter": {
        "term" : { "tag" : "tech" }
      },
      "must_not" : {
        "range" : {
          "age" : { "gte" : 10, "lte" : 20 }
        }
      },
      "should" : [
        { "term" : { "tag" : "wow" } },
        { "term" : { "tag" : "elasticsearch" } }
      ],
      "minimum_should_match" : 1,
      "boost" : 1.0
    }
  }
}
```

* `has_child`
    * joinが必要になるので、queryのperformanceが悪くなる
    * matchするparent documentの数が多くなるほどperformanceが悪くなる
    * `score_mode`
        * `none, min, max, avg`
        * matchする全てのchild documentに対して行われる
        * default is none
    * `type`
    * `min_children`
        * matchするchildの最低数
    * `max_children`
        * matchするchildの最大数

```json
GET /_search
{
    "query": {
        "has_child" : {
            "type" : "blog_tag",
            "query" : {
                "term" : {
                    "tag" : "something"
                }
            }
        }
    }
}
```

* `function_score`
    * [Function Score Query | Elasticsearch Reference [6.2] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html)
    * documentのsocreの計算方法を変更できる
    * 例えばfilterしたdocumentのみのscoreだけ計算すれば良いなど
    * `score_mode`
        * docのscoreと`function_score`のscore(複数の場合は`functions`の中)をどう利用するか
        * `multiply`
            * default
        * `replace`
            * queryのsocreを無視して、function scoreを使う
        * `sum`
        * `avg`
        * `max`
        * `min`
    * `functions`
        * scoreの計算が複数ある場合にarrayでscoreの計算方法を指定
    * `script_score`
        * queryを使ってdocumentのnumeric fieldからscoreを計算
    * `weight`
        * もとのscoreにweightをかける
    * `random_score`
        * `[0, 1]`のuniformly distributed random varをかける
    * `filed_value_factor`
    * `decay_function`

```json
GET /_search
{
    "query": {
        "function_score": {
            "query": { "match_all": {} },
            "boost": "5",
            "random_score": {}, 
            "boost_mode":"multiply"
        }
    }
}
```


## Reference
* [Elasticsearch: RESTful, Distributed Search & Analytics | Elastic](https://www.elastic.co/products/elasticsearch)
