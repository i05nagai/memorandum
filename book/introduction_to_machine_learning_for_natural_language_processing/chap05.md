---
title: Chapter5. 系列ラベリング
book_title: Introduction to Machine Learning for Natural Language Processing
book_chapter: 5
---

## 5. 系列ラベリング
品詞ダグ付に用いる系列ラベリング。

* 5.1節
    * 系列ラベリングの性質
* 5.2節
    * 基本的な方法である隠れマルコフモデル
* 5.3節
    * 分類器を逐次的に用いて行う系列ラベリングについて
* 5.4節
    * 精度の良い条件付き確率場(CRF)
* 5.5節
    * チャンキングについて

## 5.1 準備
* 系列(sequence)
    * 要素が連なったもの、単語が連なった文
* 系列ラベリング(sequence labeling)
    * 単語の系列に品詞をつけるなど
    * 品詞タグ付けはsequence labelingの一種

* 品詞タグ付

## 5.2 隠れマルコフモデル
* 隠れマルコフモデル(Hidden Markov Model)

### 5.2.1 HMMの導入
簡単のため、

* $$X_{1:T} := (X_{1}, \ldots, X_{T})$$,
    * NLPでは単語の列
    * 確率変数
    * $X_{t}$の値域は全て同じ
* $D_{X}$
    * 単語全体の集合
* $$Y_{1:T} := (Y_{1}, \ldots, Y_{T})$$,
    * NLPでは単語に対応するラベルの列
    * 確率変数
    * HMMでの隠れ変数
    * $Y_{t}$の値域は全て同じ
* $D_{Y}$
    * ラベル全体の集合
* $$x_{1:T} := (x_{1}, \ldots, x_{T})$$,
* $$y_{1:T} := (y_{1}, \ldots, y_{T})$$,

とおく。
また、$Y_{t}$は隠れ変数でマルコフ過程である。
つまり、$Y_{t}$が与えられた時以下のマルコフ性が成り立つ。

$$
    p_{Y_{t+1} \mid Y_{1:t}}
    =
    p_{Y_{t+1} \mid Y_{t}}.
$$

$X_{t}$が$t$時点の隠れ変数$Y_{t}$によってのみ決まる変数である。
よって、ある関数$g$によって

$$
    X_{t}
    =
    g(t, Y_{t})
$$

となる。
このとき、$X_{t}$の分布は$Y_{t}$の関すとしてかける。

$$\{X_{t}\}_{t=1}^{T}$$のみを観測することができるという設定のもと$$Y_{T+1}$$を推定する。
推定の仕方は色々考えられるが、

$$
    y^{*}
    :=
    \argmax_{y_{1:T}}
        p_{X_{1:T}, Y_{1:T}}(x_{1:T}, y_{1:T})
$$

と同時密度関数を最大化することを考える。
マルコフ性より、$X$と$Y$の条件付き確率密度関数は以下のようにかける。

$$
\begin{eqnarray}
    p_{X_{1:T}, Y_{1:T}}(x_{1:T}, y_{1:T})
    & = &
        p_{X_{T}, Y_{T} \mid X_{1:T-1}, Y_{1:T-1}}(x_{T}, y_{T} \mid x_{1:T-1}, y_{1:T-1})
            p_{X_{1:T-1}, Y_{1:T-1}}(x_{1:T-1}, y_{1:T-1})
    \nonumber
    \\
    & = &
        p_{X_{T}, Y_{T} \mid X_{T-1} Y_{T-1}}(x_{T}, y_{T} \mid x_{T-1}, y_{T-1})
            p_{X_{T-1}, Y_{T-1} \mid X_{T-2} Y_{T-2}}(x_{T-1}, y_{T-1} \mid x_{T-2}, y_{T-2})
    \nonumber
    \\
    & &
        \cdots
            p_{X_{2}, Y_{2} \mid X_{1}, Y_{1}}(x_{2}, y_{2} \mid x_{1}, y_{1})
            p_{X_{1}, Y_{1}}(x_{1}, y_{1})
    \nonumber
    \\
    & = &
        \prod_{t=1}^{T} p_{X_{t}, Y_{t} \mid X_{t-1}, Y_{t-1}}(x_{t}, y_{t} \mid x_{t-1}, y_{t-1})
            p_{X_{1}, Y_{1}}(x_{1}, y_{1})
    \label{HMM_joint_probability_density_function_2}
