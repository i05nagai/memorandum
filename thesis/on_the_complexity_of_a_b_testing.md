---
title: On the Complexity of A/B Testing
---

## On the Complexity of A/B Testing

* $$(\Omega, \mathcal{F}, P, \{\mathcal{F}_{t}\})$$,
    * probability space with filtration $F_{t}$
* $\nu_{1}$,
    * probability measure over $(\Omega, \mathcal{F})$,
    * distribution of treatment group
* $\nu_{2}$,
    * probability measure over $(\Omega, \mathcal{F})$,
    * distribution of treatment group
* $T \in \mathbb{N}$,
    * End of experiments
* $$\mathcal{T} := \{1, \ldots, T\}$$,
    * time partition

There are several fomrmalizations of the model of obvervations.

The first case, two type of observations occrus at the (almost) same time.
For instance, if you forward users accesing to web site to PageA or PageB randomly, this can be the case.
The assumption behind the example is that the number of access users are large and the accesses frequently occur.

* $$X_{1, s} \ (s \in \mathcal{T})$$,
    * control group
    * arm 1
* $$X_{2, s} \ (s \in \mathcal{T})$$,
    * treatment group
    * arm 2

The second case, the observation does not happen at the same time. It's always sequential and selective.

* $$A_{s} \in \{1, 2\}\ (s \in \mathcal{T})$$,
    * selection of arm for time $s$,
    * $\mathcal{F}_{s-1}$ measurable
        * selection is done prior to observation of reward at time $s$
* $$X_{A_{s}, s} \ (s \in \mathcal{T})$$,
    * reward at at time $s$,
    * $X_{A_{s}, s} \sim \nu_{1}$ if $A_{s} = 1$,
    * $X_{A_{s}, s} \sim \nu_{2}$ if $A_{s} = 2$,

The best arm $a^{*}$ is the arm which has the best expectation.

$$
    a^{*}
    :=
    \arg\min_{a \in \{1, 2\}}
        \mathrm{E}
        \left[
            \sum_{s=1}^{t}
                X_{a, s}
        \right]
    .
$$

The A/B testing in the sense of the multi armed-bandit is that to find $a^{*}$ in finite time $$\mathcal{T}$$.
The strategy of multi-armed bandit is how we find the best arm.

* $$A_{s} \in \{1, 2\} \ (s \in \mathcal{T})$$,
    * sampling rule
    * the choice of an arm at time $s$
    * $\mathcal{F}_{s-1}$ measurable
* $\tau$
    * stopping time w.r.t $(\mathcal{F}_{t})$.
* $$\hat{a} \in \{1, 2\}$$,
    * recommendation rule
    * $F_{\tau}$ measurable
    * recommendation based on sampling rule

$$(\{A_{s}\}, \hat{a})$$ is strategy, denoted by $\mathcal{A}$.

The strategy $\mathcal{A}$ is said to be $\delta$-PAC if 

$$
    P(\hat{a} = a^{*})
    \ge
    1 - \delta
    .
$$

The A/B testing is

## Reference
* [1] E. Kaufmann, O. Cappé, and A. Garivier, “On the Complexity of A/B Testing,” vol. 35, pp. 1–23, 2014.
