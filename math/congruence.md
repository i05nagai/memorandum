---
title: Congruence
---

## Congruence
合同式について。


### Proposition(properties)
性質

* 1 Refrectivity
    * $$
    a \equiv a\ (\mathrm{mod}\ m)
$$,

* 2 Symmetry
    * $$ a \equiv b\ (\mathrm{mod}\ m) $$ ならば

$$
    b \equiv a\ (\mathrm{mod}\ m),
$$

* 3 Transivity
    * $$ a \equiv b\ (\mathrm{mod}\ m), \ b \equiv c\ (\mathrm{mod}\ m) $$ ならば

$$
    a \equiv c\ (\mathrm{mod}\ m)
$$

* 4 $$ a \equiv b\ (\mathrm{mod}\ m), \ a^{\prime} \equiv b^{\prime}\ (\mathrm{mod}\ m) $$ ならば

$$
    a + a^{\prime} \equiv b + b^{\prime}\ (\mathrm{mod}\ m),
    a - a^{\prime} \equiv b - b^{\prime}\ (\mathrm{mod}\ m),
$$

* 5  $$ a \equiv b\ (\mathrm{mod}\ m), \ a^{\prime} \equiv b^{\prime}\ (\mathrm{mod}\ m) $$ ならば

$$
    aa^{\prime} \equiv bb^{\prime}\ (\mathrm{mod}\ m),
$$

* 6 $$ a \equiv b\ (\mathrm{mod}\ m)$$ならば、$\forall k \in \mathbb{Z}$について、

$$
    a \equiv b + mk\ (\mathrm{mod}\ m)
$$

* 7 $ ac \equiv bc\ (\mathrm{mod}\ m)$, $(c, m) = 1$ならば、法と素な公約数で割って良い。
つまり、

$$
    a \equiv b\ (\mathrm{mod}\ m)
$$

* 8 $ a \equiv b\ (\mathrm{mod}\ m)$ならば、$\forall k \in \mathbb{Z}_{> 0}$について

$$
    ak \equiv bk\ (\mathrm{mod}\ mk)
$$

* 9 $ a \equiv b\ (\mathrm{mod}\ m)$とし、$d$を$a, b, m$の公約数とする。
このとき、$a = a_{1}d$, $b = b_{1}d$, $m = m_{1}d$とすれば

$$
    a_{1} \equiv b_{1}\ (\mathrm{mod}\ m)
$$

* 10 $ a \equiv b\ (\mathrm{mod}\ m)$ならば、$m$の約数$d$について、

$$
    a \equiv b\ (\mathrm{mod}\ d)
$$

* 11 $ a \equiv b\ (\mathrm{mod}\ m_{1})$, $$ a \equiv b\ (\mathrm{mod}\ m_{2}), \ldots, a \equiv b\ (\mathrm{mod}\ m_{k})$$ならば、
$$m_{1}, \ldots, m_{k}$$の最小公倍数$m$について、

$$
    a \equiv b\ (\mathrm{mod}\ m)
$$

* 12 $p$を素数とすれば、$\forall x, y \in \mathbb{Z}$について、

$$
    (x + y)^{p} \equiv x^{p} + y^{p}\ (\mathrm{mod}\ p)
$$

* 13 $p$を素数とすれば、$$\forall x_{1}, \ldots, x_{n}$$に対して、

$$
    (x_{1} + \ldots + x_{n})^{p} \equiv x_{1}^{p} + \cdots + x_{n}^{p}\ (\mathrm{mod}\ p)
$$

* 14 $p$を素数、$a$を$0 \le a \le p - 1$とすると、

$$
    \left(
        \begin{array}{c}
            p - 1 \\
            a
        \end{array}
    \right)
    \equiv
    (-1)^{a}
    \ (\mathrm{mod}\ p)
$$

### proof.

<div class="QED" style="text-align: right">$\Box$</div>
