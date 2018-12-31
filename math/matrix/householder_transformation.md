---
title: Householder Transformation
---

## Householder Transformation


#### Definition 1 Householder matrix
* $v \in \mathbb{R}^{n}$,
    * $v \neq 0$,

$$
\begin{eqnarray}
    P_{v}
    & := &
        I
        -
        \frac{2}{v^{\mathrm{T}}v}
        v v ^{\mathrm{T}}
    \nonumber
    \\
    & = &
        I
        -
        \frac{2}{\norm{v}^{2}}
        v v ^{\mathrm{T}}
    \nonumber
    \\
    & = &
        I
        -
        2
        \bar{v} \bar{v}^{\mathrm{T}}
    \nonumber
    \\
    \bar{v}
    & := &
        \frac{v}{\norm{v}}
    \nonumber
\end{eqnarray}
$$

$P_{v}$ is called a Householder reflection, Householder matrix, or Householder transformation.
The $v$ is called a Householder vector.

<div class="end-of-statement" style="text-align: right">■</div>

#### Remark
$P_{v}$ is a projection onto the hyperplane $\mathrm{span}{v}^{\perp}$.

$$
\begin{eqnarray}
    P_{v}x
    & = &
        x
        -
        \frac{2}{\norm{v}^{2}}
        v v^{\mathrm{T}}
        x
    \nonumber
    \\
    & = &
        x
        -
        \frac{
            2 (v^{\mathrm{T}} x)
        }{
            \norm{v}^{2}
        }
        v
    \nonumber
    \\
    & = &
        x
        -
        2
        \langle \bar{x}, x \rangle
        \bar{v}
\end{eqnarray}
$$

$\langle \bar{v}, x \rangle$ is the length of the projected vector obtained by projecting $x$ onto $\bar{v}$.
$\langle \bar{v}, x \rangle \bar{v}$ is a projection of $x$ onto $v$.

Suppose that $Px \in \mathrm{span}(e_{1})$ where $$(e_{i})_{i=1,\ldots,n}$$ is a standard basis.
Since

$$
    Px - x
    =
    2
    \langle \bar{x}, x \rangle
    \bar{v},
$$

$v \in \mathrm{span}(x, e_{1})$.
Conversely, setting $v := x + \alpha e_{1}$ gives

$$
\begin{eqnarray}
    v^{\mathrm{T}}x
    & = &
        x^{\mathrm{T}}x
        +
        \alpha x^{1}
    \nonumber
    \\
    v^{\mathrm{T}}v
    & = &
        v^{\mathrm{T}}
        \left(
            x
            +
            \alpha
            e_{1}
        \right)
    \nonumber
    \\
    & = &
        v^{\mathrm{T}}
        x
        +
        \alpha
        v^{\mathrm{T}}
        e_{1}
    \nonumber
    \\
     & = &
        x^{\mathrm{T}}x
        +
        \alpha x^{1}
        +
        x^{1}
        \alpha
        +
        \alpha^{2}
    \nonumber
    \\
     & = &
        x^{\mathrm{T}}x
        +
        2
        \alpha x^{1}
        +
        \alpha^{2}
    \nonumber
\end{eqnarray}
$$

where $x = (x^{1}, \ldots, x^{n})^{\mathrm{T}}$.
Therefore,

$$
\begin{eqnarray}
    Px
    & = &
        x
        -
        2
        \frac{
            x^{\mathrm{T}}x + \alpha x^{1}
        }{
            x^{\mathrm{T}}x + 2 \alpha x^{1} + \alpha^{2}
        }
        \left(
            x
            +
            \alpha e_{1}
        \right)
    \nonumber
    \\
    & = &
        x
        \left(
            1
            -
            2
            \frac{
                x^{\mathrm{T}}x + \alpha x^{1}
            }{
                x^{\mathrm{T}}x + 2 \alpha x^{1} + \alpha^{2}
            }
        \right)
        -
        2
        \alpha
        \frac{
            x^{\mathrm{T}}x + \alpha x^{1}
        }{
            x^{\mathrm{T}}x + 2 \alpha x^{1} + \alpha^{2}
        }
        e_{1}
    .
    \label{householder_reflection_equation_01}
