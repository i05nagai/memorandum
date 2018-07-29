---
title: A Dynamic Near Optimal Algorithm for Online Linear Programming
---

## A Dynamic Near Optimal Algorithm for Online Linear Programming



#### Linear Programming

* $$I := \{1, \ldots, M\}$$,
    * the number of advertisements
* $$J := \{1, \ldots, N\}$$,
    * queries/impression
* $$\pi_{j} \ (j \in J)$$,
    * $\pi_{j} \ge 0$,
* $$a_{i,j} \in [0, 1]$$,
* $$a_{j} := (a_{1,j}, \ldots, a_{M, j}) \ (j \in J)$$,
* $$b_{i} \ (i \in I)$$,
    * budget for ad $i$


$$
\begin{align}
    \max_{(x_{1}, \ldots, x_{N})}
    & & &
        \sum_{j \in J}
            \pi_{j}
            x_{j}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \sum_{j \in J}
            a_{i,j}
            x_{j}
        \le
        b_{i}
        \quad
        (\forall i \in I)
    \nonumber
    \\
    & & &
        x_{j}
        \in
        [0, 1]
        \quad
        (\forall j \in J)
\end{align}
$$

<div class="end-of-statement" style="text-align: right">■</div>

#### Corresponding Online Linear Programming

We define the constraints at $t$, denoted by (C-t), as follows

$$
\begin{align}
    & & &
        \sum_{j = 1}^{t}
            a_{i, j}
            x_{j}
        \le
        b_{i}
        \quad
        (\forall i \in I)
    \nonumber
    \\
    & & &
        x_{t}
        \in
        [0, 1]
        \quad
        (\forall j \in J)
        \tag{C-t}
    .
\end{align}
$$

Online Linear Programming maximizes

$$
    \sum_{j=1}^{N}
        x_{j}
        \pi_{j}
$$

through these steps

* Step 1. $t \leftarrow 1$,
* Step 2. Choose $x_{t}$ satisfying the constraints at $t$ (C-t),
* Step 3. $t \leftarrow t + 1$,
* Step 4. Go to Step2 if $t < M$,

<div class="end-of-statement" style="text-align: right">■</div>

The worst-case analysis is very common to evaluate the performance of an online algorithm.
In this paper, they introduce the some assumptions to the worst-case (alghough it's not the worst anymore) and analyze the performance of online algorithms in the assumptions.

## Reference
