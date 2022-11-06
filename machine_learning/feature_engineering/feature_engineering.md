---
title: Feature Engineering
---

## Feature Engineering

* emsemble
    * [Kaggle Ensembling Guide \| MLWave](https://mlwave.com/kaggle-ensembling-guide/)
    * Stacking
    * Blending
    * Stacknet
        * [h2oai/pystacknet](https://github.com/h2oai/pystacknet)

## Preprocessing

#### Data cleaning

- Get rid of the corresponding instance
- Get rid of the whole attribute.
- interpolate the missing value
    - Set the values to some value (zero, the mean, the median, etc.).

```
df.dropna(subset=["attr1"]) # option 1

df.drop("attr1", axis=1) # option 2

median = df["attr1"].median() # option 3
df["attr1"].fillna(median, inplace=True)
```

## Reference
* [Best Practices for Feature Engineering](https://elitedatascience.com/feature-engineering-best-practices)
