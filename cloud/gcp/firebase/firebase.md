---
title: Firebase
---

## Firebase


## Analytics
* [Get Started with Google Analytics for Firebase for iOS  |  Firebase](https://firebase.google.com/docs/analytics/ios/start)
* [Log events  |  Firebase](https://firebase.google.com/docs/analytics/ios/events)
    * Send log events
* User properties
    * [Set User Properties  |  Firebase](https://firebase.google.com/docs/analytics/ios/properties)
    * userのpropertyを付与できる
    * propertyを元にuser segmentationを分けることができる

Google analyticsのような機能が使える。

logを送信する時に自動で収集されているevent

* [Events and properties - Firebase Help](https://support.google.com/firebase/topic/6317484?hl=en&ref_topic=6386699)
    * [Firebase API reference for Event](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event.html#VIEW_ITEM)
    * events
        * [Automatically collected events - Firebase Help](https://support.google.com/firebase/answer/6317485)
    * user properties
        * [Automatically collected user properties - Firebase Help](https://support.google.com/firebase/answer/6317486)
    * data collections
        * 追加で収集可能なData
        * iOS appではIDFAを設定すれば、自動で年齢/性別などを取得できる。
        * [Data collection - Firebase Help](https://support.google.com/firebase/answer/6318039)
        * [Firebaseのデモグラフィックデータを用いたCM分析 - inFablic | Fablic, inc. Developer's Blog.](http://in.fablic.co.jp/entry/2017/08/30/100000)
   * [Attribution - Firebase Help](https://support.google.com/firebase/answer/6317518) 
       * conversionとしてpredefinedされているevent
           * first_open
           * in_app_purchase
           * ecommerce_purchase
       * consoleからeventをconversionとして登録できる


eventの一覧
Andiroid onlyのものが多い

* first_open
    * install/re-installした後に最初に開いた時
* in_app_purchase
    * AppStore, Google Playで購入した際に、以下のparamterとともに記録される
        * product ID
        * product name
        * currency
        * quantity
* os_update
    * deviceのOSがupdateされた時
    * 以前のOS idをparameterとして渡す
* screen_view
    * 以下のいずれかでおこる
        * 今のscreenより前のscreenがない
        * 新しいscreenの名前が、前のscreenの名前と違う
        * screenのclass nameが前のと違う
        * screen idが前のscreen idと違う
* session_start
    * [setSessionTimeoutDuration](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setSessionTimeoutDuration(long))
        * default: 30min
        * 30sec以上engagementがない場合は、sessionの離脱とみなす
    * [setMinimumSessionDuration](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setMinimumSessionDuration(long))
        * default: 10 sec
        * 10sec以上engagementしていたら、sessionの開始とみなす


user_dimの一覧

* first_open_timestamp_micros
    * [firebase - Does user_dim.first_open_timestamp_micros change when app updated or reinstalled? - Stack Overflow](https://stackoverflow.com/questions/39244057/does-user-dim-first-open-timestamp-micros-change-when-app-updated-or-reinstalled)
    * reinstall, installの後に最初に開いた時間
    * appのupdateでは更新なれない


* Engagement
    * [Track Screenviews  |  Firebase](https://firebase.google.com/docs/analytics/screenviews?authuser=0)
        * screenに名前をつけられる
    * 各画面のuesrの滞在時間
* Retention cohort
    * [How firebase measures retention cohorts ? - Google Groups](https://groups.google.com/forum/#!topic/firebase-talk/Gaewx9Q2DIg)
    * [Firebase exported to BigQuery: retention cohorts query - Stack Overflow](https://stackoverflow.com/questions/41509431/firebase-exported-to-bigquery-retention-cohorts-query)
    * googleがfalse eventだと判断したものはFilterしている
    * cohortのfilterはできない
* Events
    * conversionにevent名を指定できる
    * parameterこみで指定はできない
* Funnel
    * funnelのeventにevent名しか指定できない
    * parameterこみで指定はできない
* Remote configs
    * [Set up a Firebase Remote Config project - Firebase Help](https://support.google.com/firebase/answer/6386651?hl=en&ref_topic=6386642)
    * [Create Firebase Remote Config Experiments with A/B Testing  |  Firebase](https://firebase.google.com/docs/remote-config/abtest-config)
    * A/B test用のparameterをfirebaseから送れる
    * A/B testのgoalとしてevent名を指定できる
        * A/B testのgroupごとに指標をおえる
    * User propertyを追加すれば、A/B testのgroupに指定できる


## Reference
* [Firebaseの始め方 - Qiita](https://qiita.com/kohashi/items/43ea22f61ade45972881)
- https://firebase.google.com/docs/build
