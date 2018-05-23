---
title: Bash
---

## Bash

## Tips

### /etc/profile /etc/profile.d
* [bash - What do the scripts in /etc/profile.d do? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/64258/what-do-the-scripts-in-etc-profile-d-do)
* [bash - Scripts in /etc/profile.d Being Ignored? - Ask Ubuntu](https://askubuntu.com/questions/438150/scripts-in-etc-profile-d-being-ignored)

login shellとして起動されるか、interactive shellかどうかなどで読み込まれるかどうかがかわる。


* /etc/profile
    * Bash shellの開始時に 環境変数をset
* /etc/profile.d
    * bash shellの開始時に読み込まれる
    * application固有のenvironment variableをset

## Shell Parameter Expansion
* [【シェル芸人への道】Bashの変数展開と真摯に向き合う - Qiita](https://qiita.com/t_nakayama0714/items/80b4c94de43643f4be51)


## Precedence
* [bash - Precedence of the shell logical operators &&, || - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/88850/precedence-of-the-shell-logical-operators)

* &&, ||
    * same precedence
    * left associative

## Bash variablaes
* [Bash Reference Manual: Bash Variables](https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html)


* BASH_SOURCE
    * array
    * source filename `${FUNCNAME[$i]}`
    * corresponding shell function name in FUNCNAME array
    * `${FUNCNAME[$i]}` is defined in `${BASH_SOURCE[$i]}`
    * `${FUNCNAME[$i]}` is called from `${BASH_SOURCE[$i+1]}`
    * `$0`は`source`で変更されないが、`BASH_SOURCE`はsourceされるとsource先が0番目にpushされる

## Conditoinal expressions

* `[[ expression ]]`
    * `=`, `==` は同じいみ
    * `==`, `!=`
        * 右辺を [Pattern-maching](https://tiswww.case.edu/php/chet/bash/bashref.html#Pattern-Matching)として評価
    * `=~`を含むかどうか
        * 右辺をregex3で評価

## Reference
