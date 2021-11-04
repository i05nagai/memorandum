---
title: Statistical Hypothesis Small Sampling Theory
---

## Statistical Hypothesis Small Sampling Theory

## Formulation of hypothesis testing

### Definition1 statistical hypothesis test
* $(\mathcal{X}, \mathcal{A})$,
    * measurable space
* $\Theta \subseteq \mathbb{R}^{p}$,
    * parameters
* $\{P\}_{\theta \in \Theta}$,
    * probability measure over $(\mathcal{X},\mathcal{A})$,
* $\alpha \in [0, 1]$,
    * constant

A pair of subsets $(\Theta_{0}, \Theta_{1}) \subseteq \Theta^{2}$ is said to be hypothesis and alternatives if $\Theta_{0} \cap \Theta_{1} = \emptyset$ and $\Theta_{0} \cup \Theta_{1} = \Theta$.

A measurable function $\phi: \mathcal{X} \rightarrow [0, 1]$ is said to be test, test function or critical function.
In particular, test $\phi$ is said to be non-randomized if test $\phi$ is an indicator function.
Otherwise, $\phi$ is randomized test.

For test $\phi$,

$$
    \sup_{\theta \in \Theta_{0}}
        \mathrm{E}_{\theta}
        \left[
            \phi
        \right]
$$

is said to be size of test $\phi$ for hypothesis $\Theta_{0}$.

A test $\phi$ is said to be level $\alpha$ test or test at level $\alpha$ for hypothesis $\Theta_{0}$ if

$$
    \forall \theta \in \Theta_{0},
    \
    \mathrm{E}_{\theta}
    \left[
        \phi
    \right]
    \le
    \alpha
    .
$$

We denote $\Phi_{\alpha}$ by set of level $\alpha$ tests.

For test $\phi$,

$$
    \beta_{\phi}(\theta)
    :=
    \mathrm{E}_{\theta}
    \left[
        \phi
    \right]
$$

is said to be power function or power.

For test $\bar{\phi} \in \Phi_{\alpha}$, $\bar{\phi}$ is said to be the uniformly most powerful test at level $\alpha$ if

$$
    \theta \in \Theta_{1},
    \
    \beta_{\phi}(\theta)
    \le
    \beta_{\bar{\phi}}(\theta)
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Remark2
* There is no common or standard definition for hypothesis and alternatives.
Most books define it differently.
* Most books say $(\mathcal{X}, \mathcal{A})$ is any measurable space but in many cases they implicitly assume that $\mathcal{X} \subseteq \mathbb{R}^{d}$ and $\mathcal{A}$ is subset of borrel sigma algebra over $\mathcal{X}$.
* Power of test is a measure of goodness to the test.

<div class="end-of-statement" style="text-align: right">■</div>

### Theorem3 Neyman-Peason's fundamental lemma
* $\Theta_{0} := \\{0\\}$,
* $\Theta_{1} := \\{1\\}$,
* $P_{0}, P_{1}$
    * distribution of $X$
* $\mu$
    * sigma-finite measure over $(\mathcal{X}, \mathcal{A})$
* $p_{0}, p_{1}$
    * radon nikodym derivative of $P_{i}$ with respect to $\mu$
* $H = \\{P_{0}\\}$,
    * hypothesis
* $K = \\{P_{1}\\}$,
    * alternatives
* $\alpha \in [0, 1]$,

(1)

$$
\begin{eqnarray}
    \exists \phi: \text{ test},
    \
    \exists k, \gamma \in \mathbb{R}
    \
    \text{ s.t. }
    \
    \
    \mathrm{E}_{0}
    \left[
        \phi
    \right]
    & = &
        \alpha
    \label{chap03-03-07}
    \\
    \phi(x)
    & = &
            \begin{cases}
                1
                &
                    (p_{1}(x) > kp_{0}(x))
                \\
                \gamma
                &
                    (p_{1}(x) = kp_{0}(x))
                \\
                0
                &
                    p_{1}(x) < kp_{0}(x)
            \end{cases}
    \nonumber
    \\
    & = &
        1_{\\{p_{1} > kp_{0}\\}}(x)
        +
        \gamma
        1_{\\{p_{1} = kp_{0}\\}}(x)
        \quad
        \mu
        \text{-a.e. } x
    \label{chap03-03-08}
\end{eqnarray}
$$

(2) If test $\phi$ satisifes \eqref{chap03-03-07} and \eqref{chap03-03-08}, then $\phi$ is most powerful test at level $\alpha$.

(3) If $\alpha \in (0, 1)$ and test $\phi$ is the most powerful test at level $\alpha$, then there exists $k, \gamma \in \mathbb{R}$ such that \eqref{chap03-03-08} satisfies.

### proof.
**proof of (1)**

For $\alpha = 0$,

$$
\begin{eqnarray}
    F(z)
    & := &
        P_{0}
        \left(
            \left\{
                x \in \mathcal{X}
                \mid
                p_{1}(x) \le z p_{0}(x)
            \right\}
        \right)
    \nonumber
    \\
    & = &
        \int_{\mathcal{X}}
            1_{\{\frac{p_{1}}{p_{0}} \le z\}}(x)
            p_{0}(x)
        \ \mu(dx)
    \label{theorem-fundamental-neyman-peason-lemma-02-def-of-cdf}
\end{eqnarray}
$$

$F$ is cumulative distribution function, that is, $F$ satisfies following propeties:

* (a) $F(+\infty) = 1$,
* (b) $F(-\infty) = 0$,
* (c) $F$ is right continuous,
* (d) $F$ is non decreasing.

Indeed, for (a), by monoton convergence theorem, we have

$$
\begin{eqnarray}
    \int_{\mathcal{X}}
        1_{\{x \mid \frac{p_{1}(x)}{p_{0}(x)} \le z\}}(x)
        p_{0}(x)
    \ \mu(dx)
    & \nearrow  &
        \int_{\mathcal{X}}
            p_{0}(x)
        \ \mu(dx)
        \quad
        (z \rightarrow \infty)
    \nonumber
    \\
    & = &
        1
    .
    \nonumber
\end{eqnarray}
$$

(b) is obivous since

$$
    P(p_{i}(x) < 0)
    =
    0
    .
$$

