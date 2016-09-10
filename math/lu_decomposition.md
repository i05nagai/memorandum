---
layout: math
title: LU decomposition
---

# LU decomposition
行列$A$を下三角行列$L$と上三角行列$U$に分解する方法。
つまり、以下を満たす$L, U$を見つける。

$$
A = LU
$$

## algorithm
### 1
$L$と$U$を下記のようにおく。

$$
L = 
    \left(
        \begin{array}{ccccc}
            1 & 0 & \ldots &   & 0\\
            l_{1}^{2} & 1 & 0 & \ldots & 0 \\
            l_{1}^{3} & l_{2}^{3} & 1 & \ldots & 0 \\
            \vdots & \vdots & \ddots & \ddots & \vdots \\
            l_{1}^{N} & l_{2}^{N} &  \ldots &  & l_{N}^{N}
        \end{array}
    \right)
$$

$$
U =
    \left(
        \begin{array}{ccccc}
            1 & 0 & \ldots &   & 0\\
            l_{1}^{2} & 1 & 0 & \ldots & 0 \\
            l_{1}^{3} & l_{2}^{3} & 1 & \ldots & 0 \\
            \vdots & \vdots & \ddots & \ddots & \vdots \\
            l_{1}^{N} & l_{2}^{N} &  \ldots &  & l_{N}^{N}
        \end{array}
    \right)
$$

$A = LU$から$N \times N$の連立方程式ができる。
$L$の対角成分を1としているので、未知変数も$N \times N$となって解ける。
具体的な解き方は、$A$の(1, 1)成分から順に解いていけば逐次求まる。

## referecen
[LU decomposition - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/LU_decomposition)

