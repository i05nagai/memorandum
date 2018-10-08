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
        \frac{1}{x_{t, I_{t}}}
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
            \sum_{j=1}^{n}
                y_{t + 1, j}
        }
    \nonumber
\end{eqnarray}
$$


**Step5.** End for

**Step6.** Return $x_{T + 1}$,

<div class="end-of-statement" style="text-align: right">■</div>

#### Theorem 6.2
* $\mathcal{L} := [0, 1]^{n}$,
* $\epsilon > 0$,
* $x_{1} := (1/n, \ldots, 1/n)$,
* $y_{1} := (1, \ldots, 1)$,
* $\ell_{1}, \ldots, \ell_{T} \in \mathcal{L}$,
* $I_{t}$,
    * categorical distribution with probability $x_{t}$,
    * it's independent with respect to $t$,

$$
\begin{eqnarray}
    \hat{\ell}_{t, i}
    & := &
        \begin{cases}
            \frac{1}{x_{t, I_{t}}}
            \ell_{t, I_{t}}
            &
                i = I_{t}
            \\
            0
            &
                \text{otherwise},
        \end{cases}
    \nonumber
    \\
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
            \sum_{j=1}^{n}
                y_{t + 1, j}
        }
        \in \Delta_{n}
    \nonumber
\end{eqnarray}
$$

Then

