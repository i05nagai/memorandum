---
title: Matrix Norm
---

## Matrix Norm


### Definition. Frobenius Norm
* $$A \in \mathbb{C}^{m \times n}$$,

$$
\begin{eqnarray}
    \|A\|_{\mathrm{F}}
    & := &
        \sqrt{
            \sum_{i=1}^{m}
                \sum_{j=1}^{n}
                    (a_{j}^{i})^{2}
        }
    \nonumber
    \\
    & = &
        \sqrt{
            \sum_{i=1}^{m}
                (a^{i})^{\mathrm{T}}
                (a^{i})
        }
    \nonumber
    \\
    & = &
        \sqrt{
            \sum_{j=1}^{n}
                (a_{j})^{\mathrm{T}}
                (a_{j})
        }
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>

### Remark
* $$A = (a_{1} \cdot a_{n})$$,
    * $$a_{i}$$ is column vectors of $A$.

$$
    \|A \|_{\mathrm{F}}^{2}
    =
    \mathrm{tr}(A^{\mathrm{T}}A)
$$

To see this,

$$
\begin{eqnarray}
    A^{\mathrm{T}}A
    & = &
        \left(
            \begin{array}{c}
                a_{1}^{\mathrm{T}}
                \\
                \vdots 
                \\
                a_{n}^{\mathrm{T}}
            \end{array}
        \right)
        (a_{1} \cdot a_{n})
    \\
    & = &
        (a_{j_{1}}^{\mathrm{T}}a_{j_{2}})_{j_{1},j_{2}=1,\ldots, n}
\end{eqnarray}
$$

<div class="end-of-statement" style="text-align: right">■</div>


### Propositon. Equivalent conditions
* 

### proof.

<div class="QED" style="text-align: right">$\Box$</div>


