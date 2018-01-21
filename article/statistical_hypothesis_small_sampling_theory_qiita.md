## Statistical Hypothesis Small Sampling Theory

## Formulation of hypothesis testing
Here we formulate statistical hypothesis testing and define related terminologies.

### Definition1 statistical hypothesis test
* $(\mathcal{X}, \mathcal{A})$,
    * measurable space
* $\Theta \subseteq \mathbb{R}^{p}$,
    * parameters
* $\\\{P\\\}_{\theta \in \Theta}$,
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
* Power of test is a measure of goodness for the test.

<div class="end-of-statement" style="text-align: right">■</div>

### Theorem3 Neyman-Peason's fundamental lemma
* $\Theta_{0} := \\\{0\\\}$,
* $\Theta_{1} := \\\{1\\\}$,
* $P_{0}, P_{1}$
    * distribution of $X$
* $\mu$
    * sigma-finite measure over $(\mathcal{X}, \mathcal{A})$,
* $p_{0}, p_{1}$
    * radon nikodym derivative of $P_{i}$ with respect to $\mu$
* $H = \\\{P_{0}\\\}$,
    * hypothesis
* $K = \\\{P_{1}\\\}$,
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
    \mathrm{E}_{0}
    \left[
        \phi
    \right]
    & = &
        \alpha
    \tag{chap03-03-07}
    \\\\
    \phi(x)
    & = &
        \begin{cases}
            1
            &
                (p\_{1}(x) > kp\_{0}(x))
            \\\\
            \gamma
            &
                (p\_{1}(x) = kp\_{0}(x))
            \\\\
            0
            &
                (p\_{1}(x) < kp\_{0}(x))
        \end{cases}
    \\\\
    & = &
        1\_{\\\{p\_{1} > kp\_{0}\\\}}(x)
        +
        \gamma
        1\_{\\\{p\_{1} = kp\_{0}\\\}}(x)
        \quad
        \mu
        \text{-a.e. } x
    \tag{chap03-03-08}
\end{eqnarray}
$$

(2) If test $\phi$ satisifes <a href="#mjx-eqn-chap03-03-07">(chap03-03-07)</a> and <a href="#mjx-eqn-chap03-03-08">(chap03-03-08)</a>, then $\phi$ is most powerful test at level $\alpha$.

(3) If $\alpha \in (0, 1)$ and test $\phi$ is the most powerful test at level $\alpha$, then there exists $k, \gamma \in \mathbb{R}$ such that <a href="#mjx-eqn-chap03-03-08">(chap03-03-08)</a> satisfies.

### proof.
**proof of (1)**

For $\alpha = 0$,

$$
\begin{eqnarray}
    F(z)
    & := &
        P_{0}
        \left(
            \left\\\{
                x \in \mathcal{X}
                \mid
                p_{1}(x) \le z p_{0}(x)
            \right\\\}
        \right)
    \\\\
    & = &
        \int_{\mathcal{X}}
            1\_{\{\frac{p\_{1}}{p\_{0}} \le z\}}(x)
            p\_{0}(x)
        \ \mu(dx)
    \tag{theorem-fundamental-neyman-peason-lemma-02-def-of-cdf}
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
For all sequence $\\\{z_{n}\\\}_{n \in \mathbb{N}}$, $z_{n} \searrow z$, we have

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
    \tag{theorem-fundamental-neyman-peason-lemma-01}
\end{equation}
$$

Indeed, let $\alpha \in (0, 1)$ be fixed.
We denote

$$
\begin{eqnarray}
    A
    & := &
        \\\{
            x \in \mathbb{R}
            \mid
            1 - \alpha
            \le
            F(x)
        \\\}
    \\\\
    k
    & := &
        \inf A,
    \\\\
    B
    & := &
        \\\{
            x \in \mathbb{R}
            \mid
            F(x)
            \le
            1 - \alpha
        \\\},
    \\\\
    c
    & := &
        \sup B,
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
    \forall \\\{k\_{n}\\\}\_{n \in \mathbb{N}},
    \
    k\_{n}
    \nearrow
    k,
    \
    \Rightarrow
    \
    k\_{n}
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

The equation <a href="#mjx-eqn-theorem-fundamental-neyman-peason-lemma-01">(theorem-fundamental-neyman-peason-lemma-01)</a> holds.
Now we define constant $\gamma$

$$
    \gamma
    :=
    \begin{cases}
        0
        &
            F(k) = F(k-) = 1 - \alpha
        \\\\
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
    \mathrm{E}\_{0}
    \left[
        \phi
    \right]
    & = &
        P\_{0}(p\_{1} > k p\_{0})
        +
        \gamma
        P\_{0}(p\_{1} = k p\_{0})
    \\\\
    & = &
        1 - F(k)
        +
        \gamma
        (F(k) - F(k-))
    \\\\
    & = &
        \begin{cases}
            1 - (1- \alpha)
            &
                F(k) = F(k-) =  1 - \alpha
            \\\\
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
    \\\\
    & = &
        \alpha
\end{eqnarray}
$$

**proof of (2)**

Let $\phi$ be test.
There exist $k, \gamma \in \mathbb{R}$ such that $\phi$ satisfies that <a href="#mjx-eqn-chap03-03-07">(chap03-03-07)</a> and <a href="#mjx-eqn-chap03-03-08">(chap03-03-08)</a>.
For all test $\phi^{\prime}: \mathcal{X} \rightarrow [0, 1]$ at level $\alpha$, from <a href="#mjx-eqn-chap03-03-08">(chap03-03-08)</a>,

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
    \int\_{\mathcal{X}}
        (\phi - \phi^{\prime})
        p\_{1}
    \ \mu(x)
    & \ge &
        k
        \int\_{\mathcal{X}}
            (\phi - \phi^{\prime})
            p\_{0}
        \ \mu(x)
    \\\\
    & = &
        k
        \mathrm{E}\_{0}
        \left[
            \phi
        \right]
        -
        k
        \mathrm{E}\_{0}
        \left[
            \phi^{\prime}
        \right]
    \\\\
    & = &
        k
        \left(
            \alpha
            -
            \mathrm{E}\_{0}
            \left[
                \phi^{\prime}
            \right]
        \right)
    \ge 0
    \quad
    (\because \phi^{\prime} \text{ is test at level } \alpha)
\end{eqnarray}
$$

Therefore

$$
    \mathrm{E}\_{1}
    \left[
        \phi
    \right]
    \ge
    \mathrm{E}\_{1}
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
    \mathrm{E}\_{1}
    \left[
        \phi^{\prime}
    \right]
    \ge
    \mathrm{E}\_{1}
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
    \\\\
    & = &
        \left(
            \begin{array}{c}
                n \\\\
                x
            \end{array}
        \right)
        \theta^{x}
        (1 - \theta)^{n - x}
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
* $\mathcal{P} := \\\{P_{\theta} \\\}_{\theta \in \Theta}$,
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

### Definition monotone likelihood ratio (MLR)
* $T: \mathcal{X} \rightarrow \mathbb{R}_{\ge 0}$
    * measurable function

