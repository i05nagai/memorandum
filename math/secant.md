---
title: Secant Method
---

# Secant method

## Symbol

## Definition

## Problem
$f(x) = 0$を満たす$x \in \mathbb{R}$を見つける問題。

## Algorithm
2点を与える$(x_{0}, f(x_{1}))$, $(x_{1}, f(x_{1}))$とする。

2点の線形補間が$x$軸と交差する点を求める。
つまり、

$$
    f(x_{0}) 
    +
    \frac{
        (f(x_{1}) - f(x_{0}))
    }{
        (x_{1} - x_{0})
    }
        (x - x_{0})
    =
    0
$$

を満たす$x$を求める。
これは簡単に解けて、

$$
    x
    = 
    - f(x_{0})
        \frac{
            (x_{1} - x_{0})
        }{
            (f(x_{1}) - f(x_{0}))
        }
    + x_{0}
$$

となる。
これを$x_{2} := x$とする。
同様に2点$(x_{i}, f(x_{i}))$, $(x_{i+1}, f(x_{i+1}))$について、

$$
    x_{i+2}
    := 
    - f(x_{i})
        \frac{
            (x_{i+1} - x_{i})
        }{
            (f(x_{i+1}) - f(x_{i}))
        }
    + x_{i}
$$

を解く。


## Reference


