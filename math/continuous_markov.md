---
title: Continuous Markov
---

## Continuous Markov

## Definition
* $$(\Omega, \mathcal{F}, P, (\mathcal{F}_{t})_{t \ge 0})$$,
    * fltrationつきの確率空間

### Def(Markov Process)
* $\mu$
    * $\mathbb{R}^{d}$上のBorel prob. measure

$(X_{t})_{t \ge 0}$が初期分布$\mu$の$$(\Omega, \mathcal{F}, P)$$上のMarkov processとは以下を満たすことである。

1. $$P(X_{0} \in \Gamma) = \mu(\Gamma) \quad (\forall \Gamma \in \mathcal{B}(\mathbb{R}^{d})$$,
2. $$s, t \ge 0$$, $$\Gamma \in \mathcal{B}(\mathbb{R}^{d})$$のとき、

$$
    P(X_{s+t} \in \Gamma \mid \mathcal{F}_{s})
    =
    P(X_{s+t} \in \Gamma \mid X_{s})
    \quad
    \mathrm{a.s.}
$$

### Def(Markov family)
$x \in \mathbb{R}^{d}$とすろ。
$$(X_{t}^{x})_{t \ge 0}$$がtime-homogeneous Markov familyとは

1. 以下で定義される$p$が$x$の関数としてBorel可測

$$
    p(t, x, \Gamma)
    :=
    P(X_{t}^{x} \in \Gamma)
    \quad
    (
        t \ge 0,
        x \in \mathbb{R}^{d},
        \Gamma \in \mathcal{B}(\mathbb{R}^{d})
    )
$$

2. 以下が成立

$$
    P(X_{0}^{x} = x) = 1.
$$

3.  $s, t \ge 0 $, $x \in \mathbb{R}^{d}$, $\Gamma \in \mathcal{B}(\mathbb{R}^{d})$に対して

$$
    P(X_{s+t}^{x} \in \Gamma \mid \mathcal{F}_{s})
    =
    p(t, X_{s}^{x}, \Gamma)
    \quad
    \mathrm{a.s.}
$$

成立。

このとき、$p$は遷移確率(transition function)という。
