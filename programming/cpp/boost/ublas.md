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

## vector

```cpp
A a; //A is ublas::vector
B b; //B is ublas::vector
a + b; //return type is vector_binary<A, B, scalar_plus<A, B>>
a - b; //return type is vector_binary<B, B, scalar_minus<A, B>>
(a + b)(0); //return type is scalar_plus<A, B>::result_type

//scalar_plus<A, B>::result_type is vector_binary<A, B, scalar_plus<A, B>>::value_type
//vector_binary<A, B, scalar_plus<A, B>>::value_type is vector_binary<A, B, scalar_plus<A, B>>::const_reference
//vector_binary<A, B, scalar_plus<A, B>>::const_reference is vector_binary<A, B, scalar_plus<A, B>>::reference
// type_deduction_detail::base_result_of<X, Y> promote_traits<X, Y>::base_type;
//remove_cv<X>::type x_type
//remove_cv<Y>::type y_type
```

