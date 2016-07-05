# Travis CI

## .travis.yml
### C++
下記指定でC++としてのbuildとなる。
```yml
language:cpp
```
デフォルトでは、`autotool`想定で書きコマンドが実行される。

```shell
./configure && make && make test
```

compilerの指定は次のようにする。
```cpp
compiler:
	- clang
	- gcc
```
もしくは
```shell
compiler: gcc
```

