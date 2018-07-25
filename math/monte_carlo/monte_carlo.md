---
title: Monte Carlo
---

## Monte Carlo
The monte carlo method is one of the numerical integration methods of which computational complexity does not depends on the dimension of the domain of the integrand.
To reduce the variance of the integrator are imporant for fast convergence because the convergence is ensured by the Central Limit Theorem.

$$
    \mathrm{E}
    \left[
        f(X)
    \right]
    \approx
    \frac{1}{N}
    \sum_{i=1}^{n}
        f(X_{i})
$$

where $f: [0, 1]^{s} \rightarrow \mathbb{R}$ and $$\{x^{i}\} \subset \mathbb{R}^{s}$$ is pseudo-random sequence.

## Variance Reduction Techniques
* <a href="{{ site.baseurl }}/math/monte_carlo/importance_sampling.html">importance sampling</a>
* <a href="{{ site.baseurl }}/math/monte_carlo/importance_sampling.html">rejection sampling</a>

## Reference
* [Monte Carlo Methods](https://www.unige.ch/sciences/astro/files/2713/8971/4086/3_Paltani_MonteCarlo.pdf)
