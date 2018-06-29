---
title: Packaging
---

## Packaging

* source distributions
    * unbuit source code

files

* setup.py
* setup.cfg
* README.rst / README.md
* MANIFEST.in
* LICENSE.txt

## Pckagign your porject
* [Packaging Python Projects — Python Packaging User Guide](https://packaging.python.org/tutorials/packaging-projects/)

```
pip install setuptools wheel
```

Create source distributions

```
python setup.py sdist
```

Create Wheels

```
python3 setup.py bdist_wheel
```

This command generate two files in `dist` directory

* `.tar.gz`
    * source archive
* `.whl`
    * built distribution

```
pip install twine
```

## Tips
* wheel files need to be created in each platform (e.g. osx, windows)
    * To create and upload via CI service is not easy

## Reference
* [Packaging and distributing projects — Python Packaging User Guide](https://packaging.python.org/tutorials/distributing-packages/)