\end{eqnarray}
$$

更に、

$$
\begin{eqnarray}
    p_{X_{t}, Y_{t} \mid X_{t-1}, Y_{t-1}}(x_{t}, y_{t} \mid x_{t-1}, y_{t-1})
    & = &
        p_{X_{t}, Y_{t} \mid Y_{t-1}}(x_{t}, y_{t} \mid y_{t-1})
    \nonumber
    \\
    & = &
        \frac{
            p_{X_{t}, Y_{t}, Y_{t-1}}(x_{t}, y_{t}, y_{t-1})
        }{
            p_{Y_{t-1}}(y_{t-1})
        }
    \nonumber
    \\
    & = &
        p_{X_{t} \mid Y_{t}, Y_{t-1}}(x_{t} \mid y_{t}, y_{t-1})
            \frac{
                p_{Y_{t}, Y_{t-1}}(y_{t}, y_{t-1})
            }{
                p_{Y_{t-1}}(y_{t-1})
            }
    \nonumber
    \\
    & = &
        p_{X_{t} \mid Y_{t}}(x_{t} \mid y_{t})
        p_{Y_{t} \mid Y_{t-1}}(y_{t} \mid y_{t-1})
\end{eqnarray}
$$

となってほしい。
最初の等号は、$X_{t-1}$が$Y_{t-1}$で決定されるから、条件付き確率において意味をなさないから？
最後の等号は、$Y_{t}$がマルコフなことによるから？
以上を認めれば以下のようにかける。

$$
\begin{eqnarray}
    p_{X_{1:T}, Y_{1:T}}(x_{1:T}, y_{1:T})
    & = &
        \prod_{t=1}^{T}
            \left(
                p_{X_{t} \mid Y_{t}}(x_{t} \mid y_{t})
                p_{Y_{t} \mid Y_{t-1}}(y_{t} \mid y_{t-1})
            \right)
            p_{X_{1}, Y_{1}}(x_{1}, y_{1})
    \label{HMM_joint_probability_density_function}
\end{eqnarray}
$$

ここでは、潜在変数$Y_{t}$は文の$t$番目のラベル（品詞）で、$X_{t}$は文の$t$番目の単語である。

### 5.2.2 パラメータ推定
HMMにおけるパラメータとは、なんだ？

前述したように、パラメータは最尤推定で求める。
よって$$\eqref{HMM_joint_probability_density_function}$$を$y$について最大化すれば良い。

* $N$,
    * データの個数
* $$(X_{1:T}^{1}, Y_{1:T}^{1}), \ldots, (X_{1:T}^{N}, Y_{1:T}^{N})$$,
    * $$(X_{1:T}, Y_{1:T})$$のi.i.dサンプル
* $$x_{1:T}^{i} := X_{1:T}^{i}(\omega)$$,
    * その実現値がデータとして与えられているとする
* $$y_{1:T}^{i} := Y_{1:T}^{i}(\omega)$$,
    * その実現値がデータとして与えられているとする

とおおく。
まず、$$\eqref{HMM_joint_probability_density_function}$$の対数を取ると

