## Analytics

## How a web session is defined in Analytics
sessionを決める基本的なルールは以下の2つ

* activityの間隔が30分以上空いた場合は別のsessoionとする
    * 30分はデフォルトの設定で変更可能
    * 29分59秒までは同じsession
* 午前0時になった場合に新しいsessionとする
    * どこの国の午前0時かは変更可能

## Reference
* [How a web session is defined in Analytics - Analytics Help](https://support.google.com/analytics/answer/2731565?hl=en)
