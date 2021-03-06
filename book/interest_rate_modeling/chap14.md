---
layout: math
title: Interest Rate Modeling 2
---

# 14 The Libor Market Model I

## 14.2 LM Dynamics and Measures

### 14.2.4 Separable Deterministic Volatility Function

### 14.2.5 Stochastic Volatility

spot measureの下で以下のSDEが成立するとする。

$$
\begin{equation}
    d z(t) = \theta(z_{0} - z(t)) dt 
        - \eta \psi(z(t)) dZ(t),
    \quad
    z(0) = z_{0}
    \label{chap14_lmm_volatility_process_stochastic_volatility_under_spot_measure}
\end{equation}
$$


$$
\begin{eqnarray}
    dL_{n}(t) 
        & = & \sqrt{z(t)} \phi(L_{n}(t)) \lambda_{n}(t)^{\mathrm{T}}
            \left(
                \sqrt{z(t)} \mu_{n}(t) dt + dW^{B}
            \right),
    \label{chap14_lmm_foward_rate_process_stochastic_volatility_under_spot_measure}
    \\
    \mu_{n}(t) 
        & := &
            \sum_{j=q(t)}^{n} \frac{\tau_{j} \phi(L_{j}(t)) \lambda_{j}(t)}{1 + \tau_{j}L_{j}(t)},
        \nonumber
\end{eqnarray}
$$

### 14.2.6 Time-Dependence in Model Parameters

## 14.3 Correlation

### 14.3.1 Empirical Principal Components Analysis

### 14.3.3 Negative Eigenvalues

### 14.3.4 Correlation PCA

## 14.4 Pricing of European Options

### 14.4.1 Caplets

#### Proposition 14.4.1
spot measureの下で、forward rateが$\eqref{chap14_lmm_foward_rate_process_stochastic_volatility_under_spot_measure}$及び$\eqref{chap14_lmm_volatility_process_stochastic_volatility_under_spot_measure}$とmodel化されているとする。
また、Assumption 14.2.7を仮定する。
このとき、

$$
    V_{\mathrm{caplet}}(0) = P(0, T_{n+1}) \tau_{n} \mathrm{E}^{T_{n+1}}
    \left[
        (L_{n}(T_{n}) - c)^{+}
    \right]
$$

である。
ここで、

$$
\begin{eqnarray}
    d L_{n}(t)
        & = & \sqrt{z(t)} \phi(L_{n}(t)) \| \lambda_{n}(t) \| dY^{n+1}(t),
    \\
    d z(t) 
        & = & \theta (z_{0} - z(t)) dt + \eta \psi(z(t)) dZ(t),
        \nonumber
\end{eqnarray}
$$

で、$Y^{n+1}(t)$及び$Z(t)$は独立で、$Q^{T_{n+1}}$の下で一次元BMである。
また、$Y^{n+1}$は以下で与えられる。

$$
    Y^{n+1}(t) 
        = \int_{0}^{t} \frac{\lambda_{n}(s)^{\mathrm{T}}}{\| \lambda_{n}(s) \|} \ d W^{n+1}(s).
$$

### 14.4.1 Swaptions

#### Proposition 14.4.2
$Q^{A}$を$A(t)$をnumeraireとするannuity measureとして、$W^{A}(t)$を$Q^{A}$のもとでの$m$次元BMとする。
このとき、

$$
\begin{equation}
    d S(t) = \sqrt{z(t)} \phi(S(t)) \sum_{n=j}^{k-1} w_{n}(t)\lambda_{n}(t)^{\mathrm{T}} dW^{A}(t),
\end{equation}
$$

ここで、stochastic weights$w_{n}$は

$$
\begin{eqnarray}
    w_{n}(t)    
        & = & \frac{\phi(L_{n}(t))}{\phi(S(t))} \frac{\partial S(t)}{\partial L_{n}(t)} 
        \\
        & = & \frac{\phi(L_{n}(t))}{\phi(S(t))} \frac{\tau_{n}S(t)}{1 + \tau_{n}L_{n}(t)}
            \left[
                \frac{P(t, \tau_{k})}{P(t, T_{j}) - P(t, T_{k})}
                    + \frac{\sum_{i=n}^{k-1} \tau_{i} P(t, T_{i+1})}{A(t)}
            \right]
