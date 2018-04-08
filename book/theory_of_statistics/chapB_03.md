---
title: Conditioning
book_title: Theory of statistics
book_chapter: B
book_section: 3
---

## B.3 Conditioning

## B.3.4 Conditional Independence

### Definition B.57
* $I$
    * inde set
* $Y$
    * r.v.
* $$\{X_{i}\}_{i \in I$$,
    * r.v.
* $\mathcal{A}_{i} := \sigma(X_{i})$

$$\{X_{i}\}$$ are said to be conditionally independent given $Y$ if

$$
  \forall n \in \mathbb{N},
  \
  i_{1}, \ldots_{n},
  \
  A_{1} \in \mathcal{A}_{i_{1}}, \ldots, A_{n} \in \mathcal{A}_{i_{n}},
  \
  \mu
  \left(
      \bigcup_{j=1}^{n}
      A_{j}
      \mid
      Y
  \right)
  =
  \Prod_{j=1}^{n}
  \mu
  \left(
      A_{j}
      \mid
      Y
  \right)
  \text{-a.s.}
$$

If $Y$ is constant almost surely, we say $$\{X_{i}\}$$ are independent.

<div class="end-of-statement" style="text-align: right">■</div>

## B.3.5 The Law of Total Probability

### Theorem B.70 Law of total probability
* $(\mathcal{S}, \mathcal{A}, \mu)$,
  * probability sp.
* $Z$
  * r.v.
  * $\mathrm{E}[|Z|] < \infty$,

### proof

<div class="QED" style="text-align: right">$\Box$</div>

### Corollary B.71

### proof

<div class="QED" style="text-align: right">$\Box$</div>

### Corollary B.72

### proof

<div class="QED" style="text-align: right">$\Box$</div>

### Theorem B.73
* $(\mathcal{S}, \mathcal{A}, \mu)$,
  * probability sp.
* $\mathcal{B} \subseteq \mathcal{A}$,
* $\mathcal{C}  \subseteq \mathcal{B}$,
* $Z: S \rightarrow \mathbb{R}$,
  * measurable
  * $\mathrm{E}[|Z|] < \infty$

Then following statements are equivalent;

* (i) there exits a version of $$\mathrm{E}[Z \md \mathcal{B}]$$ $\mathcal{C}$ measurable
* (ii)

$$
\mathrm{E}[Z \mid \mathcal{B}]
=
\mathrm{E}[Z \mathcal{C}]
\quad
\mu \text{-a.s.}
$$

### proof
(i) $\Rightarrow$ (ii)
Suppose that $W$ is a version of $$\mathrm{E}[Z \mid \mathcal{B}]$$ is $\mathcal{C}$ measurable.

$$
  \mathrm{E}[Z \mid \mathcal{B}]
  =
  W
  \
  \mu \text{-a.s.}
$$

$$
  C \in \mathcal{C},
  \
  \int_{C}
    W(s)
  \ \mu(ds)
  =
  \int_{C}
    \mathrm{E}[Z \mid \mathcal{B}](s)
  \ \mu(ds)
  =
  \int_{C}
    Z(s)
  \ \mu(ds)
  =
  \int_{C}
    \mathrm{E}[Z \mid \mathcal{C}](s)
  \ \mu(ds)
  .
$$

(i) $\Leftarrow$ (ii)

$\mathrm{E}[Z \mid C]$ is a version of $\mathrm{E}[Z \mid \mathcal{B}]$.

<div class="QED" style="text-align: right">$\Box$</div>
