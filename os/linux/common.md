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


## export no_proxy
* [no_proxy にネットワークアドレスとかワイルドカードを指定しても期待通りに動かない、でどうするかというお話 - 双六工場日誌](http://sechiro.hatenablog.com/entry/2013/08/06/no_proxy_%E3%81%AB%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E3%81%A8%E3%81%8B%E3%83%AF%E3%82%A4%E3%83%AB%E3%83%89%E3%82%AB%E3%83%BC%E3%83%89%E3%82%92)


## /etc/profile.d/
* [bash - What do the scripts in /etc/profile.d do? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/64258/what-do-the-scripts-in-etc-profile-d-do)
* /etc/profile が読み込まれつとき、`/etc/profile.d/`以下のfileも全て読み込まれる


## /etc/environment
* [Setting PATH variable in /etc/environment vs .profile - Ask Ubuntu](https://askubuntu.com/questions/866161/setting-path-variable-in-etc-environment-vs-profile)
* root権限で管理されるenvironment
* `PATH`などは`/etc/profile.d/`などに書いたほうが良い

## /etc/bash_completion
* [An introduction to bash completion: part 1](https://debian-administration.org/article/316/An_introduction_to_bash_completion_part_1)
* [Bash-Completion で複雑な補完をする - いますぐ実践! Linuxシステム管理 / Vol.236](http://www.usupi.org/sysad/236.html)
*
* `/etc/bash_completion`がよみこまれるとき、`/etc/bash_completion.d/`以下のファイルも全て読み込まれる


```
complete -F _known_hosts xvncviewer
```

* `_know_hosts`
    * `/etc/bash_completion` で定義されている
* `xvncviewer`
    * commandの実行時


## Reference
* [Linux グループ一覧の確認と/etc/group ファイル](http://kazmax.zpp.jp/linux_beginner/etc_group.html)
