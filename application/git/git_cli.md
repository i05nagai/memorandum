---
title: Git CLI
---

## Git CLI

## CLI

### git commit

* `--fixup <commit>`


### git log

* `-S<string>`
   * Look for differences that change the number of occurrences of the specified string (i.e. addition/deletion) in a file. Intended for the scripter's use.
   * It is useful when you're looking for an exact block of code (like a struct), and want to know the history of that block since it first came into being: use the
   feature iteratively to feed the interesting block in the preimage back into -S, and keep going until you get the very first version of the block.
* `-G<regex>`
   * Look for differences whose patch text contains added/removed lines that match <regex>.
   * To illustrate the difference between -S<regex> --pickaxe-regex and -G<regex>, consider a commit with the following diff in the same file:
   * See the pickaxe entry in gitdiffcore(7) for more information.
   * While git log -G"regexec\(regexp" will show this commit, git log -S"regexec\(regexp" --pickaxe-regex will not (because the number of occurrences of that string did
   not change).

```
       +    return !regexec(regexp, two->ptr, 1, &regmatch, 0);
       ...
       -    hit = !regexec(regexp, mf2.ptr, 1, &regmatch, 0);
```

### git bisect
* [git bisect で問題箇所を特定する - Qiita](http://qiita.com/usamik26/items/cce867b3b139ea5568a6)

```
git bisect start <bad-commit> <good-commit>
git bisect run <test-script>
git bisect view
git bisect log
git bisect reset
```

### git cherry-pick
* [4. cherry-pick【チュートリアル3 コミットを書き換えよう！】 | サルでもわかるGit入門 〜バージョン管理を使いこなそう〜 | どこでもプロジェクト管理バックログ](http://www.backlog.jp/git-guide/stepup/stepup7_4.html)

特定のcommit列をHEADに移したいときに使う。
移行先のbranchに移動する。

```
git checkout master
```

```
git cherry-pick <commit>
```

あるcommitより先のcommitすべてを移行したい場合は
`<commit>`は入らないことに注意。

```
git cherry-pick <commit>...
```

とする。
ある範囲のcommitを入れたい場合は

```
git cherry-pick -n <commit1>^..<commit2>
```

とする。
`<commit1>`から`<commit2`までのcommitがcherry-pickされる。

## git tag
タグの一覧表示

```
git tag
```

特定のpatternのtagを見たい場合は`-l` `--list`をつける。

```
git tag -l 'v1.4.2.*'
```

タグをつける場合は、`-a`でタグの名前をつけて、`-m`でタグのメッセージをつける。

```
git tag -a v1.4 -m 'my version 1.4'
```

タグのついたコミッとを見る。

```
git show v1.4
```

## git stash
git stash applyとgit stash popの違い。

* applyはstashしているものを削除しない
* popもconflictした場合はstashしているものを削除しない
    * その場合はgit stash dropを使う必要がある
* popはapplyしてdropしているのと似ている


## git diff

```
git diff [--options] [--] [<path>...]
```

* indexとの差分を見る
* indexに何が追加されるかを確認する

## git config
* `core.attributesfile = 'path/to/attributes'`
    * pathを指定すると、指定したpathの.gitattributesを参照するようになる。
* `core.excludesfile = 'path/to/gitignore'`
    * pathを指定すると、指定したpathの.gitignoreを参照するようになる。

## Reference
