---
title: IntelliJ IDEA
---

## IntelliJ IDEA

## Install
For OSX

```
brew cask install intellij-idea
```

* intellij-idea
    Ultimate Edition 有償版/機能制限なし
* intellij-idea-ce
    Community Edition (無償版/機能制限あり)

## Kotlin
* [Getting Started with IntelliJ IDEA - Kotlin Programming Language](https://kotlinlang.org/docs/tutorials/getting-started.html)

## Preference
* load style guide
    * Prereference -> Editor -> Code Style -> Schema (Settings) -> Import Schema

## Shortcut key
* [Mastering IntelliJ IDEA keyboard shortcuts - Help | IntelliJ IDEA](https://www.jetbrains.com/help/idea/mastering-intellij-idea-keyboard-shortcuts.html)

* `Cmd+,`
    * Preference
* `Cmd+Shift+A`
    * commanの検索
* `Cmd+N`
    * find class
* `Cmd+Shift+N`
    * find file
* `option+Shift+N`
* `option+F1`
    * 現在のfileを指定のviewで開く
* `Cmd+F4`
    * close tab
* `Ctlr+arrow`

## Plugins
* [既に最強なIntelliJ IDEAを更にパワーアップさせられる10個のプラグイン - Qiita](https://qiita.com/konohiroaki/items/b9a810702d87a0b6bb53)

* AceJump
    * `Ctrl+;`
        * 入力した文字のある場所に移動できる
* IDEA Jetty Runner
    * Installすると、`Run->Edit Configuration`からDebugできるようになる
* Spek
    * [raniejade/spek-idea-plugin](https://github.com/raniejade/spek-idea-plugin)
    * Run specs directly from IDEA.
    * Choose a specific group/test to run within a spec.
    * 再起動すると、project windowからfileを右clickでfile内のunit testをrunできる
    * Tool barのRunからも同様
    * 各testのdescribeの行にRun mark[▶]が表示される

## Snippets
* [Live templates, code snippets](https://www.jetbrains.com/help/idea/2016.3/live-templates.html)
* path
    * OSX: `~/Library/Preferences/IdeaIC2017.3/templates`




## Tests
* [Creating Run/Debug Configuration for Tests - Help | IntelliJ IDEA](https://www.jetbrains.com/help/idea/creating-run-debug-configuration-for-tests.html)




## Reference