\end{eqnarray}
$$

であり、$S(t)$の$L_{n}$の偏微分はforward rate$L_{j}(t), \ldots, L_{k-1}(t)$の関数とみなしたときのforwad rateによる偏微分である。


#### sketch of proof
$S(t)$がswap measureのもとでマルチンゲールであるので、$S(t)$のドリフトはswap measureの下で0である。
$S(t)$が$L_{j}(t), \ldots, L_{k-1}(t)$の関数なので、その関数を$\tilde{S}(L_{j}, \ldots, L_{k-1})$と書くとする。
Itoの補題より

$$
    d S(t) 
        = \sum_{n=j}^{k-1} \sqrt{z(t)}\phi(L_{n}(t)) \frac{\partial S(t)}{\partial L_{n}(t)} \lambda_{n}(t)^{\mathrm{T}} dW^{A}(t)
$$

より、swap rateの$L_{n}$での偏微分を求めればよい。

$$
\begin{eqnarray*}
    \sum_{n=j}^{k-1} \tau_{n} P(t, T_{n+1}) L_{n}(t)
        & = &
            \sum_{n=j}^{k-1} \left(
                P(t, T_{n}) - P(t, T_{n+1})
            \right)
            \\
        & = &
            P(t, T_{j}) - P(t, T_{k})
            \\
        & = &
            P(t, T_{j}) - \prod_{n=j}^{k-1}
            \left(
                \frac{P(t, T_{n+1})}{P(t, T_{n})} P(t, T_{j})
            \right)
            \\
        & = &
            P(t, T_{j}) - \prod_{n=j}^{k-1}(1 + \tau_{n}L_{n}(t))^{-1}P(t, T_{j})
            \\
        & = &
            P(t, T_{j})(1 - \prod_{n=j}^{k-1}(1 + \tau_{n}L_{n}(t))^{-1}
\end{eqnarray*}
$$

また、

$$
\begin{eqnarray*}
    \sum_{n=j}^{k-1} \tau_{n} P(t, T_{n+1}) 
        & = &
            \sum_{n=j}^{k-1} \tau_{n}
            \left(
                \prod_{l=j}^{n} (1 + \tau_{l}L_{l}(t))^{-1}P(t, T_{j})
            \right)
            \\
        & = &
            \sum_{n=j}^{k-1} \tau_{n}
            \left(
                \prod_{l=j}^{n} (1 + \tau_{l}L_{l}(t))^{-1}P(t, T_{j})
            \right)
            \\
        & = &
            \sum_{n=j}^{k-1} \tau_{n}
            \left(
                \prod_{l=j}^{n} (1 + \tau_{l}L_{l}(t))^{-1}
            \right)
            P(t, T_{j})
            \\
\end{eqnarray*}
$$

より、

$$
\begin{eqnarray*}
    \tilde{S} (L_{j}(t), \ldots, L_{k-1}(t))
        & := & \frac{
                \displaystyle
                \sum_{n=j}^{k-1} \tau_{n} P(t, T_{n+1}) L_{n}(t)
            }
            {
                \displaystyle
                \sum_{n=j}^{k-1} \tau_{n} P(t, T_{n+1})
            }
            \\
        & = &
            \frac{
                \displaystyle
                1 - \prod_{l=j}^{k-1} (1 + \tau_{j}L_{j}(t))^{-1}
                }{
                \displaystyle
                    \sum_{n=j}^{k-1} \tau_{n} \prod_{l=j}^{n} 
                    \left(
                        1 + \tau_{l} L_{l}
                    \right)^{-1}
                }
            \\
        & = &
            \frac{
                \displaystyle
                \prod_{l=j}^{k-1} (1 + \tau_{j}L_{j}(t)) - 1
                }{
                \displaystyle
                    \sum_{n=j}^{k-1} \tau_{n} \prod_{l=n+1}^{k-1} 
                    \left(
                        1 + \tau_{l} L_{l}
                    \right)
                }
\end{eqnarray*}
$$

である。

$$
    B(t) 
        := 
            \sum_{n=j}^{k-1} \tau_{n} \prod_{l=n+1}^{k-1} 
            \left(
                1 + \tau_{l} L_{l}
            \right),
    C(t) 
        :=
            \prod_{l=j}^{k-1} (1 + \tau_{j}L_{j}(t))
$$

とおく。

$$
\begin{eqnarray*}
    \frac{\partial B(t)}{\partial L_{m}(t)} 
        & = &
            \frac{\partial }{\partial L_{m}(t)} 
            \left(
                \sum_{n=j}^{m-1} \tau_{n} \prod_{l=n+1}^{k-1} (1 + \tau_{l}L_{l}(t))
                    + \sum_{n=m}^{k-1} \tau_{n} \prod_{l=n+1}^{k-1} (1 + \tau_{l}L_{l}(t))
            \right)
            \\
        & = &
            \frac{\partial }{\partial L_{m}(t)} 
                \sum_{n=j}^{m-1} \tau_{n} \prod_{l=n+1}^{k-1} (1 + \tau_{l}L_{l}(t))
            \\
        & = &
            \sum_{n=j}^{m-1} \tau_{n} \tau_{m} \frac{
                \prod_{l=n+1}^{k-1} (1 + \tau_{l}L_{l}(t))
            }{
                (1 + \tau_{m} L_{m}(t))
            }
            \\
        & = &
            \sum_{n=j}^{m-1} \tau_{n} \tau_{m} 
            \frac{
                P(t, T_{n+1})
            }{
                P(t, T_{k})
            }
            \frac{
                P(t, T_{m+1})
                }{
                P(t, T_{m})
            },
            \\
    B(t) 
        & = &
            \sum_{n=j}^{k-1} \tau_{n} \prod_{l=n+1}^{k-1} 
            \left(
                1 + \tau_{l} L_{l}
            \right)
            \\
        & = &
            \sum_{n=j}^{k-1} \tau_{n} \frac{P(t, T_{n+1})}{P(t, T_{k})}
            \\
        & = &
            \frac{A(t)}{P(t, T_{k})}
            \\
\end{eqnarray*}
$$

さらに、

$$
\begin{eqnarray*}
    \frac{\partial C(t)}{\partial L_{m}(t)} 
        & = &
            \tau_{m}
            \frac{
                \displaystyle
                \prod_{n=j}^{k-1} (1 + \tau_{n}L_{n}(t))
            }{
                (1 + \tau_{m}L_{m}(t))
            }
            \\
        & = &
            \tau_{m}
            \frac{P(t, T_{j})}{P(t, T_{k}) }
            \frac{P(t, T_{m+1})}{P(t, T_{m})},
            \\
    C(t)
        & = & 
            \frac{P(t, T_{j})}{P(t, T_{k})}
\end{eqnarray*}
$$

であるから、

$$
\begin{eqnarray*}
    \frac{\partial }{\partial L_{m}(t)} \tilde{S} (L_{j}(t), \ldots, L_{k-1}(t))
        & = &
            \frac{\partial }{\partial L_{m}(t)}
            \left(
                 \frac{C(t) - 1}{B(t)}
            \right)
            \\
        & = &
            \frac{1}{B(t)^{2}}
            \left(
                \tau_{m}
                \frac{P(t, T_{j})}{P(t, T_{k}) }
                \frac{P(t, T_{m+1})}{P(t, T_{m})}
                \frac{A(t)}{P(t, T_{k})}
                -
                \left(
                    \frac{P(t, T_{j})}{P(t, T_{k})} - 1
                \right)
                \sum_{n=j}^{m-1} \tau_{n} \tau_{m} 
                \frac{
                    P(t, T_{n+1})
                }{
                    P(t, T_{k})
                }
                \frac{
                    P(t, T_{m+1})
                    }{
                    P(t, T_{m})
                }
            \right)
            \\
        & = &
            \frac{1}{A(t)^{2}}
            \frac{P(t, T_{m+1})}{P(t, T_{m})}
            \left(
                \tau_{m} P(t, T_{j}) A(t)
                -
                (P(t, T_{j}) - P(t, T_{k})) \sum_{n=j}^{m-1} \tau_{n} \tau_{m} P(t, T_{n+1})
            \right)
                \\
        & = &
            \frac{S(t)}{A(t)}
            \frac{1}{(1 + \tau_{m}L_{m}(t))}
            \left(
                \frac{\tau_{m} P(t, T_{j}) A(t)}{P(t, T_{j}) - P(t, T_{k})}
                -
                \sum_{n=j}^{m-1} \tau_{n} \tau_{m} P(t, T_{n+1})
            \right)
            \\
        & = &
            \frac{S(t)}{A(t)}
            \frac{\tau_{m}}{(1 + \tau_{m}L_{m}(t))}
            \left(
                \frac{P(t, T_{j}) A(t)}{P(t, T_{j}) - P(t, T_{k})}
                -
                \sum_{n=j}^{m-1} \tau_{n}P(t, T_{n+1})
            \right)
            \\
        & = &
            \frac{S(t)\tau_{m}}{(1 + \tau_{m}L_{m}(t))}
            \left(
                \frac{P(t, T_{j})}{P(t, T_{j}) - P(t, T_{k})}
                -
                \frac{\sum_{n=j}^{m-1} \tau_{n}P(t, T_{n+1})}{A(t)}
            \right)
            \\
        & = &
            \frac{S(t)\tau_{m}}{(1 + \tau_{m}L_{m}(t))}
            \left(
                \frac{P(t, T_{j})}{P(t, T_{j}) - P(t, T_{k})}
                - 1
                + \frac{A(t)}{A(t)}
                - \frac{\sum_{n=j}^{m-1} \tau_{n}P(t, T_{n+1})}{A(t)}
            \right)
            \\
        & = &
            \frac{S(t)\tau_{m}}{(1 + \tau_{m}L_{m}(t))}
            \left(
                \frac{P(t, T_{k})}{P(t, T_{j}) - P(t, T_{k})}
                + \frac{\sum_{n=m}^{k-1} \tau_{n}P(t, T_{n+1})}{A(t)}
            \right)
            \\
        & = &
            \frac{\phi(S(t))}{\phi(L_{m}(t))} w_{m}(t)
\end{eqnarray*}
$$

となる。

<div class="QED" style="text-align: right">$\Box$</div>

##### Proposition 14.4.3
時刻0のswaptionの価格は以下で与えられる。

$$
\begin{equation}
    V_{\mathrm{swaption}}(0) 
        = A(0) \mathrm{E}^{A}
        \left[
            (S(T_{j}) - c)^{+}
        \right].
\end{equation}
$$

ここで、$w_{n}(t)$をProposition 14.4.2のものとし、

$$
    \lambda_{S}(t) 
        = \sum_{n=j}^{k-1} w_{n}(0) \lambda_{n}(t),
$$

とおく。
Proposition 14.4.2のswap rateのdynamicsは以下で近似される。

$$
\begin{eqnarray}
    d S(t)
        & \approx & \sqrt{z(t)} \phi(S(t)) \| \lambda_{S}(t) \| dY^{A},
    \\
    dz(t)
        & = & \theta (z_{0} - z(t)) dt + \eta \psi(z(t)) dZ(t),
\end{eqnarray}
$$

ここで、$Y^{A}(t)$及び$Z(t)$は独立で、$Q^{A}$の下に一次元BMである。
また、$Y^{A}(t)$は以下で与えられる。

$$
    \| \lambda_{S}(t) \| dY^{A}(t)
        = \sum_{n=j}^{k-1} w_{n}(0) \lambda_{n}(0)^{\mathrm{T}} dW^{A}(t).
$$