For (c), let $z \in \mathbb{R}$ be fixed.
For all sequence $$\{z_{n}\_{n \in \mathbb{N}}$$, $z_{n} \searrow z$, we have

$$
\begin{eqnarray}
    \int_{\mathcal{X}}
        1_{\{\frac{p_{1}}{p_{0}} \le z_{n}\}}(x)
        p_{0}(x)
    \ \mu(dx)
    -
    \int_{\mathcal{X}}
        1_{\{\frac{p_{1}}{p_{0}} \le z\}}(x)
        p_{0}(x)
    \ \mu(dx)
    & = &
        \int_{\mathcal{X}}
            (
                1_{\{\frac{p_{1}}{p_{0}} \le z_{n}\}}(x)
                -
                1_{\{\frac{p_{1}}{p_{0}} \le z\}}(x)
            )
            p_{0}(x)
        \ \mu(dx)
    .
    \nonumber
\end{eqnarray}
$$

By taking the limit of equation above as $n \rightarrow \infty$, it converges to 0 by Lebesgue dominated convergence theorem.
Hence (c) holds.
Finally we show (d).
But this is obvious since integrand satisifies that

$$
    \forall z < z^{\prime},
    \
    \Rightarrow
    \
    \forall x \in \mathcal{X},
    \
    0
    \le
    1_{\{\frac{p_{1}}{p_{0}} \le z\}}(x)
    p_{0}(x)
    <
    1_{\{\frac{p_{1}}{p_{0}} \le z^{\prime}\}}(x)
    p_{0}(x)
    .
$$

Therefore, $F$ is cumulative distribution.
Since $F$ is non decreasing and right continuous,

$$
\begin{equation}
    0 < \forall \alpha < 1,
    \
    \exists k \in \mathbb{R},
    \
    \text{ s.t. }
    \
    F(k-)
    \le
    1 - \alpha
    \le
    F(k)
    .
    \label{theorem-fundamental-neyman-peason-lemma-01}
\end{equation}
$$

Indeed, let $\alpha \in (0, 1)$ be fixed.
We denote

$$
\begin{eqnarray}
    A
    & := &
        \{
            x \in \mathbb{R}
            \mid
            1 - \alpha
            \le
            F(x)
        \}
    \nonumber
    \\
    k
    & := &
        \inf
        A
    \nonumber
    \\
    B
    & := &
        \{
            x \in \mathbb{R}
            \mid
            F(x)
            \le
            1 - \alpha
        \}
    .
    \nonumber
    \\
    c
    & := &
        \sup
        B
    .
    \nonumber
\end{eqnarray}
$$

By right-continuity,

$$
    \forall \{k_{n}\},
    \
    k_{n} \searrow k,
    \
    \lim_{n \rightarrow \infty}
    F(k_{n})
    =
    F(k)
    \ge
    1 - \alpha
    .
$$

Then $F$ is non decreasing so that

$$
    \forall \{k_{n}\}_{n \in \mathbb{N}},
    \
    k_{n}
    \nearrow
    k,
    \
    \Rightarrow
    \
    k_{n}
    \le
    c
    .
$$

We can easily check this.
Suppose there exists $n$ such that $c < k_{n}$.
$F$ is non decreasing so that $F(c) < F(k_{n})$.
If $1 - \alpha \le F(k_{n})$, $k_{n} \in A$ but this contradict to $k_{n} \le k$.
In other hand, if we assume $F(k_{n}) < 1 - \alpha$, $k_{n} \in B$ so that $k_{n} \le c$.
Therefore the above statement hold.
By combining our observations, we have

$$
    \lim_{n \rightarrow \infty} F(k_{n})
    \le
    F(c)
    \le
    1 - \alpha
    \le
    F(k)
    .
$$

The equation \eqref{theorem-fundamental-neyman-peason-lemma-01} holds.
Now we define constant $\gamma$

$$
    \gamma
    :=
    \begin{cases}
        0
        &
            F(k) = F(k-) = 1 - \alpha
        \\
        \frac{F(k) - (1 - \alpha)}{F(k) - F(k-)}
        &
            \text{otherwise}
    \end{cases}
    ,
$$

and test $\phi$

$$
    \phi(x)
    :=
    1_{\{p_{1} > k p_{0}\}}(x)
    +
    \gamma
    1_{\{p_{1} = k p_{0}\}}(x)
    .
$$

Then we have

$$
\begin{eqnarray}
    \mathrm{E}_{0}
    \left[
        \phi
    \right]
    & = &
        P_{0}(p_{1} > k p_{0})
        +
        \gamma
        P_{0}(p_{1} = k p_{0})
    \nonumber
    \\
    & = &
        1 - F(k)
        +
        \gamma
        (F(k) - F(k-))
    \nonumber
    \\
    & = &
        \begin{cases}
            1 - (1- \alpha)
            &
                F(k) = F(k-) =  1 - \alpha
            \\
            1 - F(k)
            -
            (
                F(k)
                -
                (1 - \alpha)
            )
            &
                \text{otherwise}
        \end{cases}
    \nonumber
    \\
    & = &
        \alpha
\end{eqnarray}
$$

**proof of (2)**

Let $\phi$ be test.
There exist $k, \gamma \in \mathbb{R}$ such that $\phi$ satisfies that \eqref{chap03-03-07} and \eqref{chap03-03-08}.
For all test $\phi^{\prime}: \mathcal{X} \rightarrow [0, 1]$ at level $\alpha$, from \eqref{chap03-03-08},


$$
    (\phi - \phi^{\prime})
    (p_{1} - k p_{0})
    \ge
    0
    \quad
    \mu
    \text{-a.e.}
$$

Hence the integral of the equation satisfies

$$
    \int_{\mathcal{X}}
        (\phi - \phi^{\prime})
        (p_{1} - k p_{0})
    \ \mu(x)
    \ge
    0
$$

Form the equation above,

$$
\begin{eqnarray}
    \int_{\mathcal{X}}
        (\phi - \phi^{\prime})
        p_{1}
    \ \mu(x)
    & \ge &
        k
        \int_{\mathcal{X}}
            (\phi - \phi^{\prime})
            p_{0}
        \ \mu(x)
    \nonumber
    \\
    & = &
        k
        \mathrm{E}_{0}
        \left[
            \phi
        \right]
        -
        k
        \mathrm{E}_{0}
        \left[
            \phi^{\prime}
        \right]
    \nonumber
    \\
    & = &
        k
        \left(
            \alpha
            -
            \mathrm{E}_{0}
            \left[
                \phi^{\prime}
            \right]
        \right)
    \ge 0
    \quad
    (\because \phi^{\prime} \text{ is test at level } \alpha)
    \nonumber
\end{eqnarray}
$$

Therefore

$$
    \mathrm{E}_{1}
    \left[
        \phi
    \right]
    \ge
    \mathrm{E}_{1}
    \left[
        \phi^{\prime}
    \right]
    .
$$

**proof of (3)**

Let $\phi^{\prime}$ be most powerful test at level $\alpha$.
As we have already shown in (1), there exist the most powerful test $\phi$ at level $\alpha$.
By definition of $\phi$ and (2), 

$$
    \int_{\mathcal{X}}
        (\phi - \phi^{\prime})
        (p_{1} - k p_{2})
    \ \mu(x)
    \ge
    0
    .
$$

In other hand, $\phi^{\prime}$ is most powerful test at level $\alpha$ so that we have

$$
    \mathrm{E}_{1}
    \left[
        \phi^{\prime}
    \right]
    \ge
    \mathrm{E}_{1}
    \left[
        \phi
    \right]
    .
$$

<div class="QED" style="text-align: right">$\Box$</div>

### Example4
* $n \in \mathbb{N}$,
* $\Theta := [0, 1]$,
* $\mathcal{X} := \{0, 1, \ldots, n\}$,
* $\mu: \mathcal{X} \rightarrow [0, 1]$
    * countable measure
* $P_{\theta}:= B(n, \theta)$
    * binominal distribution
* $\theta_{i} \in \Theta$,
    * $0 < \theta_{0} < \theta_{1} < 1$,

$$
\begin{eqnarray}
    p_{\theta}(x)
    & := &
        \frac{d P_{\theta}}{d \mu}(x)
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                n \\
                x
            \end{array}
        \right)
        \theta^{x}
        (1 - \theta)^{n - x}
    \nonumber
\end{eqnarray}
$$

We consinder hypothesis test:

$$
    \Theta_{H}
    :=
    \{\theta_{0}\},
    \
    \Theta_{K}
    :=
    \{\theta_{0}\}
    .
$$

We have

$$
    \log
        \frac{
            p_{\theta_{0}}(x)
        }{
            p_{\theta_{1}}(x)
        }
    =
    ax
    +
    n \log
        \frac{
            1 - \theta_{1}
        }{
            1 - \theta_{0}
        }
$$

where

$$
    a
    :=
    \log
        \frac{
            \theta_{1}/(1 - \theta_{1})
        }{
            \theta_{0}/(1 - \theta_{0})
        }
    >
    0
    .
$$

Now let

$$
    \phi(x)
    :=
    \begin{cases}
        1
        &
            x > x_{0}
        \\
        \gamma
        &
            x = x_{0}
        \\
        0
        &
            x < x_{0}
    \end{cases}
$$

where $\gamma$ and $x_{0}$ are taken to satisfy $\beta_{\phi}(\theta_{0}) = \alpha$.
$\phi$ is the unimofrmly most powerful test for hypothesis $\Theta_{H$}$ and alternatives $\Theta_{K}$.

<div class="end-of-statement" style="text-align: right">■</div>

## Monotone likehood ratio and composite hypothesis test
* $\Theta \subseteq \mathbb{R}$,
* $(\mathcal{X}, \mathcal{A})$,
    * measurable space
* $\mathcal{P} := \{P_{\theta} \}_{\theta \in \Theta}$,
    * family of probability distribution over $(\mathcal{X}, \mathcal{A})$
* $\mu: \mathcal{X} \rightarrow [0, \infty)$
    * $\sigma$ finite measure on $(\mathcal{X}, \mathcal{A})$

Assumptions

$$
    \forall \theta,
    \
    \mu
    \gg
    P_{\theta}
    .
$$

### Definition monotone likelihood ratio
* $T: \mathcal{X} \rightarrow \mathbb{R}_{\ge 0}$
    * measurable function

$$
    \mathcal{X}_{\theta_{1}, \theta_{2}}
    :=
    \mathcal{X}
    \setminus
    \{x \mid p_{\theta_{1}}(x) = p_{\theta_{2}}(x) = 0\}
    \quad
    (\theta_{1}, \theta_{2} \in \Theta)
$$

$\mathcal{P}$ is said to be monotone likelihood ration with respect to $T$ if

$$
\begin{eqnarray}
    \forall \theta_{1}, \theta_{2} \in \Theta,
    \
    \theta_{1} < \theta_{2},
    \
    \exists H_{\theta_{1}, \theta_{2}}:T(\mathcal{X}) \rightarrow [0, \infty]
    \text{ s.t. }
    & &
        H \text{ is non-decreasing},
    \nonumber
    \\
    & &
        \forall x \in
        \mathcal{X}_{\theta_{1}, \theta_{2}}
        ,
        \
        \frac{p_{\theta_{2}}}{p_{\theta_{1}}}(x)
        =
        H_{\theta_{1}, \theta_{2}}(T(x))
    \nonumber
\end{eqnarray}
$$

We assume $c/0 = \infty$ for $c > 0$.

<div class="end-of-statement" style="text-align: right">■</div>

### Example5
* $\Theta \subseteq \mathbb{R}$,
* $$\mathcal{P} := \{P_{\theta} \}_{\theta \in \Theta}$$,
    * one prameter exponential family

That is, there exist $g: \mathcal{X} \rightarrow \mathbb{R}_{\ge 0}$, $a: \Theta \rightarrow \mathbb{R}$, $\psi: \Theta \rightarrow \mathbb{R}$ such that

$$
    p_{\theta}(x)
    :=
    g(x)
    \exp
    \left(
        a(\theta) T(x)
        -
        \psi(\theta)
    \right)
    \
    (x \in \mathcal{X})
    .
$$

If $a$ is non-decreasing function, then $\mathcal{P}$ is monotone likelihood ration with respect to $T$.

<div class="end-of-statement" style="text-align: right">■</div>

### Theorem6 UMP test for MLR
* $\theta_{0} \in \Theta \subseteq \mathbb{R}$,
    * given
* $$\mathcal{P} := \{P_{\theta}\}_{\theta \in \Theta}$$,
    * monotone likelihood ratio in statistics $T$
* $$\{\theta \mid \theta > \theta_{0}\} \neq \emptyset$$,
* $c \in \mathbb{R}$,
* $\gamma \in [0, 1]$,

(a) Let

$$
\begin{eqnarray}
    \phi_{0}(x)
    & := &
        \begin{cases}
            1
            &
                (T(x) > c)
            \\
            \gamma
            &
                (T(x) = c)
            \\
            0
            &
                (T(x) < c)
        \end{cases}
    \nonumber
    \\
    & = &
        1_{\{x \mid T(x) >c\}}(x)
        +
        \gamma
        1_{\{x \mid T(x) =c\}}(x)
        \label{chap03-03-22-test}
