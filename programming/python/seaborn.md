---
title: seaborn
---

## seaborn


## Tips

### 特徴量ごとに散布図かきたい
* `pairplot(df[cols], size=2.5)`

```python
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style="whitegrid", context="notebook")
cols = ["LSTAT", "INDUS", "NOX", "RM", "MEDV"]
seaborn.pairplot(df[cols], size=2.5)
plt.show()
```

### heatmapをかきたい

```python
import numpy as np
cm = np.corrcoef(df[cols].values.T)
seaborn.set(font_scale=1.5)
hm = seaborn.heatmap(cm, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 15}, yticklabels=cols, xticklabels=cols)
plt.show()
```

* `cbar`
    * colorbarをつけるかどうか
* `annot`
    * cellに値を表示するかどうか
* `square`
    * cellを正方形で表示するかどうか
* `fmt`
    * `annot`がTrueのときに表示する値のフォーマット
* `annot_kws`
    * ax.t


## reference
* [API reference — seaborn 0.7.1 documentation](http://seaborn.pydata.org/api.html)
* [pythonで美しいグラフ描画 -seabornを使えばデータ分析と可視化が捗る その1 - Qiita](http://qiita.com/hik0107/items/3dc541158fceb3156ee0)

