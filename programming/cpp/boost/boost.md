# boost

## インストール
### github
```shell
git clone https://github.com/boostorg/boost
git submodule init
git submodule update
```

## ublas
### matrix
```cpp
ublas::matrix<double> m(size1, size2);
size1 == m.size1();
size2 == m.size2();

```

## multi_array

```cpp
#include <boost/multi_array.hpp>

//def
boost::multi_array<double, 3> hoge(boost::extents[stateSize][gridSize][simulationSize]);

for ( int i = 0 ; i < hoge.shape()[0] ; ++i ) {
    for ( int j = 0 ; j < hoge.shape()[1] ; ++j ) {
        for ( int k = 0 ; k < hoge.shape()[2] ; ++k ) {
            hoge[i][j][k] = i + j + k;
        }
    }
}

```

### 

## ublas
### dependecies
* `boost/config`
* `boost/serialization`
* `boost/mpl`
* `boost/type_traits`
* `boost/static_assert`
  * `https://github.com/boostorg/static_assert.git`
* `boost/operators.hpp`
  * `https://github.com/boostorg/utility.git`
* `boost/array`
  * `https://github.com/boostorg/array.git`
* `boost/assert`
  * `https://github.com/boostorg/assert.git`
* `boost/core`
  * `https://github.com/boostorg/core.git`
  * `swap.hpp`
* `boost/throw_exception`
  * `https://github.com/boostorg/throw_exception.git`
* `boost/typeof`
  * `https://github.com/boostorg/typeof.git`

## 

boostのwindowsのpre build version
[boost binaries](https://sourceforge.net/projects/boost/files/boost-binaries/)

* Fusion
  * tuple

* Phoenix


boostの半分くらいのライブラリはmaitainer不在。

boostのMacro一覧

boost.Buildにcompile fail用のテストがある。

[c++11_boost_mapping](https://github.com/boostjp/site/blob/master/tips/cxx11-boost-mapping.md)

PUb/subモデル。
* publisher
* subscriber
* messages pack

##
static_asssertの出力メッセージは
引数のうむに関係なく。
* lambdaで*thisをcaputure
  * オブジェクトのコピー
* class templateのtemplate引数の推論
* 式の評価順序が規定
* RVOの保証
* `if contexpr`
* 構造化束縛
  * 多重代入
  * `auto`必須
* ifとswitchに初期化文追加
* variant<int, string>
  * 共用体
* タプル展開apply
* 定レイヤの文字列変換・数値変換
    * char*からの変換
* 非推奨
  * 標準関数オブジェクトのメンバ型の削除
  * `result_type`
  * `argument_type`

* constexpr lambda

## 属性
[[nodiscard]];
[[fallthrough]];
[[maybe_unused]]

### link


