---
title: Monte Carlo
---

## Monte Carlo
The monte carlo method is one of the numerical integration methods of which computational complexity does not depends on the dimension of the domain of the integrand.

$$
    \mathrm{E}
    \left[
        f(X)
    \right]
    \approx
    \frac{1}{N}
    \sum_{i=1}^{N}
        f(X_{i})
$$

where $f: [0, 1]^{s} \rightarrow \mathbb{R}$ and $$\{X_{i}\}$$ is a I.I.D. sequence with the same distribution of $X$.
The Monte Carlo method is not competitive method for calculating lower dimensional (1-3 dimensional) integral.

The convergence is ensured by the strong law of large numbers.

* $N$,
    * the number of simulations
* $O(N^{1/2})$,
    * rate of convergence

## Variance Reduction Techniques
To reduce the variance of the integrator are imporant for fast convergence.
There are some techiniques to achieve lower variance.

* <a href="{{ site.baseurl }}/math/monte_carlo/importance_sampling.html">importance sampling</a>

## Sampling techniques
* <a href="{{ site.baseurl }}/math/monte_carlo/rejection_sampling.html">rejection sampling</a>
* Inverse Transform method

## Reference
* [Monte Carlo Methods](https://www.unige.ch/sciences/astro/files/2713/8971/4086/3_Paltani_MonteCarlo.pdf)
