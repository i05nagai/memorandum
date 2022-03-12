---
title: Kleene Star
---

## Kleene Star
Kleene star or Kleene Closure.

Given a set $V$.

$$
\begin{eqnarray}
    V^{0}
    & := &
        \{
            \epsilon
        \}
    \nonumber
    \\
    V^{1}
    & := &
        V
    \nonumber
    \\
    V^{i+1}
    & := &
        \{wv \mid w \in V^{i}, v \in V\}
\end{eqnarray}
$$

Kleene star of $V$ is

$$
    V^{*}
    :=
    \bigcup_{i \ge 0} V^{i}
    .
$$


## Reference
- [Kleene star \- Wikipedia](https://en.wikipedia.org/wiki/Kleene_star)
