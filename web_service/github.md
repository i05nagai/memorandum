---
title: GitHub
---

## GitHub

## GitHub Pages with jekyll

GitHub pagesでjekyllによるサイトの自動生成を使う場合は、`_config.yml`をrepositoryのtopにおく必要がある。
`Settings->GitHub Pages->Theme Chooser`でThemeを一度選択すれば、勝手に生成され、repositoryにコミットされる。
`index.md`がない場合は`README.md`が`index.html`の生成のために利用される。

Githubが利用しているjekyllのversionは以下にある。

* [Dependency versions | GitHub Pages](https://pages.github.com/versions/)

### disable jekyll
GitHub ioで静的web siteを公開する際にはdefaultではjekyllがONになっており、GitHubにpushした後jekyllによってcodeが処理される。
この時、jekyllのmeta directory `_`で始まるfolderなどが存在すると、除外されるなど、既にrepository内に静的HTMLを追加している場合は、jekyllの機能は邪魔になる。
jekyllを無効にする場合は、`.nojekyll`というfileをrepositoryに於けば良いが、置く場所はGitHub ioの設定によって変わる。

* master branch
    * repositoryのroot
* `/docs` folder
    * /docs/.nojekyll として置く
* gh-pages branch
    * repositoryのroot


## Private Access Token
tokenの認証情報をURLに入れる場合は以下のフォーマットで指定する。

```
git clone https://{アカウントA}:{アクセストークン}@github.com/{アカウントA}/{リポジトリ名}
```

### Reference
* [https+アクセストークンを使ってGitHubのアカウントを使い分ける - Qiita](http://qiita.com/tq_jappy/items/6e2f81f372e4abaa5139)

## Caching your GitHub password in Git
次の設定をすると、1度HTTPSでcloneすればGitHubのpasswordをきかれることはなくなる。

### Mac
Gitと`osxkeychain helper`をインストールする。

1. Gitと`osxkeychain helper`がインストールされているかcheck

```shell
$ git credential-osxkeychain
# Test for the cred helper
Usage: git credential-osxkeychain <get|store|erase>
```

2. `osxkeychain helper`がインストールされていなければ、インストールするようにプロンプトが表示される。 

```shell
$ git credential-osxkeychain
xcode-select: note: no developer tools were found at '/Applications/Xcode.app',
requesting install. Choose an option in the dialog to download the command line developer tools.
```

3. インストールができれば以下のコマンドでosxkeychainを使うように設定できる。

```shell
git config --global credential.helper osxkeychain
# Set git to use the osxkeychain credential helper
```


### Reference
* [Caching your GitHub password in Git - User Documentation](https://help.github.com/articles/caching-your-github-password-in-git/)


## Managing Deploy Keys

```
git clone git@github.com:{user}/{repo}.git
```


### Reference
* [Managing deploy keys | GitHub Developer Guide](https://developer.github.com/guides/managing-deploy-keys/)

## Error: Permission denied (publickey)

### Should the sudo command be used with Git?
`sudo`はいらない。

### Check that you are connecting to the correct server

## git clone with ssh
* settingsでpublic keyを登録しておく
    * repositroy単位user単位で登録できる

Before executing `git-clone`, you need to register your private keys through `ssh-add`

```
ssh-add /path/to/prviate_key
```

Be sure to use SSH url for `git-clone`.

## Generating a new SSH key and adding it to the ssh-agent - User Documentation
* [Using SSH Agent Forwarding | GitHub Developer Guide](https://developer.github.com/v3/guides/using-ssh-agent-forwarding/)
* [Generating a new SSH key and adding it to the ssh-agent - User Documentation](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

```
ssh-keygen -t ed25519 -C "circleci@circleci.com"
```

## Adding a new SSH key to your GitHub account - User Documentation
* [Adding a new SSH key to your GitHub account - User Documentation](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
* [Error: Permission denied (publickey) - User Documentation](https://help.github.com/articles/error-permission-denied-publickey/)
* [Travis-CI でコミットして GitHub にプッシュする - 公開鍵認証を利用してみる | そんなこと覚えてない](http://blog.eiel.info/blog/2014/02/18/github-push-from-travis/)


## Search in Github
検索対象にできるのは以下。

* access可能なrepositoryのissue
* Source code
    * default branchのみ対象になる
    * 普通はmaster
* Commits
* Users
* Wikis

制限は

* 256文字以上のqueryは非サポート
* 5こ以上の`AND`, `OR`, `NOT`

### Qualifiers
Qualifiersの前に`-`をつけるとQualifersを満たすものを除くという条件になる。
`AND`, `NOT`, `OR`が使える。

Qualifiersの一覧は以下。

* `author`
* `comitter`
* `author-name`
* `commiter-name`
* `author-email`
* `committer-email`
* `user`
* `repo`
    * `repo:name/repo_name`
* `author-date`
    * `author-date:<2016-01-01`
* `committer-date`
    * `committer-date:<2016-01-01`
* `merge`
    * `merge:true`
    * merge commitを含める
* `hash`
    * sha1 hashを指定
* `parent`
    * parentのsha1 hashを指定
* `tree`
    * treeのsha1 hashを指定
* `is`
    * repositoryのprivateかprivate
    * `is:public`
    * `is:private`
* `feature`
* `hoge in:`
    * `in:file`
        * fileの中身にhogeを含む
    * `in:path`
        * path文字列にhogeを含むcode
    * `in:file,path`
        * fileかcode
* `hoge language:scss`
    * 言語の指定
* `size`
    * `size:100`
        * sizeが100bytes
    * `size:>100`
        * sizeが100bytes以上
* `fork`
    * `fork:true`
        * forkされたrepositoryも検索に含める
* `filename`
    * `filename:.vimrc`
        * ファイル名が`.vimrc`を含む
* `extension`
    * `extension:css`
    * 拡張子を指定
* `stars`
    * starの数
* `created`
    * `created:"2012-04-30 .. 2012-07-04"`
    * 作成された日付

## Tips

### mirroring git repository
* [Duplicating a repository \- User Documentation](https://help.github.com/articles/duplicating-a-repository/)
* [Keep in sync your Git repos on GitHub, GitLab & Bitbucket](https://moox.io/blog/keep-in-sync-git-repos-on-github-gitlab-bitbucket/)
* [mirroring \- Creating an official github mirror \- Stack Overflow](https://stackoverflow.com/questions/11370239/creating-an-official-github-mirror)

Create mirror repository without fork.

* `git://want/to/mirror/repository.git`
    * this can be a GitHub repository
* `https://github.com/exampleuser/new-repository.git`
    * the repository where you will mirror repository

```
git clone --bare git://want/to/mirror/repository.git
cd repository.git
git push --mirror https://github.com/exampleuser/new-repository.git
cd ..
rm -rf repository.git
```

### Requesting organization approval
* [Requesting organization approval for OAuth Apps - User Documentation](https://help.github.com/articles/requesting-organization-approval-for-oauth-apps/)

後から、参加したorganizationにAppsの承認を出す場合は、自分の`Authorized OAuth Apps`から該当のAppsをclickしてrequestボタンを押す。
そうすると、organizationのownerに承認要求のメールがいく。
organiationのSettingsからThird-party accessのタブに移動し、該当のAppの承認をする。
承認されれば、該当のAppsから要求に応じた承認される。
OrganizationからAPpsの承認がないと、個別のrepositoryへのadmin権限があってもそのrepositoryは見ることができない。
以下の2つが導入に必須と考えて良い。

* OrgazanitonからのAppsの承認
* repositoryへのadmin権限

### Organization
* memberのorganizationのrepositoryのアクセスは、organizationのdefaultができようされる。
* 個別にrepositoryのアクセス権限をかえたい場合は、各repositoryのcollaboratorsとして、teamか個人を追加してもらう

### default labels
* [GitHubがデフォルトで用意しているIssueラベルの意味 - Qiita](http://qiita.com/maeda_t/items/4344bdeabcc6a18a34cc)
* [About labels \- User Documentation](https://help.github.com/articles/about-labels/)

| ラベル      | 意味                                                           |
|-------------|----------------------------------------------------------------|
| help wanted | 助けを求める場合                                               |
| bug         | バグの場合                                                     |
| duplicate   | すでに内容の重複したIssueが存在する場合                        |
| enhancement | 機能強化の場合                                                 |
| invalid     | 間違い、勘違い、実現不可の場合。対応しない内容を書いてクローズ |
| question    | 疑問がある場合                                                 |
| wontfix     | 対応しないバグ等がある場合。対応しない理由を書いてクローズ     |

### Templates
IssueとPull Requestのtemplateを作ることができる。
templateは`.github/`の下か`docs/`の下におく。


* [GitHub Issue and Pull Request Templates Generator](https://www.talater.com/open-source-templates/#/page/1)
    * issueとPRのtemplateのgenerator
    * 童話風のストーリの質問に回答していくとissueないしPRのtemplateを得ることができる
    * Chapter1で最初に、Issueのtemplateを作るか、PRのtemplateを作るかを選択できる
* [devspace/awesome-github-templates: Curated list of GitHub Issues and Pull Requests templates](https://github.com/devspace/awesome-github-templates)
* [stevemao/github-issue-templates: A collection of GitHub issue and pull request templates](https://github.com/stevemao/github-issue-templates)

* `PULL_REQUEST_TEMPLATE.md`
* `ISSUE_TEMPLATE.md`
* `CONTIRUBUTING.md`
* `SUPPORT.md`
    * [SUPPORT file support](https://github.com/blog/2400-support-file-support)

### keywords
* [Manage issues and pull requests with keyword updates](https://github.com/blog/2398-manage-issues-and-pull-requests-with-keyword-updates)

IssueやPRのkeywordとして使えるもの。

* close/fix/resolve
    * `close #issuenum`で`#issuenum`の課題をclose
* duplicate
    * `duplicate of #issuenum`で`#issuenum`のduplicateとしている課題とする

### Best practice for labeling
* [How We Organize GitHub Issues - A Styleguide For Tagging](https://robinpowered.com/blog/best-practice-system-for-organizing-and-tagging-github-issues/)
* [GitHub labels for better workflows • Yoast](https://yoast.com/dev-blog/github-labels/)
* [Sane GitHub Labels – Dave Lunny – Medium](https://medium.com/@dave_lunny/sane-github-labels-c5d2e6004b63)
    * Status
        * In progress
        * Pending
        * Blocked
        * Completed
        * On Hold
    * Type
        * Bug
        * Enhancement
        * Maitenance
        * Question
    * Priority
        * Critical
        * High
        * Low
        * Medium

### ipython
GitHubでjupyter-notbook形式のfileを表示可能。
Localで表示を確認するには、以下のcommandでhtmlに変換する。

```
jupyter nbconvert --to html NOTEBOOK-NAME.ipynb
```

## ssh keys
以下のURLで公開鍵が取得できる。

```
https://github.com/<user-name>.keys
```

## Code Review
* [Best Practices for Code Review | Learn Code Review](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)
* [コードレビューのベストプラクティス【和訳】 - Qiita](https://qiita.com/terra_yucco/items/d101a57566a5e9b3a076)
* [About pull request reviews - User Documentation](https://help.github.com/articles/about-pull-request-reviews/)
* [guides/code-review at master · thoughtbot/guides](https://github.com/thoughtbot/guides/tree/master/code-review)
* [andela/code-review-guidelines: Code Review Guidelines for Andela](https://github.com/andela/code-review-guidelines)
* [How to write the perfect pull request | The GitHub Blog](https://blog.github.com/2015-01-21-how-to-write-the-perfect-pull-request/)
* [GitHub「完璧なプルリクの書き方を教えるぜ」 - Qiita](https://qiita.com/umanoda/items/93aec41213f8e3ce14c8)

## Release
* When you create a release
    * it will add automatically source codes as zip and tar.gz files as release assets.
    * it will add git-tag to the refered commit/branch.

You can create git tag first.
After creating the tag, you can create release to existing tags.

### Delete release
git tag is treated as relase in github.

```
# delete git tag
git push orign :tag-name
```

Then you can delete release in GitHub.

### Reference
* [Searching GitHub - User Documentation](https://help.github.com/articles/searching-github/)
