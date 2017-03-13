---
title: Aitken's Delta-Squared process
---

## Aitken's Delta-Squared process
Aitken's extrapolationともいう。
収束する点列が与えられた時、収束のを改善する方法。
関孝和が作った。

## Good
* もとのアルゴリズムに大きな変更が必要ない

## Bad
* 収束点列の3つを保持する必要がある
* 収束値に近い場合のみ有効
    * 線形に近似できるくらい近い
* 数列ごとにAitken's delta-squared processが有効か確認が必要
* 対数数列のように収束が遅い数列には殆ど効果がない

## Definition
* $$(s_{n})_{n \in \mathbb{N}}$$,
    * $$s_{n} \in \mathbb{R}$$,
    * 収束列
* $g$,
    * $$g(s_{n}) = s_{n+1}$$,
    * 点列生成のアルゴリズム

## Algorithm
$g$を点列生成のアルゴリズムを表す関数とすると、収束点列は$g$の不動点である。
つまり

$$
    g(s) = s
$$

を満たす点は収束点の候補である。
よって、上の方程式満たす点を探せば良い。
そのため、点列の軌跡を線形補間で近似し、$y = x$との交点を求めることを考える。

$$(s_{n}, g(s_{n})) = (s_{n} , s_{n+1})$$, $$(s_{n+1}, g(s_{n+1})) = (s_{n+1}, s_{n+2})$$を通る直線を考えると

$$
\begin{eqnarray}
    & &
    y - g(s_{n+1})
    =
        (x - s_{n+1})
        \frac{
            g(s_{n+1}) - g(s_{n})
        }{
            (s_{n+1} - s_{n})
        }
    \nonumber
    \\
    & \Leftrightarrow &
    y - s_{n+2}
    =
        (x - s_{n+1})
        \frac{
            s_{n+2} - s_{n+1}
        }{
            (s_{n+1} - s_{n})
        }
    \nonumber
\end{eqnarray}
$$

となる。
これと$y=x$の直線の交点を考えると

$$
\begin{eqnarray}
    & &
        x - s_{n+2}
        =
        (x - s_{n+1})
        \frac{
            s_{n+2} - s_{n+1}
        }{
            (s_{n+1} - s_{n})
        }
    \nonumber
    \\
    & \Leftrightarrow &
        x 
        (s_{n+1} - s_{n})
        =
        (x - s_{n+1})
        (s_{n+2} - s_{n+1})
        +
        s_{n+2}
        (s_{n+1} - s_{n})
    \nonumber
    \\
    & \Leftrightarrow &
        x 
        (s_{n+1} - s_{n})
        -
        x
        (s_{n+2} - s_{n+1})
        =
        -s_{n+1}
        (s_{n+2} - s_{n+1})
        +
        s_{n+2}
        (s_{n+1} - s_{n})
    \nonumber
    \\
    & \Leftrightarrow &
        x 
        \left(
            2s_{n+1}
            - s_{n}
            - s_{n+2}
        \right)
        =
        - s_{n+1}s_{n+2} 
        + s_{n+1}^{2}
        + s_{n+2} s_{n+1}
        - s_{n} s_{n+2}
    \nonumber
    \\
    & \Leftrightarrow &
        x 
        \left(
            2s_{n+1}
            - s_{n}
            - s_{n+2}
        \right)
        =
        + s_{n+1}^{2}
        - s_{n} s_{n+2}
    \nonumber
    \\
    & \Leftrightarrow &
        x 
        =
        \frac{
            + s_{n+1}^{2}
            - s_{n} s_{n+2}
            +
            s_{n}
            \left(
                2s_{n+1}
                - s_{n}
                - s_{n+2}
            \right)
            -
            s_{n}
            \left(
                2s_{n+1}
                - s_{n}
                - s_{n+2}
            \right)
        }{
            2s_{n+1}
            - s_{n}
            - s_{n+2}
        }
    \nonumber
    \\
    & \Leftrightarrow &
        x 
        =
        s_{n}
        +
        \frac{
            + s_{n+1}^{2}
            - s_{n} s_{n+2}
            - 2s_{n+1}s_{n}
            + s_{n}^{2}
            + s_{n+2} s_{n}
        }{
            2s_{n+1}
            - s_{n}
            - s_{n+2}
        }
    \nonumber
    \\
    & \Leftrightarrow &
        x 
        =
        s_{n}
        +
        \frac{
            (s_{n+1} - s_{n})^{2}
        }{
            - s_{n}
            + 2s_{n+1}
            - s_{n+2}
        }
    \lable{aitken_next_point}
\end{eqnarray}
$$

となる。
よって$$\eqref{aitken_next_point}$$に従って新しい点列を作れば良い。

## Reference
* [エイトケンのΔ2乗加速法 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%82%A4%E3%83%88%E3%82%B1%E3%83%B3%E3%81%AE%CE%942%E4%B9%97%E5%8A%A0%E9%80%9F%E6%B3%95)
* [Aitken's delta-squared process - Wikipedia](https://en.wikipedia.org/wiki/Aitken%27s_delta-squared_process)

