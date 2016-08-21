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

