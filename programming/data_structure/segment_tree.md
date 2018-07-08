---
title: Segment tree
---

## Segment tree
In computer science, a segment tree also known as a statistic tree is a tree data structure used for storing information about intervals, or segments.

* $n$,
    * the number of intervals
* $$J_{i} := [q_{i,1}, q_{i,2}]$$,
    * $i$-th interval
* $$(p_{1}, \ldots, p_{2n})$$,
* $ k := \lfloor \log_{2}(2n) \rfloor + 1$,
    * height of tree
* $O(n)$,
    * storage complexity

Indeed,

$$
\begin{eqnarray}
    \sum_{i=1}^{k}
        \frac{
            2n
        }{
            2^{i-1}
        }
    & = &
        \sum_{i=1}^{k}
            2n
            2^{-(i-1)}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{k}
            2n
            2^{(i-1)-(k-1)}
    \nonumber
    \\
    & = &
        2^{-(k-1)}
        2n
        \sum_{i=1}^{k}
            2^{(i-1)}
    \nonumber
    \\
    & = &
        2^{-(k-1)}
        2n
        \frac{
            1 - 2^{k}
        }{
            1 - 2
        }
    \nonumber
    \\
    & = &
        2^{-(k-1)}
        2n
        (2^{k} - 1)
\end{eqnarray}
$$


* $O(n \log n)$,
    * to build

## Reference
* [Segment tree - Wikipedia](https://en.wikipedia.org/wiki/Segment_tree)
* [Microsoft PowerPoint - tutorial-stabbing.ppt](http://www.cs.nthu.edu.tw/~wkhon/ds/ds10/tutorial/tutorial6.pdf)
