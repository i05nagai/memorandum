---
title: GeoViews
---

## GeoViews

```
conda create -n env-name -c pyviz -c conda-forge geoviews iris xesmf
conda activate env-name
```

## Usage

```
gv.extension('matplotlib', 'bokeh')
%output dpi=120 fig='svg'
```

## Reference
* [GeoViews — GeoViews 1\.5\.0\+g63ddd7c\-dirty documentation](http://geo.holoviews.org/)
* https://github.com/ioam/jupytercon2017-holoviews-tutorial/blob/master/notebooks/09-working-with-large-datasets.ipynb

