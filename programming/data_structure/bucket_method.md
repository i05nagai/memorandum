---
title: Bucket Method
---

## Bucket Method


## Tips

### Size of buckets
* $a,\in \mathbb{N}$,
    * the number of elements to be put into buckets.
* $\lfloor \sqrt{a} \rfloor,\in \mathbb{N}$,
    * the number of elements in a bucket,
* $x \in \mathbb{R}$,

Let be decompose $x$ into integer part $x_{I} \in \mathbb{Z}$ and fractional part $x_{F} \in [0, 1)$.
$x$ is decomposed to

$$
    x
    =
    x_{I}
    +
    x_{F}
    .
$$

The multiplication of real values is written

$$
\begin{eqnarray}
    (x_{I} + x_{F})
    (y_{I} + y_{F})
    & = &
        x_{I}
        y_{I}
        +
        x_{I}
        y_{F}
        +
        x_{F}
        y_{I}
        +
        x_{F}
        y_{F}
    \nonumber
    \\
    & \le &
        x_{I}
        y_{I}
        +
        x_{I}
        y_{F}
        +
        x_{F}
        y_{I}
        +
        1
    \nonumber
    \\
    & \le &
        x_{I}
        y_{I}
        +
        x_{I}
        +
        y_{I}
        +
        1
    \nonumber
\end{eqnarray}
    .
$$

Since $\sqrt{a} \in \mathbb{R}$, $\sqrt{a} = x_{I} + x_{F}$ for some $x \in \mathbb{R}$.
With this notation,

$$
    \lfloor
        \sqrt{a}
    \rfloor
    =
    x_{I}
    .
$$

Since $\sqrt{a} \in \mathbb{R}$, for some $x \in \mathbb{R}, y \in \mathbb{R}$.
The gap between floor of square root and square root is

$$
\begin{eqnarray}
    a
    -
    \lfloor
        \sqrt{a}
    \rfloor
    \lfloor
        \sqrt{a}
    \rfloor
    & = &
        x_{I}
        x_{F}
        +
        x_{F}
        x_{I}
        +
        x_{F}
        x_{F}
    \nonumber
    \\
    & = &
        2
        x_{F}
        x_{I}
        +
        x_{F}
        x_{F}
    \nonumber
    \\
    & \le &
        2
        x_{I}
        +
        1
    \nonumber
    \\
    & \le &
        2
        \lfloor
            \sqrt{a}
        \rfloor
        +
        1
    .
    \nonumber
\end{eqnarray}
$$

The size of array for the bucket method need to be taken by $\lfloor \sqrt{a} \rfloor + 3$.
Indeed,

$$
\begin{eqnarray}
    \lfloor \sqrt{a} \rfloor
    (\lfloor \sqrt{a} \rfloor + 3)
    & = &
        \lfloor \sqrt{a} \rfloor
        \lfloor \sqrt{a} \rfloor
        +
        3\lfloor \sqrt{a} \rfloor
    \nonumber
    \\
    & \ge &
        \lfloor \sqrt{a} \rfloor
        \lfloor \sqrt{a} \rfloor
        +
        2
        \lfloor
            \sqrt{a}
        \rfloor
        +
        1
    \nonumber
\end{eqnarray}
$$


## Reference
* [Sqrt \(or Square Root\) Decomposition Technique \| Set 1 \(Introduction\) \- GeeksforGeeks](https://www.geeksforgeeks.org/sqrt-square-root-decomposition-technique-set-1-introduction/)
