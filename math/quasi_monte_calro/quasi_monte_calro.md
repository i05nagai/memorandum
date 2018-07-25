---
title: Quasi Monte Carlo
---

## Quasi Monte Carlo
Quasi Monte Carlo (QMC) method is a numerical integration method using low-descrepancy sequence.
The name comes from Monte Carlo (MC) methods, which is well-known numerical integration method using pseud-random sequence.
As MC method, QMC method approximate a integal by summation of the values of integrand at points given by the sequence.

$$
    \int_{0}^{1}
        f(x)
    \ dx
    \approx
    \sum_{i=1}^{n}
        f(x_{i})
$$

where $f: [0, 1]^{s} \rightarrow \mathbb{R}$ and $$\{x^{i}\} \subset \mathbb{R}^{s}$$ is low-descrepancy sequence.


## Reference

