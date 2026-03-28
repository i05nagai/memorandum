---
title: Google Analytics
---
## Google Analytics
分析をしたいsiteごとにproperty `UA-xxxx`を作成する。

## Term
* Exit rate
    * Pageごとに測る
    * PageのExit rateとは、visitの最後のpageが該当pageのvisitの数の割合
    * visitの最後が / PageのPV数
    * 離脱率
* Bounce rate
    * Pageごとに測る
    * PageのBounce rateとは、visitのfirst pageviewが該当pageのvisitで、pvが1のもの
    * 直帰率
    * 1 pageviewのvisitの数 / first pageviewが該当pageのvisitの数
    * [Exit Rate vs. Bounce Rate - Analytics Help](https://support.google.com/analytics/answer/2525491?hl=en)

* visit log
    * B -> A -> C -> exit
    * B -> exit
    * A -> C -> B -> exit
    * C -> exit
    * B -> C -> A -> exit
* Bounce rate
    * AのBounce rateは、0%
    * BのBounce rateは 33.3%
    * CのBounce rateは 100%
* Exit rate
    * AのExit rateは、33.3%
    * BのExit rateは、50%
    * CのExit rateは、50%


* Hit
* Pageview
* Visit
* Visitors
* Time on page
* Time on site
* New visitor
* Returning visitor
* Dollar index
* Pages/visit
* Direct Traffic
* Referring sites
* Search engine trafic
* Event tracking
*


## How a web session is defined in Analytics
sessionを決める基本的なルールは以下の2つ

* activityの間隔が30分以上空いた場合は別のsessoionとする
    * 30分はデフォルトの設定で変更可能
    * 29分59秒までは同じsession
* 午前0時になった場合に新しいsessionとする
    * どこの国の午前0時かは変更可能

## For Github Pages
* [igrigorik/ga-beacon: Google Analytics collector-as-a-service (using GA measurement protocol).](https://github.com/igrigorik/ga-beacon)
* [How to add Google Analytics Tracking ID to GitHub Pages - Stack Overflow](https://stackoverflow.com/questions/17207458/how-to-add-google-analytics-tracking-id-to-github-pages)

Sign upでGithub pagesの`http://`を登録する。
`Tracking info` -> `Tracking code`でjsが発行されているので、github pagesで生成されるpageのheaderに生成されたコードを挿入する。
jekyllなどでlocalhostする場合のtrackingを除く場合は以下のようにhostnameで場合分けをする。

```
  // Skip recording GA events to our account if in development.
  if (document.location.hostname != 'localhost') {
    ga('create', 'UA-xxxx', 'auto');
    ga('send', 'pageview');
  }
```

## Move property to another account
* [プロパティを移行する - アナリティクス ヘルプ](https://support.google.com/analytics/answer/6370521?hl=ja)

1. アナリティクス アカウントにログインします。
2. [管理] タブをクリックします。
3. [アカウント] 列のメニューで、移行するプロパティが含まれているアカウントを選択します。
    * アカウントの数が多い場合は、検索ボックスで対象のアカウントを検索できます。
4. [プロパティ] 列で、移行するプロパティを選択します。
5. [プロパティ設定] をクリックし、[プロパティの移行] をクリックします。
6. 移行先アカウントを選択します。
7. 権限設定を選択します。
    * 既存のプロパティとビューの権限を維持します。現在のユーザー権限がプロパティにコピーされます。移行先のアカウントの権限はプロパティに継承されません。
    * 既存のプロパティとビューの権限を移行先のアカウントの権限と置き換えます。プロパティは移行先のアカウントの権限を継承します。
8. [移行] をクリックします。
9. 移行後のデータを確認して、[保存] をクリックします。

  ga('create', 'UA-103616144-1', 'auto');

## Multiple tracking
* [Googleアナリティクス基礎：複数のトラッキングコード（マルチトラッキング）設定](http://www.kagua.biz/tracking/multitracking.html)

複数のtrackning codeを一つのweb siteに含めるだけなら以下のようにする。

```html
<script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

    //トラッカーを宣言
    ga('create', 'UA-xxxxxxxx-1', 'auto', {'allowLinker': true, 'name': 'a'});
    ga('create', 'UA-xxxxxxxx-2', 'auto', {'allowLinker': true ,'name': 'b'});

    //データをsend
    ga('a.send', 'pageview');
    ga('b.send','pageview');
</script>
```

## ga
* [analytics.js の仕組み  |  ウェブ向けアナリティクス（analytics.js）  |  Google Developers](https://developers.google.com/analytics/devguides/collection/analyticsjs/how-analyticsjs-works?hl=ja)

* `create`

```javascript
ga('create', {
  trackingId: 'UA-XXXXX-Y',
  cookieDomain: 'auto',
  name: 'myTracker',
  userId: '12345'
});
```

複数のtrackerを使う時は、`name`は必須である。
nameで指定した名前を指定してcommandを実行する。

```javascript
ga('send', 'pageview');
ga('myTracker.send', 'pageview');
```

* `require`
    * pluginを読み込む

```
ga('myTracker.require', 'displayfeatures', {
  cookieName: 'display_features_cookie'
});
```

## Recommended events
https://support.google.com/analytics/answer/9267735


## Custom dimension in looker
https://www.tribalism.com.au/blog-post/2023/12/ga4-custom-dimensions-in-looker-studio#start



## Data discrepancy betwee GA4 and Looker
https://www.reddit.com/r/GoogleAnalytics/comments/1nw0fsh/data_discrepancy_between_ga4_and_looker_what_am_i/

- GA4 uses its own aggregation logic
- 

## Channel group
https://support.google.com/analytics/answer/9756891?hl=en


## UTM parameters
https://en.wikipedia.org/wiki/UTM_parameters
https://cerebro.us/ultimate-utm-guide/
https://support.google.com/analytics/answer/10917952?hl=en
https://gaconnector.com/blog/7-examples-of-using-utm-parameters-effectively/

- Source
    - Which social network, search engine, or specific source drove the traffic to your site?
    - The source of the traffic you are receiving. Normally this is the domain or business name.
    - utm_source
        - google, facebook, nytimes, yelp, etc
- Medium
    - Which channel type (e.g., organic social, paid social, email) drove the traffic to your site?
    - The type of traffic you are receiving.
    - utm_medium
        - i.e. cpc, organic, post, promoted, boosted, etc
- Term
    - Are there paid keywords or key phrases that warrant a UTM tag?
    - The keyword or audience who clicked on your link
    - utm_term
        - i.e. keyword, las vegas locals, etc.
- Content
    - Are there different ads within a campaign? 
    - The type of ad or creative being used
        - utm_content
            - i.e. video, image, negative emotion, humor, etc
- Campaign name
    - Every campaign should have a unique name, so you can keep track of traffic. This could be the name of a contest, sale, deal, influencer ID, or even a product name.  
    - The name of the campaign or promotion you are running.
    - utm_campaign
        - i.e. thanksgiving sale, 2 for 1 deal, etc.



## Reference
* [How a web session is defined in Analytics - Analytics Help](https://support.google.com/analytics/answer/2731565?hl=en)
* [Briefmetrics - Email Reports for Google Analytics](https://briefmetrics.com/articles/remove-localhost-from-referrers)
