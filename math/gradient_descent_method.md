---
layout: math
title: Gradient Descent Method
---

# Gradient Descent Method
Steepest descentとも言う。
関数（ポテンシャル面）の傾き（一階微分）のみから、関数の最小値を探索する連続最適化問題の勾配法のアルゴリズムの一つ

## Symbol
* $x = (x_{1}, \ldots, x_{N})^{T} \in \mathbb{R}^{N}$

## Definition
* $f^{i}(\cdot) := f(\cdot; \theta_{i}): \mathbb{R}^{N} \rightarrow \mathbb{R} (\forall i = 1, \ldots, M)$
    * $\theta_{i} \in \mathbb{R}^{K}$をパラメータとする$N$変数関数
* $f(\cdot) = (f^{1}(\cdot), \ldots, f^{M}(\cdot))^{T}: \mathbb{R}^{N} \rightarrow \mathbb{R}^{M} $
    * $\theta \in \mathbb{R}^{K}$をパラメータとする$N$変数$M$次元ベクトル値関数

## Problem
以下の問題を考える。

$$
\begin{equation}
    S(x) 
        := \sum_{i=1}^{M} r^{i}(x)^{2}
        := \sum_{i=1}^{M} \left( y^{i} - f^{i}(x) \right)^{2}  \in \mathbb{R}
\end{equation}
$$

ここで、$y = (y^{1}, \ldots, y^{M}) \in \mathbb{R}^{M}$である。
$r(x) = (r^{1}(x), \ldots, r^{M}(x))$は残差を表し、$r^{i}(x) = y^{i} - f^{i}(x)$である。


またベクトル表記で

$$
\begin{equation}
S(x) 
    = \left\| r(x) \right\|^{2}
    = \left\| y - f(x) \right\|^{2}
\end{equation}
$$

とも書く。

## Theory

## Algorithm

## reference
* [Gradient descent - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Gradient_descent)
* [最急降下法 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%9C%80%E6%80%A5%E9%99%8D%E4%B8%8B%E6%B3%95)

