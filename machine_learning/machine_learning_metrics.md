---
title: Machine Learning Metrics
---

## Machine Learning Metrics


Regression

* Root Mean Square Error

$$
    \sqrt{
        \frac{ 1 }{ n }
        \sum_{i=1}^{n}
            (y_{i} - y_{i})^{2}
    }
$$

* Mean Absolute Error

$$
    \frac{ 1 }{ n }
    \sum_{i=1}^{n}
        |y_{i} - y_{i}|
$$

* Mean Error

$$
    \frac{ 1 }{ n }
    \sum_{i=1}^{n}
        (y_{i} - y_{i})
$$

* R Square
* Adjusted R Square

Classification

* Precision-Recall
* ROC-AUC
* Accuracy
* Log-Loss

Unsupervisised

* Rand index
* Mutual Information

Others

* CV Error
* Heuristic methods to find K
* Bilingual Evaluation Understudy

## Reference
* [Choosing the Right Metric for Evaluating Machine Learning Models  –  Part 1](https://www.kdnuggets.com/2018/04/right-metric-evaluating-machine-learning-models-1.html)