\end{eqnarray}
$$

If $$\mathrm{E}_{\theta_{0}} \left[ \phi_{0} \right] > 0$$,
then $\phi_{0}$ is the most powerful test at level $$\alpha^{\prime} := \mathrm{E}_{\theta_{0}}[\phi_{0}]$$ for hypothesis test

$$
\begin{equation}
    \Theta_{H}
    :=
    \{\theta \mid \theta \le \theta_{0}\},
    \
    \Theta_{K}
    :=
    \{\theta \mid \theta > \theta_{0}\},
    \label{chap03-03-23-hypothesis-test}
\end{equation}
$$

(b) For $\alpha \in (0, 1)$,

$$
    \exists c \in \mathbb{R},
    \
    \gamma \in [0, 1],
    \
    \text{ s.t. }
    \
    \phi_{0}: \ \eqref{chap03-03-22-test}
    \text{ is the most powerful test at level } \alpha
$$

### proof
(a)

Let $\Phi(\Theta_{H}, \Theta_{K}, \alpha^{\prime})$ be a set of tests for $\Theta_{H}$ and $\Theta_{K}$ at level $\alpha^{\prime}$.
We need to show

$$
\begin{equation}
    \forall \phi \in \Phi(\Theta_{H}, \Theta_{K}, \alpha^{\prime}),
    \
    \theta_{1} \in \Theta_{K},
    \
    \mathrm{E}_{\theta_{1}}[\phi_{0}]
    \ge
    \mathrm{E}_{\theta_{1}}[\phi]
    \label{chap03-monotone-likehood-ratio-ump-test}
\end{equation}
$$

and

$$
\begin{equation}
    \sup_{\theta \in \Theta_{H}}
        \mathrm{E}_{\theta}
        \left[
            \phi_{0}
        \right]
    \le
    \alpha^{\prime}
    \label{chap03-monotone-likehood-ratio-level-alpha-test}
    .
\end{equation}
$$

We first show \eqref{chap03-monotone-likehood-ratio-ump-test}.
Let $\theta_{1} \in \Theta_{K}$ be fixed and

$$
    k
    :=
    \inf
    \left\{
        \frac{p_{\theta_{1}}(x)}{p_{\theta_{0}}(x)}
        \mid
        x \in \mathcal{X}_{\theta_{1}, \theta_{2}},
        \
        T(x) \ge c
    \right\}
    .
$$

Then $k \in \mathbb{R}_{\ge 0}$.
Indeed, 

$$
\begin{eqnarray}
    \mu(
        \{
            x \in \mathcal{X}_{\theta_{0}, \theta_{1}}
            \mid
            p_{\theta_{0}}(x)
            \neq
            0,
            \
            T(x) \ge c
        \}
    )
    & = &
        \mu(
            \{
                x \in \mathcal{X}_{\theta_{0}, \theta_{1}}
                \mid
                T(x) \ge c
            \}
        )
    \nonumber
    \\
    & > &
        0
\end{eqnarray}
$$

since

$$
    \int_{\mathcal{X}_{\theta_{0}, \theta_{1}}}
        1_{\{T \ge c\}}(x)
        p_{\theta_{0}}(x)
    \ \mu(dx)
    =
    P_{\theta_{0}}(T \ge c)
    \ge
    \mathrm{E}_{\theta_{0}}[\phi_{0}]
    >
    0
    .
$$

Morever $p_{\theta_{1}} < \infty \ \mu \text{-a.e.}$ by definition.
Therefore $k < \infty$.

Now we show that 

$$
\begin{eqnarray}
    x \in \mathcal{X}_{\theta_{0}, \theta_{1}},
    \
    p_{\theta_{1}}(x)
    >
    kp_{\theta_{0}}(x),
    & \Rightarrow &
        \phi_{0}(x) = 1
    \nonumber
    \\
    x \in \mathcal{X}_{\theta_{0}, \theta_{1}},
    \
    p_{\theta_{1}}(x)
    <
    kp_{\theta_{0}}(x),
    & \Rightarrow &
        \phi_{0}(x) = 0
        \label{chap03-03-24}
    .
\end{eqnarray}
$$

Let $$x \in \mathcal{X}_{\theta_{0}, \theta_{1}}$$ be fixed.
Suppose that $p_{\theta_{1}}(x)/p_{\theta_{0}}(x) > k$.
To show $\phi(x) = 1$, it is sufficient to see $T(x) > c$.
By definition of $k$, there exists $$x^{\prime} \in \mathcal{X}_{\theta_{0}, \theta_{1}}$$ such that

$$
    k
    \le
    \frac{p_{\theta_{1}}(x^{\prime})}{p_{\theta_{0}}(x^{\prime})}
    <
    \frac{p_{\theta_{1}}(x)}{p_{\theta_{0}}(x)},
    \
    T(x^{\prime})
    \ge
    c
    .
$$

If we assume $T(x) \le c$, by definiiton of monotone likelihood ratio,

$$
\begin{eqnarray}
    \frac{
        p_{\theta_{1}}(x)
    }{
        p_{\theta_{0}}(x)
    }
    & = &
        H_{\theta_{0}, \theta_{1}}(T(x))
    \nonumber
    \\
    & \le &
        H_{\theta_{0}, \theta_{1}}(c)
    \nonumber
    \\
    & \le &
        H(T(x^{\prime}))
    \nonumber
    \\
    & \le &
        \frac{
            p_{\theta_{1}}(x^{\prime})
        }{
            p_{\theta_{0}}(x^{\prime})
        }
    \nonumber
\end{eqnarray}
$$

This is contradiction so that $\phi(x) = 1$.
Suppose that $$p_{\theta_{1}}(x)/p_{\theta_{0}}(x) < k$$.
If $T(x) \ge c$, $k$ cannot be infimum.
Hence $T(x) < c$.

From <a href="#theorem3-neyman-peasons-fundamental-lemma">theorem</a> and \eqref{chap03-03-24}, test $\phi_{0}$ is the most powerful test of hypothesis test $$\Theta_{H}^{\prime} := \{\theta_{0}\}$$ and $$\Theta_{K}^{\prime} := \{\theta_{1}\}$$ at level $$\alpha^{\prime} := \mathrm{E}_{\theta_{0}}[\phi_{0}]$$.

Let $\phi$ be test for $$\Theta_{H}$$ and $$\Theta_{K}$$ at level $$\alpha^{\prime}$$.
Then $\phi$ is also test for $$\Theta_{H}^{\prime}$$ and $$\Theta_{K}^{\prime}$$ at level $$\alpha^{\prime}$$.
Hence

$$
\begin{equation}
    \mathrm{E}_{\theta_{1}}
    \left[
        \phi_{0}
    \right]
    \ge
    \mathrm{E}_{\theta_{1}}
    \left[
        \phi
    \right]
    \label{chap03-03-26}
\end{equation}
    .
$$

$$\theta_{1}$$ is arbitrary fixed so that \eqref{chap03-03-26} holds for all $$\theta-{1} \in \Theta-{K}$$.

Now we show that \eqref{chap03-monotone-likehood-ratio-level-alpha-test}.
It suffices to show that

$$
    \forall \theta_{2} < \theta_{0},
    \
    \mathrm{E}_{\theta_{2}}
    \left[
        \phi_{0}
    \right]
    \le
    \alpha^{\prime}
$$

With out loss of generality, $$\mathrm{E}_{\theta_{2}}[\phi_{0}] > 0$$.
Indeed, if $$\mathrm{E}_{\theta_{2}}[\phi_{0}] = 0$$, the equation always holds  since $$0 \le \alpha^{\prime}$$.
Let $\theta_{2} < \theta_{0}$ be fixed.
From discussion above, $$\phi_{0}$$ is the most powerful test at level $$\alpha^{\prime\prime} := \mathrm{E}_{\theta_{2}}[\phi_{0}]$$ for hypothesis $$\Theta_{H}^{\prime\prime} := \{\theta_{2}\}$$ and alternatives $$\Theta_{K}^{\prime\prime} := \{\theta_{0} \}$$ by substituting $$\theta_{2}$$ for $$\theta_{0}$$ and $$\theta_{0}$$ for $$\theta_{1}$$, respectively.
Since $$\alpha^{\prime\prime}$$ is one of tests at level $$\alpha^{\prime\prime}$$ for hypothesis $$\Theta_{H}^{\prime\prime}$$ and alternatives $$\Theta_{K}^{\prime\prime}$$, we have

$$
\begin{eqnarray}
    &  &
        \mathrm{E}_{\theta_{0}}[\alpha^{\prime\prime}]
        \le
        \mathrm{E}_{\theta_{0}}[\phi_{0}]
    \nonumber
    \\
    & \Leftrightarrow &
        \alpha^{\prime\prime}
        \le
        \mathrm{E}_{\theta_{0}}[\phi_{0}]
    \nonumber
    \\
    & \Leftrightarrow &
        \mathrm{E}_{\theta_{2}}[\phi_{0}]
        \le
        \mathrm{E}_{\theta_{0}}[\phi_{0}]
        =
        \alpha^{\prime}
    \nonumber
\end{eqnarray}
$$

(b)

Let

$$
    F(u)
    :=
    P_{\theta_{0}}(T \le u)
    .
$$

Then there exists $c \in \mathbb{R}$ such that

$$
    F(c-)
    \le
    1 - \alpha
    \le
    F(c)
    .
$$

Now, let

