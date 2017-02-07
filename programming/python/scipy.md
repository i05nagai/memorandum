# scipy

## install

### OSX
fortranのcompilerが入っていないと`pip`でも入らない。
`gcc`をインストールすれば`gfortran`が入るのでインストール可能。

```shell
homebrew install gcc
```

#### reference
* [Building From Source on Mac OSX — SciPy.org](http://www.scipy.org/scipylib/building/macosx.html)



## stats

### norm
正規分布関数の逆関数。
percentile点を求める。

```python
from scipy.stats import norm
norm.ppf(q, loc=0, scale=1)
```

正規分布のpdf

```python
from scipy.stats import norm
norm.pdf(q, loc=0, scale=1)
```

正規分布のcdf

```python
from scipy.stats import norm
norm.cdf(x, loc=0, scale=1)
```

## optimize

### L-BFGS-B
一次元でも初期値と目的関数の入力は、`list`か、`numpy.array`にする。
Jacobian matrixを返す関数の返り値は`numpy.array`にする。