$$
\begin{eqnarray}
    \log p_{X_{1:T}^{1}, Y_{1:T}^{1}, \ldots, X_{1:T}^{N}, Y_{1:T}^{N}}(x_{1:T}, y_{1:T}^{1}, \ldots, x_{1:T}, y_{1:T})
    & = &
        \sum_{i=1}^{N}
            \log p_{X_{1:T}^{i}, Y_{1:T}^{i}}(x_{1:T}^{i}, y_{1:T}^{i})
    \nonumber
    \\
    & = &
        \sum_{i=1}^{N}
            \left[
                \sum_{t=1}^{T} 
                    \log p_{X_{t} \mid Y_{t}}(x_{t}^{i} \mid y_{t}^{i})
                +
                \sum_{t=1}^{T} 
                    \log p_{Y_{t} \mid Y_{t-1}}(y_{t}^{i} \mid y_{t-1}^{i})
                +
                \log p_{X_{1}, Y_{1}}(x_{1}^{i}, y_{1}^{i})
            \right]
    \label{HMM_joint_probability_density_function_of_sample}
\end{eqnarray}
$$

更に、以下を仮定する。

$$
\begin{eqnarray}
    \forall t = 2, \ldots, T,
    & &
        p_{X_{t} \mid Y_{t}}
        =
        p_{X_{t-1} \mid Y_{t-1}},
    \label{HMM_time_homogenous_of_xt_yt}
    \\
    \forall t = 3, \ldots, T,
    & &
        p_{Y_{t} \mid Y_{t-1}}
        =
        p_{Y_{t-1} \mid Y_{t-2}},
    \label{HMM_time_homogenous_of_yt_yt_1}
\end{eqnarray}
$$

つまり、次の系列の確率が$t$に依存しないとする。
$t$が時間の場合は、斉時性(time homogenous)を仮定しているのに等しい。
$$\eqref{HMM_time_homogenous_of_xt_yt}$$, $$\eqref{HMM_time_homogenous_of_yt_yt_1}$$は$t$に依存しないので、改めて

$$
\begin{eqnarray}
    p_{X \mid Y}
    & := &
        p_{X_{t} \mid Y_{t}}
    \label{HMM_time_homogenous_of_x_y}
    \\
    p_{Y \mid Y^{\prime}}
    & := &
        p_{Y_{t} \mid Y_{t-1}},
    \label{HMM_time_homogenous_of_y_yprime}
\end{eqnarray}
$$

とおく。
以上より、$$\eqref{HMM_joint_probability_density_function_of_sample}$$は以下のようにかける。

$$
\begin{eqnarray}
    \log p_{X_{1:T}^{1}, Y_{1:T}^{1}, \ldots, X_{1:T}^{N}, Y_{1:T}^{N}}(x_{1:T}, y_{1:T}^{1}, \ldots, x_{1:T}, y_{1:T})
    & = &
        \sum_{i=1}^{N}
            \left[
                \sum_{t=1}^{T} 
                    \log p_{X \mid Y}(x_{t}^{i} \mid y_{t}^{i})
                +
                \sum_{t=1}^{T} 
                    \log p_{Y \mid Y^{\prime}}(y_{t}^{i} \mid y_{t-1}^{i})
                +
                \log p_{X_{1}, Y_{1}}(x_{1}^{i}, y_{1}^{i})
            \right]
    \nonumber
    \\
    & = &
        \sum_{x \in D_{X}, y \in D_{Y}}
            n(x, y)
                \log p_{X \mid Y}(x \mid y)
        +
        \sum_{y^{\prime} \in D_{Y}, y \in D_{Y}}
            n(y^{\prime}, y)
                \log p_{Y \mid Y^{\prime}}(y \mid y^{\prime})
        +
        \sum_{i=1}^{N}
            \log p_{X_{1}, Y_{1}}(x_{1}^{i}, y_{1}^{i})
    \label{HMM_joint_probability_density_function_of_sample_num}
\end{eqnarray}
$$

ここで、

* $$A_{i,j} := \{i, \ldots, j\}$$,
    * $i$から$j$までの連続値
* $$n(x, y) := \mathrm{card}(\{(i, t) \in A_{1, N} \times A_{1, T} \mid x = x_{t}^{i}, y = y_{t}^{i} \})$$,
    * データ中に単語$x$にラベル$y$がついた回数
