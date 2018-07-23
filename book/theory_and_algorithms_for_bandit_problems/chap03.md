---
title: Theory and Algorithms for Bandit Problems
book_title: Theory and Algorithms for Bandit Problems
book_chapter: 3
---

# 3 確率的バンディット問題の方策

regretを最小にするような選択肢$I_{T} \in \mathcal{A}_{T}$を決めるのがバンディット問題。


## 3.1 定式化

## 3.2 理論限界

## 3.3 $\epsilon$-貪欲法

## 3.4 尤度に基づく方策

## 3.5 確率一致方法とトンプソン抽出

### 3.5.2 Thompson Sampling


#### Algorithm 3.4
* $\alpha > 0$,
    * parameter
* $\beta > 0$,
    * parameter
* $T \in \mathbb{N}$,
    * given
* $K$,
    * the number of arms

The steps in algorithm

* Step1. For each arm $i$, $n_{i} \leftarrow 0$, $m_{i} \leftarrow 0$,
* Step2. for $t = 1, \ldots, T$ do
    * Step3. Generate sample $\tilde{\mu}_{i}$ from beta distribution $$\mathrm{Beta}(\alpha + m_{i}, \beta + n_{i} - m_{i})$$ for each arm $i$,
    * Step4. $$i_{t} \leftarrow \mathop{\rm arg\,max}\limits_{i \in \{1, \ldots, K\}} \tilde{\mu}_{i}$$,
    * Step5. Observe the reward $$X_{i_{t}}(t) \in \{0, 1\}$$ from  arm $i_{t}$,
    * Step6. $$n_{i_{t}} \leftarrow n_{i_{t}} + 1$$, $$m_{i_{t}} \leftarrow m_{i_{t}} + X_{i_{t}}(t)$$,
* Step7. end for


<div class="end-of-statement" style="text-align: right">■</div>
