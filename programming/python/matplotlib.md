---
title: matplotlib
---

## matplotlib

## pyplot

## Install

### pyenvで動かす

`matplotlibrc`の38行目の

```
backend : macosx
```

これを

```
backend : Tkagg
```

に変更。
`matplotlibrc`の場所は以下のコマンドでわかる。

```shell
$python -c "import matplotlib;print(matplotlib.matplotlib_fname())"
```

* 行列のマス目で描画
    * [pyplot — Matplotlib 2.0.0 documentation](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.matshow)

```python
mat = [[]]
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(mat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va="center", ha="center")
plt.xlabel("predicted label")
plt.ylabel("true label")
plt.show()
```

## samples

```python
import scipy.misc as misc
import matplotlib.pyplot as pyplot
n_coin = 20
prob = 0.5
def pdf(x):
    return misc.comb(n_coin, x) * (prob ** x)* ((1 - prob) ** (n_coin - x))
xs = [i for i in range(n_coin)]
ys = [pdf(x) for x in xs]
pyplot.plot(xs, ys)
pyplot.show()
```

## features
* `pyplot.contourf`
    * 境界線を描く
    * [pyplot — Matplotlib 2.0.0 documentation](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.contourf)
* `pyplot.axhline`
    * Add a horizontal line across the axis
    * [pyplot — Matplotlib 2.0.0 documentation](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.contourf)

### Reference
* [pyenvとvirtualenvで環境構築した時にmatplotlib.pyplotが使えなかった時の対処法 - Qiita](http://qiita.com/Kodaira_/items/1a3b801c7a5a41c9ce49)

# Reference
* [matplotlib入門 - りんごがでている](http://bicycle1885.hatenablog.com/entry/2014/02/14/023734)


