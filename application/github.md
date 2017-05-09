## GitHub

## GitHub Pages with jekyll

GitHub pagesでjekyllによるサイトの自動生成を使う場合は、`_config.yml`をrepositoryのtopにおく必要がある。
`Settings->GitHub Pages->Theme Chooser`でThemeを一度選択すれば、勝手に生成され、repositoryにコミットされる。
`index.md`がない場合は`README.md`が`index.html`の生成のために利用される。

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

### Reference
* [Managing deploy keys | GitHub Developer Guide](https://developer.github.com/guides/managing-deploy-keys/)

## Error: Permission denied (publickey)

### Should the sudo command be used with Git?
`sudo`はいらない。

### Check that you are connecting to the correct server


## Generating a new SSH key and adding it to the ssh-agent - User Documentation

1. Terminalを開く
2. `ssh-keygen -t rsa -b 4096 -C "your_email@example.com"`
3. 

### Reference
* [Generating a new SSH key and adding it to the ssh-agent - User Documentation](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

## Adding a new SSH key to your GitHub account - User Documentation


### Reference
* [Adding a new SSH key to your GitHub account - User Documentation](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)


### Reference
* [Error: Permission denied (publickey) - User Documentation](https://help.github.com/articles/error-permission-denied-publickey/)

### Reference
* [Travis-CI でコミットして GitHub にプッシュする - 公開鍵認証を利用してみる | そんなこと覚えてない](http://blog.eiel.info/blog/2014/02/18/github-push-from-travis/)

## Search in Github
検索対象にできるのは以下。

* access可能なrepositoryのissue
* Source code
* Commits
* Users
* Wikis

制限は

* 256文字以上のqueryは非サポート
* 5こ以上の`AND`, `OR`, `NOT`

### Qualifiers
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

### Reference
* [Searching GitHub - User Documentation](https://help.github.com/articles/searching-github/)