* $$n(y^{\prime}, y) := \mathrm{card}(\{(i, t) \in A_{1, N} \times A_{2, T} \mid y^{\prime} = y_{t-1}^{i}, y = y_{t}^{i}\})$$,
    * データ中にラベル$y^{\prime}$の次($t+1$)にラベル$y$がついた回数

である。
後は、$$\eqref{HMM_joint_probability_density_function_of_sample_num}$$を最大化する$$\eqref{HMM_time_homogenous_of_x_y}$$と$$\eqref{HMM_time_homogenous_of_y_yprime}$$を見つければ良い。
これは、

* $$\{p_{X \mid Y}(x \mid y) \}_{x \in D_{X}, y \in D_{Y}}$$,
    * 未知変数
    * $$\mathrm{card}(D_{X}) \times \mathrm{card}(D_{Y})$$個
    * 簡単のため変数を$p(x \mid y)$とかく
* $$\{ p_{Y \mid Y^{\prime}}(y \mid y^{\prime})\}_{y \in D_{Y}, y^{\prime} \in D_{Y}} $$,
    * 未知変数
    * $$\mathrm{card}(D_{Y})^{2}$$個
    * 簡単のため変数を$p(y \mid y^{\prime})$とかく
* $$\{ p_{X_{i} \mid Y_{i}}(x_{1}^{i}, y_{1}^{i})\}_{i = 1, \ldots, N}$$,
    * 未知変数
    * $N$個
    * 簡単のため変数を$p(x_{1}^{i}, y_{1}^{i})$とかく

を変数とする最大化問題である。
確率1の制約を入れて、Lagrangeの未定乗数法でとける。

$$
\begin{eqnarray}
    \sum_{x \in D_{X}} 
        p(x \mid y) - 1
    & = & 
        0
        \quad
        (\forall y \in D_{Y}),
    \nonumber
    \\
    \sum_{x \in D_{X}, y \in D_{Y}} 
        p(x \mid y) - 1
    & = & 
        0,
    \nonumber
    \\
    \sum_{y \in D_{X}} 
        p(y \mid y^{\prime}) - 1
    & = & 
        0
        \quad
        (\forall y^{\prime} \in D_{Y}),
    \nonumber
    \\
    \sum_{y \in D_{Y}, y^{\prime} \in D_{Y}} 
        p(y \mid y^{\prime}) - 1
    & = & 
        0,
    \nonumber
\end{eqnarray}
$$

より、Langrange関数は

$$
\begin{eqnarray}
    L
    :=
    & &
        \sum_{x \in D_{X}, y \in D_{Y}}
            n(x, y)
                \log p_{X \mid Y}(x \mid y)
        +
        \sum_{y^{\prime} \in D_{Y}, y \in D_{Y}}
            n(y^{\prime}, y)
                \log p_{Y \mid Y^{\prime}}(y \mid y^{\prime})
        +
        \sum_{i=1}^{N}
            \log p_{X_{1}, Y_{1}}(x_{1}^{i}, y_{1}^{i})
    \nonumber
    \\
    & - &
        \sum_{y \in D_{Y}}
            \lambda_{y}
            \left(
                \sum_{x \in D_{X}} p(x \mid y)
                -
                1
            \right)
        - \gamma_{1}
            \left(
                \sum_{x \in D_{X}, y \in D_{Y}} p(x \mid y)
                -
                1
            \right)
    \nonumber
    \\
    & - &
        \sum_{y^{\prime} \in D_{Y}}
            \mu_{y^{\prime}}
            \left(
                \sum_{y \in D_{Y}} p(y \mid y^{\prime})
                -
                1
            \right)
        - \gamma_{2}
            \left(
                \sum_{y \in D_{Y}, y^{\prime} \in D_{Y}} p(y \mid y^{\prime})
                -
                1
            \right)
    \nonumber
    \\
    & &
\end{eqnarray}
$$

となる。
微分を計算すると、

