---
title: Givens Rotation
---

## Givens Rotation
* $$[1:n] := \{1, \ldots, n\}$$,

#### Definition 1
* $n$,

Let

$$
\begin{eqnarray}
    G(i, j, c, s; m)
    & := &
        \left(
            \begin{array}{ccccccc}
                1      & \ldots & 0      & \cdots & 0      & \cdots & 0
                \\
                \vdots & \ddots & \vdots &        & \vdots &        & \vdots
                \\
                0      & \cdots & c      & \cdots & s      & \cdots & 0
                \\
                \vdots &        & \vdots & \ddots & \vdots &        & \vdots
                \\
                0      & \cdots & -s     & \cdots & c      & \cdots & 0
                \\
                \vdots &        & \vdots &        & \vdots & \ddots & \vdots
                \\
                0      & \cdots & 0      & \cdots & 0      & \cdots & 1
            \end{array}
        \right)
    \nonumber
    \\
    (G(i, j, c, s; m))_{i}
    & = &
        \left(
            \begin{array}{c}
                0      
                \\
                \vdots
                \\
                c      
                \\
                \vdots
                \\
                -s     
                \\
                \vdots
                \\
                0      
            \end{array}
        \right)
    \nonumber
    \\
    (G(i, j, c, s; m))_{j}
    & = &
        \left(
            \begin{array}{c}
                0
                \\
                \vdots
                \\
                s
                \\
                \vdots
                \\
                c
                \\
                \vdots
                \\
                0
            \end{array}
        \right)
    \nonumber
    \\
    (G(i, j, c, s; m))_{(i, j)}^{(i, j)}
    & = &
        \left(
            \begin{array}{cc}
                c & s \\
                -s & c
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

where $c := \cos(\theta)$, $s := \sin(\theta)$.
$G(i, j, c, s)$ is called Givens rotations.

<div class="end-of-statement" style="text-align: right">■</div>

#### Proposition 2
* $c := \cos(\theta)$
* $s := \sin(\theta)$
* $m \in \mathbb{N}$,
* $1 \ge i \ge j \ge m$,

* (1) $G(i, j, c, s; m)$ is orthonormal.

#### proof

**proof of (1)**

$$
\begin{eqnarray}
    k \notin \{i, j\}
    \
    \text{or}
    \
    l \notin \{i, j\},
    \
    \langle
        g_{k}, g_{l}
    \rangle
    & = &
        \langle
            e_{k}, e_{l}
        \rangle
    \nonumber
    \\
    & = &
        0,
    \nonumber
    \\
    \langle
        g_{i}, g_{j}
    \rangle
    & = &
        c s - cs
    \nonumber
    \\
    & = &
        0
        .
    \nonumber
\end{eqnarray}
$$

and

$$
\begin{eqnarray}
    k \in \{i, j\},
    \
    \norm{g_{k}}_{2}
    & = &
        \sqrt{c^{2} + s^{2}}
    \nonumber
    \\
    & = &
        1
    \nonumber
    \\
    k \notin \{i, j\},
    \
    \norm{g_{k}}_{2}
    & = &
        \norm{e_{k}}_{2}
    \nonumber
    \\
    & = &
        1
    .
    \nonumber
\end{eqnarray}
$$

Thus, $G(i, j, c, s; m)$ is orthonormal.

<div class="QED" style="text-align: right">$\Box$</div>

Let $x := (x^{1}, \ldots, x^{n})^{\mathrm{T}} \in \mathbb{R}^{n}$.

$$
\begin{eqnarray}
    \left(
        G(i, j, c, s; m)^{\mathrm{T}}
        x
    \right)^{l}
    & = &
        \begin{cases}
            c x^{i} - s x^{j}
            &
                l = i
            \\
            s x^{i} + c x^{j}
            &
                l = j
            \\
            x^{l}
            &
        \end{cases}
    \nonumber
\end{eqnarray}
$$

Conversely, to zero $y^{j}$, we need to set 

$$
\begin{eqnarray}
    c
    & = &
        \frac{
            x^{i}
        }{
            \sqrt{
                (x^{i})^{2}
                +
                (x^{j})^{2}
            }
        }
    \nonumber
    \\
    & = &
        \frac{
            1
        }{
            \sqrt{
                1
                +
                (\frac{x^{j}}{x^{i}})^{2}
            }
        }
    \nonumber
    \\
    s
    & = &
        \frac{
            -x^{j}
        }{
            \sqrt{
                (x^{i})^{2}
                +
                (x^{j})^{2}
            }
        }
    \nonumber
    \\
    & = &
        - \frac{x^{j}}{x^{i}}
        \frac{
            1
        }{
            \sqrt{
                1
                +
                (\frac{x^{j}}{x^{i}})^{2}
            }
        }
    \nonumber
\end{eqnarray}
$$

#### Algorithm 2
Given rotations algorithm is to find $s, c$ which satisfy

$$
\begin{eqnarray}
    \left(
        \begin{array}{cc}
            c & s
            \\
            -s & c
        \end{array}
    \right)^{\mathrm{T}}
    \left(
        \begin{array}{c}
            a
            \\
            b
        \end{array}
    \right)
     & = &
        \left(
            \begin{array}{c}
                r
                \\
                0
            \end{array}
        \right)
    .
    \nonumber
\end{eqnarray}
$$

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{ComputeGivensRotation}
    \begin{algorithmic}
    \PROCEDURE{ComputeGivensRotation}{$a, b$}
        \IF{$b = 0$} 
            \STATE $c = 1$
            \STATE $s = 0$
        \ELSE
            \IF{$b > a$}
                \STATE $\tau \leftarrow - a/b$
                \COMMENT{1 division}
                \STATE $s \leftarrow 1/\sqrt{1 + \tau^{2}}$
                \COMMENT{1 addition, 1 multiplication, 1 division}
                \STATE $c \leftarrow s \tau$
                \COMMENT{1 multiplication}
            \ELSE
                \STATE $\tau \leftarrow - b/a$
                \STATE $c \leftarrow 1/\sqrt{1 + \tau^{2}}$
                \STATE $s \leftarrow c \tau$
            \ENDIF
        \ENDIF
        \RETURN $c, s$.
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

The algorithm requires at most 5 flops (2 division, 1 addition and 2 multiplication) and a single square root.

<div class="end-of-statement" style="text-align: right">■</div>

#### Algorithm 3 Applying Givens Rotation
* $A := (a_{j}^{i})_{i \in [1:m], j \in [1:n]} \in \mathbb{R}^{m \times n}$,

This is the algorithm to compute multiplication of Givens rotation and a matrix $A$.

$$
\begin{eqnarray}
    G(i, j, c, s; m)^{\mathrm{T}}
    A
    & = &
        \left(
            \begin{array}{ccc}
                G(i, j, c, s; m)^{\mathrm{T}}
                a_{1},
                &
                \cdots, 
                &
                G(i, j, c, s; m)^{\mathrm{T}}
                a_{n}
            \end{array}
        \right)^{\mathrm{T}}
    \nonumber
\end{eqnarray}
$$

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{MultiplyGivensRotation}
    \begin{algorithmic}
    \REQUIRE $A$: matrix to which Givens rotations is multipled
    \REQUIRE $c$: $\cos \theta$ in Given rotations
    \REQUIRE $s$: $\sin \theta$ in Given rotations
    \PROCEDURE{MultiplyGivensRotation}{$i, j, c, s, A$}
        \FOR{$k = 1$ \TO $n$}
            \STATE $\tau_{1} \leftarrow A_{k}^{i}$
            \STATE $\tau_{2} \leftarrow A_{k}^{j}$
            \STATE $A_{k}^{i} \leftarrow c \tau_{1} - s \tau_{2}$
            \STATE $A_{k}^{j} \leftarrow s \tau_{1} + c \tau_{2}$
        \ENDFOR
        \RETURN $A$.
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

$$
\begin{eqnarray}
    A
    G(i, j, c, s; n)
    & = &
        \left(
            \begin{array}{c}
                a^{1}
                G(i, j, c, s; n)
                \\
                \vdots, 
                \\
                a^{m}
                G(i, j, c, s; n)
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{MultiplyGivensRotation}
    \begin{algorithmic}
    \REQUIRE $A \in \mathbb{R}^{m \times n}$: matrix to which Givens rotations is multipled
    \REQUIRE $c$: $\cos \theta$ in Given rotations
    \REQUIRE $s$: $\sin \theta$ in Given rotations
    \PROCEDURE{MultiplyGivensRotation}{$A, i, j, c, s$}
        \FOR{$k = 1$ \TO $m$}
            \STATE $\tau_{1} \leftarrow A_{i}^{k}$
            \STATE $\tau_{2} \leftarrow A_{j}^{k}$
            \STATE $A_{j}^{k} \leftarrow c \tau_{1} - s \tau_{2}$
            \STATE $A_{j}^{k} \leftarrow s \tau_{1} + c \tau_{2}$
        \ENDFOR
        \RETURN $A$.
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Wallace Givens \- Wikipedia](https://en.wikipedia.org/wiki/Wallace_Givens)
* [Givens rotation \- Wikipedia](https://en.wikipedia.org/wiki/Givens_rotation)
* G. H. Golub and C. F. Van Loan. Matrix Computations. Johns Hopkins University Press, Baltimore, MD, USA, fourth edition, 2012
