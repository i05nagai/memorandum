---
title: ipywidgets
---

## ipywidgets
IPython widgets for the jupyter notebook

```
pip install ipywidgets
jupyter nbextension enable --py --sys-prefix widgetsnbextension
```

## Usage

```python
import ipywidgets
# upepr, lower, default
@ipywidgets.interact(x=(-10, 10, 2))
def f(x):
    print(x)
```

```python
import ipywidgets
# upepr, lower, default
@ipywidgets.interact(x=(0.0, 1.0, 0.2))
def f(x):
    print(x)
```

## Reference
* [jupyter-widgets/ipywidgets: IPython widgets for the Jupyter Notebook](https://github.com/jupyter-widgets/ipywidgets)
