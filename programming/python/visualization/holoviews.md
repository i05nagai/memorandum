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


## image
* http://holoviews.org/reference/elements/bokeh/Image.html

## RGB
* http://holoviews.org/reference/elements/bokeh/RGB.html

```
hv.RGB.load_image('../assets/penguins.png')
```

## Reference
* [HoloViews — HoloViews](http://holoviews.org/)
* [Pythonの可視化ツールはHoloViewsが標準になるかもしれない - Qiita](http://qiita.com/driller/items/53be86cea3c3201e7e0f)

