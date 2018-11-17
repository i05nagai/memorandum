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

## Tables


```python
n = np.arange(1000)
xs = np.repeat(range(2), 500)
ys = n%4
zs = np.random.randn(1000)
hv.Table((xs, ys, zs), kdims=['x', 'y'], vdims=['z'])
```

* name
    * short alias
* label
    * descriptive label

```python
key_dimensions = [
    # name, label
    ('year', 'Year'),
    ('country', 'Country')
]
value_dimensions = [
    ('unem', 'Unemployment'),
    ('capmob', 'Capital Mobility'),
    ('gdp', 'GDP Growth'),
    ('trade', 'Trade')
]
macro = hv.Table(macro_df, kdims=key_dimensions, vdims=value_dimensions)
```

## Curve

```
hv.Overlay([ hv.Curve((x,y)),  hv.Curve((x ,y + y))])
```

## Table
[Pandas Conversion — HoloViews](http://build.holoviews.org/Tutorials/Pandas_Conversion.html)

## Tips

### Secondary axis
* [Twin axis · Issue \#396 · ioam/holoviews](https://github.com/ioam/holoviews/issues/396)

## Reference
* [HoloViews — HoloViews](http://holoviews.org/)
* [Pythonの可視化ツールはHoloViewsが標準になるかもしれない - Qiita](http://qiita.com/driller/items/53be86cea3c3201e7e0f)

