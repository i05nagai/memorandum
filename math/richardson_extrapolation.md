---
title: Richardson Extrapolation
---

## Richardson Extrapolation
誤差評価が分かっている近似手法に対して、収束次数をあげる為の手法。
適用範囲が広く実用上も有益。
ただし、数値計算上は桁落ちなどに注意が必要。

Romberg's methodはRichardson extraplationの積分への応用である。

## Good
* 誤差評価が多項式の形であればよいので、適用範囲が広い
* 実装も簡単

## Bad
* 桁落ちなどに注意する必要がある
* 近似手法を複数回（最低2回)計算する必要があるので、近似計算がボトルネックの場合は非常に遅い

## Definition
* $h$,
    * 近似手法のパラメータ
    * 数値積分や数値微分の区間幅になる
* $A^{*}$,
    * 真値
* $A(h)$,
    * 真値の近似手法
    * Newton法や数値積分、数値微分法など

## Algorithm
$h$を近似手法のパラメータとし、真値$A^{*}$との誤差が以下で表現できるとする。

$$
\begin{eqnarray}
    A(h)
    & = &
        A^{*} 
        + c_{n} h^{n}
        + O(h^{n+1})
    \nonumber
    \\
    & = &
        A^{*} 
        + O(h^{n})
    \nonumber
\end{eqnarray}
$$

ここで、$c_{n} \in \mathbb{R}$は定数である。
このとき、

$$
    A(kh)
    =
    A^{*} 
    + k^{n} c_{n} h^{n}
    + O(h^{n+1})
$$

より、

$$
\begin{eqnarray}
    k^{n} A(h)
    -
    A(kh)
    & = &
        k^{n}
        \left(
            A^{*} 
            + c_{n} h^{n}
            + O(h^{n+1})
        \right)
        -
        A^{*} 
        + k^{n} c_{n} h^{n}
        + O(h^{n+1})
    \nonumber
    \\
    & = &
        (k^{n} - 1)
            A^{*} 
        + O(h^{n+1})
    \nonumber
\end{eqnarray}
$$

となる。
よって、近似手法$\bar{A}(h, k)$を新しく

$$
\begin{eqnarray}
    \bar{A}(h, k)
    & := &
        \frac{
            k^{n} A(h) - A(kh)
        }{
            k^{n} - 1
        }
    \nonumber
    \\
    & = &
        A^{*} + O(h^{n+1})
    \nonumber
\end{eqnarray}
$$

とおけば、$h^{n+1}$で収束する手法となる。

## Example
例を見たほうが理解が早い。


## Reference
* [Richardson extrapolation - Wikipedia](https://en.wikipedia.org/wiki/Richardson_extrapolation)
