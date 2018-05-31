---
title: wheel
---

## wheel
built package.

* universal wheel
    * wheels that are pure Python (i.e. contain no compiled extensions) and support Python 2 and 3. 
* Pure Python Wheels
    * wheels taht are pure Python
* platform wheels
    * wheels that are specific to a certain platform like Linux, macOS, or Windows, usually due to containing compiled extensions.

## Install

```
pip install wheel
```

## Usage
build the universal wheel

```
python setup.py bdist_wheel --universal
```

or in `setup.cfg`

```cfg
[bdist_wheel]
universal=1
```

Create Pure python wheels

```
python setup.py bdist_wheel
```

Create platform wheel

```
python setup.py bdist_wheel
```

## Reference