\end{eqnarray}
$$

In order that the coefficient of $x$ is zero, we set $\alpha = \pm \norm{x}_{2}$.

$$
\begin{eqnarray}
    v^{\mathrm{T}}x
    & = &
        \norm{x}_{2}^{2}
        \pm
        \norm{x}_{2} x^{1}
    \nonumber
    \\
    v^{\mathrm{T}}v
    & = &
        \norm{x}_{2}^{2}
        \pm
        2
        \norm{x}_{2} x^{1}
        +
        \norm{x}_{2}^{2}
    \nonumber
    \\
    & = &
        2
        \norm{x}_{2}^{2}
        \pm
        2
        \norm{x}_{2} x^{1}
    \nonumber
    .
\end{eqnarray}
$$

Form $$\eqref{householder_reflection_equation_01}$$,

$$
\begin{eqnarray}
    Px
    & = &
        x
        \left(
            1
            -
            2
            \frac{
                \norm{x}_{2}^{2}
                \pm
                \norm{x}_{2}x^{1}
            }{
                2
                \norm{x}_{2}^{2}
                \pm
                2
                \norm{x}_{2}x^{1}
            }
        \right)
        \mp
        2
        \norm{x}_{2}
        \frac{
            \norm{x}_{2}^{2}
            \pm
            \norm{x}_{2}x^{1}
        }{
            2
            \norm{x}_{2}^{2}
            \pm
            2
            \norm{x}_{2}x^{1}
        }
        e_{1}
    \nonumber
    \\
    & = &
        \mp
        \norm{x}_{2}
        e_{1}
    .
    \nonumber
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

There are various algorithms to compute a householder $v$ for given $x$ such that $$P_{v}x = \norm{x}_{2} e_{1}$$ and $P = I - \beta v v^{\mathrm{T}}$ is orthogonal where $\beta := 2 / v^{\mathrm{T}}v$.
Here we describe one of the algorithms.
For the reason that $$\alpha = - \norm{x}_{2}$$ yields the property that $Px$ is positive, we take $\alpha = -\norm{x}_{2}$.
In that case,

$$
    v^{1}
    =
    x^{1}
    -
    \norm{x}_{2}
    .
$$

If $x^{1} \approx \norm{x}$, that is, $x \approx x^{1}e_{1}$, catastrophic cancellation would occur.
To avoid the cancellation, when $x \ge 0$, instead of the above equation we compute the following formula

$$
\begin{eqnarray}
    v^{1}
    & = &
        x^{1}
        -
        \norm{x}_{2}
    \nonumber
    \\
    & = &
        \frac{
            x_{1}^{2}
            -
            \norm{x}_{2}^{2}
        }{
            x^{1} + \norm{x}_{2}
        }
    \nonumber
    \\
    & = &
        \frac{
            -
            (
                (x^{2})^{2}
                +
                \cdots
                +
                (x^{n})^{2}
            )
        }{
            x^{1} + \norm{x}_{2}
        }
    \nonumber
\end{eqnarray}
$$

#### Algorithm 1

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Computing Householder Vector}
    \begin{algorithmic}
    \PROCEDURE{ComputeHouseholderVector}{$x$}
        \STATE $n := \mathrm{length}(x)$
        \STATE $\sigma := (x^{2:n})^{\mathrm{T}}x^{2:n}$
        \COMMENT{$2(n - 1)$ flops}
        \STATE $
            v :=
            \left(
                \begin{array}{c}
                    1
                    \\
                    x^{2:n}
                \end{array}
            \right)
        $,
        \IF{$\sigma = 0$}
            \COMMENT{$x$ is contained in span $e_{1}$}
            \STATE $\beta := 0$
        \ELSE
            \STATE $\mu := \sqrt{(x^{1})^{2} + \sigma}$
            \COMMENT{norm of $x$}
            \IF{ $x^{1} \le 0$ }
                \STATE $v^{1} \leftarrow x^{1} - \mu$
            \ELSE
                \COMMENT{to avoid catastrophic cancellation}
                \STATE $v^{1} \leftarrow -\sigma/(x^{1} + \mu)$
            \ENDIF
            \STATE $\beta := 2 (v^{1})^{2} / (\sigma + (v^{1})^{2})$
            \STATE $v \leftarrow v / v^{1}$
            \COMMENT{$n$ flops}
        \ENDIF
        \RETURN $(v, \beta)$
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