$$
    \mathcal{X}\_{\theta\_{1}, \theta\_{2}}
    :=
    \mathcal{X}
    \setminus
    \\\{x \mid p\_{\theta\_{1}}(x) = p\_{\theta\_{2}}(x) = 0\\\}
    \quad
    (\theta\_{1}, \theta\_{2} \in \Theta)
$$

$\mathcal{P}$ is said to be monotone likelihood ration with respect to $T$ if

$$
\begin{eqnarray}
    \forall \theta\_{1}, \theta\_{2} \in \Theta,
    \
    \theta\_{1} < \theta\_{2},
    \
    \exists H\_{\theta\_{1}, \theta\_{2}}:T(\mathcal{X}) \rightarrow [0, \infty]
    \text{ s.t. }
    & &
        H \text{ is non-decreasing},
    \\\\
    & &
        \forall x \in
        \mathcal{X}\_{\theta\_{1}, \theta\_{2}}
        ,
        \
        \frac{p\_{\theta\_{2}}}{p\_{\theta\_{1}}}(x)
        =
        H\_{\theta\_{1}, \theta\_{2}}(T(x))
\end{eqnarray}
$$

We assume $c/0 = \infty$ for $c > 0$.

<div class="end-of-statement" style="text-align: right">■</div>

### Example5
* $\Theta \subseteq \mathbb{R}$,
* $\mathcal{P} := \\\{P_{\theta} \\\}_{\theta \in \Theta}$,
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
* $\mathcal{P} := \\\{P_{\theta}\\\}_{\theta \in \Theta}$,
    * monotone likelihood ratio in statistics $T$
* $\\\{\theta \mid \theta > \theta_{0}\\\} \neq \emptyset$,
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
            \\\\
            \gamma
            &
                (T(x) = c)
            \\\\
            0
            &
                (T(x) < c)
        \end{cases}
    \\\\
    & = &
        1_{\\\{x \mid T(x) >c\\\}}(x)
        +
        \gamma
        1_{\\\{x \mid T(x) =c\\\}}(x)
        \tag{chap03-03-22-test}
\end{eqnarray}
$$

If $\mathrm{E}\_{\theta\_{0}} \left[ \phi\_{0} \right] > 0$, then $\phi\_{0}$ is the most powerful test at level $\alpha^{\prime} := \mathrm{E}\_{\theta\_{0}}[\phi\_{0}]$ for hypothesis test

$$
\begin{equation}
    \Theta\_{H}
    :=
    \\\{\_\theta \mid \theta \le \theta\_{0}\\\},
    \
    \Theta\_{K}
    :=
    \\\{\_\theta \mid \theta > \theta\_{0}\\\},
    \tag{chap03-03-23-hypothesis-test}
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
    \phi_{0}: \ \text{ (chap03-03-22-test)}
    \text{ is the most powerful test at level } \alpha
$$

### proof
(a)

Let $\Phi(\Theta_{H}, \Theta_{K}, \alpha^{\prime})$ be a set of tests for $\Theta_{H}$ and $\Theta_{K}$ at level $\alpha^{\prime}$.
We need to show

$$
\begin{equation}
    \forall \phi \in \Phi(\Theta\_{H}, \Theta\_{K}, \alpha^{\prime}),
    \
    \theta\_{1} \in \Theta\_{K},
    \
    \mathrm{E}\_{\theta\_{1}}[\phi\_{0}]
    \ge
    \mathrm{E}\_{\theta\_{1}}[\phi]
    \tag{chap03-monotone-likehood-ratio-ump-test}
\end{equation}
$$

and

$$
\begin{equation}
    \sup\_{\theta \in \Theta\_{H}}
        \mathrm{E}\_{\theta}
        \left[
            \phi\_{0}
        \right]
    \le
    \alpha^{\prime}
    \tag{chap03-monotone-likehood-ratio-level-alpha-test}
\end{equation}
    .
$$

We first show <a href="#mjx-eqn-chap03-monotone-likehood-ratio-ump-test">(chap03-monotone-likehood-ratio-ump-test)</a>.
Let $\theta_{1} \in \Theta_{K}$ be fixed and

$$
    k
    :=
    \inf
    \left\\\{
        \frac{p\_{\theta\_{1}}(x)}{p\_{\theta\_{0}}(x)}
        \mid
        x \in \mathcal{X}\_{\theta\_{1}, \theta\_{2}},
        \
        T(x) \ge c
    \right\\\}
    .
$$

Then $k \in \mathbb{R}_{\ge 0}$.
Indeed,

$$
\begin{eqnarray}
    \mu(
        \\\{
            x \in \mathcal{X}\_{\theta\_{0}, \theta\_{1}}
            \mid
            p\_{\theta\_{0}}(x)
            \neq
            0,
            \
            T(x) \ge c
        \\\}
    )
    & = &
        \mu(
            \\\{
                x \in \mathcal{X}\_{\theta\_{0}, \theta\_{1}}
                \mid
                T(x) \ge c
            \\\}
        )
    \\\\
    & > &
        0
\end{eqnarray}
$$

since

$$
    \int\_{\mathcal{X}\_{\theta\_{0}, \theta\_{1}}}
        1\_{\\\{T \ge c\\\}}(x)
        p\_{\theta\_{0}}(x)
    \ \mu(dx)
    =
    P\_{\theta\_{0}}(T \ge c)
    \ge
    \mathrm{E}\_{\theta\_{0}}[\phi\_{0}]
    >
    0
    .
$$

Morever $p_{\theta_{1}} < \infty \ \mu \text{-a.e.}$ by definition.
Therefore $k < \infty$.

Now we show that 

$$
\begin{eqnarray}
    x \in \mathcal{X}\_{\theta\_{0}, \theta\_{1}},
    \
    p\_{\theta\_{1}}(x)
    >
    kp\_{\theta\_{0}}(x),
    & \Rightarrow &
        \phi\_{0}(x) = 1
    \nonumber
    \\
    x \in \mathcal{X}\_{\theta\_{0}, \theta\_{1}},
    \
    p\_{\theta\_{1}}(x)
    <
    kp\_{\theta\_{0}}(x),
    & \Rightarrow &
        \phi\_{0}(x) = 0
        \tag{chap03-03-24}
    .
\end{eqnarray}
$$

Let $x \in \mathcal{X}\_{\theta\_{0}, \theta\_{1}}$ be fixed.
Suppose that $p\_{\theta\_{1}}(x)/p\_{\theta\_{0}}(x) > k$.
To show $\phi(x) = 1$, it is sufficient to see $T(x) > c$.
By definition of $k$, there exists $x^{\prime} \in \mathcal{X}\_{\theta\_{0}, \theta\_{1}}$ such that

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
    \\\\
    & \le &
        H_{\theta_{0}, \theta_{1}}(c)
    \\\\
    & \le &
        H(T(x^{\prime}))
    \\\\
    & \le &
        \frac{
            p_{\theta_{1}}(x^{\prime})
        }{
            p_{\theta_{0}}(x^{\prime})
        }
\end{eqnarray}
$$

