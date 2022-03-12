---
title: Catalan Number
---

## Catalan Number

$$
\begin{eqnarray}
    C_{n}
    & :=l &
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
    \\
    & = &
        \frac{
            (2n)!
        }{
            n! (n + 1)!
        }
    \\
    & = &
        \prod_{k=2}^{n}
            \frac{
                n + k
            }{
                k
            }
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
    .
\end{eqnarray}
$$

1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786,...



## Reference
- [Catalan number \- Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)
- https://klein.mit.edu/~rstan/ec/catalan.pdf