$$
    \mathrm{E}
    \left[
        \sum_{t=1}^{T}
            \ell_{t, I_{t}}
        -
        \min_{I \in \mathcal{I}}
            \sum_{t=1}^{T}
                \ell_{t, I_{t}}
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
First of all, we have

$$
\begin{eqnarray}
    \mathrm{E}
    \left[
        \ell_{t, I_{t}}
    \right]
    & = &
        \sum_{j=1}^{n}
            \ell_{t, j}
            x_{t, j}
    \nonumber
\end{eqnarray}
    .
$$

Thus, $\ell_{t} \in \mathcal{L}$,

$$
\begin{eqnarray}
    i^{*} \in \{1, \ldots, n\},
    \
    \mathrm{E}
    \left[
        \min_{I \in \mathcal{I}}
            \sum_{t=1}^{T}
                \ell_{t, I_{t}}
    \right]
    & = &
        \sum_{t=1}^{T}
            \ell_{t, i^{*}}
    \nonumber
\end{eqnarray}
    .
$$

Thus, what we need to prove is 

$$
    \sum_{t=1}^{T}
        \ell_{t, j}^{\mathrm{T}}
        x_{t}
        -
        \sum_{t=1}^{T}
            \ell_{t, i^{*}}
    \le
    2
    \sqrt{
        T
        n
        \log n
    }
    .
$$

Now we will prove the following result with a similar discussion in Theorem 1.5.

$$
    \sum_{t=1}^{T}
        \hat{\ell}_{t}^{\mathrm{T}}
        x_{t}
    -
    \sum_{t=1}^{T}
        \hat{\ell}_{t, k}
    \le
    \frac{
        \log n
    }{
        \epsilon
    }
    +
    \epsilon
    \sum_{t=1}^{T}
        \sum_{i=1}^{n}
            x_{t, i}
            (\hat{\ell}_{t, i})^{2}
    .
$$

Let

$$
\begin{eqnarray}
    \Phi_{t + 1}
    & := &
        \sum_{i=1}^{n}
            y_{t, i}
    .
    \nonumber
\end{eqnarray}
$$

We have

$$
\begin{eqnarray}
    \Phi_{t + 1}
    & = &
        \sum_{i=1}^{n}
            y_{t, i}
            \exp
            \left(
                - \epsilon
                \hat{\ell}_{t, i}
            \right)
    \nonumber
    \\
    & = &
        \Phi_{t}
        \frac{1}{
            \sum_{j=1}^{n}
                y_{t, j}
        }
        \sum_{i=1}^{n}
            y_{t, i}
            \exp
            \left(
                - \epsilon
                \hat{\ell}_{t, i}
            \right)
    \nonumber
    \\
    & = &
        \Phi_{t}
        \sum_{i=1}^{n}
            x_{t, i}
            \exp
            \left(
                - \epsilon
                \hat{\ell}_{t, i}
            \right)
    \nonumber
    \\
    & \le &
        \Phi_{t}
        \sum_{i=1}^{n}
            x_{t, i}
            \left(
                1
                -
                \epsilon
                \hat{\ell}_{t, i}
                +
                \epsilon^{2}
                (\hat{\ell}_{t, i})^{2}
            \right)
        \quad
        (\because x \ge 0, e^{-x} \le 1 - x + x^{2})
    \nonumber
    \\
    & = &
        \Phi_{t}
        \left(
            1
            -
            \epsilon
            \hat{\ell}_{t}^{\mathrm{T}}
            x_{t}
            +
            \epsilon^{2}
            \sum_{i=1}^{n}
                x_{t, i}
                (\hat{\ell}_{t, i})^{2}
        \right)
    \nonumber
    \\
    & \le &
        \Phi_{t}
        \exp
        \left(
            -
            \epsilon
            \hat{\ell}_{t}^{\mathrm{T}}
            x_{t}
            +
            \epsilon^{2}
            \sum_{i=1}^{n}
                x_{t, i}
                (\hat{\ell}_{t, i})^{2}
        \right)
        \quad
        (\because 1 + x \le e^{x})
    .
\end{eqnarray}
$$

On the other hand, for $$ k = \{1, \ldots, n\}$$,

$$
\begin{eqnarray}
    y_{T, k}
    & \le &
        \Phi_{T}
    \nonumber
    \\
    & \le &
        \Phi_{1}
        \prod_{t=1}^{T}
        \exp
        \left(
            -
            \epsilon
            \hat{\ell}_{t}^{\mathrm{T}}
            x_{t}
            +
            \epsilon^{2}
            \sum_{i=1}^{n}
                x_{t, i}
                (\hat{\ell}_{t, i})^{2}
        \right)
    \nonumber
    \\
    & = &
        n
        \exp
        \left(
            -
            \epsilon
            \sum_{t=1}^{T}
                \hat{\ell}_{t}^{\mathrm{T}}
                x_{t}
            +
            \epsilon^{2}
            \sum_{t=1}^{T}
                \sum_{i=1}^{n}
                    x_{t, i}
                    (\hat{\ell}_{t, i})^{2}
        \right)
    \nonumber
\end{eqnarray}
$$

Taking the logarithm of both sides we get

$$
\begin{eqnarray}
    & &
        -\epsilon
        \sum_{t=1}^{T}
            \hat{\ell}_{t, k}
        \le
        \log n
        -
        \epsilon
        \sum_{t=1}^{T}
            \hat{\ell}_{t}^{\mathrm{T}}
            x_{t}
        +
        \epsilon^{2}
        \sum_{t=1}^{T}
            \sum_{i=1}^{n}
                x_{t, i}
                (\hat{\ell}_{t, i})^{2}
    \nonumber
    \\
    & \Leftrightarrow &
        -
        \sum_{t=1}^{T}
            \hat{\ell}_{t, k}
        \le
        \frac{
            \log n
        }{
            \epsilon
        }
        -
        \sum_{t=1}^{T}
            \hat{\ell}_{t}^{\mathrm{T}}
            x_{t}
        +
        \epsilon
        \sum_{t=1}^{T}
            \sum_{i=1}^{n}
                x_{t, i}
                (\hat{\ell}_{t, i})^{2}
    .
    \nonumber
\end{eqnarray}
$$

By taking both side of equations

$$
\begin{eqnarray}
    & &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                \hat{\ell}_{t}^{\mathrm{T}}
                x_{t}
            -
            \sum_{t=1}^{T}
                \hat{\ell}_{t, k}
        \right]
        \le
        \frac{
            \log n
        }{
            \epsilon
        }
        +
        \mathrm{E}
        \left[
            \epsilon
            \sum_{t=1}^{T}
                \sum_{i=1}^{n}
                    x_{t, i}
                    (\hat{\ell}_{t, i})^{2}
        \right]
    \nonumber
    \\
    & \Leftrightarrow &
        \mathrm{E}
        \left[
            \sum_{t=1}^{T}
                \ell_{t, I_{t}}
            -
            \sum_{t=1}^{T}
                \ell_{t, I_{t}}
                \frac{1}{x_{t, I_{t}}}
                1_{\{I_{t}=k\}}
        \right]
        \le
        \frac{
            \log n
        }{
            \epsilon
        }
        +
        \mathrm{E}
        \left[
            \epsilon
            \sum_{t=1}^{T}
                (\ell_{t, I_{t}})^{2}
                \frac{1}{x_{t, I_{t}}}
        \right]
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{t=1}^{T}
        \sum_{i=1}^{n}
            \ell_{t, i}
            x_{t, i}
            -
        \sum_{t=1}^{T}
            \ell_{t, k}
            \frac{1}{x_{t, k}}
            x_{t, k}
        \le
        \frac{
            \log n
        }{
            \epsilon
        }
        +
        \epsilon
        \sum_{t=1}^{T}
        \sum_{i=1}^{n}
                (\ell_{t, i})^{2}
                \frac{1}{x_{t, i}}
                x_{t, i}
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{t=1}^{T}
        \sum_{i=1}^{n}
            \ell_{t, i}
            x_{t, i}
            -
        \sum_{t=1}^{T}
            \ell_{t, k}
        \le
        \frac{
            \log n
        }{
            \epsilon
        }
        +
        \epsilon
        \sum_{t=1}^{T}
        \sum_{i=1}^{n}
            (\ell_{t, i})^{2}
    \nonumber
