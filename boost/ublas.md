# ublas

## detail

### `vector_assign`
`detail::expression_type_check`は2つの`vector_expression`型の比較を行う。
`double`値などの場合も各要素を`norm_inf`で比較するので、正しく動く。

```cpp
#include <boost/numeric/ublas/detail/vector_assign.hpp>
bool isSame = ublas::detail::expression_type_check(m1, m2);
```

### `matrix_assign`
`detail::expression_type_check`は2つの`matrix_expression`型の比較を行う。
`double`値などの場合も各要素を`norm_inf`で比較するので、正しく動く。

```cpp
#include <boost/numeric/ublas/detail/matrix_assign.hpp>
bool isSame = ublas::detail::expression_type_check(m1, m2);
```

## matrix
### iterator
コメント部分が出力。
行列の一行目と一列目のiterator
```cpp
    namespace ublas = boost::numeric::ublas;
    ublas::matrix<double> m(3, 3);
    m(0, 0) = 0.0; m(0, 1) = 1.0; m(0, 2) = 2.0;
    m(1, 0) = 3.0; m(1, 1) = 4.0; m(1, 2) = 5.0;
    m(2, 0) = 6.0; m(2, 1) = 7.0; m(2, 2) = 8.0;

    for (auto e = m.begin1(); e != m.end1(); ++e) {
        std::cout << *e << std::endl;
    }
    //0
    //3
    //6
    
    for (auto e = m.begin2(); e != m.end2(); ++e) {
        std::cout << *e << std::endl;
    }
    //0
    //1
    //2
    
    for (auto e = m.rbegin1(); e != m.rend1(); ++e) {
        std::cout << *e << std::endl;
    }
    //6
    //3
    //0

    for (auto e = m.rbegin2(); e != m.rend2(); ++e) {
        std::cout << *e << std::endl;
    }
    //2
    //1
    //0
```
