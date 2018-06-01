---
title: Jekyll GitHub io
---

## Jekyll GitHub io
Github.io

### markdonw
Githubのmarkdownのパーサーは`kramdown`
`kramdown`


### Relateive URL
github.ioで、rootのURLは`http://user_name.github.io/repository_name`となっている。
この状態で、`<a href="/js/main.js">`とすると`http://user_name.github.io/js/main.js`と解釈される。
解決策としては、 `_config.yml`に`site.baseurl`を設定し、`<a href="{{ site.baseurl }}/js/main.js">`とする。

```yaml
baseurl: /repository_name
```

github上でURLが`/repository_name/js/main.js`と解釈される。
また、ローカルでも`jekyll s`とすると、URLが`http://127.0.0.1:4000/repository_name/`で立ち上がる為整合的となる。

### theme
Githubがsupportしているthemaは今の所下記のみ
* [Supported themes - GitHub Pages](https://pages.github.com/themes/)

### GitHub Metadata: No GitHub API authentication could be found. Some fields may be missing or have incorrect data
jekyll用にGithubのpersonal access tokenを設定する必要がある。

1. GitHubの`Settings`->`personal access token` -> `Generate new token`
2. `public_repo`にcheckをいれてtokenを作成
3. 作成したtokenを`export JEKYLL_GITHUB_TOKEN=<token>`で環境変数に設定する。

### Github Pagesで使えるMetadata一覧
* [Repository metadata on GitHub Pages - User Documentation](https://help.github.com/articles/repository-metadata-on-github-pages/)


### Github
必要なもの

* `_layouts/math.html`
* `_layouts/default.html`
* `index.html`

## Configuration
* [Repository metadata on GitHub Pages - User Documentation](https://help.github.com/articles/repository-metadata-on-github-pages/)
    * Githubが設定するmetadata
    * Githubがdefaultで設定する項目
    * `_config.yml`で上書き可能

```yaml
github: [metadata]
kramdown:
  input: GFM
  hard_wrap: false
gems:
  - jekyll-coffeescript
  - jekyll-paginate
```

上書きできない項目は以下。

```yaml
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

## Reference
* [baseurl / base-url: GitHub Pages Project Pages - Relative Links Fail · Issue #332 · jekyll/jekyll](https://github.com/jekyll/jekyll/issues/332)
* [Using Jekyll as a static site generator with GitHub Pages - User Documentation](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)
