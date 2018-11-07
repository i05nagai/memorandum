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

* $$\mathcal{X}$$,
    * the domain of inputs
* $$\mathcal{Y} := \{0, 1\}$$,
* $f: \mathcal{X} \rightarrow \mathcal{Y}$,
    * prediction model
* $n \in \mathbb{N}$,
    * the number of data
* $$\{(x_{i}, y_{i})\}_{i=1,\ldots,n} \subseteq \mathcal{X} \times \mathcal{Y}$$,

$$
\begin{eqnarray}
    \mathrm{TP}
    & := &
        \sum_{i=1}^{n}
            1_{\{
                f(x_{i}) + y_{i}
                =
                2
            \}}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            1_{\{
                f(x_{i}) = 1
            \}}
            1_{\{
                y_{i} = 1
            \}}
    \nonumber
    \\
    \mathrm{TN}
    & := &
        \sum_{i=1}^{n}
            1_{\{
                f(x_{i}) = 0
            \}}
            1_{\{
                y_{i} = 0
            \}}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            \left(
                1
                -
                1_{\{
                    f(x_{i}) = 1
                \}}
            \right)
            1_{\{
                y_{i} = 0
            \}}
    \nonumber
    \\
    & = &
        \sum_{i=1}^{n}
            1_{\{
                y_{i} = 0
            \}}
        -
        \mathrm{FP}
    \nonumber
    \\
    \mathrm{FP}
    & := &
        \sum_{i=1}^{n}
            1_{\{
                f(x_{i}) = 1
            \}}
            1_{\{
                y_{i} = 0
            \}}
    \nonumber
    \\
    \mathrm{FN}
    & := &
        \sum_{i=1}^{n}
            1_{\{
                f(x_{i}) = 0
            \}}
            1_{\{
                y_{i} = 1
            \}}
    \nonumber
\end{eqnarray}
    .
$$

* true positive
    * the number of samples which has label 1 and is indentified as 1 by the model
    * the model correctly predicts the data belongs to 1 class
* true negative
    * the number of samples which has label 0 and is indentified as 0 by the model
    * the model correctly predicts the data belongs to 0 class
* False Positive
    * falsly choose positve class
    * the number of samples which has label 0 and is identified as 1 by the model
    * the model predicts positive class but it turns out negative
* False Negative
    * falsly choose negative class
    * the number of samples which has label 1 and is identified as 0 by the model
    * the model predicts negative class but it turns out positive

$$
\begin{eqnarray}
    \mathrm{Acc}
    & := &
        \frac{
            \mathrm{TP}
            +
            \mathrm{TN}
        }{
            \mathrm{TP}
            +
            \mathrm{TN}
            +
            \mathrm{FP}
            +
            \mathrm{FN}
        }
    \nonumber
    \\
    & = &
        \frac{
            \mathrm{TP}
            +
            \mathrm{TN}
        }{
            n
        }
    \nonumber
    \\
    \mathrm{Precsion}
    & = &
        \frac{
            \mathrm{TP}
        }{
            \mathrm{TP}
            +
            \mathrm{FP}
        }
    \nonumber
    \\
    \mathrm{Recall}
    & = &
        \frac{
            \mathrm{TP}
        }{
            \mathrm{TP}
            +
            \mathrm{FN}
        }
\end{eqnarray}
$$

* accuracy
    * True Positive plus True Negative over all data
    * (TP + TN) over (TP + TN + FP + FN)
    * the number of correct predictions over total number of predictions
    * high accuracy means that 
* precision
    * True Positive over the number of predictions predicted as Positve class
    * TP over TP + FP
    * The value of precision is lower may mean the model predicts positive class too much
* recall
    * True Positve Rate
    * True Positive over the number of positive classes in data
    * TP over TP + FN
    * The value of recall is lower may mean that the model predicts negative class too much

$$
\begin{eqnarray}
    \mathrm{FPR}
    & := &
        \frac{
            \mathrm{FP}
        }{
            \mathrm{FP}
            +
            \mathrm{TN}
        }
    \nonumber
    \\
    \mathrm{FDR}
    & := &
        \frac{
            \mathrm{FP}
        }{
            \mathrm{FN}
            +
            \mathrm{TP}
        }
\end{eqnarray}
$$

* False Positive Rate
    * FP over FP + TN
    * high False Positive Rate means that the model fail to predict negative class more
* False Discovery Rate
    * FP over FN + TP
* Receiver Operating Characteristic curve
    * draw curve whose x axis is FP rate and whose y axis is TP rate by changing the threshold of the binary-prediction model
* Area Under the Curve
* ROC-AUC
* Accuracy
* Log-Loss
* F1-score

Unsupervisised

* Rand index
* Mutual Information

Others

* CV Error
* Heuristic methods to find K
* Bilingual Evaluation Understudy

## Reference
* [Choosing the Right Metric for Evaluating Machine Learning Models  –  Part 1](https://www.kdnuggets.com/2018/04/right-metric-evaluating-machine-learning-models-1.html)
* [F1 score \- Wikipedia](https://en.wikipedia.org/wiki/F1_score)
* [machine learning \- What if high validation accuracy but low test accuracy in research? \- Cross Validated](https://stats.stackexchange.com/questions/147786/what-if-high-validation-accuracy-but-low-test-accuracy-in-research)
