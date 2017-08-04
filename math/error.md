---
title: error
---

## error
* $x$
    * 比較対象の値
* $x_{0}$
    * 真の値

Relative error

$$
    \left|
        \frac{
            x_{0} - x
        }{
            x
        }
    \right|
$$

Percentage error

$$
    \left|
        \frac{
            x_{0} - x
        }{
            x
        }
        \times
        100
    \right|
$$

Absolute error

$$
    x_{0} - x
$$

Round-off error

* 1/3などはcomputerでは表現できない
* computerで表現できる範囲にしたものがround-off error

Truncation error

* 無限和を有限和で表現することによるerror
* sin関数などを有限和で近似した場合の誤差


## Reference
* [How do I determine if the error in my answer is the result of round-off error or a bug? - MATLAB Answers - MATLAB Central](https://jp.mathworks.com/matlabcentral/answers/102419-how-do-i-determine-if-the-error-in-my-answer-is-the-result-of-round-off-error-or-a-bug)

