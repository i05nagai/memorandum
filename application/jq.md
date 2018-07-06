---
title: jq
---

## jq
`jq`コマンドは、基本的には標準入力からしか受け取らない。

```
echo "{'python': 1}" |  jq '{"hoge": 1}'
```

You need to `'.'` to pipe output of jq.

```
echo "{'python': 1}" |  jq '.' | cat
```

## Install
For OSX,

```
brew install jq
```

For ubuntu16.04,

```
apt-get install jq
```


## Types and Values
* Array construction
* Object Construction
* Recursive Descent 

## Basic Filters
入力されたjsonに対して、filteringできる。

* identity
* Object Identifier-Index: `.foo`, `.foo.bar`
    * jsonのkeyを指定できる。
    * ここの`foo`は、jsonのkey
* Optional Object Identifier-Index: `.foo?`
    * Object Identifer-Indexはkeyがなかったらerrorが起こるが、これはnullがかえる
* Generic Object Index: `.[<string>]`
    * Object Identifer-Indexはこの記法の簡略系
    * keyをstringとして指定する
* Array Index: `.[2]`, `.[2, 4]`
    * jsonの配列に対して、要素を取り出す
* Array/String Slice: `.[10:15]`
    * jsonの配列に対して、区間を指定して要素を取り出す
* Array/Object Value Iterator: `.[]`

## Builtin operators and functions
* Addition
* Subtraction
* Multiplication, division, modulo

* length
* utf8bytelength
* keys, keys_unsorted


## Examples

```
jq '[.[] | {message: .commit.message, name: .commit.committer.name}]'
```

## Reference
* [jq Manual (development version)](https://stedolan.github.io/jq/manual/)

