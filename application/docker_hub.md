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


## Reference

