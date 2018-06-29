## Docker Hub

## Organization and teams in Docker Hub
* [Organizations and teams in Docker Hub | Docker Documentation](https://docs.docker.com/docker-hub/orgs/)

* Oarganizationは複数のteamをもてる
* 各teamは別々の権限を持てる
* Namespaceはorganizationは一意の識別子で、dokcer imageは`organization_namespace/docker_image_name`に配置される
* teamごとにinviteができる
* `owners` teamは全ての権限を持っている

## Automated Build
* [Docker Hubを使ってGitHubにあるDockerfileからimageを自動生成する – Simple IT Life](https://simple-it-life.com/2016/03/27/dockerhub/)

Githubのrepositoryからgit hubのpushを起点に自動ビルドできる。

* `Create->Create Automated Build`
    * アカウントのリンクができてない場合はlinkの画面がでる
* link後に`Create->Create Automated Build`
    * GithubかBitBucketを選ぶ
* sourceとなるrepositoryを選択する
* 以下を決める
    * repositoryのnamespace
    * imageの名前
    * public/private
    * 100文字の簡単な説明

* [Configure automated builds on Docker Hub | Docker Documentation](https://docs.docker.com/docker-hub/builds/#limitations)

automted buildでTagをつける方法。
git tagかbranchでbuildを制御できる。
git tag名かbranch名にdockerのtag名を付与して、build時に自動でdocker imageにtagを付与することができる。

`BuildSettings`からTypeをtagにして、設定を追加すればcommitにつけたtagがdocker imageのtagになる。

```
git tag -a hoge-1.1.1
git push hoge-1.1.1
```

## Collaborator
defaultでは、repositoryの作成者にしか権限がない？
Collaboratorの所から必要なteamをaddする必要がある。

## Delete account/organization
* [How do I delete a Docker Hub or Docker Cloud account? - Docker, Inc.](https://success.docker.com/Cloud/Solve/How_do_I_delete_a_Docker_Hub_or_Docker_Cloud_account%3F)

supportに削除依頼する前に以下を実施する。

* accountのpublic repositroyとprivate repositoryを削除
* subscription planは全てcancelしてfree planにする
* organizationに属している場合は、organizationから抜ける
* organizationの唯一のownerの場合は、別のownerをつけて自分は抜けるo
    * それかorganizationも合わせて削除申請する
    * organiztionを削除する場合は、owenerは自分だけにする
* liscence keyが必要な場合は削除前にDLしておく
* GitHubとBitbucketをunlinkする

全部終わったら[Technical Support - Docker, Inc.](https://success.docker.com/Support)の下部にあるcustomer serviceからrequestを送る。
emailは自分のaccoutのemailと同じものにする。

```
Delete an organization in docker hub

Dear customer supports,

I would like to delete an organization, 'xxxxx', which we don't use anymore.
Could you delete 'xxxxx' organization?
Here is my account information.

* account name: uuuuuu
* account URL: https://hub.docker.com/u/uuuuuu/
* xxxxx organization which I want to delete: https://hub.docker.com/u/xxxxx/dashboard/

Thank you in advance.

Best reagards,
Name
```


## Reference

