---
title: Beatty Sequence
---

## Beatty Sequence
Let $r \in \mathbb{R} \setminus \mathbb{Q}$ be a irrational number satisfying $r > 1$.

$$
    B_{r}
    :=
    (\lfloor nr \rfloor)_{n \in \mathbb{N}}
    .
$$

Let $s := r / (r - 1)$.

$$
\begin{eqnarray}
    \frac{1}{r}
    +
    \frac{1}{s}
    & = &
        \frac{1}{r}
        +
        \frac{r - 1}{r}
    \nonumber
    \\
    & = &
        1
    .
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    \frac{r}{s}
    & = &
        r - 1
    .
    \nonumber
\end{eqnarray}
$$

## Theorem
- $r > 1$
    - a irrational number
- $s := r / (r - 1)$,

For all $n \in \mathbb{N}$, either $n \in B_{r}$ or $n \in B_{s}$.

## proof1
Let $j \in \mathbb{N}$.

Suppose that there exist $k, m \in \mathbb{N}$ such that

$$
    j
    = \lfloor k r \rfloor 
    = \lfloor m s \rfloor 
    .
$$

$$
\begin{eqnarray}
    & &
        j \le k r < j + 1,
    \nonumber
    \\
    & \Leftrightarrow &
        \frac{j}{r}
        \le k <
        \frac{j + 1}{r}
    \nonumber
    \\
    & &
        j \le m s < j + 1,
    \nonumber
    \\
    & \Leftrightarrow &
        \frac{j}{s}
        \le m <
        \frac{j + 1}{s}
    \nonumber
\end{eqnarray}
$$

$$
\begin{eqnarray}
    & &
        \frac{j}{r}
        +
        \frac{j}{s}
        \le
        k + m
        <
        \frac{j + 1}{r}
        +
        \frac{j + 1}{s}
    \nonumber
    & \Leftrightarrow &
        j
        \le
        k + m
        <
        j + 1
    .
    \nonumber
\end{eqnarray}
$$

Since $k, m \in \mathbb{N}$, this doesn't hold.
Thus, $j$ doesn't belong to both sequences at the same time.

Now we will show $j \in \mathbb{N}$ belongs to one of the sequences.
Suppose that $j$ doesn't belongs to both of the sequence.

$$
    \forall k, m \in \mathbb{N},
    \
    j \neq \lfloor kr \rfloor,
    \
    j \neq \lfloor ms \rfloor.
$$

Thus,

$$
\begin{eqnarray}
    & &
        \forall k, m \in \mathbb{N},
        \
        kr \notin [j , j + 1),
        \
        ms \notin [j , j + 1).
    \nonumber
    \\
    & \Rightarrow &
        \forall k, m \in \mathbb{N},
        \
        kr \notin [j , j + 1),
        \
        ms \notin [j , j + 1).
    \nonumber
    \\
    & \Rightarrow &
        \forall k, m \in \mathbb{N},
        \
        k \notin [\frac{j}{r} , \frac{j+1}{r}),
        \
        m \notin [\frac{j}{s} , \frac{j+1}{s}),
    \nonumber
    \\
    & \Rightarrow &
        \forall k, m \in \mathbb{N},
        \
        k + m \notin [\frac{j}{r} + \frac{j}{s} , \frac{j+1}{r} + \frac{j+1}{s}),
    \nonumber
    \\
    & \Rightarrow &
        \forall k, m \in \mathbb{N},
        \
        k + m \notin [j, j + 1),
    \nonumber
    .
\end{eqnarray}
$$

If $j > 1$, this does not hold.
Let us assume $j = 1$.
If $r \in (1, 2]$, $\lfloor r \rfloor = 1 = j$.
If $r \in (2, \infty)$, 

$$
    s
    =
    \frac{ r }{ r - 1 }
    =
    \frac{ r  - 1 + 1}{ r - 1 }
    =
    1 + \frac{ 1 }{ r - 1 }
    \in
    (1, 2]
    .
$$

This implies $\lfloor s \rfloor = 1 = j$.
Therefore, $j$ belongs to one of the sequences.

## proof2

We claim that for all $i, j \in \mathbb{N}$

$$
    \frac{
        j
    }{
        r
    }
    \neq
    \frac{i}{s}
    .
$$

Indeed, if there are such $i, j$,

$$
\begin{eqnarray}
    \frac{j}{i}
    & = &
        \frac{r}{s}
    \nonumber
    \\
    & = &
        (r - 1)
    .
\end{eqnarray}
$$

However, $r - 1$ is irrational.

Suppose that there are 
Let $j \in \mathbb{N}$.

$$
\begin{eqnarray}
    j + \lfloor js/r \rfloor 
    & = &
        j + \lfloor j (s - 1) \rfloor 
    \nonumber
    \\
    & = &
        \lfloor js \rfloor 
    .
    \nonumber
\end{eqnarray}
$$




<div class="QED" style="text-align: right">$\Box$</div>

## Reference
- https://en.wikipedia.org/wiki/Beatty_sequence
