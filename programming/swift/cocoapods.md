---
title: Cocoapods
---

## Cocoapods

```
bundle init
```

```ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

gem "cocoapods"
```

```
bundle install --path=vendor/bundle
```

```
bundle exec pod init
```

`Podfile`ができるので、編集する。

```
project 'path/to/XcodeProject.xcodeproj'
```

## CLI

* `pod init`
* `pod install`
* `pod list`

## Tips
以下のErrorがでたら、`pod repo update`

```
Unable to find a specification for `SwiftLint`
```

## Reference

