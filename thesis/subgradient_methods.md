---
title: Subgradient Methods
---

## Subgradient Methods
凸関数に対するgradient descent method.

* $f: \mathbb{R}^{n} \rightarrow \mathbb{R}$
    * convex function
* $$\partial_{x}f$$,
    * $x$における$f$のsubdifferential

Algoritmは以下のようになる。
step幅の取り方によって、幾つか種類があるが step幅$$\alpha_{k}$$の与え方については、後述する。

* Step1. $x^{(0)}$を適当な初期値とする。
* Step2. $k = 0$とする
* Step3. $c^{(k}) \in \partial_{x^{(k)}}f$とし、$$\alpha_{k}$$を適当な規則で選ぶ

$$
    x^{(k+1)}
    :=
    x^{(k)}
    -
    \alpha_{k}
    c^{(k)}
$$

* Step4. $x^{(k + 1)}$が収束していれば終了
* Step5. $k \Leftarrow k + 1$として、Step3へ


## 2. Basic Subgradient Method

### 2.1 Negative subgradient update



### 2.3 Convergence reuslts


## 3 Convergence proof
Algorithmが収束することを示す。

### 3.1 Asusmptions
以下を仮定する。

* $f$の最小値$x^{*}$が存在する
* $f$のsubgradientのnormはbounded
    * $f$がLipschitzであれば、この仮定は満たされる

つまり、ある$G \in \mathbb{R}$が存在して、

$$
\begin{equation}
    \forall x \in \mathbb{R}^{n},
    \
    \forall c \in \partial_{x}f,
    \
    \| c\|_{2} \le G
    \label{inequality_subgradient_bound}
\end{equation}
$$

である。

* 以下を満たす定数$R \in \mathbb{R}$が存在

$$
\begin{equation}
    \| x^{(1)} - x^{*} \|
    \le
    R
    \label{inequality_initial_value_optimal_value}
\end{equation}
$$

### 3.2 Some basic inequalities
$g^{(k)}$は$x^{(k)}$のsubgradientなので、

$$
\begin{eqnarray}
    & &
        f(x^{*}) - f(x^{(k)})
        \ge
        (g^{(k)})^{\mathrm{T}}(x^{*} - x^{(k)})
    \nonumber
    \\
    & \Leftarrow &
        -
        (f(x^{(k)}) - f(x^{*}))
        \ge
        -(g^{(k)})^{\mathrm{T}}(x^{(k)} - x^{*})
\end{eqnarray}
$$

である。
上の不等式より、

$$
\begin{eqnarray}
    \| x^{(k + 1)} - x^{*} \|
    & = &
        \|x^{(k)} - \alpha_{k}g^{(k)} - x^{*} \|_{2}^{2}
    \nonumber
    \\
    & = &
        \|(x^{(k)} - x^{*}) - \alpha_{k}g^{(k)}\|_{2}^{2}
    \nonumber
    \\
    & = &
        \|x^{(k)} - x^{*} \|_{2}^{2}
        -
        2 \alpha_{k} (g^{(k)})^{\mathrm{T}}
        (x^{(k)} - x^{*})
        +
        \alpha_{k}^{2}\|g^{(k)} \|
    \nonumber
    \\
    & \le &
        \|x^{(k)} - x^{*} \|_{2}^{2}
        -
        2 \alpha_{k}
        (f(x^{(k)}) - f(x^{*}))
        +
        \alpha_{k}^{2}\|g^{(k)} \|
    \label{inequality_basic_subgradient}
\end{eqnarray}
$$

$k$について繰り返し適用すると

$$
\begin{eqnarray}
    \| x^{(k + 1)} - x^{*} \|
    & \le &
        \|x^{(1)} - x^{*} \|_{2}^{2}
        -
        2
        \sum_{i=1}^{k}
            \alpha_{i}
            (f(x^{(i)}) - f(x^{*}))
        +
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
            \|g^{(i)}\|_{2}^{2}
    \nonumber
\end{eqnarray}
$$

を得る。
また、

$$
\begin{eqnarray}
    i_{\mathrm{best}}^{(k)}
    & := &
        \arg \min_{i = 1, \ldots, k}
            (f(x^{(i)}) - f(x^{*}))
    \nonumber
    \\
    f_{\mathrm{best}}^{(k)}
    & := &
        f(x^{(i_{\mathrm{best}}^{(k)})})
