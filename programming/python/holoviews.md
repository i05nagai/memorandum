---
title: HoloViews
---

## HoloViews

```
pip install 'holoviews[recommended]'
pip install matplotlib bokeh plotly
```

setup backend.

```
import holoviews as hv
hv.extension('matplotlib')
```

Scatter plotting

```
xs = []
ys = []
paths = hv.Points((xs, ys))
```



## Reference
* [HoloViews — HoloViews](http://holoviews.org/)
* [Pythonの可視化ツールはHoloViewsが標準になるかもしれない - Qiita](http://qiita.com/driller/items/53be86cea3c3201e7e0f)

