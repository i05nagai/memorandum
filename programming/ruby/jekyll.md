---
title: jekyll
---

## jekyll
Jekyll（ジキル）は静的サイトの生成を行うための、RubyGemsで配布されているRuby製のツール。

## Install

```
gem install jekyll
```

### Requirements
* Ruby
* RubyGems
* Linux, Unix または Mac OS X
* NodeJSか、あるいは別のJavaScriptランタイム(CoffeeScriptをサポートするため)

## Basic Usage

```
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

```
gem install bundler
```

rootで下記を実行し`Gemfile`を作成する。

```
bundle init
```

`Gemfile`に以下を追加する。

```gem
gem "minima"
```

## Plugins
* [Plugins \| Jekyll • Simple, blog\-aware, static sites](https://jekyllrb.com/docs/plugins/)

You have 3 options for installing plugins:

* `/_plugins` directory
* `_config.yml`
    * Then install your plugins using `gem install` command


## Configuration

## Tips

### Invalid date
* [Troubleshooting | jekyll](https://jekyllrb.com/docs/troubleshooting/#configuration-problems)

```
            ERROR: YOUR SITE COULD NOT BE BUILT:
                    ------------------------------------
                    Invalid date '<%= Time.now.strftime('%Y-%m-%d %H:%M:%S %z') %>': Document 'vendor/bundler/ruby/2.3.0/gems/jekyll-3.4.5/lib/site_template/_posts/0000-00-00-welcome-to-jekyll.markdown.erb' does not have a valid date in the YAML front matter.
```

`_config.yml`に以下を追加する。

```
exclude: [vendor]
```

### Generating sitemap
* [GitHub - jekyll/jekyll-sitemap: Jekyll plugin to silently generate a sitemaps.org compliant sitemap for your Jekyll site](https://github.com/jekyll/jekyll-sitemap)
* [jekyllでサイトマップ(sitemap.xml)を生成する -- ぺけみさお](https://www.xmisao.com/2014/08/25/generate-sitemap-in-jekyll.html)


### Table of Contetns
* [dafi/jekyll-toc-generator: Liquid filter to generate Table of Content into Jeklyll pages](https://github.com/dafi/jekyll-toc-generator)
* [dafi/tocmd-generator: Table of Contents Generator for Markdown pages](https://github.com/dafi/tocmd-generator)

## Reference
* [30分のチュートリアルでJekyllを理解する](http://melborne.github.io/2012/05/13/first-step-of-jekyll/)
* [Jekyll • シンプルで、ブログのような、静的サイト](https://jekyllrb-ja.github.io/)
* [Jekyllで作るシンプルWebサイト - Jekyllとはなにか | CodeGrid](https://app.codegrid.net/entry/jekyll-introduction)
* [mattn/mattn.github.io: mattn.github.io](https://github.com/mattn/mattn.github.io)
* [Extras - Jekyll • Simple, blog-aware, static sites](https://jekyllrb.com/docs/extras/)
