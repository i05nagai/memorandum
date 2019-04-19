---
title: clang-format
---

## clang-format
formatter for c++.


## Install

Alpine Linux

* [Alpine packages](https://pkgs.alpinelinux.org/contents?branch=v3.6&name=clang&arch=ppc64le&repo=main)

```
apk add clang
```

OSX

```shell
brew install clnag-format
```

```
npm install -g clang-format
```

```
git clone https://github.com/llvm-mirror/clang.git
cd clang
cmake -G Ninja -DCMAKE_BUILD_TYPE=MinSizeRel -DLLVM_BUILD_STATIC=true .
ninja clang-format
```

For ubuntu 14.04, https://apt.llvm.org/

```
# to install 5.0
apt-add-repository "deb http://apt.llvm.org/trusty/ llvm-toolchain-trusty-5.0 main"
apt search clang-format-5.0
```

## Usage

```
clang-format <filename>
```

* `-i`
    * in-place format
* `-style [<option>]`
    * `google`
    * `llvm`
    * `webkit`
    * `mozilla`
    * ファイル名を指定するとファイルのスタイルの定義に従う

## Style
* [clang-format を イイ感じに設定する - def yasuharu519(self):](http://yasuharu519.hatenablog.com/entry/2015/12/13/210825)

styleのファイルはdefaultでは、`.clang-format`, `_clang-format`の名前のものが利用される。
以下でスタイルのconfigを出力できる。

```
clang-format -style=llvm -dump-config > .clang-format
```

styleのconfigの一覧は以下

* [Clang-Format Style Options — Clang 5 documentation](https://clang.llvm.org/docs/ClangFormatStyleOptions.html)

## vim integration
vimで利用する場合は付属のpythonファイルを利用すると簡単にできる。

```vim
map <C-K> :pyf <path-to-this-file>/clang-format.py<cr>
imap <C-K> <c-o>:pyf <path-to-this-file>/clang-format.py<cr>
```

保存時に自動でformatする場合は、以下の設定をする。

```vim
function! Formatonsave()
  let l:formatdiff = 1
  pyf ~/llvm/tools/clang/tools/clang-format/clang-format.py
endfunction
autocmd BufWritePre *.h,*.cc,*.cpp call Formatonsave()
```

## Reference
* [C や C++ のコードを自動で整形する clang-format を Vim で - はやくプログラムになりたい](http://rhysd.hatenablog.com/entry/2013/08/26/231858)
