---
title: Display Advertising
---

## Display Advertising



Targeting

* Estimating value of an impression
    * Behavioral Targeting
    * Contextual Targeting
    * Creative optimization

* Estimating CTR
    * Budgeted Multi-armed Bandit
* Probability of Conversion
* Long-term vs Short-term value of display ads?


Online Allocation


* Online Stochastic Assignment Problems
    * Online Stochastic Matching
    * Online Stochastic Packing
    * Online Generalized Assignment with free disposal
    * Experimental Results
* Online Learning and Allocation


Common Parameters

* $N \in \mathbb{N}$,
    * the number of pages
* $$I := \{1, \ldots, N\}$$,
    * pages (impressions)
* $M \in \mathbb{N}$,
    * the number of ads
* $$A := \{1, \ldots, M\}$$,
    * ads


#### Online matching
Variables

* $$x_{i, a} \in [0, 1] \ (a \in A, i \in I)$$,
    * allocates ad $a$ to page $i$ at rate $x_{i, a}$

$$
\begin{align}
    \max_{x_{i, a}}
    & & &
        \sum_{i \in I, a \in A}
            x_{i, a}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \sum_{i \in I}
            x_{i, a}
        \le
        C_{a}
        \quad
        (\forall a \in A)
    \nonumber
    \\
    & & &
        x_{i, a}
        \in
        \{0, 1\}
        \quad
        (\forall a \in A, \forall i \in I)
\end{align}
$$

<div class="end-of-statement" style="text-align: right">■</div>


#### Display ad problemns
Parameters

* $v_{i, a} \in \mathbb{R}$,
    * the value of ad $a$ if it is allocated in page $i$,
    * e.g. click probability
* $C_{a} \in \mathbb{N}$,
    * capacity of ad $a$

Variables

* $$x_{i, a} \in [0, 1] \ (a \in A, i \in I)$$,
    * allocates ad $a$ to page $i$ at rate $x_{i, a}$

$$
\begin{align}
    \max_{x_{i, a}}
    & & &
        \sum_{i \in I, a \in A}
            v_{i, a}
            x_{i, a}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \sum_{a \in A}
            x_{i, a}
        \le
        1
        & &
        (\forall i \in I)
    \nonumber
    \\
    & & &
        \sum_{i \in I}
            x_{i, a}
        \le
        C_{a}
        & &
        (\forall a \in A)
    \nonumber
\end{align}
$$

The second constraint restricts the number of impressions(allocation) of ad $a$.

<div class="end-of-statement" style="text-align: right">■</div>

#### AdWords Problem
Parameters

* $b_{i, a} \in \mathbb{R}$,
    * bid
* $B_{a} \in \mathbb{R}$,
    * budget of ad $a$,

Variables

* $$x_{i, a} \in [0, 1] \ (a \in A, i \in I)$$,
    * allocates ad $a$ to page $i$ at rate $x_{i, a}$

$$
\begin{align}
    \max_{x_{i, a}}
    & & &
        \sum_{i \in I, a \in A}
            b_{i, a}
            x_{i, a}
    \nonumber
    \\
    \mathrm{subject\ to}
    & & &
        \sum_{a \in A}
            x_{i, a}
        \le
        1
        & &
        (\forall i \in I)
    \nonumber
    \\
    & & &
        \sum_{i \in I}
            b_{i, a}
            x_{i, a}
        \le
        B_{a}
        & &
        (\forall a \in A)
    \nonumber
\end{align}
$$

<div class="end-of-statement" style="text-align: right">■</div>

* Worst case
    * $1 - 1/e$ approximation
* Worst case

## Reference
* Mehta, A., & Mirrokni, V. (2011). Online Ad Serving: Theory and Practice.
* Agrawal, S., Wang, Z., & Ye, Y. (2009). A Dynamic Near-Optimal Algorithm for Online Linear Programming, 1–22. https://doi.org/10.1287/opre.2014.1289
* Devanur, N. R., & Hayes, T. P. (2009). The Adwords Problem: Online Keyword Matching with Budgeted Bidders under Random Permutations. Science, 71–78. https://doi.org/10.1145/1566374.1566384
* Feldman, J., Henzinger, M., Korula, N., Mirrokni, V. S., & Stein, C. (2010). Online stochastic packing applied to display ad allocation. Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 6346 LNCS(PART 1), 182–194. https://doi.org/10.1007/978-3-642-15775-2_16
* Feldman, J., Korula, N., Mirrokni, V., Muthukrishnan, S., & Pál, M. (2009). Online Ad assignment with free disposal. Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 5929 LNCS, 374–385. https://doi.org/10.1007/978-3-642-10841-9_34
* Karp, R. M., Vazirani, U. V., & Vazirani, V. V. (1990). An optimal algorithm for on-line bipartite matching. Proceedings of the Twenty-Second Annual ACM Symposium on Theory of Computing  - STOC ’90, 352–358. https://doi.org/10.1145/100216.100262
* Mehta, A., Saberi, A., Vazirani, U., & Vazirani, V. (2007). AdWords and Generalized On-line Matching. 46th Annual IEEE Symposium on Foundations of Computer Science (FOCS’05), V(August), 264–273. https://doi.org/10.1109/SFCS.2005.12
* Tan, B., & Srikant, R. (2010). Online Advertisement, Optimization and Stochastic Networks, 1–32. Retrieved from http://arxiv.org/abs/1009.0870
