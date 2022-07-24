---
title: Integer Partitions
---

## Integer Partitions


##
[A000009 \- OEIS](https://oeis.org/A000009)

$$
    p(n)
    :=
    #\{
        (a_{1}, \ldots, a_{k})
        \mid
        \sum_{i=1}^{k}a_{i}
        =
        n,
        k \in \mathbb{N}
    \}
    .
$$

$$
\begin{eqnarray}
    (1 + x^{1} + x^{2} + \cdots)
    (1 + x^{2} + x^{4} + \cdots)
    (1 + x^{3} + x^{3} + \cdots)
    \cdots
    & = &
        \frac{
            1
        }{
            1 - x
        }
        \frac{
            1
        }{
            1 - x^{2}
        }
        \frac{
            1
        }{
            1 - x^{3}
        }
        \cdots
    \\
    & = &
        \sum_{n=0}^{\infty}
            p(n)
            x^{n}
\end{eqnarray}
$$


## Distinct
- [A111133 \- OEIS](https://oeis.org/A111133)

## Reference
- https://www2.math.upenn.edu/~wilf/PIMS/PIMSLectures.pdf
- [Partition \(number theory\) \- Wikipedia](https://en.wikipedia.org/wiki/Partition_(number_theory))
- [Number of partitions of an integer into distinct parts: Introduction to partitions](https://functions.wolfram.com/IntegerFunctions/PartitionsQ/introductions/Partitions/ShowAll.html)
- [partitions\.pdf](https://math.berkeley.edu/~mhaiman/math172-spring10/partitions.pdf)