This is contradiction so that $\phi(x) = 1$.
Suppose that $p_{\theta_{1}}(x)/p_{\theta_{0}}(x) < k$.
If $T(x) \ge c$, $k$ cannot be infimum.
Hence $T(x) < c$.

From <a href="#theorem3-neyman-peasons-fundamental-lemma">theorem</a> and <a href="#mjx-eqn-chap03-03-24">(chap03-03-24)</a>, test $\phi\_{0}$ is the most powerful test of hypothesis test $\Theta\_{H}^{\prime} := \\\{\theta\_{0}\\\}$ and $\Theta\_{K}^{\prime} := \\\{\theta\_{1}\\\}$ at level $\alpha^{\prime} := \mathrm{E}\_{\theta\_{0}}[\phi\_{0}]$.

Let $\phi$ be test for $\Theta_{H}$ and $\Theta_{K}$ at level $\alpha^{\prime}$.
Then $\phi$ is also test for $\Theta_{H}^{\prime}$ and $\Theta_{K}^{\prime}$ at level $\alpha^{\prime}$.
Hence

$$
\begin{equation}
    \mathrm{E}\_{\theta\_{1}}
    \left[
        \phi\_{0}
    \right]
    \ge
    \mathrm{E}\_{\theta\_{1}}
    \left[
        \phi
    \right]
    \tag{chap03-03-26}
\end{equation}
    .
$$

$\theta_{1}$ is arbitrary fixed so that <a href="#mjx-eqn-chap03-03-26">(chap03-03-26)</a> holds for all $\theta_{1} \in \Theta_{K}$.

Now we show that <a href="#mjx-eqn-chap03-monotone-likehood-ratio-level-alpha-test">(chap03-monotone-likehood-ratio-level-alpha-test)</a>.
It suffices to show that

$$
    \forall \theta\_{2} < \theta\_{0},
    \
    \mathrm{E}\_{\theta\_{2}}
    \left[
        \phi\_{0}
    \right]
    \le
    \alpha^{\prime}
$$

With out loss of generality, $\mathrm{E}\_{\theta\_{2}}[\phi\_{0}] > 0$.
Indeed, if $\mathrm{E}\_{\theta\_{2}}[\phi\_{0}] = 0$, the equation always holds  since $0 \le \alpha^{\prime}$.
Let $\theta_{2} < \theta_{0}$ be fixed.
From discussion above, $\phi\_{0}$ is the most powerful test at level $\alpha^{\prime\prime} := \mathrm{E}\_{\theta\_{2}}[\phi\_{0}]$ for hypothesis $\Theta\_{H}^{\prime\prime} := \{\theta\_{2}\}$ and alternatives $\Theta\_{K}^{\prime\prime} := \{\theta\_{0} \}$ by substituting $\theta\_{2}$ for $\theta\_{0}$ and $\theta\_{0}$ for $\theta\_{1}$, respectively.
Since $\alpha^{\prime\prime}$ is one of tests at level $\alpha^{\prime\prime}$ for hypothesis $\Theta\_{H}^{\prime\prime}$ and alternatives $\Theta\_{K}^{\prime\prime}$, we have

$$
\begin{eqnarray}
    &  &
        \mathrm{E}\_{\theta\_{0}}[\alpha^{\prime\prime}]
        \le
        \mathrm{E}\_{\theta\_{0}}[\phi\_{0}]
    \\\\
    & \Leftrightarrow &
        \alpha^{\prime\prime}
        \le
        \mathrm{E}\_{\theta\_{0}}[\phi\_{0}]
    \\\\
    & \Leftrightarrow &
        \mathrm{E}\_{\theta\_{2}}[\phi\_{0}]
        \le
        \mathrm{E}\_{\theta\_{0}}[\phi\_{0}]
        =
        \alpha^{\prime}
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
        \\\\
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

Then $\phi\_{0}$ defined in <a href="#mjx-eqn-chap03-03-22-test">(chap03-03-22-test)</a> is the most powerful test at level $\alpha := \mathrm{E}\_{\theta\_{0}}[\phi\_{0}]$ for hypothesis $\Theta_{H}$ and alternative $\Theta_{K}$ by (a).

<div class="end-of-statement" style="text-align: right">■</div>

## Generalized Neyman Peason's lemma

### Theorem7 Generalized neyman pearson fundamental lemma
* $(\mathcal{X}, \mathcal{A})$,
    * measurable sp.
* $\mu: \Omega \rightarrow [0, \infty)$,
    * $\sigma$-finite measure over $(\mathcal{X}, \mathcal{A})$
* $\Phi := \\\{\phi \mid \phi: \mathcal{X} \rightarrow [0, 1]: \text{ measurable function}\\\}$,
* $f_{1}, \ldots, f_{m}, g \in L^{1}(\mathcal{X}, \mathcal{A}, \mu)$,

$$
    c := (c\_{1}, \ldots, c\_{m})
    \in
    \mathbb{R}^{m},
    \
    \Phi\_{c}
    :=
    \left\\\{
        \phi \in \Phi
        \mid
        \int_{\mathcal{X}}
            \phi(x) f\_{i}(x)
        \ \mu(dx)
        =
        c\_{i},
        (i = 1, \ldots, m)
    \right\\\}
    \neq
    \emptyset
    .
$$

Then

(a) Let $\phi_{0} \in \Phi_{c}$.
If there eixist $k_{1}, \ldots, k_{m} \in \mathbb{R}$ such that

$$
\begin{equation}
    \phi\_{0}(x)
    =
    \begin{cases}
        1
        &
            (g(x) > \sum\_{i=1}^{m}k\_{i}f\_{i}(x))
        \\\\
        0
        &
            (g(x) < \sum\_{i=1}^{m}k\_{i}f\_{i}(x))
    \end{cases}
    \
    \mu \text{-a.e.}
    \tag{chap03-03-27-test}
    ,
\end{equation}
$$

then

$$
    \int\_{\mathcal{X}}
        \phi\_{0}(x) g(x)
    \ \mu(dx)
    =
    \sup
    \left\\\{
        \int\_{\mathcal{X}}
            \phi(x) g(x)
        \ \mu(dx)
        \mid
        \phi \in \Phi\_{c}
    \right\\\}
    .
$$

(b) Let $\phi_{0} \in \Phi_{c}$.
If there exists $k\_{1}, \ldots, k\_{m} \in \mathbb{R}\_{\ge 0}$ such that <a href="#mjx-eqn-chap03-03-27-test">(chap03-03-27-test)</a> is satisfied, then

$$
    \int\_{\mathcal{X}}
        \phi\_{0}(x) g(x)
    \ \mu(dx)
    =
    \sup
    \left\\\{
        \int\_{\mathcal{X}}
            \phi(x) g(x)
        \ \mu(dx)
        \mid
        \phi \in \Phi,
        \
        \int\_{\mathcal{X}}
            \phi(x) f\_{i}(x)
        \ \mu(dx)
        \le
        c\_{i}
        (i = 1, \ldots, m)
    \right\\\}
$$

### proof
(a)

Since $\phi_{0} \in \Phi_{c}$,

