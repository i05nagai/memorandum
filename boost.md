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
