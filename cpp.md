# C++

## 環境変数
### g++
下記の環境変数のパスのheader fileを探す。
```shell
CPATH
C_INCLUDE_PATH
CPLUS_INCLUDE_PATH
OBJC_INCLUDE_PATH
```

下記の環境変数のパスのlibファイルを探す。
```shell
LD_LIBRARY_PATH
```

### clang
下記の環境変数のパスのheader fileを探す。
```shell
CPATH
C_INCLUDE_PATH
CPLUS_INCLUDE_PATH
OBJC_INCLUDE_PATH
```


```shell
LIBRARY_PATH
```

## pyclewn
debugger

http://pyclewn.sourceforge.net/

## template

### templateクラスの型推論
```cpp
template <typename E>
class test {

};

template <typename E>
class base {

};

class derived : public base <derived> {

};

template <typename E>
struct traits {
    static void apply() {
        std::cout << "traits<E>" << std::endl;
    }
};

template <typename E>
struct traits<test<E> > {
    static void apply() {
        std::cout << "traits<test<E> >" << std::endl;
    }
};

template <typename E>
struct traits<base<E> > {
    static void apply() {
        std::cout << "traits<base<E> >" << std::endl;
    }
};

int main(int argc, char const* argv[])
{
    traits<double>::apply();
    traits<test<double> >::apply();
    traits<test<base<test<double> > > >::apply();
    traits<base<derived> >::apply();
    traits<derived>::apply();
    traits<test< base<derived> > >::apply();
    traits<base<test<double> > >::apply();
    /*
    output here
    traits<E>
    traits<test<E> >
    traits<test<E> >
    traits<base<E> >
    traits<E>
    traits<test<E> >
    traits<base<E> >
    */
    return 0;
}
```
型推論時に型の継承関係は考慮されない。
```cpp
template <typename E>
class base {

};

class derived : public base <derived> {

};

template <typename E>
struct traits {
    static void apply() {
        std::cout << "traits<E>" << std::endl;
    }
};

template <typename E>
struct traits<base<E> > {
    static void apply() {
        std::cout << "traits<base<E> >" << std::endl;
    }
};

int main(int argc, char const* argv[])
{
    traits<derived>::apply();
    /*
    output here
    traits<E>
    */
    return 0;
}

```


## typedef
### 配列のtypedef

```cpp
//int[2]のtypedef
typedef int type[2];
```
### typedefのprivate, public

```cpp
class A {
private:
    typedef int private_type;
public:
    typedef int public_type;
};

void main() {
    //A::private_type hoge; //error
    A::public_type hoge;
}
```

### typedefの継承
```cpp
class base {
public:
    typedef int type1[1];
    typedef int type2[1];
public:
    static int apply1()
    {
        return sizeof(type1);
    }
    static int apply2()
    {
        return sizeof(type2);
    }
};

class derived {
public:
    typedef int type2[2];
public:
    static int apply1()
    {
        return sizeof(type1);
    }
    static int apply2()
    {
        return sizeof(type2);
    }
};

void main()
{
    std::cout << base::apply1() << std::endl; //4
    std::cout << derived::apply1() << std::endl; //8
    std::cout << base::apply2() << std::endl; //4
    std::cout << derived::apply2() << std::endl; //4
}

```


## tips
### case1: CRTPのインスタンス化の順序
CRTPでtypedefするときの注意。
下記はderivedのtypedefされる前にbaseのtypedefが評価されるが、このときderivedのtypedefは評価されていないのでエラー。
```cpp
template <typename T>
struct base {
    typedef typename T::value_type value_type;
    static const T& operator()()
    {
        return static_cast<const T&>(*this);
    }
};

struct derived : base<derived> {
    typedef double value_type;
};
```


## c++コンパイラの仕組み

1. プリプロセッサが`main.cpp`を解析し、includeやマクロを展開する。
```shell
cpp -E main.cpp -o main.ii
```
2. コンパイラが展開されたソースファイルを解析し、アセンブリコードに変換
```shell
cc1plus -S main.cpp -o main.s
```
3. アセンブラがアセンブリコードからオブジェクトファイルを生成
```shell
as -c main.s -o main.o
```
4. リンカがオブジェクトファイルをまとめて実行ファイルを生成
    * `ld`はオブジェクトファイルとアーカイブ`.a`を静的にリンクする。
```shell
ld main.o 
```


### オブジェクトファイルの中身を見る
objdumpコマンドを使う。
* `-r`
    * リロケーション情報
* `-R`
    * 動的リロケーション情報
* `-x`
    * オブジェクトファイル内のヘッダーの全情報
* `-t`
    * オブジェクトファイル内のヘッダーのSYMBOL情報
* `-T`
    * オブジェクトファイル内のヘッダーのDynamicSYMBOL情報

## pre_compiled_header
### gcc
下記で`pre_compiled_header.h`から`pre_compiled_header.h.pch`が生成される。
```shell
g++ -I/path/to/hearder pre_compiled_header.h
```

`pre_compiled_header.H`の中身は下記の通り。
```cpp
#pragma once
#include <boost/shared_ptr.hpp>
```

### clang
下記で`pre_compiled_header.h`から`pre_compiled_header.h.pch`が生成される。
```shell
clang++ -cc1 -emit-pch -o pre_compiled_header.h.gch pre_compiled_header.h
```

```shell
clang++ -include-pch pre_compiled_header.h.gch source.cpp
```

## clang

### c++11
下記を指定

```shell
clang++ -std=c++11 -stdlib=libc++ main.cpp
```

### mac
macでのclangのupdateはxcodeからupdateする。

[](http://minus9d.hatenablog.com/entries/2013/08/06)

### error
* `-fcxx-exceptions`
```shell
error: C++ exceptions was disabled in PCH file but is currently enabled
```
* `-fexceptions`
```shell
error: exception handling was disabled in PCH file but is currently enabled
```
* `-x c++`
* `-x c++-headers`
* `-fblocks`
```shell
error: blocks extension to C was disabled in PCH file but is currently enable
```
* `-fmax-type-align=16`
    * 数字は？
```
error: default maximum alignment for types differs in PCH file vs. current file
```
*
```shell

```


## 参考
* [isocpp](https://isocpp.org/)
* [msgpack/msgpack-c: MessagePack implementation for C and C++ / msgpack.org](https://github.com/msgpack/msgpack-c)



