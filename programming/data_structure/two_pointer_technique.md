---
title: Two Pointer Technique
---

## Two Pointer Technique
* Calculate summation of subsequence in constant-time. It's worths consder whether the condition can be written in summation form.
* It is also known as Caterpillar method


## Example
* $a_{0}, \ldots, a_{n-1}$,
    * $a_{i} \in \mathbb{N}$,
* $S \in \mathbb{N}$,

Let $I(s)$ be the first index after $s$ to which summation from $s$ is over S.

$$
    I(s)
    :=
    \arg\min
        \{
            j \ge s
            \mid
            \sum_{i=s:j}
                a_{i}
            \ge
            S
        \}
    .
$$

Then

$$
    \sum_{i \in [s+1:I(s)-1]}
        a_{i}
    <
    \sum_{i \in [s:I(s)-1]}
        a_{i}
    <
    S
    .
$$

Thus,

$$
\begin{equation}
    I(s)
    \le
    I(s+1)
    \label{two_pointer_technique_relation}
\end{equation}
    .
$$

The problem is to find

$$
    \min\{
        I(s) - s
        \mid
        s \in [0:n)
    \}
    .
$$

Since $$\eqref{two_pointer_technique_relation}$$, if we find $I(s)$, $I(s+1)$ is in $[I(s), n)$.
We hold the value of $s$ and $I(s)$, then 

## Generalize
We can generalize this discussion as binary search.
Let $I(s)$ be the first index after $s$ to which subsequence from $s$ satifsfy Condition $C$.

$$
    I(s)
    :=
    \arg\min
        \{
            j \ge s
            \mid
            C([s:j])
        \}
    .
$$

Suppose that for some $s \le j$,

$$
    C([s+1:j])
    \Rightarrow
    C([s:j])
    .
$$

Thus,

$$
\begin{equation}
    I(s)
    \le
    I(s+1)
\end{equation}
    .
$$

Indeed, by our assumption,

$$
    C([s+1:I(s+1)]
    \Rightarrow
    C([s:I(s+1)]
    .
$$

## Reference
* [Two Pointers Technique - GeeksforGeeks](https://www.geeksforgeeks.org/two-pointers-technique/)
* [13\-CaterpillarMethod](https://codility.com/media/train/13-CaterpillarMethod.pdf)
