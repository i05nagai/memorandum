---
title: gcc
---

## gcc

## CLI

```
```


## Compiler options
[Using the GNU Compiler Collection \(GCC\): Warning Options](https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html)

* `-w`
* `-Wextra`
    * `-Wmissing-field-initializer`を含む
* `-Werror`
    * make all warnings into error
* `-Werror=`
    * make the specified warning into error
* `-Wall`
* `-Waddress`
    * Warn about suspicious uses of memory addresses.



## Tips

### Path to stdlib
* [c\+\+ \- What are the GCC default include directories? \- Stack Overflow](https://stackoverflow.com/questions/4980819/what-are-the-gcc-default-include-directories)

```
gcc -xc++ -E -v -
```

* `/usr/lib/x86_64-linux-gnu`
* `/usr/include/c++`


## gcc-4.6
* friend宣言はclassキーワードがいる
```
frined class HogeClass;//OK
frined HogeClass;//NO
```

## C++11 Suport in GCC
* [C++ Standards Support in GCC - GNU Project - Free Software Foundation (FSF)](https://gcc.gnu.org/projects/cxx-status.html#cxx11)

### GCC4.6
* [Status of Experimental C++0x Support in GCC 4.6 - GNU Project - Free Software Foundation (FSF)](https://gcc.gnu.org/gcc-4.6/cxx0x_status.html)

compiler optionは`-std=c++0x` or `-std=gnu++0x`

### GCC4.8
* [Status of Experimental C++11 Support in GCC 4.8 - GNU Project - Free Software Foundation (FSF)](https://gcc.gnu.org/gcc-4.8/cxx0x_status.html)

compiler optionは`-std=c++11` or `-std=c++11`


## Reference
* [C言語の構造体の初期化 sturct hoge\_t hoge = \{0\} 部分で 初期化子を欠いています\(missing initializer\) の警告が出る件 \- shouhの日記](http://d.hatena.ne.jp/shouh/20140510/1399680764)
