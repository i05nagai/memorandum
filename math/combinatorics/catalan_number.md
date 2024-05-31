---
title: Catalan Number
---

## Catalan Number

$$
\begin{eqnarray}
    C_{n}
    & := &
        \frac{
            1
        }{
            n + 1
        }
        \left(
            \begin{array}{c}
                2n \\
                n
            \end{array}
        \right)
    \nonumber
    \\
    & = &
        \frac{
            (2n)!
        }{
            n! (n + 1)!
        }
    \nonumber
    \\
    & = &
        \prod_{k=2}^{n}
            \frac{
                n + k
            }{
                k
            }
    \nonumber
    \\
    & = &
        \left(
            \begin{array}{c}
                2n \\
                n
            \end{array}
        \right)
        -
        \left(
            \begin{array}{c}
                2n \\
                n + 1
            \end{array}
        \right)
    \nonumber
\end{eqnarray}
$$

The first 12 values of the catalan numbers are

$$
\begin{eqnarray}
    C_{0} & = & 1
    \nonumber
    \\
    C_{1} & = & 1
    \nonumber
    \\
    C_{2} & = & 2
    \nonumber
    \\
    C_{3} & = & 5
    \nonumber
    \\
    C_{4} & = & 14
    \nonumber
    \\
    C_{5} & = & 42
    \nonumber
    \\
    C_{6} & = & 132
    \nonumber
    \\
    C_{7} & = & 429
    \nonumber
    \\
    C_{8} & = & 1430
    \nonumber
    \\
    C_{9} & = & 4862
    \nonumber
    \\
    C_{10} & = & 16796
    \nonumber
    \\
    C_{11} & = & 58786
    \nonumber
    \\
    & \vdots &
    \nonumber
\end{eqnarray}
$$

The recurrence releations are given by

$$
\begin{eqnarray}
    C_{n}
    & = &
        \sum_{i = 0}^{n - 1}
            C_{i}
            C_{n - (i + 1)}
    .
    \nonumber
\end{eqnarray}
$$


## Reference
- [Catalan number \- Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)
- https://klein.mit.edu/~rstan/ec/catalan.pdf