$$
\begin{eqnarray}
    \frac{\partial L}{\partial p(\bar{x} \mid \bar{y})} 
    & = &
        \frac{
            n(\bar{x}, \bar{y})
        }{
            p(\bar{x} \mid \bar{y})
        }
        - \lambda_{\bar{y}}
        - \gamma_{1}
    \\
    \frac{\partial L}{\partial p(\bar{y} \mid \bar{y}^{\prime})} 
    & = &
        \frac{
            n(\bar{y}, \bar{y}^{\prime})
        }{
            p(\bar{y} \mid \bar{y}^{\prime})
        }
        - \mu_{\bar{y}^{\prime}}
        - \gamma_{2}
    \\
\end{eqnarray}
$$

である。
KKT条件は

$$
\begin{eqnarray}
    \frac{
        n(x, y)
    }{
        p(x \mid y)
    }
    - \lambda_{y}
    - \gamma_{1}
    & = &
        0
    \label{HMM_KKT_derivative1}
    \\
    \frac{
        n(y, y^{\prime})
    }{
        p(y \mid y^{\prime})
    }
    - \mu_{y^{\prime}}
    - \gamma_{2}
    \label{HMM_KKT_derivative2}
    & = &
        0
    \\
    \lambda_{y}
    \left(
        \sum_{x \in D_{X}}
            p(x \mid y)
        -
        1
    \right)
    & = &
        0
    \label{HMM_KKT_lambda}
    \\
    \mu_{y^{\prime}}
    \left(
        \sum_{y \in D_{Y}}
            p(y \mid y^{\prime})
        -
        1
    \right)
    & = &
        0
    \label{HMM_KKT_mu}
    \\
    \gamma_{1}
    \left(
        \sum_{x \in D_{X}, y \in D_{Y}}
            p(x \mid y)
        -
        1
    \right)
    & = &
        0
    \label{HMM_KKT_gamma1}
    \\        
    \gamma_{2}
    \left(
        \sum_{y \in D_{Y}, y^{\prime} \in D_{Y}}
            p(y \mid y^{\prime})
        -
        1
    \right)
    & = &
        0
    \label{HMM_KKT_gamma2}
\end{eqnarray}
$$

である。
まず、$$\eqref{HMM_KKT_derivative1}$$より

$$
\begin{eqnarray}
    \sum_{x \in D_{X}, y \in D_{Y}}
        n(x, y)
    -
    \sum_{x \in D_{X}, y \in D_{Y}}
        \lambda_{y}
        p(x \mid y)
    & = &
        \gamma_{1}
        \sum_{x \in D_{X}, y \in D_{Y}}
            p(x \mid y)
\end{eqnarray}
$$

また、$$\eqref{HMM_KKT_derivative1}$$ と $$\eqref{HMM_KKT_lambda}$$より

$$
\begin{eqnarray}
    & &
        \sum_{x \in D_{X}}
            n(x, y)
        = 
        (
            \gamma_{1}
            +
            \lambda_{y}
        )
        \sum_{x \in D_{X}}
            p(x \mid y)
    \nonumber
    \\
    & \Leftrightarrow &
        \sum_{x \in D_{X}}
            n(x, y)
        = 
        \gamma_{1}
        \sum_{x \in D_{X}}
            p(x \mid y)
            +
            \lambda_{y}
\end{eqnarray}
$$

これを$$\eqref{HMM_KKT_gamma1}$$に代入すると

$$
\begin{eqnarray}
    & &
        \lambda_{y}    
        \left(
            \frac{
                \sum_{x \in D_{X}}
                    n(x, y)
            }{
                (\gamma_{1} + \lambda_{y})
            }
            -
            1
        \right)
        =
        0
    \\
    & \Leftrightarrow &
        \sum_{x \in D_{X}}
            n(x, y)
        =
        \lambda_{y}
        +
        \gamma_{1}
\end{eqnarray}
$$

以下のようになる。