$$
\begin{eqnarray}
    Q
    & := &
        Q_{1} \cdots Q_{r}
    \nonumber
    \\
    Q_{j}
    & := &
        I - \beta_{j} v^{(j)}(v^{(j)})^{\mathrm{T}}
    \nonumber
    \\
    v^{(j)}
    & := &
        (
            \underbrace{0, \ldots, 0,}_{j - 1}
            1,
            v^{j+1,(j)},
            \cdots,
            v^{n,(j)}
        )^{\mathrm{T}}
    \nonumber
    .
\end{eqnarray}
$$

Since the algorithm requires approximately $3n$, and time complexy is $O(n)$.

#### Proposition 1
* $P_{v}$,

(1)

$$
    P_{v}^{\mathrm{T}} = P_{v}
    .
$$

(2)

$$
    P_{v}^{-1} = P_{v}^{\mathrm{T}} = P
    .
$$

(3) $P^{2} = I$.

(4) $P_{v}P_{v^{\prime}}$ is symetric and orthonomal.

#### proof

**proof of (1)**

$$
\begin{eqnarray}
    P_{v}^{\mathrm{T}}
    & = &
        (I - 2 \bar{v}\bar{v}^{\mathrm{T}})^{\mathrm{T}}
    \nonumber
    \\
    & = &
        I
        -
        2 (\bar{v}^{\mathrm{T}}))^{\mathrm{T}}\bar{v}^{\mathrm{T}}
    \nonumber
    \\
    & = &
        I
        -
        2 \bar{v}\bar{v}^{\mathrm{T}}
    \nonumber
\end{eqnarray}
$$

**proof of (2)**

$$
\begin{eqnarray}
    P
    P_{v}^{\mathrm{T}}
    & = &
        (I - 2 \bar{v}\bar{v}^{\mathrm{T}})
        (I - 2 \bar{v}\bar{v}^{\mathrm{T}})
    \nonumber
    \\
    & = &
        I
        -2 \bar{v}\bar{v}^{\mathrm{T}})
        -2 \bar{v}\bar{v}^{\mathrm{T}})
        +
        4
        (\bar{v}\bar{v}^{\mathrm{T}})
        (\bar{v}\bar{v}^{\mathrm{T}})
    \nonumber
    \\
    & = &
        I
        -4 \bar{v}\bar{v}^{\mathrm{T}}
        +
        4
        \bar{v}
        (\bar{v}^{\mathrm{T}} \bar{v})
        \bar{v}^{\mathrm{T}}
    \nonumber
    \\
    & = &
        I
        -4 \bar{v}\bar{v}^{\mathrm{T}}
        +
        4
        \bar{v}
        \bar{v}^{\mathrm{T}}
        \quad
        (\because \norm{\bar{v}} = 1)
    \nonumber
    \\
    & = &
        I
    \nonumber
\end{eqnarray}
$$

**proof of (3)**

$PP^{\mathrm{T}} = P^{2} = I$.

**proof of (4)**

This is from a fact that multiplication of orthonomal matrix is also orthonomal.

<div class="QED" style="text-align: right">$\Box$</div>


## Reference
* [Householder transformation \- Wikipedia](https://en.wikipedia.org/wiki/Householder_transformation)
* [s93\.pdf](http://web.csulb.edu/~tgao/math423/s93.pdf)
