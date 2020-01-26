---
title: Adaptive Quadrature
---

## Adaptive Quadrature

## Theory

#### Algorithm


$\mathrm{integrate}(f, a, b, \tau)$ method.

* Step1. approximate integral $Q \approx \int_{a}^{b} f(x) \ dx$,

* Step2.

$$
    \epsilon
    =
    \abs{
        Q
        -
        \int_{a}^{b}
            f(x)
        \ dx
    }
    .
$$

* Step3. If $\epsilon > \tau$, calculates

$$
\begin{eqnarray}
    m
    & = &
        (a + b) / 2,
    Q
    & = &
        \mathrm{integrate}(f, a, m \tau/2)
        +
        \mathrm{integrate}(f, m, b \tau/2)
    .
\end{eqnarray}
$$

* Step4. return $Q$

#### Adaptive simpson
- [Adaptive Simpson's method \- Wikipedia](https://en.wikipedia.org/wiki/Adaptive_Simpson%27s_method)

There are many termination criteria. Let

* $I_{1}$, $I_{2}$,
    * two estimates for the integrals
* $\mathrm{tol} > 0$,
* $\eta > 0$.

**Conventional termination criteria**

$$
\begin{eqnarray}
    \abs{
        I_{1} - I_{2}
    }
    & < &
        \mathrm{tol} \abs{I_{1}}
    \label{equation_criteria_01}
    .
\end{eqnarray}
$$

Another criterion which terminate the algorithm if $I_{1}$ or $I_{2}$ is negligible compareted to the whole integral.

$$
\begin{eqnarray}
    \abs{I_{1}}
    & < &
        \eta
    \label{equation_criteria_02}
    .
\end{eqnarray}
$$

We can combine both criteria.

$$
\begin{eqnarray}
    & &
        \abs{I_{1} - I_{2}}
        <
        \mathrm{tol} \abs{I_{1}}
        \text{ or }
        \abs{ I_{1} }
        < \eta \abs{
                \int_{a}^{b}
                    f(x)
                \ dx
            }
    \nonumber
\end{eqnarray}
$$

For instance, if we choose $\eta$ and $\mathrm{tol}$ properly, the above can be written

$$
\begin{eqnarray}
    \abs{I_{1} - I_{2}}
    <
    (0.1)^{4} \abs{I_{1}}
    \text{ or }
    \abs{ I_{1}} < (0.1)^{4}
    \nonumber
\end{eqnarray}
$$


**Improved criteria to eliminate $\eta$ and $\mathrm{tol}$**.

* $Q$,
    * the (rough) estimator of $\abs{I}$,

Criteria $$\eqref{equation_criteria_02}$$ would be



```
Q + I1 == Q.
```

Criteria $$\eqref{equation_criteria_01}$$ would be


```
Q + (I1 - I2) == Q.
```

**Other Criteria**
One introduced by [1] is

$$
\begin{eqnarray}
    m
    & = &
        (a + b) /2,
    \nonumber
    \\
    \abs{
        S(a, m)
        +
        S(m, b)
        -
        S(a, b)
    }
    <
    15 \epsilon,
\end{eqnarray}
$$


**Algortihm**

* $S(a, b)$,
    * estimate of the integral by 3-points simpson method 
* $\epsilon > 0$,

<p class="pseudocode-js">
<pre class="pseudocode-js-code" style="display:none">
    \begin{algorithm}
    \caption{Adaptive Simpson}
    \begin{algorithmic}
    \PROCEDURE{RecursiveSimpson}{$f, a, b, Q, \epsilon$}
        \STATE $m \leftarrow (a + b) / 2$,
        \STATE $I_{l} \leftarrow S(f, a, m)$,
        \STATE $I_{r} \leftarrow S(f, m, b)$,
        \STATE $\delta \leftarrow I_{l} + I_{r} - Q$,
        \IF{$|\delta| \leq 15 \epsilon$}
            \RETURN $I_{l} + I_{r} + \delta / 15$,
        \ENDIF
        \RETURN \CALL{RecursiveSimpson}{$f, a, m, Q, \epsilon$} + \CALL{RecursiveSimpson}{$f, m, b, Q, \epsilon$}
    \ENDPROCEDURE
    \PROCEDURE{AdaptiveSimpson}{$f, a, b, \epsilon$}
        \STATE $Q \leftarrow S(f, a, b)$
        \RETURN \CALL{RecursiveSimpson}{$f, a, b, Q, \epsilon$}
    \ENDPROCEDURE
    \end{algorithmic}
    \end{algorithm}
</pre>
</p>


* Step5. Return $a \leftarrow 



## Reference
* [Adaptive quadrature \- Wikipedia](https://en.wikipedia.org/wiki/Adaptive_quadrature)
* [1] Gander, W., & Gautschi, W. (2000). Adaptive quadrature - Revisited. BIT Numerical Mathematics, 40(1), 84–101. https://doi.org/10.1023/A:1022318402393
* [2] J.N. Lyness (1969), "Notes on the adaptive Simpson quadrature routine", Journal of the ACM, 16 (3): 483–495, doi:10.1145/321526.321537