$$
\begin{eqnarray}
    \int\_{\mathcal{X}}
        \phi\_{0}(x) g(x)
    \ \mu(dx)
    -
    \sum\_{i=1}^{m}
        k\_{i}c\_{i}
    & = &
        \int\_{\mathcal{X}}
            \phi\_{0}(x)
            g(x)
        \ \mu(dx)
                -
        \int\_{\mathcal{X}}
                \sum\_{j=1}
                    k\_{i}f\_{i}(x)
        \ \mu(dx)
    \\\\
    & = &
        \int\_{\mathcal{X}}
            \phi\_{0}(x)
            \left(
                g(x)
                -
                \sum\_{j=1}
                    k\_{i}f\_{i}(x)
            \right)
        \ \mu(dx)
\end{eqnarray}
$$

On the other hand, for all $\phi \in \Phi_{c}$

$$
\begin{eqnarray}
    \int\_{\mathcal{X}}
        \phi(x) g(x)
    \ \mu(dx)
    -
    \sum\_{i=1}^{m}
        k\_{i}c\_{i}
    & = &
        \int\_{\mathcal{X}}
            \phi(x)
                g(x)
        \ \mu(dx)
                -
        \int\_{\mathcal{X}}
                \sum\_{j=1}
                    k\_{i}f\_{i}(x)
        \ \mu(dx)
    \\\\
    & = &
        \int\_{\mathcal{X}}
            \phi(x)
            \left(
                g(x)
                -
                \sum\_{j=1}
                    k\_{i}f\_{i}(x)
            \right)
        \ \mu(dx)
    .
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
    \left\\\{
        \phi \in \Phi
        \mid
        \int\_{\mathcal{X}}
            \phi(x)f\_{i}(x)
        \ \mu(dx),
        \le
        c\_{i}
        \
        (i = 1, \ldots, m)
    \right\\\}
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
    \\\\
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
    \\\\
    & = &
        \int_{g(x) > \sum_{j=1}^{m}k_{i}f_{i}(x)}
            (1 - \phi(x))
            \left(
                g(x)
                -
                \sum_{j=1} k_{i}f_{i}(x)
            \right)
        \ \mu(dx)
    \\\\
    & \ge &
        0
    .
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
* $\beta_{\phi}: \Theta \rightarrow [0, 1]$,
    * continuous

Then $\phi$ is similar to $\Theta^{\prime}$.

### proof
Let $\theta \in \Theta^{\prime}$ and $\epsilon > 0$ be fixed.
Since $\beta_{\phi}$ is continuous,

$$
    \exists \theta\_{0} \in \Theta\_{0},
    \
    \exists \theta\_{1} \in \Theta\_{1},
    \
    \text{ s.t. }
    \
    |
        \mathrm{E}\_{\theta\_{i}}
        \left[
            \phi
        \right]
        -
        \mathrm{E}\_{\theta^{\prime}}
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
        \mathrm{E}\_{\theta^{\prime}}
        \left[
            \phi
        \right]
    \right|
    & \le &
        \left|
            \mathrm{E}\_{\theta^{\prime}}
            \left[
                \phi
            \right]
            -
            \mathrm{E}\_{\theta\_{0}}
            \left[
                \phi
            \right]
        \right|
        +
        \left|
            \mathrm{E}\_{\theta\_{0}}
            \left[
                \phi
            \right]
        \right|
    \\\\
    & \le &
        \epsilon
        +
        \alpha
\end{eqnarray}
$$


$$
\begin{eqnarray}
    \left|
        \mathrm{E}\_{\theta^{\prime}}
        \left[
            \phi
        \right]
    \right|
    & \ge &
        -
        \left|
            \mathrm{E}\_{\theta^{\prime}}
            \left[
                \phi
            \right]
            -
            \mathrm{E}\_{\theta\_{1}}
            \left[
                \phi
            \right]
        \right|
        +
        \left|
            \mathrm{E}\_{\theta\_{1}}
            \left[
                \phi
            \right]
        \right|
    \\\\
    & \ge &
        -
        \epsilon
        +
        \alpha
\end{eqnarray}
$$

Since $\epsilon$ is arbitrary, $\beta_{\phi}(\theta^{\prime}) = \alpha$.
<div class="end-of-statement" style="text-align: right">■</div>

### Proposition11
* $\Theta^{\prime} \neq \emptyset \subset \Theta$

$$
    \Phi\_{\alpha}^{\prime}
    :=
    \\\{
        \phi \in \Phi
        \mid
        \mathrm{E}\_{\theta}
        \left[
            \phi
        \right]
        =
        \alpha
        \
        (\theta \in \Theta^{\prime})
    \\\}
$$

* $\phi_{0} \in \Phi_{\alpha}^{\prime}$,

If $\phi_{0}$ satisfies

$$
\begin{eqnarray}
    \forall \theta \in \Theta\_{0},
    \
    \forall \phi \in \Phi\_{\alpha}^{\prime},
    \
    \mathrm{E}\_{\theta}
    \left[
        \phi\_{0}
    \right]
    & \le &
        \mathrm{E}\_{\theta}
        \left[
            \phi
        \right]
    \\\\
    \forall \theta \in \Theta\_{1},
    \
    \forall \phi \in \Phi\_{\alpha}^{\prime},
    \
    \mathrm{E}\_{\theta}
    \left[
        \phi\_{0}
    \right]
    & \ge &
        \mathrm{E}\_{\theta}
        \left[
            \phi
        \right]
\end{eqnarray}
$$

then, $\phi_{0}$ is a unbiased test at level $\alpha$ for hypothesis $\Theta_{0}$ and alternative $\Theta_{1}$.

### proof
Since $\phi \equiv \alpha \in \Phi_{\alpha}^{\prime}$ and assumptions of $\phi_{0}$, we obtain

$$
    \forall \theta \in \Theta\_{0},
    \
    \mathrm{E}\_{\theta}
    \left[
        \phi\_{0}
    \right]
    \le
    \alpha
    .
$$

Hence $\phi_{0}$ is test at level $\alpha$.
Similarly, we obtain

