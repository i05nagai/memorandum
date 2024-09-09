---
title: Birthday Problem
---

## Birthday Problem


- $x$ is the number of possible patterns
    - 365 for birthday
- $k$ is the number of patterns

The probability of the collision in the $k$ patterns is

$$
\begin{eqnarray}
    1
    -
    \frac{
        \frac{
            x!
        }{
            (x - k)!
        }
    }{
        x^{k}
    }
    & = &
        1 - 
        \frac{
            x!
        }{
            x^{k} (x - k)!
        }
    \nonumber
    \\
    & = &
        \frac{
            x^{k} (x - k)! - x!
        }{
            x^{k} (x - k)!
        }
    \nonumber
\end{eqnarray}
$$


## Reference
- https://en.wikipedia.org/wiki/Birthday_problem