$$
    \gamma
    :=
    \begin{cases}
        0
        &
            F(c) - F(c-) = 0
        \\
        \frac{
            (\alpha - 1 + F(c))
        }{
            F(c) - F(c-)
        }
        &
            F(c) - F(c-) > 0
    \end{cases}
    .
$$

Then $\phi_{0}$ defined in \eqref{chap03-03-22-test} is the most powerful test at level $$\alpha := \mathrm{E}_{\theta_{0}}[\phi_{0}]$$ for hypothesis $$\Theta_{H}$$ and alternative $$\Theta-{K}$$ by (a).

<div class="end-of-statement" style="text-align: right">■</div>

## Generalized Neyman Peason's lemma

### Theorem7 Generalized neyman pearson fundamental lemma
* $(\mathcal{X}, \mathcal{A})$,
    * measurable sp.
* $\mu: \Omega \rightarrow [0, \infty)$,
    * $\sigma$-finite measure over $(\mathcal{X}, \mathcal{A})$
* $$\Phi := \{\phi \mid \phi: \mathcal{X} \rightarrow [0, 1]: \text{ measurable function}\}$$,
* $$f_{1}, \ldots, f_{m}, g \in L^{1}(\mathcal{X}, \mathcal{A}, \mu)$$,

$$
    c := (c_{1}, \ldots, c_{m})
    \in
    \mathbb{R}^{m},
    \
    \Phi_{c}
    :=
    \left\{
        \phi \in \Phi
        \mid
        \int_{\mathcal{X}}
            \phi(x) f_{i}(x)
        \ \mu(dx)
        =
        c_{i},
        (i = 1, \ldots, m)
    \right\}
    \neq
    \emptyset
    .
$$

Then

(a) Let $$\phi_{0} \in \Phi_{c}$$.
If there eixist $$k_{1}, \ldots, k_{m} \in \mathbb{R}$$ such that

$$
\begin{equation}
    \phi_{0}(x)
    =
    \begin{cases}
        1
        &
        (g(x) > \sum_{i=1}^{m}k_{i}f_{i}(x))
        \\
        0
        &
        (g(x) < \sum_{i=1}^{m}k_{i}f_{i}(x))
    \end{cases}
    \
    \mu \text{-a.e.}
    \label{chap03-03-27-test}
\end{equation}
    ,
$$

then

$$
    \int_{\mathcal{X}}
        \phi_{0}(x) g(x)
    \ \mu(dx)
    =
    \sup
    \left\{
        \int_{\mathcal{X}}
            \phi(x) g(x)
        \ \mu(dx)
        \mid
        \phi \in \Phi_{c}
    \right\}
    .
$$

(b) Let $$\phi_{0} \in \Phi_{c}$$.
If there exists $$k_{1}, \ldots, k_{m} \in \mathbb{R}_{\ge 0}$$ such that \eqref{chap03-03-27-test} is satisfied, then

$$
    \int_{\mathcal{X}}
        \phi_{0}(x) g(x)
    \ \mu(dx)
    =
    \sup
    \left\{
        \int_{\mathcal{X}}
            \phi(x) g(x)
        \ \mu(dx)
        \mid
        \phi \in \Phi,
        \
        \int_{\mathcal{X}}
            \phi(x) f_{i}(x)
        \ \mu(dx)
        \le
        c_{i}
        (i = 1, \ldots, m)
    \right\}
$$

### proof
(a)

Since $$\phi_{0} \in \Phi_{c}$$,

$$
\begin{eqnarray}
    \int_{\mathcal{X}}
        \phi_{0}(x) g(x)
    \ \mu(dx)
    -
    \sum_{i=1}^{m}
        k_{i}c_{i}
    & = &
        \int_{\mathcal{X}}
            \phi_{0}(x)
            g(x)
        \ \mu(dx)
                -
        \int_{\mathcal{X}}
                \sum_{j=1}
                    k_{i}f_{i}(x)
        \ \mu(dx)
    \nonumber
    \\
    & = &
        \int_{\mathcal{X}}
            \phi_{0}(x)
            \left(
                g(x)
                -
                \sum_{j=1}
                    k_{i}f_{i}(x)
            \right)
        \ \mu(dx)
    \nonumber
\end{eqnarray}
$$

On the other hand, for all $\phi \in \Phi_{c}$

$$
\begin{eqnarray}
    \int_{\mathcal{X}}
        \phi(x) g(x)
    \ \mu(dx)
    -
    \sum_{i=1}^{m}
        k_{i}c_{i}
    & = &
        \int_{\mathcal{X}}
            \phi(x)
                g(x)
        \ \mu(dx)
                -
        \int_{\mathcal{X}}
                \sum_{j=1}
                    k_{i}f_{i}(x)
        \ \mu(dx)
    \nonumber
    \\
    & = &
        \int_{\mathcal{X}}
            \phi(x)
            \left(
                g(x)
                -
                \sum_{j=1}
                    k_{i}f_{i}(x)
            \right)
        \ \mu(dx)
    .
    \nonumber
\end{eqnarray}
$$

Therefore,

$$
\begin{eqnarray}
    \forall \phi \in \Phi_{c},
    \
    \int_{\mathcal{X}}
        \phi_{0}(x) g(x)
        -
        \phi(x) g(x)
    \ \mu(dx)
    & = &
        \int_{\mathcal{X}}
            \phi_{0}(x) g(x)
            -
            \phi(x) g(x)
        \ \mu(dx)
        +
        \sum_{i=1}^{m}
            k_{i}c_{i}
        -
        \sum_{i=1}^{m}
            k_{i}c_{i}
    \nonumber
    \\
    & = &
        \int_{\mathcal{X}}
            (\phi_{0}(x) - \phi(x))
            \left(
                g(x)
                -
                \sum_{j=1}
                    k_{i}f_{i}(x)
            \right)
        \ \mu(dx)
    \nonumber
    \\
    & = &
        \int_{g(x) > \sum_{j=1}^{m}k_{i}f_{i}(x)}
            (1 - \phi(x))
            \left(
                g(x)
                -
                \sum_{j=1}
                    k_{i}f_{i}(x)
            \right)
        \ \mu(dx)
    \nonumber
    \\
    & \ge &
        0
    .
    \nonumber
\end{eqnarray}
$$

(b)

For simplicity, let

$$
    B
    :=
    \left\{
        \phi \in \Phi
        \mid
        \int_{\mathcal{X}}
            \phi(x)f_{i}(x)
        \ \mu(dx),
        \le
        c_{i}
        \
        (i = 1, \ldots, m)
    \right\}
    .
$$

Since $\phi_{0} \in \Phi_{c}$, we have $\phi \in B$.
For all $\phi \in B$,

$$
\begin{eqnarray}
    \int_{\mathcal{X}}
        \phi(x) g(x)
    \ \mu(dx)
    -
    \sum_{i=1}^{m}
        k_{i}c_{i}
    & \le &
        \int_{\mathcal{X}}
            \phi(x)
                g(x)
        \ \mu(dx)
                -
        \int_{\mathcal{X}}
            \sum_{j=1}
                k_{i}f_{i}(x)
        \ \mu(dx)
    \nonumber
    \\
    & = &
        \int_{\mathcal{X}}
            \phi
            \left(
                g(x)
                -
                \sum_{j=1}
                    k_{i}f_{i}(x)
            \right)
        \ \mu(dx)
    .
    \nonumber
\end{eqnarray}
$$

Therefore,

$$
\begin{eqnarray}
    \forall \phi \in B,
    \
    \int_{\mathcal{X}}
        \phi_{0}(x) g(x)
        -
        \phi(x) g(x)
    \ \mu(dx)
    & = &
        \int_{\mathcal{X}}
            \phi_{0}(x) g(x)
        \ \mu(dx)
        -
        \sum_{i=1}^{m}
            k_{i}c_{i}
        -
        \left(
            \int_{\mathcal{X}}
                \phi(x) g(x)
            \ \mu(dx)
            -
            \sum_{i=1}^{m}
                k_{i}c_{i}
        \right)
    \nonumber
    \\
    & \ge &
        \int_{\mathcal{X}}
            (\phi_{0}(x) - \phi(x))
            \left(
                g(x)
                -
                \sum_{j=1}
                    k_{i}f_{i}(x)
            \right)
        \ \mu(dx)
    \nonumber
    \\
    & = &
        \int_{g(x) > \sum_{j=1}^{m}k_{i}f_{i}(x)}
            (1 - \phi(x))
            \left(
                g(x)
                -
                \sum_{j=1} k_{i}f_{i}(x)
            \right)
        \ \mu(dx)
    \nonumber
    \\
    & \ge &
        0
    .
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

## Unbiased test


### Definition8 Unbiased test
* $(\mathcal{X}, \mathcal{A})$,
    * measurable sp.
* $\Theta = \Theta_{0} \sqcup \Theta_{1}$,
    * parameter sp.
    * $\Theta_{0} \neq \emptyset$,
        * Hypothesis
    * $\Theta_{1} \neq \emptyset$,
        * Alternatives
* $\alpha \in [0, 1]$,
* $\phi: \mathcal{X} \rightarrow [0, 1]$
    * test at level$\alpha$

$\phi$ is said to be unibiased if

$$
    \forall \theta \in \Theta_{1},
    \
    \mathrm{E}_{\theta}
    \left[
        \phi
    \right]
    \ge
    \alpha
    .
$$

That is, power of the test $\phi$ is uniformly higher or equal to power of a trivial test $\phi^{\prime} \equiv \alpha$ at level $\alpha$.

We denote $\Phi_{\alpha}^{\mu}$ by a set of all unibiased test at level $\alpha$.

