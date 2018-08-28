---
title: Interview Question Data Scientist
---

## Interview Question Data Scientist

* A/B Tests
* Maths / stats
* Machine learning experience
* Analytics experience
* true positive
    * the number of predition is true.
    * the model predicts positive class
* true negative
    * the number of predition is false and the model predicts negative class
    * the model predicts negative class
* False Positive
    * falsly choose positve class
    * the number of predition is false negative class and the model predicts postive class
    * the model predicts positive class but it's actually negative
* False Negative
    * falsly choose negative class
    * the number of predition is false to predict negative classs.
    * the model predicts negative class but it's actually positive
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
* False Positive Rate
    * FP over FP + TN
    * high False Positive Rate means that the model fail to predict negative class more
* Receiver Operating Characteristic curve
    * draw curve whose x axis is FP rate and whose y axis is TP rate by changing the threshold of the binary-prediction model
* Area Under the Curve

## Reference