$$
    \forall \theta \in \Theta\_{1},
    \
    \mathrm{E}\_{\theta}
    \left[
        \phi\_{0}
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
* $\\\{P_{\theta}\\\}_{\theta \in \Theta}$,
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
    t^{\*}
    & := &
        (t\_{2}, \ldots, t\_{m}),
        \quad
        (t := (t\_{1}, \ldots, t\_{m}) \in \mathbb{R}^{m})
    \\\\
    \theta^{\*}
    & := &
        (\theta\_{2}, \ldots, \theta\_{m}),
        \quad
        (\theta := (\theta\_{1}, \ldots, \theta\_{m}) \in \Theta)
    \\\\
    \Theta^{\*}
    & := &
        \\\{
            \theta^{\*} \mid \theta \in \Theta
        \\\},
    \\\\
    T^{\*}
    & := &
        (T\_{2}, \ldots, T\_{m})
\end{eqnarray}
$$

### Theorem13 unbiased UMP
* $b \in \mathbb{R}$,
    * given
* $\Theta_{0} := \\\{(b, \theta^{*}) \mid \theta \in \Theta\\\}$,
* $\Theta_{1} := \\\{\theta \mid \theta_{1} \neq b \in \Theta\\\}$,
* $0 < \alpha < 1$,

For test for hypothesis $\Theta_{0}$ and alternatiev $\Theta_{1}$, there exists uniformly most powerful test at level level $\alpha$ such that

$$
    \phi\_{0}(x)
    =
    \begin{cases}
        1
        &
            (T\_{1}(x) < u\_{1}(T^{\*}(x)) \lor T\_{1}(x) > u\_{2}(T^{\*}(x)))
        \\\\
        \gamma\_{1}(T^{\*}(x))
        &
            T\_{1}(x) = u\_{1}(T^{\*}(x))
        \\\\
        \gamma\_{2}(T^{\*}(x))
        &
            T\_{1}(x) = u\_{2}(T^{\*}(x))
        \\\\
        0
        &
            u\_{1}(T^{\*}(x)) < T\_{1}(x) < u\_{2}(T^{\*}(x))
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
    \tag{chap03-03-33}
    .
\end{equation}
$$

$\\\{P_{(b, \theta{\*})}\\\}_{\theta^{\*} \in \Theta^{\*}}$ is an exponential family.


By <a href="#theorem-a-1">theorem in appendix</a>, $T^{\*}$ is sufficient to $\{P\_{(b, \theta^{\*})}\}\_{\theta^{\*} \in \Theta^{\*}}$.
Moreover, since the inner of $\Theta$ is not empty, $T^{\*}$ is complete with respect to $\{P\_{(b, \theta^{\*})}\}\_{\theta^{\*} \in \Theta^{\*}}$ by theorem 3.18.
Then follwoing equation holds

$$
\begin{equation}
    \forall \theta^{\*} \in \Theta^{\*},
    \
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
        \phi
        \mid
        T^{\*}
        =
        \cdot
    \right]
    =
    \alpha
    \quad
    P\_{(b, \theta^{\*})}^{T^{\*}} \text{-a.s.}
    \tag{chap03-theorem-03-33-equation-for-03-34}
\end{equation}
$$

Indeed,

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \int\_{\mathbb{R}^{m-1}}
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            \phi
            \mid
            T^{\*}
            =
            t^{\*}
        \right]
    \ P\_{(b, \theta^{\*})}^{T^{\*}}(d t^{\*})
    & = &
        \int\_{(T^{\*})^{-1}(\mathbb{R}^{m-1})}
            \phi(x)
        \ P\_{(b, \theta^{\*})}(dx)
    \\\\
    & = &
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            \phi
        \right]
    \\\\
    & = &
        \alpha
\end{eqnarray}
$$

Then by completeness of $T^{\*}$ with respect to $\\\{P_{(b, \theta^{\*})}\\\}_{\theta^{\*} \in \Theta^{\*}}$, we obtain the equation <a href="#mjx-eqn-chap03-theorem-03-33-equation-for-03-34">(chap03-theorem-03-33-equation-for-03-34)</a>.
Now we show

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
    \left.
        \phi
    \right|
        T^{\*}
    \right]
    =
    \alpha
    \quad
    P\_{(b, \theta^{\*})} \text{-a.s.}
    \tag{chap03-03-34}
\end{eqnarray}
$$

By using <a href="#mjx-eqn-chap03-theorem-03-33-equation-for-03-34">(chap03-theorem-03-33-equation-for-03-34)</a> and the definition of conditional expectation, we have

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \forall (T^{\*})^{-1}(B) \in \sigma(T^{\*}),
    \
    \int\_{(T^{\*})^{-1}(B)}
        \mathrm{E}\_{(b, \theta^{\*})}
        \left\[
            \phi
            \mid
            T^{\*}
        \right\](x)
    \ P\_{(b, \theta^{\*})}(dx)
    & = &
        \int\_{(T^{\*})^{-1}(B)}
            \phi(x)
        \ P\_{(b, \theta^{\*})}(dx)
    \\\\
    & = &
        \int\_{B}
            \mathrm{E}
            \left[
            \left.
                \phi
            \right|
                T^{\*} = t
            \right]
        \ P\_{(b, \theta^{\*})}^{T^{\*}}(dt)
    \\\\
    & = &
        \int\_{B}
            \alpha
        \ P\_{(b, \theta^{\*})}^{T^{\*}}(dt)
    \\\\
    & = &
        \int\_{(T^{\*})^{-1}(B)}
            \alpha
        \ P\_{(b, \theta^{\*})}(dx)
\end{eqnarray}
$$

Then by the definition of conditional expectation, we obtain <a href="#mjx-eqn-chap03-03-34">(chap03-03-34)</a>.

By proposition 3.17, $\beta_{\phi}(\theta)$ is differentialble with respect to $\theta_{1}$.

$$
\begin{eqnarray}
    \frac{\partial}{\partial \theta\_{1}} 
        \mathrm{E}\_{\theta}
        \left[
            \phi
        \right]
    & = &
        \frac{\partial}{\partial \theta\_{1}} 
        \int\_{\mathcal{X}}
            \phi(x)
            \exp
            \left(
                \sum\_{i=1}^{m}
                    \theta\_{i}T\_{i}(x)
                -
                \psi(\theta)
            \right)
            g(x)
        \ \mu(dx)
    \\\\
    & = &
        \int\_{\mathcal{X}}
            \phi(x)
            \left(
                T\_{1}(x)
                -
                \frac{\partial}{\partial \theta\_{1}} \psi(\theta)
            \right)
            \exp
            \left(
                \sum\_{i=1}^{m}
                    \theta\_{i}T\_{i}(x)
                -
                \psi(\theta)
            \right)
            g(x)
        \ \mu(dx)
    \\\\
    & = &
        \int\_{\mathcal{X}}
            \phi(x)
            T\_{1}(x)
            \exp
            \left(
                \sum\_{i=1}^{m}
                    \theta\_{i}T\_{i}(x)
                -
                \psi(\theta)
            \right)
            g(x)
        \ \mu(dx)
        -
        \int\_{\mathcal{X}}
            \phi(x)
            \frac{\partial}{\partial \theta\_{1}} \psi(\theta)
            \exp
            \left(
                \sum\_{i=1}^{m}
                    \theta\_{i}T\_{i}(x)
                -
                \psi(\theta)
            \right)
            g(x)
        \ \mu(dx)
    \\\\
    & = &
        \mathrm{E}\_{(\theta\_{1}, \theta^{\*})}
        \left[
            \phi
            T\_{1}
        \right]
        -
        \mathrm{E}\_{(\theta\_{1}, \theta^{\*})}
        \left[
            \phi
            \frac{\partial}{\partial \theta\_{1}} \psi(\theta)
        \right]
    .
\end{eqnarray}
$$

$\phi$ is level $\alpha$ unbiased test so that we have