<div class="end-of-statement" style="text-align: right">■</div>

### Remark
A trival test $\phi^{\prime} \equiv \alpha$ at level $\alpha$ is interpreted as the test is accepted at random with the probability $\alpha$.
An unbiased test at level $\alpha$ means that the unbiased test is not worse than at random.

<div class="end-of-statement" style="text-align: right">■</div>

### Definition9
* $\Theta^{\prime} \subset \Theta$,
* $\phi$
    * test

$\phi$ is said to be similar to $\Theta^{\prime}$ if

$$
    \exists c \in \mathbb{R}
    \text{ s.t. }
    \forall \theta \in \Theta^{\prime},
    \
    c
    =
    \mathrm{E}_{\theta}
    \left[
        \phi
    \right]
    .
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Proposition10
* $\Theta$,
    * topological space
* $\Theta_{i} \subseteq \Theta \ (i = 0, 1)$,
    * disjoint set
* $(\Theta_{i})^{b} \ (i = 0, 1)$,
    * boundary of set $\Theta_{i}$,
* $\Theta^{\prime} := (\Theta_{0})^{b} \cap (\Theta_{1})^{b} \neq \emptyset$,
* $\phi: \mathcal{X} \rightarrow [0, 1]$,
    * unbiased test for Hypothesis $\Theta_{0}$ and alternative $\Theta_{1}$,
* $$\beta_{\phi}: \Theta \rightarrow [0, 1]$$,
    * continuous

Then $\phi$ is similar to $\Theta^{\prime}$.

### proof
Let $\theta \in \Theta^{\prime}$ and $\epsilon > 0$ be fixed.
Since $\beta_{\phi}$ is continuous,

$$
    \exists \theta_{0} \in \Theta_{0},
    \
    \exists \theta_{1} \in \Theta_{1},
    \
    \text{ s.t. }
    \
    |
        \mathrm{E}_{\theta_{i}}
        \left[
            \phi
        \right]
        -
        \mathrm{E}_{\theta^{\prime}}
        \left[
            \phi
        \right]
    |
    \le
    \epsilon
    \
    (i = 0, 1)
$$

$\phi$ is unbiased,

$$
    \forall \theta \in \Theta_{1},
    \
    \mathrm{E}_{\theta}
    \left[
        \phi
    \right]
    \ge
    \alpha
    .
$$

Then

$$
\begin{eqnarray}
    \left|
        \mathrm{E}_{\theta^{\prime}}
        \left[
            \phi
        \right]
    \right|
    & \le &
        \left|
            \mathrm{E}_{\theta^{\prime}}
            \left[
                \phi
            \right]
            -
            \mathrm{E}_{\theta_{0}}
            \left[
                \phi
            \right]
        \right|
        +
        \left|
            \mathrm{E}_{\theta_{0}}
            \left[
                \phi
            \right]
        \right|
    \nonumber
    \\
    & \le &
        \epsilon
        +
        \alpha
    \nonumber
\end{eqnarray}
$$


$$
\begin{eqnarray}
    \left|
        \mathrm{E}_{\theta^{\prime}}
        \left[
            \phi
        \right]
    \right|
    & \ge &
        -
        \left|
            \mathrm{E}_{\theta^{\prime}}
            \left[
                \phi
            \right]
            -
            \mathrm{E}_{\theta_{1}}
            \left[
                \phi
            \right]
        \right|
        +
        \left|
            \mathrm{E}_{\theta_{1}}
            \left[
                \phi
            \right]
        \right|
    \nonumber
    \\
    & \ge &
        -
        \epsilon
        +
        \alpha
    \nonumber
\end{eqnarray}
$$

Since $\epsilon$ is arbitrary, $$\beta_{\phi}(\theta^{\prime}) = \alpha$$.
<div class="end-of-statement" style="text-align: right">■</div>

### Proposition11
* $\Theta^{\prime} \neq \emptyset \subset \Theta$

$$
    \Phi_{\alpha}^{\prime}
    :=
    \{
        \phi \in \Phi
        \mid
        \mathrm{E}_{\theta}
        \left[
            \phi
        \right]
        =
        \alpha
        \
        (\theta \in \Theta^{\prime})
    \}
$$

* $\phi_{0} \in \Phi_{\alpha}^{\prime}$,

If $\phi_{0}$ satisfies

$$
\begin{eqnarray}
    \forall \theta \in \Theta_{0},
    \
    \forall \phi \in \Phi_{\alpha}^{\prime},
    \
    \mathrm{E}_{\theta}
    \left[
        \phi_{0}
    \right]
    & \le &
        \mathrm{E}_{\theta}
        \left[
            \phi
        \right]
    \nonumber
    \\
    \forall \theta \in \Theta_{1},
    \
    \forall \phi \in \Phi_{\alpha}^{\prime},
    \
    \mathrm{E}_{\theta}
    \left[
        \phi_{0}
    \right]
    & \ge &
        \mathrm{E}_{\theta}
        \left[
            \phi
        \right]
    \nonumber
\end{eqnarray}
$$

then, $\phi_{0}$ is a unbiased test at level $\alpha$ for hypothesis $\Theta_{0}$ and alternative $\Theta_{1}$.

### proof
Since $\phi \equiv \alpha \in \Phi_{\alpha}^{\prime}$ and assumptions of $\phi_{0}$, we obtain

$$
    \forall \theta \in \Theta_{0},
    \
    \mathrm{E}_{\theta}
    \left[
        \phi_{0}
    \right]
    \le
    \alpha
    .
$$

Hence $\phi_{0}$ is test at level $\alpha$.
Similarly, we obtain

$$
    \forall \theta \in \Theta_{1},
    \
    \mathrm{E}_{\theta}
    \left[
        \phi_{0}
    \right]
    \ge
    \alpha
    .
$$

Therefore $\phi_{0}$ is unbiased test.

<div class="QED" style="text-align: right">$\Box$</div>

### Remark12
From both proposition, we can find an unbiased test by finding the best test only in  a set of similar tests.

<div class="end-of-statement" style="text-align: right">■</div>

* $m \le 2$,
* $\Theta \subseteq \mathbb{R}^{m}$,
    * open interval
* $$\{P_{\theta}\}_{\theta \in \Theta}$$,
    * exponential family

$$
    \frac{
        d P_{\theta}
    }{
        d \mu
    }(x)
    =
    \exp
    \left(
        \sum_{i=1}^{m}
            \theta_{i}
            T_{i}(x)
        -
        \psi(\theta)
    \right)
    g(x)
    .
$$


$$
\begin{eqnarray}
    t^{*}
    & := &
        (t_{2}, \ldots, t_{m}),
        \quad
        (t := (t_{1}, \ldots, t_{m}) \in \mathbb{R}^{m})
    \nonumber
    \\
    \theta^{*}
    & := &
        (\theta_{2}, \ldots, \theta_{m}),
        \quad
        (\theta := (\theta_{1}, \ldots, \theta_{m}) \in \Theta)
    \nonumber
    \\
    \Theta^{*}
    & := &
        \{\theta^{*} \mid \theta \in \Theta\},
    \nonumber
    \\
    T^{*}
    & := &
        (T_{2}, \ldots, T_{m})
    \nonumber
\end{eqnarray}
$$

### Theorem13 unbiased UMP
* $b \in \mathbb{R}$,
    * given
* $$\Theta_{0} := \{(b, \theta^{*}) \mid \theta \in \Theta\}$$,
* $$\Theta_{1} := \{\theta \mid \theta_{1} \neq b \in \Theta\}$$,
* $0 < \alpha < 1$,

For test for hypothesis $\Theta_{0}$ and alternatiev $\Theta_{1}$, there exists uniformly most powerful test at level level $\alpha$ such that

$$
    \phi_{0}(x)
    =
    \begin{cases}
        1
        &
        (T_{1}(x) < u_{1}(T^{*}(x)) \lor T_{1}(x) > u_{2}(T^{*}(x)))
        \\
        \gamma_{1}(T^{*}(x))
        &
        T_{1}(x) = u_{1}(T^{*}(x))
        \\
        \gamma_{2}(T^{*}(x))
        &
        T_{1}(x) = u_{2}(T^{*}(x))
        \\
        0
        &
        u_{1}(T^{*}(x)) < T_{1}(x) < u_{2}(T^{*}(x))
    \end{cases}
$$

where

* $\gamma_{i}: \mathbb{R}^{m-1} \rightarrow \mathbb{R} \ (i = 1, 2)$,
    * $\mathcal{B}(\mathbb{R}^{m-1})$ measurable function
* $u_{i}: \mathbb{R}^{m-1} \rightarrow \mathbb{R} \ (i = 1, 2)$,
    * $\mathcal{B}(\mathbb{R}^{m-1})$ measurable function

### proof
Since $\Theta$ is an open interval, $(b , \theta^{*})$ is an interior point for all $\theta \in \Theta$.
By proposition 3.31, any unbiased test at level $\alpha$ is similar to $\Theta_{0}$:

$$
\begin{equation}
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        \phi
    \right]
    =
    \alpha
    \
    (\forall \theta \in \Theta)
    \label{chap03-03-33}
    .
\end{equation}
$$

$$\{P_{(b, \theta{*})}\}_{\theta^{*} \in \Theta^{*}}$$ is an exponential family.


By <a href="#theorem-a-1">theorem in appendix</a>, $$T^{*}$$ is sufficient to $$\{P_{(b, \theta^{*})}\}_{\theta^{*} \in \Theta^{*}}$$.
Moreover, since the inner of $\Theta$ is not empty, $T^{*}$ is complete with respect to $$\{P_{(b, \theta^{*})}\}_{\theta^{*} \in \Theta^{*}}$$ by theorem 3.18.
Then follwoing equation holds

