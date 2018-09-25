---
title: Introduction to Online Convex Optimization Chapter06
---

## Introduction to Online Convex Optimization Chapter06

## 6.1 The Bandit Convex Optimization model
The Bandit Convex Optimizaton model is identical to the general OCO model except that we are only available to the value of $f_{t}(x_{t})$ but we cannot access to $f_{t}$.
Thus, we cannot calculate the gradient of $f_{t}(x_{t})$ explicitly.

The definition of the regret is the same as the regret of the OCO model.

$$
    \mathrm{Regret}_{T}
    :=
    \sup_{(f_{1}, \ldots, f_{T}) \subseteq \mathcal{F}}
    \left(
        \sum_{t=1}^{T}
            f_{t}(x_{t})
        -
        \min_{x \in \mathcal{K}}
            \sum_{t=1}^{T}
                f_{t}(x)
    \right)
    .
$$

## 6.2 The Multiu Armed Bandit problem
The term MAB nowadays referes to a multitude of different variants and sub-senarios that are too large to survey.
This section addresses perhaps the simplest variant -- the non-stochastic MAB problem -- which is defined as follows.

#### Definition general OCO algorithm
* $T \in \mathbb{N}$,
* $\mathcal{K} \subseteq \mathbb{R}^{n}$,
    * convex set
* $\mathcal{F}$,
    * real-valued convex functions whose domain is $\mathcal{K}$,
* $f_{1}, \ldots, f_{T} \in \mathcal{F}$,
    * loss functions
* $\Theta$,
    * parameter space
* $\theta \in \Theta$,
    * parameters of algorithm
* $\mathcal{A}_{t}(\cdot; \theta): \mathcal{F}^{t} \rightarrow \mathcal{K}$ $(t = 1, \ldots, T)$,

The function $\mathcal{A}_{t}(\cdot; \theta)$ is called an OCO algorithm with parameter $\theta$.
We define $$x_{t + 1} := \mathcal{A}_{t}(f_{1}, \ldots, f_{t}; \theta) \in \mathcal{K}$$.

<div class="end-of-statement" style="text-align: right">■</div>


#### MAB probelm
* $T$,
* $n$,
    * the number of arms


Step1. For $t=1$ to $T$

Step2. choose $$i_{t} \in \{1, 2, \ldots, n\}$$,

Step3. observe the value of loss $\ell_{t} \in [0, 1]^{n}$,

Step4. end for

The objectives of this problem is the minimize the regret.

<div class="end-of-statement" style="text-align: right">■</div>

#### Algorithm 17 Simple MAB algorithm
* $T \in \mathbb{N}$,
* $\delta > 0$,
* $B_{t}$
    * bernoulli r.v. with probability $\delta$
    * i.i.d.
* $$U_{t} \in \{1, \ldots, n\}$$
    * uniformly distributed
* $$\mathrm{Unif}(\cdot; n)$$,
* $M_{t} \in \{1, \ldots, n\}$,
    * multinomial distribution with probability $x_{t} \in \mathcal{K}$,


**Step1.** for $t=1$ to $T$ do

**Step2.** Draw $B_{t}$,

**Step3.** if $B_{t} = 1$ then

**Step3-1.** Play $$U_{t} \in \{1, \ldots, n\}$$ and observe loss $\ell_{t}$,

**Step3-2.** Let

$$
\begin{eqnarray}
    \hat{\ell}_{t, i}
    & = &
        \begin{cases}
            \frac{n}{\delta} \ell_{t, U_{t}}
            &
                i = U_{t}
            \\
            0
            &
                \text{otherwise}
        \end{cases}
    \nonumber
\end{eqnarray}
$$

**Step3-3.** Let

$$
\begin{eqnarray}
    \hat{f}_{t}(x)
    & := &
        \hat{\ell}_{t}^{\mathrm{T}}
        x
    \nonumber
    \\
    x_{t + 1}
    & := &
        \mathcal{A}(\hat{f}_{1}, \ldots, \hat{f}_{t})
    \nonumber
\end{eqnarray}
$$

**Step4.** else

**Step4-1.** Play $M_{t}$ and observe loss $\ell_{t}$,

**Step4-2.** Update

$$
\begin{eqnarray}
    \hat{f}_{t}
    & = &
        0
        \in \mathbb{R}
    \nonumber
    \\
    \hat{\ell}_{t}
    & = &
        0 \in \mathbb{R}^{n}
    \nonumber
    \\
    x_{t + 1}
    & = &
        \mathcal{A}(\hat{f}_{1}, \ldots, \hat{f}_{t})
    \nonumber
\end{eqnarray}
$$

**Step5.** end if

**Step6.** end for

<div class="end-of-statement" style="text-align: right">■</div>

#### Algorithm 17-2 Simplified Algorithm 17
* $T \in \mathbb{N}$,
* $\delta > 0$,
* $B_{t}$
    * bernoulli r.v. with probability $\delta$
    * i.i.d.