$$
\begin{eqnarray}
    \forall \theta \in \Theta\_{0},
    \
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
        \phi
    \right]
    & \le &
        \alpha
        \quad
        (\because \text{ level } \alpha)
    \\\\
    \forall \theta \in \Theta\_{1},
    \
    \mathrm{E}\_{(\theta\_{1}, \theta^{\*})}
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
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            \phi
            T\_{1}
        \right]
        =
        \frac{\partial}{\partial \theta\_{1}} \psi(b, \theta^{\*})
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            \phi
        \right]
    \\\\
    & \Leftrightarrow &
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            \phi
            T\_{1}
        \right]
        =
        \frac{\partial}{\partial \theta\_{1}} \psi(b, \theta^{\*})
        \alpha
        \quad
        (\because \text{ (chap03-03-33)})
        .
\end{eqnarray}
$$

Since $\phi$ is arbitrary unbiased test at level $\alpha$, we put $\phi \equiv \alpha$.

$$
\begin{eqnarray}
    & &
        \alpha
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            T\_{1}
        \right]
        =
        \frac{\partial}{\partial \theta\_{1}} \psi(b, \theta^{\*})
        \alpha
    \\\\
    & \Leftrightarrow &
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            T\_{1}
        \right]
        =
        \frac{\partial}{\partial \theta\_{1}} \psi(b, \theta^{\*})
    .
\end{eqnarray}
$$

Then for all level $\alpha$ unbiased test $\phi$ we obtain

$$
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
        \phi
        T\_{1}
    \right]
    =
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
        T\_{1}
    \right]
    \alpha
    .
$$

With the same way discussed in <a href="#mjx-eqn-chap03-03-34">(chap03-03-34)</a>, we have

$$
\begin{equation}
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
        T\_{1}\phi
        \mid
        T^{\*} = t
    \right]
    =
    \alpha
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
        T\_{1}
        \mid
        T^{\*} = t
    \right]
    \quad
    P\_{(b, \theta^{\*})}^{T^{\*}} \text{-a.s.}
    \tag{chap03-theorem-03-33-equation-for-03-35}
\end{equation}
$$

Indeed,

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \int\_{\mathbb{R}^{m-1}}
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
        \left.
            T\_{1}\phi
        \right|
            T^{\*} = t
        \right]
    \ P\_{(b, \theta^{\*})}^{T^{\*}}(dt)
    & = &
        \int\_{(T^{\*})^{-1}(\mathbb{R}^{m-1})}
            T\_{1}(x)\phi(x)
        \ P\_{(b, \theta^{\*})}(dt)
    \\\\
    & = &
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            T\_{1}
        \right]
        \alpha
    .
\end{eqnarray}
$$

Since $T^{\*}$ is completewith respect to $\\\{P_{(b, \theta^{\*})}\\\}_{\theta \in \Theta^{\*}}$, we obtain <a href="#mjx-eqn-chap03-theorem-03-33-equation-for-03-35">(chap03-theorem-03-33-equation-for-03-35)</a>
Now we show

$$
\begin{equation}
    \forall \theta \in \Theta,
    \
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
        T\_{1}\phi
        \mid
        T^{\*}
    \right]
    =
    \alpha
    \mathrm{E}\_{(b, \theta^{\*})}
    \left[
        T\_{1}
        \mid
        T^{\*}
    \right]
    \quad
    P\_{(b, \theta^{\*})} \text{-a.s.}
    \tag{chap03-03-35}
\end{equation}
$$

Indeed,

