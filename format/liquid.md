---
title: Liquid
---

## Liquid


## Assign Variables
変数への代入はassignを使う。

```liquid
{% assign str_variable_name = "string" %}
{% assign int_variable_name = 999 %}
```

代入する値に、Liquid変数を使いたい場合は、captureを使う。

```liquid
{% assign int_variable_name = 999 %}
{% capture variable_name %}Price is {{ int_variable_name}}{% endcapture %}
{{ variable_name }}
```

* `Price is 999`が出力となる。


## Reference
* [Liquid for Designers · Shopify/liquid Wiki](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers)
