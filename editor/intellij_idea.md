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
* `Cmd+option+LeftArrow`
    * back to previous location
* `Cmd+E`
    * 直近で開いてたfile
    * jump先から戻れる

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
* snippetの追加
    * [Creating and Editing Live Templates](https://www.jetbrains.com/help/idea/2016.3/creating-and-editing-live-templates.html)
    * `$<variable name>$`でvariables

## Add doc comment
* [Creating Documentation Comments - Help | IntelliJ IDEA](https://www.jetbrains.com/help/idea/creating-documentation-comments.html)
    * kotlinでは動かない

1. Place the caret before the declaration.
2. Type the opening block comment `/**`, and press Enter.
3. Add meaningful description of parameters and return values.


### Surrounding word
* [HOW-TO: Surround text with quote in IntelliJ ~ Codeleak.pl](http://blog.codeleak.pl/2014/06/how-to-surround-text-with-quote-in.html)

Editor -> LiveTemplate -> surrounded

でsurrounded用のLive templateがあるので追加する。

### Standard library
* [apply - Kotlin Programming Language](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/apply.html)

```kotlin
inline fun <T> T.apply(block: T.() -> Unit): T (source)
```

## Tests
* [Creating Run/Debug Configuration for Tests - Help | IntelliJ IDEA](https://www.jetbrains.com/help/idea/creating-run-debug-configuration-for-tests.html)
* [Creating Tests - Help | IntelliJ IDEA](https://www.jetbrains.com/help/idea/creating-tests.html)

testを追加するdirectoryをtest directoryとしてmarkできる。
markしたdirectoryはtestの自動生成の際にtestの保存先として指定できる。
Project windowから`右クリック->Mark Directory as->Test Resources Root`でtest directoryになる。

Testの自動追加は、classを選択して、`option + Enter`で`Create test`を選択する。
diaglogに必要な設定を記述した後、OKを押せば、Test fileの保存先が指定できる。

Test classで`Cmd + N`でtest methodの生成ができる。

### Never use wildcard imports
* [settings - IntelliJ: Never use wildcard imports - Stack Overflow](https://stackoverflow.com/questions/3348816/intellij-never-use-wildcard-imports)

Editor -> CodeStyle -> Kotlin -> Package to use codestyle


#### Debugging
- [Debugging Docker with IntelliJ IDEA \| ngeor\.com](https://ngeor.com/2017/03/26/debugging-docker-with-intellij-idea.html)


## Java

#### Gradle
Update dependency. `gradle build` doesn't udpate the dependency.

* Open Gradle Window: `Ctrl+A` + `gradle`
* Right click gradle window and choose `Refresh dependencies`

## Python

#### Change test runner
- `Preference` -> `Tool` -> `Python Integrated Tool`
    - Change `Testing` 


#### Command Shift A opens terminal
- https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003430700--Apropos-terminal-pops-up-when-typing-cmd-shift-A-to-get-actions-bar

- Go to `Keyboard` -> `Shortcut` and find Command Shift A short cut and disbale it.
    - probably in `Services`

## Reference
