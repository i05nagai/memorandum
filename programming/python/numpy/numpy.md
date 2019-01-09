---
title: numpy
---

## numpy

## tensor

* (3行, 2列)の行列が4つ表示になる

```python
a = np.array(range(0, 24))
a.shape = (4, 3, 2)
print(a)
[[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]

 [[12 13]
  [14 15]
  [16 17]]

 [[18 19]
  [20 21]
  [22 23]]]
```


### contraction
channel方向のcontraction

$$
    b_{h,w}
    =
    \sum_{c=0}^{2}
        a_{h,w}^{c}
        b_{c}
$$

tensordotを使う。

```python
import numpy as np
a = np.array(range(0, 24))
a.shape = (4, 3, 2)
b = np.array(range(0, 2))
b.shape = (2)
np.tensordot(a, b, 1)
```


## function
* `vstack(tup)`
    * 配列を行に連結
* `hstack(tup)`
    * 配列を列方向に連結
* `logical_xor`
    * 2つの配列の要素ごとの排他的論理和をとる
* `newaxis`
    * 配列に新しい次元を挿入したいときに利用。
    * `[:, np.newaxis]`で1次元配列が2次元配列になる
* `np.squeeze(x, axis=0)`
    * axisで指定した次元を減らす
* `np.expand_dims(x, axis=0)`

* `tensordot`
    [numpy\.tensordot — NumPy v1\.14 Manual](https://docs.scipy.org/doc//numpy/reference/generated/numpy.tensordot.html)


```python
a = np.ones((2, 3, 4))
b = np.ones((4, 5, 6))
c = np.ones((3, 4, 5))

np.tensordot(a, b, axes=0).shape
# (2, 3, 4, 4, 5, 6)

np.tensordot(a, b, axes=1).shape
# (2, 3, 5, 6)
np.tensordot(a, c, axes=1).shape
# error

np.tensordot(a, b, axes=2).shape
# error
np.tensordot(a, c, axes=2).shape
# (2, 5)

np.tensordot(a, b, axes=[2, 0]).shape
np.tensordot(a, b, axes=[[2], [0]]).shape
# sumover a[:, :, ?] * b[?, :, :]
# (2, 3, 5, 6)
np.tensordot(a, c, axes=[2, 0]).shape
np.tensordot(a, c, axes=[[1], [0]]).shape
# (2, 4, 4, 5)
np.tensordot(a, c, axes=[[1, 2], [0, 1]]).shape
# (2, 5)
```

$$
    a = a_{i_{1}, i_{2}, i_{3}}
    b = b_{j_{1}, j_{2}, j_{3}}
    a \times b
    =
    a_{i_{1}, i_{2}, i_{3}}
    b^{j_{1}, j_{2}, j_{3}}
$$

## operators
* 配列に対して、条件比較ができる
    * 要素ごとの条件比較に置きかわる

## vectorize
* [numpy\.vectorize — NumPy v1\.14 Manual](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.vectorize.html#numpy.vectorize)
    * The vectorize function is provided primarily for convenience, not for performance. The implementation is essentially a for loop.

#### Broadcasting
* [Broadcasting — NumPy v1\.15 Manual](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)


## Reference
* [Numpyでデータを生成する色々な方法(arange/linspace/logspace/zeros/ones/mgrid/ogrid) - Qiita](http://qiita.com/supersaiakujin/items/4410efe5dc81982ef208)