$$
\begin{equation}
    \forall \theta^{*} \in \Theta^{*},
    \
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        \phi
        \mid
        T^{*}
        =
        \cdot
    \right]
    =
    \alpha
    \quad
    P_{(b, \theta^{*})}^{T^{*}} \text{-a.s.}
    \label{chap03-theorem-03-33-equation-for-03-34}
\end{equation}
$$

Indeed,

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \int_{\mathbb{R}^{m-1}}
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            \phi
            \mid
            T^{*}
            =
            t^{*}
        \right]
    \ P_{(b, \theta^{*})}^{T^{*}}(d t^{*})
    & = &
        \int_{(T^{*})^{-1}(\mathbb{R}^{m-1})}
            \phi(x)
        \ P_{(b, \theta^{*})}(dx)
    \nonumber
    \\
    & = &
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            \phi
        \right]
    \nonumber
    \\
    & = &
        \alpha
    \nonumber
\end{eqnarray}
$$

Then by completeness of $T^{*}$ with respect to $$\{P_{(b, \theta^{*})}\}_{\theta^{*} \in \Theta^{*}}$$, we obtain the equation \eqref{chap03-theorem-03-33-equation-for-03-34}.
Now we show

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \mathrm{E}_{(b, \theta^{*})}
    \left[
    \left.
        \phi
    \right|
        T^{*}
    \right]
    =
    \alpha
    \quad
    P_{(b, \theta^{*})} \text{-a.s.}
    \label{chap03-03-34}
\end{eqnarray}
$$

By using $$\eqref{chap03-theorem-03-33-equation-for-03-34}$$ and the definition of conditional expectation, we have

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \forall (T^{*})^{-1}(B) \in \sigma(T^{*}),
    \
    \int_{(T^{*})^{-1}(B)}
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            \phi
            \mid
            T^{*}
        \right](x)
    \ P_{(b, \theta^{*})}(dx)
    & = &
        \int_{(T^{*})^{-1}(B)}
            \phi(x)
        \ P_{(b, \theta^{*})}(dx)
    \nonumber
    \\
    & = &
        \int_{B}
            \mathrm{E}
            \left[
            \left.
                \phi
            \right|
                T^{*} = t
            \right]
        \ P_{(b, \theta^{*})}^{T^{*}}(dt)
    \nonumber
    \\
    & = &
        \int_{B}
            \alpha
        \ P_{(b, \theta^{*})}^{T^{*}}(dt)
    \nonumber
    \\
    & = &
        \int_{(T^{*})^{-1}(B)}
            \alpha
        \ P_{(b, \theta^{*})}(dx)
    \nonumber
\end{eqnarray}
$$

Then by the definition of conditional expectation, we obtain \eqref{chap03-03-34}.

By proposition 3.17, $$\beta_{\phi}(\theta)$$ is differentialble with respect to $\theta_{1}$.

$$
\begin{eqnarray}
    \frac{\partial}{\partial \theta_{1}} 
        \mathrm{E}_{\theta}
        \left[
            \phi
        \right]
    & = &
        \frac{\partial}{\partial \theta_{1}} 
        \int_{\mathcal{X}}
            \phi(x)
            \exp
            \left(
                \sum_{i=1}^{m}
                    \theta_{i}T_{i}(x)
                -
                \psi(\theta)
            \right)
            g(x)
        \ \mu(dx)
    \nonumber
    \\
    & = &
        \int_{\mathcal{X}}
            \phi(x)
            \left(
                T_{1}(x)
                -
                \frac{\partial}{\partial \theta_{1}} \psi(\theta)
            \right)
            \exp
            \left(
                \sum_{i=1}^{m}
                    \theta_{i}T_{i}(x)
                -
                \psi(\theta)
            \right)
            g(x)
        \ \mu(dx)
    \nonumber
    \\
    & = &
        \int_{\mathcal{X}}
            \phi(x)
            T_{1}(x)
            \exp
            \left(
                \sum_{i=1}^{m}
                    \theta_{i}T_{i}(x)
                -
                \psi(\theta)
            \right)
            g(x)
        \ \mu(dx)
        -
        \int_{\mathcal{X}}
            \phi(x)
            \frac{\partial}{\partial \theta_{1}} \psi(\theta)
            \exp
            \left(
                \sum_{i=1}^{m}
                    \theta_{i}T_{i}(x)
                -
                \psi(\theta)
            \right)
            g(x)
        \ \mu(dx)
    \nonumber
    \\
    & = &
        \mathrm{E}_{(\theta_{1}, \theta^{*})}
        \left[
            \phi
            T_{1}
        \right]
        -
        \mathrm{E}_{(\theta_{1}, \theta^{*})}
        \left[
            \phi
            \frac{\partial}{\partial \theta_{1}} \psi(\theta)
        \right]
    .
    \nonumber
\end{eqnarray}
$$

$\phi$ is level $\alpha$ unbiased test so that we have

$$
\begin{eqnarray}
    \forall \theta \in \Theta_{0},
    \
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        \phi
    \right]
    & \le &
        \alpha
        \quad
        (\because \text{ level } \alpha)
    \nonumber
    \\
    \forall \theta \in \Theta_{1},
    \
    \mathrm{E}_{(\theta_{1}, \theta^{*})}
    \left[
        \phi
    \right]
    & \ge &
        \alpha
        \quad
        (\because \text{ unbiased})
    .
\end{eqnarray}
$$

Hence $\beta_{\phi}((\theta_{1}, \theta^{*}))$ achieves the minimum at $\theta = b$ as a function of $\theta_{1}$.
From above observations,

$$
\begin{eqnarray}
    & &
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            \phi
            T_{1}
        \right]
        =
        \frac{\partial}{\partial \theta_{1}} \psi(b, \theta^{*})
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            \phi
        \right]
    \nonumber
    \\
    & \Leftrightarrow &
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            \phi
            T_{1}
        \right]
        =
        \frac{\partial}{\partial \theta_{1}} \psi(b, \theta^{*})
        \alpha
        \quad
        (\because \eqref{chap03-03-33})
        .
    \nonumber
\end{eqnarray}
$$

Since $\phi$ is arbitrary unbiased test at level $\alpha$, we put $\phi \equiv \alpha$.

$$
\begin{eqnarray}
    & &
        \alpha
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            T_{1}
        \right]
        =
        \frac{\partial}{\partial \theta_{1}} \psi(b, \theta^{*})
        \alpha
    \nonumber
    \\
    & \Leftrightarrow &
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            T_{1}
        \right]
        =
        \frac{\partial}{\partial \theta_{1}} \psi(b, \theta^{*})
    \nonumber
    .
\end{eqnarray}
$$

Then for all level $\alpha$ unbiased test $\phi$ we obtain

$$
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        \phi
        T_{1}
    \right]
    =
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        T_{1}
    \right]
    \alpha
    .
$$

With the same way discussed in \eqref{chap03-03-34}, we have

$$
\begin{equation}
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        T_{1}\phi
        \mid
        T^{*} = t
    \right]
    =
    \alpha
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        T_{1}
        \mid
        T^{*} = t
    \right]
    \quad
    P_{(b, \theta^{*})}^{T^{*}} \text{-a.s.}
    \label{chap03-theorem-03-33-equation-for-03-35}
\end{equation}
$$

Indeed,

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \int_{\mathbb{R}^{m-1}}
        \mathrm{E}_{(b, \theta^{*})}
        \left[
        \left.
            T_{1}\phi
        \right|
            T^{*} = t
        \right]
    \ P_{(b, \theta^{*})}^{T^{*}}(dt)
    & = &
        \int_{(T^{*})^{-1}(\mathbb{R}^{m-1})}
            T_{1}(x)\phi(x)
        \ P_{(b, \theta^{*})}(dt)
    \nonumber
    \\
    & = &
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            T_{1}
        \right]
        \alpha
    .
    \nonumber
\end{eqnarray}
$$

Since $T^{*}$ is completewith respect to $\{P_{(b, \theta^{*})}\}_{\theta \in \Theta^{*}}$, we obtain \eqref{chap03-theorem-03-33-equation-for-03-35}
Now we show

$$
\begin{equation}
    \forall \theta \in \Theta,
    \
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        T_{1}\phi
        \mid
        T^{*}
    \right]
    =
    \alpha
    \mathrm{E}_{(b, \theta^{*})}
    \left[
        T_{1}
        \mid
        T^{*}
    \right]
    \quad
    P_{(b, \theta^{*})} \text{-a.s.}
    \label{chap03-03-35}
\end{equation}
$$

