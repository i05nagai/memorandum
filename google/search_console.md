---
title: Search Console
---

## Search Console
Googleのsiteの検索ワードや検索順位などを調べることができる。
SEO用のtool.

## Google Analytics
`property settings` -> `Edit`でSearch consoleに移動する。
`Add a site to Search Console`でGoogle Analyticsに登録しているものと、同じsiteを登録する。　
URLを入力して`Propertyを追加`.
所有権の確認で、Google Analyticsを使用するで、確認を押す。


## Crawl budget
* [Official Google Webmaster Central Blog: What Crawl Budget Means for Googlebot](https://webmasters.googleblog.com/2017/01/what-crawl-budget-means-for-googlebot.html)

Googlebotはweb userの良い手本となるように設計されている。

### Crawl rate limit
googlebotのcrawlのlimit

Crawl rate limitは主に以下の2つの要素によって変更される。

* Crawl health
    * web siteが一定期間早いresponseを返した場合、limitは引き上げられ、google botはcrawlの際に多くのconnectionを利用するようになる
    * 逆にresponseが遅いやserverがerrorを返した場合は、limitは引き下げられ、googlebotのcrawlは減る
* Limit set in search console
    * web siteのowenerはSearch consoleから明示的にcrawlを減らすことができる
    * Search consoleでLimitを引き上げても、必ずしも反映されるわけではない

### Crawl Demand
Crawl rate limitに

### Top questions
* Q: Does site speed affect my crawl budget? How about errors?


## Reference
* [Briefmetrics - Email Reports for Google Analytics](https://briefmetrics.com/articles/remove-localhost-from-referrers)
* [サーチコンソール（Google Search Console）の使い方と登録方法教えます](http://seolaboratory.jp/other/2016062936916.php)
