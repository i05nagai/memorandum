---
title: Maxima
---

## Maxima

## Install

```
brew install maxima
brew install wxmaxima
```

## Commands

Define functions

```
f(x,y):=(a*x^2 + b*x*y);
```

Calculate hessian matrix

```
hessian(f(x, y), [x, y]);
```

Eigen values

```
A: matrix([1, 1], [1, 1]);
eigenvalues(A)
# [[eigenvalues], [multiplicity of eigenvalues]]
```

Eigen values

```
A: matrix([1, 1], [1, 1]);
eigenvectors(A);
# [[[固有値のリスト], [解空間の次元のリスト]], [固有ベクタのリスト]]
```

## Reference