Indeed,

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \forall (T^{*})^{-1}(B) \in \sigma(T^{*}),
    \
    \int_{(T^{*})^{-1}(B)}
        \mathrm{E}_{(b, \theta^{*})}
        \left[
            T_{1}\phi
            \mid
            T^{*}
        \right]
    \ P_{(b, \theta^{*})}(d x)
    & = &
        \int_{(T^{*})^{-1}(B)}
            T_{1}\phi
        \ P_{(b, \theta^{*})}(d x)
    \nonumber
    \\
    & = &
        \int_{B}
            \mathrm{E}_{(b, \theta^{*})}
            \left[
                T_{1}\phi
                \mid
                T^{*} = t
            \right]
        \ P_{(b, \theta^{*})}^{T^{*}}(d t)
    \nonumber
    \\
    & = &
        \int_{B}
            \alpha
            \mathrm{E}_{(b, \theta^{*}}
            \left[
                T_{1}
            \right]
        \ P_{(b, \theta^{*})}^{T^{*}}(d t)
    \nonumber
    \\
    & = &
        \int_{(T^{*})^{-1}(B)}
            \alpha
            \mathrm{E}_{(b, \theta^{*}}
            \left[
                T_{1}
            \right]
        \ P_{(b, \theta^{*})}(d x)
\end{eqnarray}
$$

Then by the definition of conditional expectation, we obtain \eqref{chap03-03-35}.

Let $$\vartheta_{0} := (b, b^{*}) \in \Theta_{0}$$, $$\vartheta_{1} := (\theta_{1}, \theta^{*}) \in \Theta_{1}$$ and $$t^{*} \in \mathbb{R}^{m - 1}$$ be fixed.
We denote

$$
\begin{eqnarray}
    \Phi
    & := &
    \left\{
        f: \mathbb{R}^{m} \rightarrow [0, 1]
        \mid
        f: \text{ measurable}
    \right\}
    \nonumber
    \\
    \int_{\mathbb{R}}
        f(t_{1}, t^{*})
    \ P_{(b, b^{*})}(t^{*}, dt)
    & = &
        \alpha
    \label{chap03-theorem-03-33-condition-01}
    \\
    \int_{\mathbb{R}}
        t f(t_{1}, t^{*})
    \ P_{(b, b^{*})}(t^{*}, dt)
    & = &
        \int_{\mathbb{R}}
            \alpha t
        \ P_{(b, b^{*})}(t^{*}, dt)
    \label{chap03-theorem-03-33-condition-02}
    \\
    \Phi_{\alpha}^{\vartheta_{0} \vartheta_{1}, t^{*}}
    & := &
        \left\{
            f \in \Phi
            \mid
            f: \text{satisfies }
                \eqref{chap03-theorem-03-33-condition-01}
                \
                \eqref{chap03-theorem-03-33-condition-02}
        \right\}
    \label{chap03-theorem-03-33-set-of-functions}
\end{eqnarray}
$$

We can reduce problem to find $\bar{f} \in \Phi_{\alpha}^{\vartheta_{0} \vartheta_{1}, t^{*}}$ such that

$$
\begin{eqnarray}
    \forall f \in \Phi_{\alpha}^{\vartheta_{0} \vartheta_{1}, t^{*}},
    \
    \int_{\mathbb{R}}
        f(t_{1}, t^{*})
    \ P_{\vartheta_{1}}(t^{*}, dt)
    & \le &
        \int_{\mathbb{R}}
            \bar{f}(t_{1}, t^{*})
        \ P_{\vartheta_{1}}(t^{*}, dt)
    .
    \label{chap03-theorem-03-33-ump-condition}
\end{eqnarray}
$$

Indeed, suppose that there exists such $\bar{f}$.
Since the above equation holds for all $\vartheta_{1} \in \Theta_{1}$ and $t^{*} \in \mathbb{R}^{m-1}$, we have

$$
\begin{eqnarray}
    & &
        \int_{\mathbb{R}^{m-1}}
            \int_{\mathbb{R}}
                f(t_{1}, t^{*})
            \ P_{\theta}(t^{*}, dt)
        \ P_{\theta}^{T^{*}}(d t^{*})
    & \le &
        \int_{\mathbb{R}^{m-1}}
            \int_{\mathbb{R}}
                \bar{f}(t_{1}, t^{*})
            \ P_{\theta}(t^{*}, dt)
        \ P_{\theta}^{T^{*}}(d t^{*})
    \nonumber
    \\
    & \Leftrightarrow &
        \int_{\mathbb{R}^{m}}
            f(t)
        \ P_{\theta}^{T}(d t)
    & \le &
        \int_{\mathbb{R}^{m}}
            \bar{f}(t)
        \ P_{\theta}^{T}(d t)
    \nonumber
    \\
    & \Leftrightarrow &
        \int_{\mathbb{R}^{m}}
            f(T(x))
        \ P_{\theta}(d x)
    & \le &
        \int_{\mathbb{R}^{m}}
            \bar{f}(T(x))
        \ P_{\theta}(d x)
    .
    \nonumber
\end{eqnarray}
$$

Hence $\bar{f} \circ T$ is the UMP test.
Moreover, Since $f \equiv \alpha \in \Phi_{\alpha}^{\vartheta_{0}\vartheta_{1},t^{*}}$, $\bar{f} \circ T$ is unbiased test.
By \eqref{chap03-theorem-03-33-condition-02}, we have

$$
\begin{eqnarray}
    & &
        \int_{\mathbb{R}^{m}}
            \bar{f}(T(x))
        \ P_{(b, b^{*})}(d x)
    & \le &
        \alpha
    .
    \nonumber
\end{eqnarray}
$$

Hence $\bar{f} \circ T$ is unbiased UMP at level $\alpha$.

Now we will show the existence of $\bar{f}$.
Let $$\vartheta_{0} := (b, b^{*}) \in \Theta_{0}, \vartheta_{1} := (\theta_{1}, \theta^{*}) \in \Theta_{1}$$ be fixed.
From proposition 3.19 by taking $m_{1} = 1$, $m_{2} = m - 1$, there exists $\sigma$-finite measure $$\mu_{t^{*}}$$ such that

$$
\begin{eqnarray}
    \vartheta
    :=
    \vartheta_{0},
    \
    \vartheta_{1},
    \
    N_{\vartheta}
    & := &
        \left\{
            t_{m_{1}+1:m}
            \in
            \mathbb{R}^{m_{2}}
            \mid
            \int_{\mathbb{R}^{m_{1}}}
                \exp
                \left(
                    \langle \vartheta_{1:m_{1}}, t_{1:m_{1}} \rangle
                \right)
            \ \mu_{\vartheta^{*}}(d t_{1:m_{1}})
            =
            0
            \text{ or }
            \infty
        \right\}
    \nonumber
    \\
    P_{\vartheta_{1:m}}^{T^{*}}(N_{\vartheta})
    & = &
        0
    \nonumber
\end{eqnarray}
$$

Let

$$
\begin{eqnarray}
    N
    & := &
        N_{\vartheta_{0}}
        \cap
        N_{\vartheta_{1}}
        .
    \nonumber
\end{eqnarray}
$$

Then

$$
\begin{eqnarray}
    \vartheta
    :=
    \vartheta_{0},
    \
    \vartheta_{1},
    \
    \forall t^{*} \in N^{c},
    \
    P_{\vartheta}(t^{*}, d t_{1})
    & = &
        \frac{
            \displaystyle
            \exp
            \left(
                \langle
                    \vartheta_{1}, t_{1}
                \rangle
            \right)
            \nu_{t^{*}}(dt_{1})
        }{
            K_{\vartheta}
        }
    \nonumber
    \\
    K_{\vartheta}
    & := &
        \displaystyle
        \int_{\mathbb{R}^{m_{1}}}
            \exp
            \left(
                \langle
                    \vartheta_{1}, \tau_{1}
                \rangle
            \right)
        \nu_{t^{*}}(d\tau_{1})
    \nonumber
\end{eqnarray}
$$

By taking

* $\mu := P_{\vartheta_{1}}(t^{*}, \cdot)$,
* $g(t_{1}) := e^{(\theta_{1} - b)t_{1}} K_{\vartheta_{0}}/K_{\vartheta_{1}}$,
* $f_{1}(t_{1}) = 1$,
* $f_{2}(t_{1}) = t_{1}$,
* $c_{1} := \alpha$
* and $c_{2} := \alpha \int_{\mathbb{R}} t_{1} P_{\vartheta_{0}}(t^{*}, dt_{1})$,

$\Phi_{(c_{1}, c_{2})}$ in generalized Neyman-Peason's lemma equals to \eqref{chap03-theorem-03-33-set-of-functions}.

$$
\begin{eqnarray}
    \int_{\mathbb{R}}
        g(t)
        \bar{f}(t_{1}, t^{*})
    \ \mu(dx)
    & = &
        \int_{\mathbb{R}}
            \frac{
                K_{\vartheta_{0}}
            }{
                K_{\vartheta_{1}}
            }
            e^{(\theta_{1} - b)t_{1}}
            \bar{f}(t_{1}, t^{*})
            \frac{
                e^{bt_{1}}
            }{
                K_{\vartheta_{0}}
            }
        \ \mu_{t^{*}}(d t_{1})
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}}
            e^{\theta_{1}t_{1}}
            \bar{f}(t_{1}, t^{*})
            \frac{
                1
            }{
                K_{\vartheta_{1}}
            }
        \ \mu_{t^{*}}(d t_{1})
    \nonumber
    \\
    & = &
        \int_{\mathbb{R}}
            \bar{f}(t_{1}, t^{*})
        \ P_{\vartheta_{1}}(t^{*}, dt_{1})
    \nonumber
\end{eqnarray}
$$

Now we construct $\bar{f} \in \Phi_{\alpha}^{\vartheta_{0}, \vartheta_{1}, t^{*}}$.
Let

