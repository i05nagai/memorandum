---
title: linux/common
---

## linux/common

## /etc/group

```
hoge_group:x:501:hoge_user3,hoge_user2
```

| hoge_group            | グループ名                                                                                             |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| x                     | 「 x 」という文字か、暗号化されたパスワード。「 x 」はシャドウパスワードを使用している事を意味します。 |
| 501                   | グループID( GID )                                                                                      |
| hoge_user3,hoge_user2 | サブグループとして所属しているユーザーアカウントのリスト。カンマ区切り。                               |

* userは複数のgroupに所属できる
* primary group/initial group
    * userの基本group
* fileを作成した場合は、userのprimary groupに設定される
* primary groupは`id` commandで確認できる


## Reference
* [Linux グループ一覧の確認と/etc/group ファイル](http://kazmax.zpp.jp/linux_beginner/etc_group.html)
