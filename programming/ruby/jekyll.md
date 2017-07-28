## jekyll
Jekyll（ジキル）は静的サイトの生成を行うための、RubyGemsで配布されているRuby製のツール。

## Install

```shell
gem install jekyll
```

### Requirements
* Ruby
* RubyGems
* Linux, Unix または Mac OS X
* NodeJSか、あるいは別のJavaScriptランタイム(CoffeeScriptをサポートするため)

## Basic Usage

```shell
$ jekyll build
# => カレントフォルダが ./_site の下に生成されます

$ jekyll build --destination <destination>
# => カレントフォルダが <destination> の下に生成されます

$ jekyll build --source <source> --destination <destination>
# => <source> フォルダが <destination> の下に生成されます

$ jekyll build --watch
# => カレントフォルダが ./_site の下に生成されます
#    変更を監視し、自動的に再生成を行います
```

## Directory Structure

```
.
├── _config.yml
├── _drafts
|   ├── begin-with-the-crazy-ideas.textile
|   └── on-simplicity-in-technology.markdown
├── _includes
|   ├── footer.html
|   └── header.html
├── _layouts
|   ├── default.html
|   └── post.html
├── _posts
|   ├── 2007-10-29-why-every-programmer-should-play-nethack.textile
|   └── 2009-04-26-barcamp-boston-4-roundup.textile
├── _data
|   └── members.yml
├── _site
└── index.html
```

* `_layouts/default.html`
* `_layouts/post.html`

### syntax hight

jekyll3.0からは`rouge`がデフォルト

## Theme
Bundlerを使う。
Bundlerが入っていない場合は、インストールする。
```shell
gem install bundler
```

rootで下記を実行し`Gemfile`を作成する。

```shell
bundle init
```

`Gemfile`に以下を追加する。

```gem
gem "minima"
```

## Github.io連携
Github pagesではgemは利用できない。
gemを利用したい場合は、ローカルで生成してpushするしか今のところない。


### Table of Contetns

* [dafi/jekyll-toc-generator: Liquid filter to generate Table of Content into Jeklyll pages](https://github.com/dafi/jekyll-toc-generator)
* [dafi/tocmd-generator: Table of Contents Generator for Markdown pages](https://github.com/dafi/tocmd-generator)

### Github向け導入
必要なもの
* `_layouts/math.html`
* `_layouts/default.html`
* `index.html`

### config
Githubがdefaultで設定する項目。
`_config.yml`で上書き可能。
```yml
github: [metadata]
kramdown:
  input: GFM
  hard_wrap: false
gems:
  - jekyll-coffeescript
  - jekyll-paginate
```

上書きできない項目は以下。
```yml
lsi: false
safe: true
source: [your repo's top level directory]
incremental: false
highlighter: rouge
gist:
  noscript: false
kramdown:
  math_engine: mathjax
```

Githubが設定するメタデータは下記にまとまっている。
[Repository metadata on GitHub Pages - User Documentation](https://help.github.com/articles/repository-metadata-on-github-pages/)


### markdonw
Githubのmarkdownのパーサーは`kramdown`
`kramdown`

### theme
Githubがsupportしているthemaは今の所下記のみ
* [Supported themes - GitHub Pages](https://pages.github.com/themes/)

### Relateive URL
github.ioで、rootのURLは`http://user_name.github.io/repository_name`となっている。
この状態で、`<a href="/js/main.js">`とすると`http://user_name.github.io/js/main.js`と解釈される。
解決策としては、 `_config.yml`に`site.baseurl`を設定し、`<a href="{{ site.baseurl }}/js/main.js">`とする。

```yml
baseurl: /repository_name
```

github上でURLが`/repository_name/js/main.js`と解釈される。
また、ローカルでも`jekyll s`とすると、URLが`http://127.0.0.1:4000/repository_name/`で立ち上がる為整合的となる。

#### reference
* [baseurl / base-url: GitHub Pages Project Pages - Relative Links Fail · Issue #332 · jekyll/jekyll](https://github.com/jekyll/jekyll/issues/332)
* [Using Jekyll as a static site generator with GitHub Pages - User Documentation](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)

## Tips

### GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data
jekyll用にGithubのpersonal access tokenを設定する必要がある。

1. GitHubの`Settings`->`personal access token` -> `Generate new token`
2. `public_repo`にcheckをいれてtokenを作成
3. 作成したtokenを`export JEKYLL_GITHUB_TOKEN=<token>`で環境変数に設定する。

### Github Pagesで使えるMetadata一覧

* [Repository metadata on GitHub Pages - User Documentation](https://help.github.com/articles/repository-metadata-on-github-pages/)

### Invalid date

```
            ERROR: YOUR SITE COULD NOT BE BUILT:
                    ------------------------------------
                    Invalid date '<%= Time.now.strftime('%Y-%m-%d %H:%M:%S %z') %>': Document 'vendor/bundler/ruby/2.3.0/gems/jekyll-3.4.5/lib/site_template/_posts/0000-00-00-welcome-to-jekyll.markdown.erb' does not have a valid date in the YAML front matter.
```

`_config.yml`に以下を追加する。

```
exclude: [vendor]
```

* [Troubleshooting | jekyll](https://jekyllrb.com/docs/troubleshooting/#configuration-problems)

## Reference
* [30分のチュートリアルでJekyllを理解する](http://melborne.github.io/2012/05/13/first-step-of-jekyll/)
* [Jekyll • シンプルで、ブログのような、静的サイト](https://jekyllrb-ja.github.io/)
* [Jekyllで作るシンプルWebサイト - Jekyllとはなにか | CodeGrid](https://app.codegrid.net/entry/jekyll-introduction)
* [mattn/mattn.github.io: mattn.github.io](https://github.com/mattn/mattn.github.io)
* [Extras - Jekyll • Simple, blog-aware, static sites](https://jekyllrb.com/docs/extras/)