$$
\begin{eqnarray}
    F^{t^{*}}(z)
    & := &
        \int_{(-\infty, z]}
            
        \ P_{\vartheta_{0}}(t^{*}, dt_{1})
    \nonumber
    \\
    U_{1}^{t^{*}}(p)
    & := &
        \inf
        \{
            z \in \mathbb{R}
            \mid
            F^{t^{*}}(z)
            \ge
            p
        \}
    \nonumber
    \\
    U_{2}^{t^{*}}(p)
    & := &
        \inf
        \{
            z \in \mathbb{R}
            \mid
            F^{t^{*}}(z)
            \ge
            1 - \alpha + p
        \}
    \nonumber
    \\
    \Gamma_{1}^{t^{*}}(p)
    & := &
        (p - F^{t^{*}}(U_{1}^{t^{*}}(p)-))
        (F^{t^{*}}(U_{1}^{t^{*}}(p)) -  F^{t^{*}}(U_{1}^{t^{*}}(p)-))^{-}
    \nonumber
    \\
    \Gamma_{2}^{t^{*}}(p)
    & := &
        (F^{t^{*}}(U_{2}^{t^{*}}(p)) - (1 - \alpha) - p)
        (F^{t^{*}}(U_{2}^{t^{*}}(p)) -  F^{t^{*}}(U_{2}^{t^{*}}(p)-))^{-}
    \nonumber
    \\
    \Psi^{t^{*}}(t_{1}, p)
    & := &
        1_{(-\infty, U_{1}^{t^{*}}(p))}(t)
        +
        \Gamma_{1}^{t^{*}}(p)
        1_{U_{1}^{t^{*}}(p)}(t)
        +
        \Gamma_{2}^{t^{*}}(p)
        1_{U_{2}^{t^{*}}(p)}(t)
        +
        1_{(U_{2}^{t^{*}}(p)), \infty)}(t)
    \nonumber
    \\
    S^{t^{*}}(p)
    & := &
        \int_{\mathbb{R}}
            t
            \Psi^{t^{*}}(t_{1}, p)
        \ P_{\vartheta_{0}}(t^{*}, dt_{1})
    \nonumber
\end{eqnarray}
$$

where $x^{-}$ is zero if $x=0$ otherwise $x^{-1}$.
Now we show that

$$
    \exists p^{t^{*}} \in [0, \alpha],
    \
    \text{ s.t. }
    \
    S^{t^{*}}(p^{t^{*}})
    =
    \alpha
    \int_{\mathbb{R}}
        t_{1}
    \ P_{(b, b^{*})}(dt_{1}, t^{*})
    .
$$

It is enough to show that 

* $S^{t^{*}}$ is continuous in $[0, p]$,
* If $p = 0$,

$$
    S^{t^{*}}(0)
    >
    \alpha
    \int_{\mathbb{R}}
        t_{1}
    \ P_{(b, b^{*})}(dt_{1}, t^{*})
    ,
$$

* If $p = \alpha$,

$$
    S^{t^{*}}(0)
    <
    \alpha
    \int_{\mathbb{R}}
        t_{1}
    \ P_{(b, b^{*})}(dt_{1}, t^{*})
    .
$$

Then by intermediate value theorem, we obtain $p^{t^{*}}$.
Now we define

$$
    \bar{p}^{t^{*}}
    :=
    \inf
    \{
        p \in [0, \alpha]
        \mid
        S^{t^{*}}(p)
        =
        \alpha
        \int_{\mathbb{R}}
            t_{1}
        \ P_{(b, b^{*})}(dt_{1}, t^{*})
    \}
    .
$$

Finally, we constract $\bar{f}$ by

$$
    \bar{f}(t_{1}, t^{*})
    :=
    \Psi^{t^{*}}(t_{1}, p^{t^{*}})
    .
$$

$\bar{f}$ satisfies \eqref{chap03-theorem-03-33-condition-01};

$$
\begin{eqnarray}
    \int_{\mathbb{R}}
        \bar{f}(t_{1}, t^{*})
    \ P_{\vartheta_{0}}(t^{*}, d t_{1})
    & = &
        \alpha
    \nonumber
\end{eqnarray}
$$

Moreover, $\bar{f}$ satisfies \eqref{chap03-theorem-03-33-condition-02} by right continuity of $\Psi$ with respect to $p$, that is,

$$
\begin{eqnarray}
    \int_{\mathbb{R}}
        t
        \bar{f}(t_{1}, t^{*})
    \ P_{\vartheta_{0}}(t^{*}, d t_{1})
    & = &
        \alpha
        \int_{\mathbb{R}}
            t
        \ P_{\vartheta_{0}}(t^{*}, d t_{1})
    \nonumber
\end{eqnarray}
$$

By generalized Neyman-Peason's lemma, the following equation holds

$$
\begin{eqnarray}
    \int_{\mathbb{R}}
        \bar{f}(t_{1}, t^{*})
        g(t_{1})
    \ P_{\vartheta_{0}}(t^{*}, dt_{1})
    & = &
        \int_{\mathbb{R}}
            \bar{f}(t_{1}, t^{*})
            g(t_{1})
        \ P_{\vartheta_{1}}(t^{*}, dt_{1})
    \nonumber
    \\
    & = &
        \sup
        \left\{
            \int_{\mathbb{R}}
                f(t_{1}, t^{*})
                g(t_{1})
            \ P_{\vartheta_{0}}(t^{*}, dt_{1})
            =
            \int_{\mathbb{R}}
                f(t_{1}, t^{*})
            \ P_{\vartheta_{1}}(t^{*}, dt_{1})
            \mid
            f \in \Psi_{\alpha}^{\vartheta_{0}, \vartheta_{1}, t^{*}}
        \right\}
    \nonumber
\end{eqnarray}
$$

This implies that \eqref{chap03-theorem-03-33-ump-condition} holds.

<div class="QED" style="text-align: right">$\Box$</div>


## Appendix

### Theorem A-1
* $(\mathcal{X}, \mathcal{A})$,
    * measurable space
* $$\mathcal{P} := \{ P_{\theta}\}_{\theta \in \Theta}$$,
    * probability measure over $(\mathcal{X}, \mathcal{A})$,
* $k \in \mathbb{N}$,
* $(\mathcal{X}^{(i)}, \mathcal{A}^{(i)})$,
    * measurable space for $i = 1, \ldots, k$
* $$\mathcal{P}^{(i)} := \{P_{\theta}^{(i)}\}_{\theta \in \Theta}$$,
    * probability measure over $(\mathcal{X}^{(i)}, \mathcal{A}^{(i)})$ for $i = 1, \ldots, k$

The following statements hold:

* (a) If $\mathcal{P}$ is an exponential family, $\forall P_{\theta}, P_{\theta^{\prime}} \in \mathcal{P}$, $P_{\theta} \ll P_{\theta^{\prime}}$, $P_{\theta} \ll P_{\theta^{\prime}}$,
* (b) If for all $i = 1, \ldots, n$, $\mathcal{P}^{(i)}$ is exponential family, then $$\{\prod_{i=1}^{n} P_{\theta}^{(i)}\}$$ is an exponential family over $( \prod_{i=1}^{n} \mathcal{X}^{(i)}, \prod_{i=1}^{n} \mathcal{A}^{(i)})$.
* (c) $T$ is sufficinet with respect to $\mathcal{P}$.

### proof
(a)

Let $A \in \mathcal{A}$ be fixed.

$$
    P_{\theta}(A)
    =
    \int_{A}
        \exp
        \left(
            \sum_{i=1}^{m}
                a_{i}(\theta)
                T_{i}(x)
            -
            \psi(\theta)
        \right)
    \ \mu(dx)
$$

$$
\begin{eqnarray}
    \frac{
        d P_{\theta}
    }{
        d P_{\theta^{\prime}}
    }
    & = &
        \frac{
            d P_{\theta}
        }{
            d\mu
        }
        \frac{
            1
        }{
            \frac{
                d P_{\theta^{\prime}}
            }{
                d\mu
            }
        }
    \\
    & = &
        \exp
        \left(
            \sum_{j=1}^{m}
                (a_{j}(\theta) - a_{j}(\theta^{\prime}))
                T_{j}(x)
        \right)
    \nonumber
\end{eqnarray}
$$

$$
    P_{\theta}(A)
    =
    \int_{A}
        \exp
        \left(
            \sum_{j=1}^{m}
                (a_{j}(\theta) - a_{j}(\theta^{\prime}))
                T_{j}(x)
        \right)
    \ P_{\theta^{\prime}}(dx)
$$

The integrand is positive so that $P_{\theta^{\prime}}(A) = 0$.

(b)
Let $\mathcal{C}$ be a cylinder set.
That is,

$$
    \mathcal{C}
    :=
    \{
        A_{1} \times \cdots \times A_{n}
        \mid
        A_{i} \in \mathcal{A}^{(i)}
    \}
    .
$$

Then

$$
\begin{eqnarray}
    \forall A_{1} \times \cdots A_{n} \in \mathcal{C},
    \
    \left(
        \prod_{i=1}^{n} P_{\theta}^{(i)}
    \right)
    (A_{1} \times \cdots A_{n})
    & = &
        \prod_{i=1}^{n} P_{\theta}^{(i)}(A_{i})
        \
        (\because \text{ by definition of product measure})
    \\
    & = &
        \prod_{i=1}^{n}
        \left(
            \int_{A_{i}}
                \frac{
                    d P_{\theta}^{(i)}
                }{
                    d \mu
                }(x_{i})
            \ \mu(d x_{i})
        \right)
    \\
    & = &
        \int_{A_{1}\times \cdots A_{n}}
            \frac{
                d P_{\theta}^{(1)}
            }{
                d \mu
            }(x_{1})
            \times
            \cdots
            \times
            \frac{
                d P_{\theta}^{(n)}
            }{
                d \mu
            }(x_{n})
        \ \mu(d x)
        .
    \nonumber
\end{eqnarray}
$$

Therefore,

$$
    \frac{
        d
        \left(
            \prod_{i=1}^{n}
            P_{\theta}^{(i)}
        \right)
    }{
        d \mu
    }
    =
    \prod_{i=1}^{n}
    \left(
        \frac{
            d P_{\theta}^{(i)}
        }{
            d \mu
        }
    \right)
    .
$$

Obviously, the RHS of the equation is an exponential family.

(c)

Immediate consequence of factorization theorem.

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
