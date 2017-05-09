---
title: Missing Data Analysis
---

## Missing Data Analysis
欠損値を埋める方法のまとめ。
LittleとRudinの方がStandardな本。

欠損値はができる要因は以下。

* データが正しく取得できなかった
    * logが壊れている
* データがそもそも取れない
    * 非会員のユーザの情報
        * 年齢、性別、住所など個人情報
    * 個人情報の提供拒否
    * 

欠損値の分類として以下のようなものが知られているらしい。
名前の付け方は意味不明だが、

* Missing Completely At Random (MCAR)
    * データが完全にRandomに欠損する
* Not Missing Not At Random (NMAR)
    * データが欠損データの値の影響で欠損する
    * 体重測定で太っているから、測りたくない
        * 体重が重いほど欠損が増える
* Missing At Random (MAR)
    * データが観測データの値の影響で欠損する
    * 体重測定で、女性の方が体重を測りたくない
        * 性別の変数によって欠損値が増減する

## Methods
欠損値を埋める方法として以下の方法が知られている。

* Listwise deletion
    * Complete cases analysis
    * 一変数でも欠損値があれば、そのデータを除く
    * データが少ないと使えるデータも減る
    * Graham曰く古い手法で、使わない方が良いらしい
* Pairwise deletion
    * 2変数間相関を計算する
        * 相関の計算時、選んだ2組とも欠損がないデータのみを用いる
    * 各変数間で使用するデータが異なるので、通常の意味の相関行列などにはならない
    * Graham曰く古い手法で、使わない方が良いらしい
* 適当
    * 平均とか中央値で適当に埋める
* 回帰
    * 欠損値を他の変数から推定する
    * 時系列性がある場合は、時系列回帰などにもなる
* 欠損した値を確率変数としてモデル化する
    * EM algorithm
        * 欠損値を所謂、潜在変数としてEM algorithmなどでとく
* 欠損するかどうかを確率変数としてモデル化
    * Maximum Likelihood (ML)
        * 最尤法
    * Multiple Imputation (MI)
        * ベイズ

## Formulation
* $N$
    * データの数
* $d$
    * 変数の数
    * 観測している変数の数
* $$X_{1}, \ldots, X_{N}$$,
    * $$X_{i} := (X_{i}^{1}, \ldots, X_{i}^{d})^{\mathrm{T}}$$,
    * $\mathbb{R}^{d}$値の確率変数
    * $X$に対して独立同分布
* $$\bar{X}_{N} := (X_{1}, \ldots, X_{N})$$,
    * 記法を簡潔するために、確率変数全体を上のようにかく
* $$x_{k} := X_{1}(\omega)$$,
    * 確率変数の$$\mathbb{R}^{d}$$値の観測値
* $$\bar{x}_{N} := (x_{1}, \ldots, x_{N})$$,
    * 記法を簡潔するために、実現値全体を上のようにかく
* $\theta \in \mathbb{R}^{d}$
    * モデルのパラメータを表す変数
* $$M := (M_{1}^{1}, \ldots, M_{1}^{d}, M_{2}^{1}, \ldots, M_{N}^{d})$$,
    * $$\{0 , 1\}$$に値をとる確率変数
    * 0の時対応する$$X_{i}^{j}$$は観測される
    * 1の時対応する$$X_{i}^{j}$$は欠損する