$$
\begin{eqnarray}
    p_{X_{t} \mid Y_{t}}(x \mid y)
    & := &
        \frac{
            n(x, y)
        }{
            \sum_{\bar{x} \in D_{x}} 
                n(\bar{x}, y)
        }
    \\
    p_{Y_{t} \mid Y_{t-1}}(y^{\prime} \mid y)
    & := &
        \frac{
            n_{y_{t} \mid y_{t-1}}(y^{\prime}, y)
        }{
            \sum_{\bar{y} \in D_{Y}} 
                n_{y^{\prime} \mid y}(y^{\prime}, y)
        }
\end{eqnarray}
$$

### 5.2.3 HMMの推論
文（単語の列）$x_{1:T}$を与えた時の予測を考える。
ここでは、同時確率を最大とするようなラベルを予測として出力する。
つまり、

$$
\begin{equation}
    y_{1:T}^{\max}
    :=
    \argmax_{y_{1:T}} p_{X_{1:T}, Y_{1:T}}(x_{1:T}, y_{1:T})
\end{equation}
$$

とする。
ラベルの組み合わせは、ラベル数の$T$乗に比例するので、全列挙で計算することはできない。
よって、動的計画法を用いたViterbi algorithmを用いる。
以降はアンダーフローを避けるために、対数をとった確率を考える。

$$\eqref{HMM_joint_probability_density_function_2}$$から以下を最大化すれば良い。　


$$
\begin{eqnarray}
    \log p_{X_{1:T}, Y_{1:T}}(x_{1:T}, y_{1:T})
    & = &
        \sum_{t=2}^{T} 
            p_{X_{t}, Y_{t} \mid X_{t-1}, Y_{t-1}}(x_{t}, y_{t} \mid x_{t-1}, y_{t-1})
        + 
        p_{X_{1}, Y_{1}}(x_{1}, y_{1})
\end{eqnarray}
$$

## 5.4 条件付き確率場
条件付き確率場は対数線形モデル。
対数線形でないといけない理由はなさそうだが？
確率を扱いたいから対数線形（ロジスティック）にしてるだけのよう。

## 5.4.1 条件付き確率場の導入
Conditional Random Fields でCRFとも言われる。

* $$X_{1:T} := (X_{1}, \ldots, X_{T})$$,
    * $T$個の単語の列
    * 一般には文
    * $T$が添字に付いているが、HMMのように必ずしも時系列性を考慮しているわけではないので、$T$次元の確率変数のベクトルと思っても良い
