## Analytics

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

## Reference
* [How a web session is defined in Analytics - Analytics Help](https://support.google.com/analytics/answer/2731565?hl=en)