* $$m := (m_{i}^{j} := M_{i}^{j}(\omega)\ \forall i = 1, \ldots, N, j= 1, \ldots, d$$,
    * $$M_{i}^{j}$$の実現値
    * $$m_{i}^{j} = 0$$の時対応する$$x_{i}^{j}$$は観測される
    * $$m_{i}^{j} = 1$$の時対応する$$x_{i}^{j}$$は欠損
    * 1の時対応する$$X_{i}^{j}$$は欠損する
* $$I_{\mathrm{mis}} \subset \{1, \ldots, N\}\times \{1, \ldots, d\}$$,
    * 欠損している確率変数の添字の集合
    * 集合値の確率変数
    * 欠損している確率変数の全体は$$X_{\mathrm{mis}} := (X_{i}^{j})_{(i,j) \in I_{\mathrm{mis}}}$$
        * $i, j$の順に辞書順
* $$I_{\mathrm{obs}} := \{1, \ldots, N\}\times \{1, \ldots, d\} \setminus I_{\mathrm{mis}}$$,
    * 観測できる確率変数の添字
    * 集合値の確率変数
    * 観測できる確率変数の全体は$$X_{\mathrm{obs}} := (X_{i}^{j})_{(i,j) \in I_{\mathrm{obs}}}$$
        * $i, j$の順に辞書順
* $p_{X}$
    * $X$の密度関数
    * 条件付き密度関数も同様に定義する

### Remark
* $$I_{\mathrm{obs}}$$の分布は$$\{M_{i}^{j}\}$$で完全にきまる
* $$I_{\mathrm{obs}}$$の分布は$$I_{\mathrm{mis}}$$で完全にきまる

<div class="QED" style="text-align: right">■</div>

### Definition. (Missing Completely At Random)
欠損が以下を満たすとき、Missing Completely At Randomという。

$$
\begin{equation}
    p_{M \mid X_{\mathrm{obs}}, X_{\mathrm{mis}}}(m \mid x_{\mathrm{obs}}, x_{\mathrm{mis}})
    =
    p_{M}(m)
    \label{def_missing_completely_at_random}
\end{equation}
$$

<div class="QED" style="text-align: right">■</div>

### Definition. (Missing At Random)
欠損が以下を満たすとき、Missing At Randomという。

$$
\begin{equation}
    p_{M \mid X_{\mathrm{obs}}, X_{\mathrm{mis}}}(m \mid x_{\mathrm{obs}}, x_{\mathrm{mis}})
    =
    p_{M \mid X_{\mathrm{obs}}}(m \mid x_{\mathrm{obs}})
    \label{def_missing_at_random}
\end{equation}
$$

<div class="QED" style="text-align: right">■</div>

### Definition. (Not Missing At Random)
MCARでもMARでもないとき、Not Missing At Randomという。

<div class="QED" style="text-align: right">■</div>

### Remark
* NMARのとき、$$M$$は欠損値$$X_{i}^{j}\ (\forall (i, j) \in I_{\mathrm{}})$$に依存してきまる

<div class="QED" style="text-align: right">■</div>

ML法（尤度推定）とMI法（ベイズ推定）に基づく方法について述べる。
通常のMLとMIの議論と同様2つの手法の違いは、パラメータを確率変数とみなすかどうかのみである。
まず、ML法について述べる。

### Maximum Likelihood
* $p_{1}, p_{2} \in \mathbb{N}$
    * parameterの次元
    * $p_{1}$が$X$のparameter$\theta$の次元
    * $p_{2}$が$M$のparameter$\phi$の次元
* $(\theta, \phi) \in \Theta \subseteq \mathbb{R}^{p_{1}} \times \mathbb{R}^{p_{2}}$
    * parameterの空間

$$
    p_{X_{\mathrm{obs}}}(x_{\mathrm{obs}}; \theta)
    =
    \int
        p_{X_{\mathrm{obs}}, X_{\mathrm{mis}}}(x_{\mathrm{obs}}, x_{\mathrm{mis}}; \theta)
    \ d x_{\mathrm{mis}}
$$

likehood of $\theta$ ignoring the missing data mechanismを以下で定義する。

$$
    L_{\mathrm{ign}}(\theta; x_{\mathrm{obs}})
    :=
    \log
    \left(
        p_{X_{\mathrm{obs}}}(x_{\mathrm{obs}}; \theta)
    \right).
$$

ベイズの公式より

$$
    p_{\bar{X}_{N}, M}(\bar{x}_{N}, m; \theta, \phi)
    =
    p_{\bar{X}_{N}}(\bar{x}_{N}; \theta)
    p_{M \mid \bar{X}_{N}}(\bar{x}_{N}, m; \theta, \phi)
$$

とかける。

$$
\begin{eqnarray}
    p_{X_{\mathrm{obs}}, M}(x_{\mathrm{obs}}, m; \theta, \phi)
    & = &
        \int
            p_{X_{\mathrm{obs}, X_{\mathrm{mis}}}, M}(x_{\mathrm{obs}}, x_{\mathrm{mis}}, m; \theta, \phi)
        \ d x_{\mathrm{mis}}
    \nonumber
    \\
    & = &
        \int
            p_{X_{\mathrm{obs}, X_{\mathrm{mis}}}}(x_{\mathrm{obs}}, x_{\mathrm{mis}}; \theta)
            p_{M \mid X_{\mathrm{obs}, X_{\mathrm{mis}}}}(m \mid x_{\mathrm{obs}}, x_{\mathrm{mis}}; \theta, \phi)
        \ d x_{\mathrm{mis}}
    \label{eq_01}
\end{eqnarray}
$$

$$
    L_{\mathrm{full}}(\theta, \phi)
    :=
    \log
    \left(
        p_{X_{\mathrm{obs}}, M}(x_{\mathrm{obs}}, m; \theta, \phi)
    \right)
$$

通常の最尤推定と同様に$$L_{\mathrm{full}}$$を最大にする$\theta, \phi$を求める。
特別な場合として、$$L_{\mathrm{ign}}$$と$$L_{\mathrm{full}}$$を独立にとけば良い場合がある。
次の条件を満たすとき独立にとける。

* MAR
* $M$と$X$が独立

実際、MARの場合は$$\eqref{eq_01}$$と$$\eqref{def_missing_at_random}$$より

$$
\begin{eqnarray}
    p_{X_{\mathrm{obs}}, M}(x_{\mathrm{obs}}, m; \theta, \phi)
    & = &
        \int
            p_{X_{\mathrm{obs}, X_{\mathrm{mis}}}}(x_{\mathrm{obs}}, x_{\mathrm{mis}}; \theta)
            p_{M \mid X_{\mathrm{obs}, X_{\mathrm{mis}}}}(m \mid x_{\mathrm{obs}}, x_{\mathrm{mis}}; \theta, \phi)
        \ d x_{\mathrm{mis}}
    \nonumber
    \\
    & = &
        \int
            p_{X_{\mathrm{obs}, X_{\mathrm{mis}}}}(x_{\mathrm{obs}}, x_{\mathrm{mis}}; \theta)
            p_{M \mid X_{\mathrm{obs}}}(m \mid x_{\mathrm{obs}}; \theta, \phi)
        \ d x_{\mathrm{mis}}
    \nonumber
    \\
    & = &
        p_{M \mid X_{\mathrm{obs}}}(m \mid x_{\mathrm{obs}}; \theta, \phi)
        \int
            p_{X_{\mathrm{obs}}, X_{\mathrm{mis}}}(x_{\mathrm{obs}}, x_{\mathrm{mis}}; \theta)
        \ d x_{\mathrm{mis}}
    \nonumber
    \\
    & = &
        p_{M \mid X_{\mathrm{obs}}}(m \mid x_{\mathrm{obs}}; \theta, \phi)
        p_{X_{\mathrm{obs}}}(x_{\mathrm{obs}}; \theta)
    \nonumber
    \\
    & = &
        p_{M}(m; \phi)
        p_{X_{\mathrm{obs}}}(x_{\mathrm{obs}}; \theta)
\end{eqnarray}
$$

となる。
最後の不等式は$M$と$X$の独立性による。
よって、$\theta$と$\phi$について独立に最尤方程式をとけば良い。

### Maximum Imputation
ML法の議論を各々のparameterが、確率変数だと思ってベイズの議論をすれば良い。
TBD

### Example

<div class="QED" style="text-align: right">■</div>


## Reference
1. [欠損値があるデータの分析  Sunny side up!](http://norimune.net/1811)
1. [欠損値 - 機械学習の「朱鷺の杜Wiki」](http://ibisforest.org/index.php?%E6%AC%A0%E6%90%8D%E5%80%A4)
1. Book/The Elements of Statistical Learning 9.6節
1. Graham, J. W. (2009). Missing data analysis: making it work in the real world. Annual Review of Psychology. https://doi.org/10.1146/annurev.psych.58.110405.085530
1. R.J.A.Little, et al. Statistical Analysis with Missing Data.