**Step1.** for $t=1$ to $T$ do

**Step2.** Draw $B_{t}$,

**Step3.** Play $$i_{t} \in \{1, \ldots, n\}$$,

$$
\begin{eqnarray}
    \hat{\ell}_{t, i}
    & = &
        \begin{cases}
            \frac{n}{\delta} \ell_{t, U_{t}}
            B_{t}
            &
                i = U_{t}
            \\
            0
            &
                \text{otherwise}
        \end{cases}
    \nonumber
    \\
    \hat{f}_{t}(x)
    & := &
        \hat{\ell}_{t}^{\mathrm{T}}
        x
    \nonumber
    \\
    x_{t + 1}
    & := &
        \mathcal{A}(\hat{f}_{1}, \ldots, \hat{f}_{t})
    \nonumber
\end{eqnarray}
$$

**Step5.** end if

**Step6.** end for

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma

(1)

$$
    \norm{
        \nabla
        \hat{f}(x)
    }
    \le
    \frac{n}{\delta}
$$

(2)

$$
    \mathrm{E}
    \left[
        \norm{
            \nabla
            \hat{f}(x)
        }
    \right]
    \le
    n
$$

#### proof
(1)

$$
\begin{eqnarray}
    \norm{
        \nabla
        \hat{f}_{t}(x)
    }
    & = &
        \norm{
            \hat{\ell}_{t}
        }
    \nonumber
    \\
    & = &
        \frac{n}{\delta}
        \hat{\ell}_{t, U_{t}}
        B_{t}
    \nonumber
    \\
    & \le &
        \frac{n}{\delta}
        \hat{\ell}_{t, U_{t}}
    \nonumber
    \\
    & \le &
        \frac{n}{\delta}
    \nonumber
\end{eqnarray}
$$

(2)

With simlar argument to (1),

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \norm{
            \nabla
            \hat{f}_{t}(x)
        }
    \right]
    & = &
        \mathrm{E}
        \left[
            \frac{n}{\delta}
            \hat{\ell}_{t, U_{t}}
            B_{t}
        \right]
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \frac{1}{\delta}
            \hat{\ell}_{t, i}
        \mathrm{E}
        \left[
            B_{t}
        \right]
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \hat{\ell}_{t, i}
    \nonumber
    \\
    & \le &
        n
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>


#### Lemma 6.1
* ,

In Algorithm 16,

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            \ell_{t, i_{t}}
        -
        \min_{i}
        \sum_{t=1}^{T}
            \ell_{t, i}
    \right]
    & \le &
        O(T^{3/4}\sqrt{n})
    \nonumber
\end{eqnarray}
$$

#### proof
TODO: proof and fix Algorithm 17.

$$
\begin{eqnarray}
    \forall x \in \mathcal{K},
    \
    \mathrm{E}
    \left[
        \hat{f}_{t}(x)
    \right]
    & = &
        \mathrm{E}
        \left[
            \frac{n}{\delta}
            \hat{\ell}_{t}^{\mathrm{T}}
            x
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \frac{n}{\delta}
            \hat{\ell}_{t, U_{t}}^{\mathrm{T}}
            x_{U_{t}}
            B_{t}
        \right]
    \nonumber
    \\
    & = &
        \frac{1}{n}
        \sum_{i=1}^{n}
            \frac{n}{\delta}
            \hat{\ell}_{t, i}^{\mathrm{T}}
            x_{i}
        \mathrm{E}
        \left[
            B_{t}
        \right]
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            \frac{1}{\delta}
            \hat{\ell}_{t, i}^{\mathrm{T}}
            x_{i}
            \delta
    \nonumber
    \\
    & = &
        \hat{\ell}_{t}^{\mathrm{T}}
        x
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        
    \right]
    & = &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                f_{t}(x_{t})
                -
            \min_{x \in \Delta_{n}}
                \sum_{t=1}^{T}
                    f_{t}(x)
        \right]

\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

#### Algorithm 17-3 Modified Algorithm 17
* $T \in \mathbb{N}$,
* $\delta > 0$,
* $I_{t}$,
    * categorical distribution with probability $x_{t}$,

**Step1.** for $t=1$ to $T$ do

**Step2.** Play $I_{t}$ and observe loss $\ell_{t}$

$$
\begin{eqnarray}
    \hat{\ell}_{t, i}
    & = &
        \begin{cases}
            \ell_{t, I_{t}}
            &
                i = I_{t}
            \\
            0
            &
                \text{otherwise}
        \end{cases}
    \nonumber
    \\
    \hat{f}_{t}(x)
    & := &
        \hat{\ell}_{t}^{\mathrm{T}}
        x
    \nonumber
    \\
    x_{t + 1}
    & := &
        \mathcal{A}(\hat{f}_{1}, \ldots, \hat{f}_{t})
    \nonumber
\end{eqnarray}
$$

**Step5.** end if

**Step6.** end for

