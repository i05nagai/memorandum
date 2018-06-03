---
title: jekyll-jupyter-notebook
---

## jekyll-jupyter-notebook

## Install

```Gemfile
gem "jekyll-jupyter-notebook"
```


```yaml
plugins:
- jekyll-jupyter-notebook
```

Then you write your markdown file


```
{% raw  %}
{% jupyter_notebook sample.ipynb %}
{% endraw %}
```

or if you use `kramdown` as markdonw parser, you write

```
{% raw  %}
{::nomarkdown}
{% jupyter_notebook sample.ipynb %}
{:/nomarkdown}
{% endraw %}
```

## Reference
* [red\-data\-tools/jekyll\-jupyter\-notebook: Jekyll Jupyter Notebook plugin](https://github.com/red-data-tools/jekyll-jupyter-notebook)