\end{eqnarray}
$$

Since $\ell_{t} \in \mathcal{L}$,

$$
\begin{eqnarray}
    \sum_{t=1}^{T}
    \sum_{i=1}^{n}
        \ell_{t, i}
        x_{t, i}
        -
    \sum_{t=1}^{T}
        \ell_{t, k}
    & \le &
        \frac{
            \log n
        }{
            \epsilon
        }
        +
        \epsilon
        \sum_{t=1}^{T}
        \sum_{i=1}^{n}
            (\ell_{t, i})^{2}
    \nonumber
    \\
    & \le &
        \frac{
            \log n
        }{
            \epsilon
        }
        +
        \epsilon
        nT
    \nonumber
    \\
    & \le &
        \frac{
            \log n
        }{
            \sqrt{
                \frac{
                    \log n
                }{
                    T n
                }
            }
        }
        +
        \sqrt{
            \frac{
                \log n
            }{
                T n
            }
        }
        nT
    \nonumber
    \\
    & \le &
        2
        \sqrt{
            nT
            \log n
        }
    \nonumber
\end{eqnarray}
$$

<div class="QED" style="text-align: right">$\Box$</div>

TODO: We use similar discussion in Theorem 1.5.
The discussion could be generalized.

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
By Theorem 6.2.

<div class="QED" style="text-align: right">$\Box$</div>

## 6.3 A reduction from limited information to full information

### 6.3.1 Part 1: using unbiased estimators
The key ideaa behind many of the efficient algorithms for bandit convex optimization is the following

* Altough we cannot calculate the gradient of cost function $f$ explicitly, it is possible to estimate the value of gradient,

In this seciton, we design a online convex problem from given first oder OCO algorithm.

#### Definition 6.1 first order OCO Algorithm


<div class="end-of-statement" style="text-align: right">■</div>

#### Algorithm 19 Reduction to bandit feedback
* $\mathcal{K} \subseteq \mathbb{R}^{n}$,
    * convex set
    * $D$-bounded
* $\mathcal{A}$,
    * a first order OCO algorithm
* $x_{1} := \mathcal{A}_{0}$,
    * the inital value of the algorith $\mathcal{A}$,
* $\theta$,
    * parameters of the algorithm
* $F$,
    * distribution funciton
* $Y_{t}$
    * $\mathcal{K}$-valued r.v. whose distribution function is $F$,
    * independent with respect to $t$,
    * $$\mathrm{E}[Y_{t}] = x_{t}$$,
* $G_{t}$
    * $\mathbb{R}^{n}$-valued r.v.
    * independent with respect to $t$,
    * $$\mathrm{E}[G_{t}] = \nabla f_{t}(x_{t})$$,

**Step1.** For $t=1$ to $T$ do

**Step2.** Observe $Y_{t}$

**Step3.** Play $Y_{t}$

**Step4.** Observe $f_{t}(Y_{t})$

**Step5.** Observe $G_{t}$

**Step6.** Let

$$
    x_{t + 1}
    :=
    \mathcal{A}(f_{1}, \ldots, f_{n}, g_{1}, \ldots, g_{t}; \theta)
    .
$$

**Step7.** end for

**Step8.** Return $x_{T + 1}$.

<div class="end-of-statement" style="text-align: right">■</div>

#### Lemma 6.3
* $u \in \mathcal{K}$,
* $f_{1}, \ldots, f_{T}:\mathcal{K} \rightarrow \mathbb{R}$,
* $G_{1}, \ldots, G_{T}$,
    * $G_{t}$: $\sigma(x_{t})$-measurable
* $x_{1} := \mathcal{A}_{0} \in \mathcal{K}$,
    * initial point


$$
    
$$

## Reference