$$
\begin{eqnarray}
    \forall \theta \in \Theta,
    \
    \forall (T^{\*})^{-1}(B) \in \sigma(T^{\*}),
    \
    \int\_{(T^{\*})^{-1}(B)}
        \mathrm{E}\_{(b, \theta^{\*})}
        \left[
            T\_{1}\phi
            \mid
            T^{\*}
        \right]
    \ P\_{(b, \theta^{\*})}(d x)
    & = &
        \int\_{(T^{\*})^{-1}(B)}
            T\_{1}\phi
        \ P\_{(b, \theta^{\*})}(d x)
    \\\\
    & = &
        \int\_{B}
            \mathrm{E}\_{(b, \theta^{\*})}
            \left[
                T\_{1}\phi
                \mid
                T^{\*} = t
            \right]
        \ P\_{(b, \theta^{\*})}^{T^{\*}}(d t)
    \\\\
    & = &
        \int\_{B}
            \alpha
            \mathrm{E}\_{(b, \theta^{\*}}
            \left[
                T\_{1}
            \right]
        \ P\_{(b, \theta^{\*})}^{T^{\*}}(d t)
    \\\\
    & = &
        \int\_{(T^{\*})^{-1}(B)}
            \alpha
            \mathrm{E}\_{(b, \theta^{\*}}
            \left[
                T\_{1}
            \right]
        \ P\_{(b, \theta^{\*})}(d x)
\end{eqnarray}
$$

Then by the definition of conditional expectation, we obtain <a href="#mjx-eqn-chap03-03-35">(chap03-03-35)</a>.

Let $\vartheta_{0} := (b, b^{\*}) \in \Theta_{0}$, $\vartheta_{1} := (\theta_{1}, \theta^{\*}) \in \Theta_{1}$ and $t^{\*} \in \mathbb{R}^{m - 1}$ be fixed.
We denote

$$
\begin{eqnarray}
    \Phi
    & := &
        \left\\\{
            f: \mathbb{R}^{m} \rightarrow [0, 1]
            \mid
            f: \text{ measurable}
        \right\\\}
    \\\\
    \int\_{\mathbb{R}}
        f(t\_{1}, t^{\*})
    \ P\_{(b, b^{\*})}(t^{\*}, dt)
    & = &
        \alpha
    \tag{chap03-theorem-03-33-condition-01}
    \\\\
    \int\_{\mathbb{R}}
        t f(t\_{1}, t^{\*})
    \ P\_{(b, b^{\*})}(t^{\*}, dt)
    & = &
        \int\_{\mathbb{R}}
            \alpha t
        \ P\_{(b, b^{\*})}(t^{\*}, dt)
    \tag{chap03-theorem-03-33-condition-02}
    \\\\
    \Phi\_{\alpha}^{\vartheta\_{0} \vartheta\_{1}, t^{\*}}
    & := &
        \left\\\{
            f \in \Phi
            \mid
            f: \text{satisfies (chap03-theorem-03-33-condition-01) and (chap03-theorem-03-33-condition-02)}
        \right\\\}
    \tag{chap03-theorem-03-33-set-of-functions}
\end{eqnarray}
$$

We can reduce problem to find $\bar{f} \in \Phi\_{\alpha}^{\vartheta\_{0} \vartheta\_{1}, t^{*}}$ such that

$$
\begin{eqnarray}
    \forall f \in \Phi\_{\alpha}^{\vartheta\_{0} \vartheta\_{1}, t^{\*}},
    \
    \int\_{\mathbb{R}}
        f(t\_{1}, t^{\*})
    \ P\_{\vartheta\_{1}}(t^{\*}, dt)
    & \le &
        \int\_{\mathbb{R}}
            \bar{f}(t\_{1}, t^{\*})
        \ P\_{\vartheta\_{1}}(t^{\*}, dt)
    .
    \tag{chap03-theorem-03-33-ump-condition}
\end{eqnarray}
$$

Indeed, suppose that there exists such $\bar{f}$.
Since the above equation holds for all $\vartheta_{1} \in \Theta_{1}$ and $t^{*} \in \mathbb{R}^{m-1}$, we have

$$
\begin{eqnarray}
    & &
        \int\_{\mathbb{R}^{m-1}}
            \int\_{\mathbb{R}}
                f(t\_{1}, t^{\*})
            \ P\_{\theta}(t^{\*}, dt)
        \ P\_{\theta}^{T^{\*}}(d t^{\*})
    & \le &
        \int\_{\mathbb{R}^{m-1}}
            \int\_{\mathbb{R}}
                \bar{f}(t\_{1}, t^{\*})
            \ P\_{\theta}(t^{\*}, dt)
        \ P\_{\theta}^{T^{\*}}(d t^{\*})
    \\\\
    & \Leftrightarrow &
        \int\_{\mathbb{R}^{m}}
            f(t)
        \ P\_{\theta}^{T}(d t)
    & \le &
        \int\_{\mathbb{R}^{m}}
            \bar{f}(t)
        \ P\_{\theta}^{T}(d t)
    \\\\
    & \Leftrightarrow &
        \int\_{\mathbb{R}^{m}}
            f(T(x))
        \ P\_{\theta}(d x)
    & \le &
        \int\_{\mathbb{R}^{m}}
            \bar{f}(T(x))
        \ P\_{\theta}(d x)
    .
\end{eqnarray}
$$

Hence $\bar{f} \circ T$ is the UMP test.
Moreover, Since $f \equiv \alpha \in \Phi\_{\alpha}^{\vartheta\_{0}\vartheta\_{1},t^{\*}}$, $\bar{f} \circ T$ is unbiased test.
By <a href="#mjx-eqn-chap03-theorem-03-33-condition-02">(chap03-theorem-03-33-condition-02)</a>, we have

$$
\begin{eqnarray}
    & &
        \int\_{\mathbb{R}^{m}}
            \bar{f}(T(x))
        \ P\_{(b, b^{\*})}(d x)
    & \le &
        \alpha
    .
\end{eqnarray}
$$

Hence $\bar{f} \circ T$ is unbiased UMP at level $\alpha$.

Now we will show the existence of $\bar{f}$.
Let $\vartheta\_{0} := (b, b^{\*}) \in \Theta\_{0}, \vartheta\_{1} := (\theta\_{1}, \theta^{\*}) \in \Theta\_{1}$ be fixed.
From proposition 3.19 by taking $m\_{1} = 1$, $m\_{2} = m - 1$, there exists $\sigma$-finite measure $\mu\_{t^{\*}}$ such that

$$
\begin{eqnarray}
    \vartheta
    :=
    \vartheta\_{0},
    \
    \vartheta\_{1},
    \
    N\_{\vartheta}
    & := &
        \left\\\{
            t\_{m\_{1}+1:m}
            \in
            \mathbb{R}^{m\_{2}}
            \mid
            \int\_{\mathbb{R}^{m\_{1}}}
                \exp
                \left(
                    \langle \vartheta\_{1:m\_{1}}, t\_{1:m\_{1}} \rangle
                \right)
            \ \mu\_{\vartheta^{\*}}(d t\_{1:m\_{1}})
            =
            0
            \text{ or }
            \infty
        \right\\\}
    \\\\
    P\_{\vartheta\_{1:m}}^{T^{\*}}(N\_{\vartheta})
    & = &
        0
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
    \vartheta\_{0},
    \
    \vartheta\_{1},
    \
    \forall t^{\*} \in N^{c},
    \
    P\_{\vartheta}(t^{\*}, d t\_{1})
    & = &
        \frac{
            \displaystyle
            \exp
            \left(
                \langle
                    \vartheta\_{1}, t\_{1}
                \rangle
            \right)
            \nu\_{t^{\*}}(dt\_{1})
        }{
            K\_{\vartheta}
        }
    \\\\
    K\_{\vartheta}
    & := &
        \displaystyle
        \int\_{\mathbb{R}^{m\_{1}}}
            \exp
            \left(
                \langle
                    \vartheta\_{1}, \tau\_{1}
                \rangle
            \right)
        \nu\_{t^{\*}}(d\tau\_{1})
\end{eqnarray}
$$

By taking

* $\mu := P_{\vartheta_{1}}(t^{*}, \cdot)$,
* $g(t_{1}) := e^{(\theta_{1} - b)t_{1}} K_{\vartheta_{0}}/K_{\vartheta_{1}}$,
* $f_{1}(t_{1}) = 1$,
* $f_{2}(t_{1}) = t_{1}$,
* $c_{1} := \alpha$
* and $c_{2} := \alpha \int_{\mathbb{R}} t_{1} P_{\vartheta_{0}}(t^{*}, dt_{1})$,

$\Phi_{(c_{1}, c_{2})}$ in generalized Neyman-Peason's lemma equals to <a href="#mjx-eqn-chap03_theorem_03_33_set_of_functions">(chap03_theorem_03_33_set_of_functions)</a>.

$$
\begin{eqnarray}
    \int\_{\mathbb{R}}
        g(t)
        \bar{f}(t\_{1}, t^{\*})
    \ \mu(dx)
    & = &
        \int\_{\mathbb{R}}
            \frac{
                K\_{\vartheta\_{0}}
            }{
                K\_{\vartheta\_{1}}
            }
            e^{(\theta\_{1} - b)t\_{1}}
            \bar{f}(t\_{1}, t^{\*})
            \frac{
                e^{bt\_{1}}
            }{
                K\_{\vartheta\_{0}}
            }
        \ \mu\_{t^{\*}}(d t\_{1})
    \\\\
    & = &
        \int\_{\mathbb{R}}
            e^{\theta\_{1}t\_{1}}
            \bar{f}(t\_{1}, t^{\*})
            \frac{
                1
            }{
                K\_{\vartheta\_{1}}
            }
        \ \mu\_{t^{\*}}(d t\_{1})
    \\\\
    & = &
        \int\_{\mathbb{R}}
            \bar{f}(t\_{1}, t^{\*})
        \ P\_{\vartheta\_{1}}(t^{\*}, dt\_{1})
\end{eqnarray}
$$

Now we construct $\bar{f} \in \Phi\_{\alpha}^{\vartheta\_{0}, \vartheta\_{1}, t^{*}}$.
Let

$$
\begin{eqnarray}
    F^{t^{\*}}(z)
    & := &
        \int\_{(-\infty, z]}
        \ P\_{\vartheta\_{0}}(t^{\*}, dt\_{1})
    \\\\
    U\_{1}^{t^{\*}}(p)
    & := &
        \inf
        \\\{
            z \in \mathbb{R}
            \mid
            F^{t^{\*}}(z)
            \ge
            p
        \\\}
    \\\\
    U\_{2}^{t^{\*}}(p)
    & := &
        \inf
        \\\{
            z \in \mathbb{R}
            \mid
            F^{t^{\*}}(z)
            \ge
            1 - \alpha + p
        \\\}
    \\\\
    \Gamma\_{1}^{t^{\*}}(p)
    & := &
        (p - F^{t^{\*}}(U\_{1}^{t^{\*}}(p)-))
        (F^{t^{\*}}(U\_{1}^{t^{\*}}(p)) -  F^{t^{\*}}(U\_{1}^{t^{\*}}(p)-))^{-}
    \\\\
    \Gamma\_{2}^{t^{\*}}(p)
    & := &
        (F^{t^{\*}}(U\_{2}^{t^{\*}}(p)) - (1 - \alpha) - p)
        (F^{t^{\*}}(U\_{2}^{t^{\*}}(p)) -  F^{t^{\*}}(U\_{2}^{t^{\*}}(p)-))^{-}
    \\\\
    \Psi^{t^{\*}}(t\_{1}, p)
    & := &
        1\_{(-\infty, U\_{1}^{t^{\*}}(p))}(t)
        +
        \Gamma\_{1}^{t^{\*}}(p)
        1\_{U\_{1}^{t^{\*}}(p)}(t)
        +
        \Gamma\_{2}^{t^{\*}}(p)
        1\_{U\_{2}^{t^{\*}}(p)}(t)
        +
        1\_{(U\_{2}^{t^{\*}}(p)), \infty)}(t)
    \\\\
    S^{t^{\*}}(p)
    & := &
        \int\_{\mathbb{R}}
            t
            \Psi^{t^{\*}}(t\_{1}, p)
        \ P\_{\vartheta\_{0}}(t^{\*}, dt\_{1})
\end{eqnarray}
$$

where $x^{-}$ is zero if $x=0$ otherwise $x^{-1}$.
Now we show that

$$
    \exists p^{t^{\*}} \in [0, \alpha],
    \
    \text{ s.t. }
    \
    S^{t^{\*}}(p^{t^{\*}})
    =
    \alpha
    \int\_{\mathbb{R}}
        t\_{1}
    \ P\_{(b, b^{\*})}(dt\_{1}, t^{\*})
    .
$$

It is enough to show that 

* $S^{t^{*}}$ is continuous in $[0, p]$,
* If $p = 0$,

$$
    S^{t^{\*}}(0)
    >
    \alpha
    \int\_{\mathbb{R}}
        t\_{1}
    \ P\_{(b, b^{\*})}(dt\_{1}, t^{\*})
    ,
$$

* If $p = \alpha$,

$$
    S^{t^{\*}}(0)
    <
    \alpha
    \int\_{\mathbb{R}}
        t\_{1}
    \ P\_{(b, b^{\*})}(dt\_{1}, t^{\*})
    .
$$

Then by intermediate value theorem, we obtain $p^{t^{*}}$.
Now we define

$$
    \bar{p}^{t^{\*}}
    :=
    \inf
    \{
        p \in [0, \alpha]
        \mid
        S^{t^{\*}}(p)
        =
        \alpha
        \int_{\mathbb{R}}
            t_{1}
        \ P_{(b, b^{\*})}(dt_{1}, t^{\*})
    \}
    .
$$

Finally, we constract $\bar{f}$ by

$$
    \bar{f}(t_{1}, t^{\*})
    :=
    \Psi^{t^{\*}}(t_{1}, p^{t^{\*}})
    .
$$

$\bar{f}$ satisfies <a href="#mjx-eqn-chap03-theorem-03-33-condition-01">(chap03-theorem-03-33-condition-01)</a>;

$$
\begin{eqnarray}
    \int_{\mathbb{R}}
        \bar{f}(t_{1}, t^{\*})
    \ P_{\vartheta_{0}}(t^{\*}, d t_{1})
    & = &
        \alpha
\end{eqnarray}
$$

Moreover, $\bar{f}$ satisfies <a href="#mjx-eqn-chap03-theorem-03-33-condition-02">(chap03-theorem-03-33-condition-02)</a> by right continuity of $\Psi$ with respect to $p$, that is,

$$
\begin{eqnarray}
    \int\_{\mathbb{R}}
        t
        \bar{f}(t\_{1}, t^{\*})
    \ P\_{\vartheta\_{0}}(t^{\*}, d t\_{1})
    & = &
        \alpha
        \int\_{\mathbb{R}}
            t
        \ P\_{\vartheta\_{0}}(t^{\*}, d t\_{1})
\end{eqnarray}
$$

By generalized Neyman-Peason's lemma, the following equation holds

$$
\begin{eqnarray}
    \int\_{\mathbb{R}}
        \bar{f}(t\_{1}, t^{\*})
        g(t\_{1})
    \ P\_{\vartheta\_{0}}(t^{\*}, dt\_{1})
    & = &
        \int\_{\mathbb{R}}
            \bar{f}(t\_{1}, t^{\*})
            g(t\_{1})
        \ P\_{\vartheta\_{1}}(t^{\*}, dt\_{1})
    \\\\
    & = &
        \sup
        \left\\\{
            \int\_{\mathbb{R}}
                f(t\_{1}, t^{\*})
                g(t\_{1})
            \ P\_{\vartheta\_{0}}(t^{\*}, dt\_{1})
            =
            \int\_{\mathbb{R}}
                f(t\_{1}, t^{\*})
            \ P\_{\vartheta\_{1}}(t^{\*}, dt\_{1})
            \mid
            f \in \Psi\_{\alpha}^{\vartheta\_{0}, \vartheta\_{1}, t^{\*}}
        \right\\\}
\end{eqnarray}
$$

This implies that <a href="#mjx-eqn-chap03_theorem_03_33_ump_condition">(chap03_theorem_03_33_ump_condition)</a> holds.

<div class="QED" style="text-align: right">$\Box$</div>


## Appendix

### Theorem A-1
* $(\mathcal{X}, \mathcal{A})$,
    * measurable space
* $\mathcal{P} := \\\{ P_{\theta}\\\}_{\theta \in \Theta}$,
    * probability measure over $(\mathcal{X}, \mathcal{A})$,
* $k \in \mathbb{N}$,
* $(\mathcal{X}^{(i)}, \mathcal{A}^{(i)})$,
    * measurable space for $i = 1, \ldots, k$
* $\mathcal{P}^{(i)} := \\\{P_{\theta}^{(i)}\\\}_{\theta \in \Theta}$,
    * probability measure over $(\mathcal{X}^{(i)}, \mathcal{A}^{(i)})$ for $i = 1, \ldots, k$

The following statements hold:

* (a) If $\mathcal{P}$ is an exponential family, $\forall P_{\theta}, P_{\theta^{\prime}} \in \mathcal{P}$, $P_{\theta} \ll P_{\theta^{\prime}}$, $P_{\theta} \ll P_{\theta^{\prime}}$,
* (b) If for all $i = 1, \ldots, n$, $\mathcal{P}^{(i)}$ is exponential family, then $\\\{\prod_{i=1}^{n} P_{\theta}^{(i)}\\\}$ is an exponential family over $( \prod_{i=1}^{n} \mathcal{X}^{(i)}, \prod_{i=1}^{n} \mathcal{A}^{(i)})$.
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
