---
title: Make
---

## Make
makefileは以下の５つで構成される。

* implicit rule
* explicit rule
    * prerequisite に依存関係を記述する
* comment
* variable definition
* directive
    * `include`

## Recipes

Overriding recipes



## Directive

## Automatic variables
* [GNU make: Automatic Variables](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html#Automatic-Variables)

* `$@`
    * RuleのTarget name
* `$%`
    * targetがarchive`.a`の場合のmember
    * `target.a(member1.o,member2.o)`
* `$<`
    * targetの最初のprerequisite
* `$?`
    * space区切りの全てのprerequisiteのlist
* `$^`
    * prerequisiteに同じ名前が複数あっても一度だけ
* `$+`
    * 
* `$|`
* `$*`


## Functions
Call

```make
$(function arguments)
# or
${function arguments}
```

Example

```make
$(subst a,b,${x})
```

* `$(shell )`
* `$(subst from,to,text)`
* `$(patsubst pattern,replacement,text)`
* `$(strip string)`
* `$(findstring find,in)`
* `$(filter pattern…,text)`
* `$(filter-out pattern…,text)`

## For docker
* [mvanholsteijn/docker-makefile: Makefile for building docker repository releases](https://github.com/mvanholsteijn/docker-makefile)
* [A reusable Makefile to build and release Docker images](https://binx.io/blog/2017/10/07/makefile-for-docker-images/)


## Show the commands
* [makefile - How do I force make/gcc to show me the commands? - Stack Overflow](https://stackoverflow.com/questions/5820303/how-do-i-force-make-gcc-to-show-me-the-commands)
* [[Make] make実行時の詳細表示有効化メモ - Qiita](https://qiita.com/koara-local/items/4e047e47b8cde52919a6)

## Double colon
* [Makefiles - Make and the Double colon](http://owen.sj.ca.us/~rk/howto/slides/make/slides/makecolon.html)

```
libxxx.a :: sub1.o
	ar rv libxxx.a sub1.o
libxxx.a :: sub2.o
	ar rv libxxx.a sub2.o
```

### How to get a Makefile directory path
* [How to get a Makefile directory path « timmurphy.org](http://timmurphy.org/2015/09/27/how-to-get-a-makefile-directory-path/)
* [Re: How to get the absolute path of a makefile?](https://lists.gnu.org/archive/html/help-make/2009-05/msg00009.html)


```
$(realpath $(lastword $(MAKEFILE_LIST)))
```

## Reference
* [GNU make: Rules](https://www.gnu.org/software/make/manual/html_node/Rules.html)
* [Makefiles - Best practices and suggestions - Mozilla | MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Build_Instructions/How_Mozilla_s_build_system_works/Makefiles_-_Best_practices_and_suggestions)