<div class="end-of-statement" style="text-align: right">■</div>


#### Lemma
In the above Algorithm

#### proof
Let 

$$
    \mathcal{I}
    :=
    \{
        I \sim \mathrm{Categ}(\cdot; x)
        \mid
        x \in \Delta_{n}
    \}
$$

and variables in $\mathcal{I}$ are all independent.
Let $G$ be

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \norm{
            \nabla
            \hat{f}_{t}(x)
        }
    \right]
    & = &
        \mathrm{E}
        \left[
            \norm{
                \ell_{t, I_{t}}
            }
        \right]
    \nonumber
    \\
    & = &
        \mathrm{E}
        \left[
            \ell_{t, I_{t}}
        \right]
    \nonumber
    \\
    & = &
        \ell_{t}^{\mathrm{T}}
        x_{t}
    \nonumber
    \\
    & \le &
        n
        =:
        G
    .
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \norm{
        \nabla
        \mathrm{E}
        \left[
            \hat{f}_{t}(x)
        \right]
    }
    & = &
        \norm{
            \nabla
            \left(
                \ell_{t}^{\mathrm{T}}
                x_{t}
            \right)
        }
    \nonumber
    \\
    & = &
        \norm{
            \ell_{t}
        }
    \nonumber
    \\
    & \le &
        \sqrt{n}
    .
    \nonumber
\end{eqnarray}
$$

$$
    \mathrm{E}
    \left[
        \ell_{t, I_{t}}
    \right]
    \le
    \sum_{i=1}^{n}
        \ell_{t, i}^{\mathrm{T}}
        x_{t}
    .
$$

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \sum_{i=1}^{T}
            \ell_{t, I_{t}}
        -
        \min_{I \in \mathcal{I}}
            \sum_{i=1}^{T}
                \ell_{t, I}
    \right]
    & = &
        \sum_{i=1}^{T}
            \ell_{t}^{\mathrm{T}}
            x_{t}
        -
        \mathrm{E}
        \left[
            \min_{I \in \mathcal{I}}
                \sum_{i=1}^{T}
                    \ell_{t, I}
        \right]
    \nonumber
    \\
    & = &
        \sum_{i=1}^{T}
            f_{t}(x_{t})
        -
        \min_{x \in \Delta_{n}}
            \sum_{i=1}^{T}
                \ell_{t}^{\mathrm{T}}
                x
    \nonumber
    \\
    & \le &
        G
        D
        \sqrt{T}
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

### 6.2.1 EXP3: simultaneous exploration-exploitati


#### Algorithm 18 EXP3 - simple version
* $\epsilon > 0$,
* $x_{1} := (1/n, \ldots, 1/n)$,
* $I_{t}$,
    * categorical distribution with probability $x_{t}$,
    * it's independent with respect to $t$,


**Step1.** For $$t \in \{1, \ldots, T\}$$ do

**Step2.** Play $I_{t}$ and observe loss $\ell_{t} \in [0, 1]^{n}$,

**Step3.** Let

$$
\begin{eqnarray}
    \hat{\ell}_{t, i}
    :=
    \begin{cases}
        \frac{1}{x_{t, I_{t}}
        \ell_{t, I_{t}}
        &
            i = I_{t}
        \\
        0
        &
            \text{otherwise},
    \end{cases}
\end{eqnarray}
$$

**Step4.** Update

$$
\begin{eqnarray}
    i = 1, \ldots, n,
    \
    y_{t + 1, i}
    & := &
        x_{t, i}
        \exp
        \left(
            - \epsilon
            \hat{\ell}_{t, i}
        \right)
    \nonumber
    \\
    x_{t + 1}
    & := &
        \frac{
            y_{t + 1}
        }{
            \norm{
                y_{t + 1}
            }_{1}
        }
    \nonumber
\end{eqnarray}
$$


**Step5.** End for

**Step6.** Return $x_{T + 1}$,

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma 6.2

In Algorithm 18,

$$
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            l_{t, I_{t}}
        -
        \min_{I \in \mathcal{I}}
            \sum_{t=1}^{T}
                l_{t, I_{t}}
    \right]
    \le
    2
    \sqrt{
        T
        n
        \log n
    }
    .
$$

#### proof
Note that

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \hat{\ell}_{t, i}
    \right]
    & = &
        \mathrm{E}
        \left[
            \ell_{t, I_{t}}
            \frac{1}{x_{t, I_{t}}}
            1_{I_{t} = i}
        \right]
    \nonumber
    \\
    & = &
        \sum_{j=1}^{n}
            \ell_{t, j}
            \frac{1}{x_{t, j}}
            1_{j = i}
            x_{j}
    \nonumber
    \\
    & = &
        \sum_{j=1}^{n}
            \ell_{t, i}
    \nonumber
    \\
    \mathrm{E}
    \left[
        \sum_{j=1}^{n}
            x_{t, j}
            (\hat_{\ell}_{t, j})^{2}
    \right]
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

## Reference