\end{eqnarray}
$$

とおくと、

$$
\begin{eqnarray}
    \sum_{i=1}^{k}
        \alpha_{k}(f(x^{(i)} - x^{*})
    & \ge &
        \sum_{i=1}^{k}
            \alpha_{k}\min_{i=1,\ldots,k} \{ (f(x^{(i)} - f(x^{*})) \}
    \nonumber
    \\
    & \ge &
        \min_{i=1,\ldots,k} \{ (f(x^{(i)} - f(x^{*})) \}
        \left(
            \sum_{i=1}^{k}
                \alpha_{k}
        \right)
    \nonumber
    \\
    & \ge &
        \{ (f_{\mathrm{best}} - f(x^{*})) \}
        \left(
            \sum_{i=1}^{k}
                \alpha_{k}
        \right)
    \nonumber
\end{eqnarray}
$$

となる。
$$\eqref{inequality_initial_value_optimal_value}$$より、

$$
\begin{eqnarray}
    0
    & \le &
        \|x^{(1)} - x^{*} \|_{2}^{2}
        -
        2
        \sum_{i=1}^{k}
            \alpha_{i}
            (f(x^{(i)}) - f(x^{*}))
        +
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
            \|g^{(i)}\|_{2}^{2}
    \nonumber
    \\
    & \le &
        R^{2}
        -
        2
        \sum_{i=1}^{k}
            \alpha_{i}
            (f(x^{(i)}) - f(x^{*}))
        +
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
            \|g^{(i)}\|_{2}^{2}
    \nonumber
\end{eqnarray}
$$

つづけて、

$$
\begin{eqnarray}
    R^{2}
    +
    \sum_{i=1}^{k}
        \alpha_{i}^{2}
        \|g^{(i)}\|_{2}^{2}
    & \ge  &
        2
        \sum_{i=1}^{k}
            \alpha_{i}
            (f(x^{(i)}) - f(x^{*}))
    \label{01_inequality_strict_lower_bound}
    \\
    & \ge &
        2
        (f_{\mathrm{best}}^{(k)} - f(x^{*}))
        \left(
            \sum_{i=1}^{k}
                \alpha_{k}
        \right)
    \nonumber
\end{eqnarray}
$$

上の結果をあわせて、以下を得る。

$$
\begin{eqnarray}
    (f_{\mathrm{best}}^{(k)} - f(x^{*}))
    & \le &
        \frac{
            R^{2}
            +
            \sum_{i=1}^{k}
                \alpha_{i}^{2}
                \| g^{(k)} \|_{2}^{2}
        }{
            2
            \left(
                \sum_{i=1}^{k}
                    \alpha_{k}
            \right)
        }
    \label{inequality_general_basic_subgradient_method}
    \\
    & \le &
        \frac{
            R^{2}
            +
            G^{2}
            \sum_{i=1}^{k}
                \alpha_{i}^{2}
        }{
            2
            \left(
                \sum_{i=1}^{k}
                    \alpha_{k}
            \right)
        }
    \label{inequality_basic_subgradient_method}
\end{eqnarray}
$$

最後の不等式は、$$\eqref{inequality_subgradient_bound}$$による。
以上より、$$\eqref{inequality_basic_subgradient_method}$$の右辺が収束するように、step sizeの列$$(\alpha_{k})$$を取れば良いことがわかる。

そのような$\alpha_{k}$の取り方として、以下のものが知られている。

* Constant step size
* Constant step length
* Square summable but not summable
* Diminishing step size rule
* Nonsummable diminishing step length

#### Constant step size
$$ \alpha_{k} := \alpha$$とおくと、$$\eqref{inequality_basic_subgradient_method}$$の右辺は


$$
    \frac{
        R^{2}
        +
        G^{2}
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
    }{
        2
        \left(
            \sum_{i=1}^{k}
                \alpha_{k}
        \right)
    }
    =
    \frac{
        R^{2}
        +
        G^{2}
        k
        \alpha^{2}
    }{
        2
        k \alpha
    }
    \rightarrow
    \frac{
        G^{2}
        \alpha
    }{
        2
    }
    \quad
    (k \rightarrow \infty)
$$

となる。

#### Constant step length
$\gamma \ge 0$とし、 $$\alpha_{k} := \gamma /  \| g^{(k)} \|_{2}$$とおく。
$$\eqref{inequality_general_basic_subgradient_method}$$の右辺は、

$$
\begin{eqnarray}
    \frac{
        R^{2}
        +
        G^{2}
        \sum_{i=1}^{k}
            \|g^{(k)} \|_{2}^{2}
            \alpha_{i}^{2}
    }{
        2
        \left(
            \sum_{i=1}^{k}
                \alpha_{k}
        \right)
    }
    & = &
        \frac{
            R^{2}
            +
            k
            \gamma^{2}
        }{
            2
            \left(
                \sum_{i=1}^{k}
                    \frac{\gamma}{ \| g^{(k)} \|_{2} }
            \right)
        }
    \nonumber
    \\
    & \le &
        \frac{
            R^{2}
            +
            k
            \gamma^{2}
        }{
            2
            \frac{k\gamma}{ G }
        }
        \rightarrow
        \frac{
            \gamma
            G
        }{
            2
        }
        \quad
        (k \rightarrow \infty)
\end{eqnarray}
$$

となる。

#### Square summable but not summable
$$\alpha_{k}$$を以下の満たすように取る。

$$
\begin{eqnarray}
    \| \alpha \|_{2}^{2}
    & := &
        \sum_{k=1}^{\infty}
            \alpha_{k}^{2}
        <
        \infty
    \nonumber
    \\
    \sum_{k=1}^{\infty}
        \alpha_{k}
    & = &
        \infty
    \nonumber
\end{eqnarray}
$$

とおく。
$$\eqref{inequality_basic_subgradient_method}$$の右辺は

$$
    \frac{
        R^{2}
        +
        G^{2}
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
    }{
        2
        \left(
            \sum_{i=1}^{k}
                \alpha_{k}
        \right)
    }
    \le
    \frac{
        R^{2}
        +
        G^{2}
        \| \alpha \|
    }{
        2
        \sum_{i=1}^{k}
            \alpha_{k}
    }
    \rightarrow
    0
$$

となって、収束する。

#### Diminishing step size rule
$$\alpha_{k}$$を次のようにとる。

$$
\begin{eqnarray}
    \alpha_{k}
    & \rightarrow &
        0
        \quad
        (k \rightarrow \infty)
        \label{diminishing_step_size_rule_condition_1}
    \\
    \sum_{i=1}^{\infty}
        \alpha_{k}
    & = &
        \infty
        \label{diminishing_step_size_rule_condition_2}
\end{eqnarray}
$$

このとき、$$\eqref{inequality_basic_subgradient_method}$$の右辺は0に収束する。
$\epsilon > 0$とすると、$$\eqref{diminishing_step_size_rule_condition_1}$$より、ある$$\exists N_{1}$$が存在して、$$i > N_{1}$$について$$\epsilon / G^{2} \ge \alpha_{i}$$となるようにとることができる。
更に、$$\eqref{diminishing_step_size_rule_condition_2}$$から$$\exists N_{2}$$が存在して、

$$
\begin{equation}
    \sum_{i=1}^{N_{2}}
        \alpha_{k}
    \ge
    \frac{1}{\epsilon}
    \left(
        R^{2}
        +
        G^{2}
        \sum_{i=1}^{N_{1}}
            \alpha_{i}
    \right)
\end{equation}
$$

とできる。
$$N := \max{N_{1}, N_{2}}$$とおけば、$k > N$について、

$$
\begin{eqnarray}
    \frac{
        R^{2}
        +
        G^{2}\sum_{i=1}^{k}
            \alpha_{i}^{2}
    }{
        2 \sum_{i=1}^{k}
            \alpha_{i}
    }
    & \le &
        \frac{
            R^{2}
            +
            G^{2}\sum_{i=1}^{N_{1}}
                \alpha_{i}^{2}
            +
            G^{2}\sum_{i=N_{1}+1}^{k}
                \alpha_{i}^{2}
        }{
            2 \sum_{i=1}^{k}
                \alpha_{i}
        }
    \nonumber
    \\
    & \le &
        \frac{
            R^{2}
            +
            G^{2}\sum_{i=1}^{N_{1}}
                \alpha_{i}^{2}
        }{
            2 \sum_{i=1}^{k}
                \alpha_{i}
        }
        +
        \frac{
            G^{2}\sum_{i=N_{1}+1}^{k}
                \alpha_{i}^{2}
        }{
            2 \sum_{i=1}^{N_{1}}
                \alpha_{i}
            +
            2 \sum_{i=N_{1}+1}^{k}
                \alpha_{i}
        }
    \nonumber
    \\
    & \le &
        \frac{
            R^{2}
            +
            G^{2}\sum_{i=1}^{k}
                \alpha_{i}^{2}
        }{
            2
            \frac{1}{\epsilon}
            \left(
                R^{2}
                +
                G^{2}
                \sum_{i=1}^{N_{1}}
                    \alpha_{i}
            \right)
        }
        +
        \frac{
            G^{2}\sum_{i=N_{1}+1}^{k}
                \alpha_{i}^{2}
        }{
            2 \sum_{i=N_{1}+1}^{k}
                \alpha_{i}
        }
    \nonumber
    \\
    & \le &
        \frac{ \epsilon }{ 2 }
        +
        \frac{
            G^{2}
            \sum_{i=N_{1}+1}^{k}
                \left(
                    \alpha_{i}
                    \frac{\epsilon}{G^{2}}
                \right)
        }{
            2 \sum_{i=N_{1}+1}^{k}
                \alpha_{i}
        }
    \nonumber
    \\
    & = &
        \frac{\epsilon}{2}
        +
        \frac{\epsilon}{2}
    =
    \epsilon
    \label{diminishing_step_size_rule_convergence}
\end{eqnarray}
$$

$\epsilon$は任意だから、subgradient methodは収束する。

#### Nonsummable diminishing step length
$$\alpha_{k}$$を以下のようにとる。

$$
\begin{eqnarray}
    \gamma_{k}
    & \rightarrow &
        0
        \quad
        (k \rightarrow \infty)
        \label{nonsummable_diminishing_step_length_condition_1}
    \\
    \sum_{i=1}^{\infty}
        \gamma_{k}
    & = &
        \infty
        \label{nonsummable_diminishing_step_length_condition_2}
    \\
    \alpha_{k}
    & := &
        \frac{\gamma_{k}}{\| g^{(k)}\|}
\end{eqnarray}
$$

$$\eqref{inequality_general_basic_subgradient_method}$$の右辺について、

$$
\begin{eqnarray}
    \frac{
        R^{2}
        +
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
            \|g^{(k)}\|_{2}^{2}
    }{
        2 \sum_{i=1}^{k}
            \alpha_{i}
    }
    & \le &
        \frac{
            R^{2}
            +
            \sum_{i=1}^{k}
                \gamma_{k}^{2}
        }{
            2 \sum_{i=1}^{k}
                \frac{\gamma_{k}}{\|g^{(k)}\|_{2}}
        }
    \nonumber
    \\
    & \le &
        \frac{
            R^{2}
            +
            \sum_{i=1}^{k}
                \gamma_{k}^{2}
        }{
            \frac{2}{G}
            \sum_{i=1}^{k}
                \gamma_{k}
        }
    \nonumber
\end{eqnarray}
$$

となる。
この形は$$\eqref{diminishing_step_size_rule_convergence}$$の$$\alpha_{k}$$を$$\gamma_{k}$$とおいたものと$G$を除き同等であるから、同様の結果を得る。

### 3.3. A bound on the suboptimality bound
次に、$$f_{\mathrm{best}} - f(x^{*})$$の上界を考える。
前節の議論、特に$$\eqref{inequality_basic_subgradient_method}$$によって、

$$
    f_{\mathrm{best}} - f(x^{*})
    \le
    \frac{
        R^{2}
        +
        G^{2}
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
    }{
        2
        \left(
            \sum_{i=1}^{k}
                \alpha_{i}
        \right)
    }
    =:
    h(\alpha_{1}, \ldots, \alpha_{k})
$$

である。
この時、右辺を最小にするようなstep幅を考える。
上式の右辺は、$$\alpha_{1}, \ldots, \alpha_{k}$$について、convexかつsymmetric(i.e. $$\sigma \in \mathfrak{S}_{k}, h(\alpha_{\sigma(1)}, \ldots, \alpha_{\sigma(k)}) = h(\alpha_{1}, \ldots, \alpha_{k}))$$なので、step幅を等長(e.g. $\alpha$)として取れば良い。
実際、convexityは以下から分かる。

$$

$$

convexityから極小値が最小値となるが、最小値の一意性とsymmetricであることより、解は等長でなければならない。
よって、極小値では、$$\alpha_{i} = \alpha_{j}\ (i \neq j)$$である。
極小値では一階微分はゼロであるから、一階微分を考えると、

$$
\begin{eqnarray}
    & &
        \frac{\partial h}{\partial \alpha_{j}}  = 0
    \\
    & \Leftrightarrow &
        \frac{
            G^{2} 2\alpha_{j}
            \left(
                \sum_{i=1}^{k}
                    \alpha_{i}
            \right)
            -
            \left(
                R^{2} + G^{2} 
                    \sum_{i=1}^{k}
                        \alpha_{i}^{2}
            \right)
        }{
            2
            \left(
                \sum_{i=1}^{k}
                    \alpha_{i}
            \right)^{2}
        }
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        G^{2} 2\alpha_{j}
        \left(
            \sum_{i=1}^{k}
                \alpha_{i}
        \right)
        -
        \left(
            R^{2} + G^{2} 
                \sum_{i=1}^{k}
                    \alpha_{i}^{2}
        \right)
        =
        0
    \nonumber
    \\
    & \Leftrightarrow &
        2\alpha_{j}
        \left(
            \sum_{i=1}^{k}
                \alpha_{i}
        \right)
        -
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
        =
        \frac{R^{2}}{G^{2}}
    \nonumber
    \\
    & \Leftrightarrow &
        2k\alpha^{2}
        -
        k
        \alpha^{2}
        =
        \frac{R^{2}}{G^{2}}
    \nonumber
    \\
    & \Leftrightarrow &
        k\alpha^{2}
        =
        \frac{R^{2}}{G^{2}}
    \nonumber
    \\
    & \Leftrightarrow &
        \alpha
        =
        \frac{
            R
        }{
            G \sqrt{k}
        }
\end{eqnarray}
$$

このとき、不等式$$\eqref{inequality_basic_subgradient_method}$$は以下となる。

$$
\begin{eqnarray}
    f_{\mathrm{best}} - f(x^{*})
    & \le &
        \frac{
            R^{2}
            +
            G^{2}
            \sum_{i=1}^{k}
                \alpha_{i}^{2}
        }{
            2
            \left(
                \sum_{i=1}^{k}
                    \alpha_{k}
            \right)
        }
    \nonumber
    \\
    & = &
        \frac{
            R^{2}
            +
            G^{2} k \alpha^{2}
        }{
            2k \alpha
        }
    \nonumber
    \\
    & = &
        \frac{
            R^{2}
            +
            R^{2}
        }{
            2\sqrt{k}R/G
        }
    \nonumber
    \\
    & = &
        \frac{
            GR
        }{
            \sqrt{k}
        }
\end{eqnarray}
$$

### 3.4 A stopping criterion
algorithmのstopping criterionについて考える。
$$\eqref{01_inequality_strict_lower_bound}$$は$$\eqref{inequality_basic_subgradient_method}$$及び$$\eqref{inequality_general_basic_subgradient_method}$$よりstrictなlower boundを与える。
$$\eqref{01_inequality_strict_lower_bound}$$から、

$$
    f^{*}
    \ge
    l_{k}
    :=
    \frac{
        2 \sum_{i=1}^{k}\alpha_{i}f(x^{(i)})
        - R^{2}
        - \sum_{i=1}^{k}
            \alpha_{i}^{2} \|g^{(i)}\|_{2}^{2}
    }{
        2
        \sum_{i=1}^{k}
            \alpha_{i}
    }
$$

$$l_{k}$$は減少する可能性もあるから、

$$
    l_{\mathrm{best}}^{(k)}
    :+
    \max\{l_{1}, \ldots, l_{k}\}
$$

をlower boundとする。
最適解のlower boundとの差$$f_{\mathrm{best}}^{(k)}  f_{\mathrm{best}}^{(k)}$$がthresholdを超えたらalgorithmを終了する。

これは、$G$に依存してい点で$$$$\eqref{inequality_general_basic_subgradient_method}$$より良いが、一般にこの差は0に収束するのに非常に多くのstepを要する。
そのため、このstopping criterionが使われることは殆どない。

### 3.5 Numerical example




## 4 Polyak's step length

### 4.1 Optimal step size choice when $$f^{*}$$ is known
Polyakは$$f^{*}$$が既知の場合のstep sizeの決め方について提案している。
$$f^{*}$$が既知であることはないように思えるが、これについては後で述べる。
step sizeとして、

$$
\begin{eqnarray}
    \alpha_{k}
    :=
    \frac{
        f(x^{(k)}) - f^{*}
    }{
        \|g^{(k)}\|_{2}^{2}
    }
    \label{05_step_size_polyak}
\end{eqnarray}
$$

このstep sizeの動機としては、$f$の$x^{(k)}$の周りでの1次のtaylor approximationを考え

$$
    f(x^{(k)} - \alpha g^{(k)})
    \approx
    f(x^{(k)})
    +
    (g^{(k)})^{\mathrm{T}}
    (x^{(k)} - \alpha g^{(k)} - x^{(k)})
    =
    f(x^{(k)})
    -
    \alpha (g^{(k)})^{\mathrm{T}} g^{(k)}
$$

この左辺を$$f^{*}$$として、$\alpha$について解けば得られる。
$\alpha$が十分小さければ良い近似を与えるから、$$f^{*}$$に近い所では良い収束を示すことが期待できる。

また、別の解釈として$$\eqref{05_step_size_polyak}$$は、$$\eqref{inequality_basic_subgradient}$$の右辺を最小にするstep sizeである。
実際

$$
    \|x^{(k+1)} - x^{*}\|_{2}^{2}
    \le
    \|x^{(k)} - x^{*}\|_{2}^{2}
    -
    2\alpha_{k} (f(x^{(k)}) - f^{*})
    +
    \alpha_{k}^{2}\| g^{(k)}\|_{2}^{2}
$$

から右辺の１階微分が0となる$$\alpha_{k}$$を考えれば良い。

収束については、$$\eqref{05_step_size_polyak}$$を$$\eqref{01_inequality_strict_lower_bound}$$に代入すると、

$$
\begin{eqnarray}
    & &
        R^{2}
        +
        \sum_{i=1}^{k}
            \alpha_{i}^{2}
            \|g^{(i)}\|_{2}^{2}
        \ge
        2
        \sum_{i=1}^{k}
            \alpha_{i}
            (f(x^{(i)}) - f(x^{*}))
    \nonumber
    \\
    & \Leftrightarrow &
        R^{2}
        +
        \sum_{i=1}^{k}
            \frac{
                (f(x^{(i)}) - f^{*})^{2}
            }{
                \|g^{(i)}\|_{2}^{2}
            }
        \ge
        2
        \sum_{i=1}^{k}
            \frac{
                (f(x^{(i)}) - f^{*})^{2}
            }{
                \|g^{(i)}\|_{2}^{2}
            }
    \nonumber
    \\
    & \Leftrightarrow &
        R^{2}
        \ge
        \sum_{i=1}^{k}
            \frac{
                (f(x^{(i)}) - f^{*})^{2}
            }{
                \|g^{(i)}\|_{2}^{2}
            }
    \nonumber
\end{eqnarray}
$$

ここで、$$\eqref{inequality_subgradient_bound}$$より、

$$
    R^{2}
    G^{2}
    \ge
    \sum_{i=1}^{k}
        (f(x^{(i)}) - f^{*})^{2}
$$

となる。
よって、右辺のsummationは収束する必要があるから、$$f(x^{(k)}) \rightarrow f^{*}$$を得る。

### 4.2 Plyak step size choice with estimated $$f^{*}$$,
$$f^{*}$$のestimationを考える。
$$f_{\mathrm{best}} - \gamma^{k}$$, $$\gamma^{k} > 0$$, $$\gamma^{k} \rightarrow 0$$


## Reference
* Boyd, S., Xiao, L., & Mutapcic, A. (2003). Subgradient methods. Lecture Notes of EE392o, Stanford …, 1(May), 1–21. Retrieved from http://xxpt.ynjgy.com/resource/data/20100601/U/stanford201001010/02-subgrad_method_notes.pdf