* $$Y_{1:T} := (Y_{1}, \ldots, Y_{T})$$,
    * $$\forall t = 1, \ldots, T, Y_{t}:\Omega \rightarrow \{1, \ldots, K\}$$と仮定する
        * 離散値に値をとることは重要
        * 各$t$について1から$K$は、特に一般性を失わないので仮定している(離散値なので最大値へ拡張すれば良い）
    * 単語に対応する品詞のラベル
    * 一般には文の各単語のラベル
    * $T$が添字に付いているが、HMMのように必ずしも時系列性を考慮しているわけではないので、$T$次元の確率変数のベクトルと思っても良い

$Y$のとる値の集合を以下のように定義しておく

データとして$$X_{1:T}$$, $$Y_{1:T}$$の独立同分布な確率変数の実現値が与えられているとする。
つまり、

* $$(X_{1:T}^{i})_{i} \quad (\forall i = 1, \ldots, N)$$,
    * $X$のi.i.d
* $$(Y_{1:T}^{i})_{i} \quad (\forall i = 1, \ldots, N)$$,
    * $Y$のi.i.d

$$
\begin{eqnarray}
    p_{Y_{1:T} \mid X_{1:T}}( y_{1:T} \mid x_{1:T})
    & := &
        \frac{
            \exp
            \left(
                (w_{1:T})^{\mathrm{T}}
                \phi(x_{1:T}, y_{1:T})
            \right)
        }{
            Z(x_{1:T}, w_{1:T})
        },
    \\
    Z(x_{1:T}, w_{1:T})
    & := &
        \sum_{y_{1:T} \in \{1, \ldots, K\}^{T}}
            \exp
            \left(
                (w_{1:T})^{\mathrm{T}}
                \phi(x_{1:T}, y_{1:T})
            \right)
\end{eqnarray}
$$

とする。
ここで、$w_{1:T}$は素性に対する重みベクトルで、訓練データから学習し決定する。
$\phi(\cdot, \cdot)$は、4章導入した単語と単語ラベルから素性を対応づける適当な関数である。

$\phi$を適当に与え、$w_{1:T}$を学習で求めれば、CRFでの予測が可能となる。
CRFでは、同時確率を最大にするものを次の予測とする。
つまり、単語列$x_{1:T}$が与えられた時、そのラベル列を

$$
\begin{eqnarray}
    y_{1:T}^{*}
    & := &
        \argmax_{y_{1:T}}
            p_{Y_{1:T} \mid X_{1:T}}( y_{1:T} \mid x_{1:T})
    \nonumber
    \\
    & = &
        \argmax_{y_{1:T}}
            \frac{
                \exp
                \left(
                    (w_{1:T})^{\mathrm{T}}
                    \phi(x_{1:T}, y_{1:T})
                \right)
            }{
                Z(x_{1:T}, w_{1:T})
            },
    \nonumber
    \\
    & = &
        \argmax_{y_{1:T}}
            (w_{1:T})^{\mathrm{T}}
                \phi(x_{1:T}, y_{1:T})
    \label{CRF_argmax_conditional_probability}
\end{eqnarray}
$$

として予測する。
$y_{1:T}$は$T$次元だから$y_{t}$の取る値の数$K$だけある。
上記の最大化は$O(K^{T})$で計算できるが、$K$はラベルの数、$T$は単語の列の長さとなって現実的でない。

上記の最大化の計算のために、仮定をおく。
仮定の置き方は色々考えられるが、ここでは$$\phi(x_{1:T}, y_{1:T})$$について以下の仮定をおく。

$$
    \phi(x_{1:T}, y_{1:T})
    =
    \sum_{t=2}^{T} 
        \phi(x_{1:T}, y_{t-1}, y_{t})
$$

つまり、$$\phi$$は$$y_{1:T}$$については2変数(2である必要は必ずしもない）についてしか依存せず、その和で$$\phi(x_{1:T}, y_{1:T})$$が表現されているとする。
以上の仮定をおけば、$$\eqref{CRF_argmax_conditional_probability}$$は

$$
\begin{eqnarray}
    (w_{1:T})^{\mathrm{T}}
        \phi(x_{1:T}, y_{1:T})
    & = &
        \sum_{t=2}^{T}
            (w_{1:T})^{\mathrm{T}}
                \phi(x_{1:T}, y_{t-1}, y_{t})
\end{eqnarray}
$$

とかける。
これはHMMのViterbiアルゴリズムと同様に動的計画法でとける。

### 5.4.2 条件付き確率場の学習
$w$の学習方法について触れる。
CRFは対数線形モデルなので、通常の一般化線形モデルの学習と同様の方法で学習できる。
つまり、

$$
    L(w)
    :=
    \sum_{i=1}^{N} 
        \log p_{Y_{1:T} \mid X_{1:T}}(y_{1:T}^{i} \mid x_{1:T}^{i})
        -
        \lambda \|w \|_{2}^{2}
$$

を$w$について最大化する問題を解く。
第二項は正則化項でここでは$l^{2}$正則化である。
正則化が$l^{2}$でなければならない理由はないが、ここでは$l^{2}$とする。
本では最急勾配法で最小化する方法が記載されているが、最急勾配法に限る必要はない。
一般に、微分を用いる最大化方法について注意すべき点を述べる。

$$
\begin{eqnarray}
    \log p_{Y_{1:T} \mid X_{1:T}}(y_{1:T}^{i} \mid x_{1:T}^{i})
    & = &
        (w_{1:T}^{i})^{\mathrm{T}} \phi(x_{1:T}^{i}, y_{1:T}^{i})
        -
        Z(x_{1:T}^{i}, w_{1:T})
    \nonumber
\end{eqnarray}
$$

より$w$についての微分を考えると、


