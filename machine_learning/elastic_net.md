---
title: Elastic Net
---

## Elastic Net
二乗誤差とparameterのL1 normとL2 normの最小化をする。

$$
\begin{eqnarray}
    \sum_{i=0}^{N}
        (y_{i} - \hat{y}_{i})^{2}
    +
    \lambda_{1}
    \|w\|_{1}
    +
    \lambda_{2}
    \|w\|_{2}^{2}
\end{eqnarray}
$$

## Reference
