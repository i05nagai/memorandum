---
title: What Crawl Budget Means for GoogleBot
---

## What Crawl Budget Means for GoogleBot
* [Official Google Webmaster Central Blog: What Crawl Budget Means for Googlebot](https://webmasters.googleblog.com/2017/01/what-crawl-budget-means-for-googlebot.html)

Googlebotはweb userの良い手本となるように設計されている。
Crawl budgetはCrawl rate limitとCrawl demandにもとづいて、googlebotがcrawlするURLの数として定義されている。

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
Crawl rate limitに達していなくても、indexの要求がなければGoogleBotはactiveにindexをしようとしない。
indexの要求は以下の2つの要素が重要である。

* Popularity
    * internetのtrendでpopularなものは情報を最新に保つためよりcrawlされる
* Staleness
    * indexされているものが現状と乖離して古くなりすぎないようにする


siteのURLの変更/移動もまた、crawl demandを増やす要因である。

### Factor affecting crawl budget
価値の低いURLの追加が、crawlingとindexingの数に影響を与えることがわかっている。
価値の低いURLとして以下のようなものがある。
数字が小さいものほど重要である。

1. Faceted navigation/ session identifier
    * Faceted navigation
        * [Official Google Webmaster Central Blog: Faceted navigation best (and 5 of the worst) practices](https://webmasters.googleblog.com/2014/02/faceted-navigation-best-and-5-of-worst.html)
        * 価格や色などで、filteringできる機能
        * faceted navigationは同じようなcontentsを持つ複数のURLを持つ場合が多いので、crawlingには悪い影響を与える
    * [Official Google Webmaster Central Blog: Google, duplicate content caused by URL parameters, and you](https://webmasters.googleblog.com/2007/09/google-duplicate-content-caused-by-url.html)
2. On-site duplicate contents
3. Soft error page
    * [Official Google Webmaster Central Blog: Crawl Errors now reports soft 404s](https://webmasters.googleblog.com/2010/06/crawl-errors-now-reports-soft-404s.html)
4. Hacked pages
5. Infinite spaces and proxies
    * [Official Google Webmaster Central Blog: To infinity and beyond? No!](https://webmasters.googleblog.com/2008/08/to-infinity-and-beyond-no.html)
6. Low quality and span content

### Top questions
* Q: Does site speed affect my crawl budget? How about errors?
    * siteの高速はUXの向上とcrawl rateの向上に繋がる
    * GoogleBotはsite speedが早いsiteを良いsiteとみなして、多くのcontentを取得しようとする
* Q: Is crawling a ranking factor?
    * craw rateの向上はsearch resultの順位とは無関係
    * search resultの順位は数百の要素によって決まる
    * crawlingはただsearch resultに表示する候補のpageを取得するだけ
* Q: Do alternate URLs and embedded content count in the crawl budget?
    * 一般的に、GoogleBotがcrawlするURLは全て、crawl budgetを消費する
    * Alternate URL(AMP, hreflang), embedded content (CSS, JavaScript)なども全てcrawl budgetを消費する
    * 同様にlong redirect chainもcrawlingに影響を与える
* Q: Can I control Googlebot with the "crawl-delay" directive?
    * `robots.txt`の`crawl-delay`はGoogleBotは考慮しない
* Q: Does the nofollow directive affect crawl budget?
    * 場合による
    * crawlしたURLは全てcrawl budgetを消費する
    * `nofollow`にしてもcrawlされたのであれば、消費する


Crawlingの最適化をしたいのであれば、下記の古い記事はまだ有効である。

[Official Google Webmaster Central Blog: Optimize your crawling & indexing](https://webmasters.googleblog.com/2009/08/optimize-your-crawling-indexing.html)

## Reference
* [Official Google Webmaster Central Blog: What Crawl Budget Means for Googlebot](https://webmasters.googleblog.com/2017/01/what-crawl-budget-means-for-googlebot.html)
